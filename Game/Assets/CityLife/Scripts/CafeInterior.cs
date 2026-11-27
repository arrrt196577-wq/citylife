using UnityEngine;

/// <summary>
/// 根据主角脚下位置是否在室内区域内，切换咖啡厅外观覆盖层的显示与隐藏。
/// </summary>
[DisallowMultipleComponent]
public sealed class CafeInterior : MonoBehaviour
{
    // 咖啡厅外观覆盖层渲染器；主角进入室内时关闭以露出室内画面。
    [SerializeField] private SpriteRenderer exterior;
    // 咖啡厅室内判定区域，用于检测主角是否位于室内。
    [SerializeField] private BoxCollider2D interiorBounds;
    // 主角 Transform，以其位置（脚下接地点）作为室内外判定点。
    [SerializeField] private Transform player;

    private void LateUpdate()
    {
        // 在本帧移动完成后判定主角位置：位于室内时隐藏外观，离开室内后恢复显示。
        if (exterior != null && interiorBounds != null && player != null)
            exterior.enabled = !interiorBounds.OverlapPoint(player.position);
    }
}
