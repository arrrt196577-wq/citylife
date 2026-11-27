using UnityEngine;
using UnityEngine.InputSystem;

[DisallowMultipleComponent]
[RequireComponent(typeof(Rigidbody2D))]
public sealed class PlayerMovement : MonoBehaviour
{
    // Keep these values aligned with the Facing conditions in the Player controller.
    private enum Facing { Down, Left, Right, Up }

    private static readonly int FacingParameter = Animator.StringToHash("Facing");
    private static readonly int IsMovingParameter = Animator.StringToHash("IsMoving");

    [SerializeField, Min(0f)] private float moveSpeed = 3f;

    private Rigidbody2D body;
    private Animator animator;
    private InputAction moveAction;
    private Vector2 moveDirection;
    private Facing facing;

    private void Reset()
    {
        // Default to top-down physics when adding the component in the Editor.
        Rigidbody2D playerBody = GetComponent<Rigidbody2D>();
        playerBody.gravityScale = 0f;
        playerBody.constraints |= RigidbodyConstraints2D.FreezeRotation;
    }

    private void Awake()
    {
        body = GetComponent<Rigidbody2D>();
        TryGetComponent(out animator);
        moveAction = InputSystem.actions?.FindAction("Player/Move");
        if (moveAction == null)
        {
            Debug.LogError("PlayerMovement requires the project-wide Player/Move input action.", this);
            enabled = false;
        }
    }

    private void Update()
    {
        moveDirection = Vector2.ClampMagnitude(moveAction.ReadValue<Vector2>(), 1f);
        if (animator == null || animator.runtimeAnimatorController == null)
            return;

        bool isMoving = moveSpeed > 0f && moveDirection != Vector2.zero;
        if (isMoving)
        {
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
        body.linearVelocity = moveDirection * moveSpeed;
    }

    private void OnDisable()
    {
        moveDirection = Vector2.zero;
        if (body != null)
            body.linearVelocity = Vector2.zero;

        if (animator != null && animator.runtimeAnimatorController != null)
            animator.SetBool(IsMovingParameter, false);
    }
}
