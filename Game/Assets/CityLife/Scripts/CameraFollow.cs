using UnityEngine;

/// <summary>
/// 在角色移动后跟随其平面位置，保留场景中设置的初始构图与相机深度。
/// </summary>
[DisallowMultipleComponent]
[RequireComponent(typeof(Camera))]
public sealed class CameraFollow : MonoBehaviour
{
    // 需要跟随的主角，在场景中指定，避免依赖物体名称或标签。
    [SerializeField] private Transform target;

    // 记录启动时的相对位置，使镜头移动时保持原有的取景偏移。
    private Vector3 initialOffset;

    private void Awake()
    {
        if (target != null)
            initialOffset = transform.position - target.position;
    }

    private void LateUpdate()
    {
        if (target == null)
            return;

        // 在角色移动完成后更新镜头的 X、Y，保持相机原有的 Z 深度。
        Vector3 position = transform.position;
        position.x = target.position.x + initialOffset.x;
        position.y = target.position.y + initialOffset.y;
        transform.position = position;
    }
}
