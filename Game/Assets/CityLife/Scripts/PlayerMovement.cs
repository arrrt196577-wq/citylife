using UnityEngine;
using UnityEngine.InputSystem;

/// <summary>
/// 控制主角在 2D 俯视角场景中的四方向移动，并同步驱动走路与待机动画。
/// </summary>
[DisallowMultipleComponent]
[RequireComponent(typeof(Rigidbody2D))]
public sealed class PlayerMovement : MonoBehaviour
{
    // 枚举顺序需与主角 Animator Controller 中 Facing 参数的条件值保持一致。
    private enum Facing { Down, Left, Right, Up }

    // 缓存 Animator 参数哈希，避免每帧通过字符串查找。
    private static readonly int FacingParameter = Animator.StringToHash("Facing");
    private static readonly int IsMovingParameter = Animator.StringToHash("IsMoving");

    // 移动速度（单位：世界单位/秒）。
    [SerializeField, Min(0f)] private float moveSpeed = 3f;
    // 主角动画控制器；未在 Inspector 指定时会在运行时尝试自动获取。
    [SerializeField] private Animator animator;

    // 2D 刚体组件，用于在物理更新中应用移动速度。
    private Rigidbody2D body;
    // 项目全局输入配置中的 Player/Move 动作。
    private InputAction moveAction;
    // 当前帧限制长度后的移动方向输入（最大模长为 1）。
    private Vector2 moveDirection;
    // 主角当前朝向；停止移动时保持上一次的朝向。
    private Facing facing;

    private void Reset()
    {
        // 在编辑器中首次挂载组件时，默认设为无重力并锁定旋转的 2D 俯视角物理参数。
        Rigidbody2D playerBody = GetComponent<Rigidbody2D>();
        playerBody.gravityScale = 0f;
        playerBody.constraints |= RigidbodyConstraints2D.FreezeRotation;
    }

    private void Awake()
    {
        body = GetComponent<Rigidbody2D>();
        if (animator == null)
            TryGetComponent(out animator);

        // 查找项目级 Player/Move 输入动作，缺失时报错并禁用当前组件。
        moveAction = InputSystem.actions?.FindAction("Player/Move");
        if (moveAction == null)
        {
            Debug.LogError("PlayerMovement requires the project-wide Player/Move input action.", this);
            enabled = false;
        }
    }

    private void Update()
    {
        // 读取并限制移动输入向量长度，避免斜向移动超出设定速度。
        moveDirection = Vector2.ClampMagnitude(moveAction.ReadValue<Vector2>(), 1f);
        if (animator == null || animator.runtimeAnimatorController == null)
            return;

        bool isMoving = moveSpeed > 0f && moveDirection != Vector2.zero;
        if (isMoving)
        {
            // 按水平与垂直分量绝对值较大的轴确定四方向朝向。
            if (Mathf.Abs(moveDirection.x) > Mathf.Abs(moveDirection.y))
                facing = moveDirection.x < 0f ? Facing.Left : Facing.Right;
            else
                facing = moveDirection.y < 0f ? Facing.Down : Facing.Up;
        }

        animator.SetInteger(FacingParameter, (int)facing);
        animator.SetBool(IsMovingParameter, isMoving);
    }

    private void FixedUpdate()
    {
        // 在固定物理步进中更新刚体线性速度，保证移动与碰撞行为稳定。
        body.linearVelocity = moveDirection * moveSpeed;
    }

    private void OnDisable()
    {
        // 组件禁用时清空输入方向与刚体速度，并将动画切换回待机状态。
        moveDirection = Vector2.zero;
        if (body != null)
            body.linearVelocity = Vector2.zero;

        if (animator != null && animator.runtimeAnimatorController != null)
            animator.SetBool(IsMovingParameter, false);
    }
}
