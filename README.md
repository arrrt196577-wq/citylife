# CityLife 仓库索引

供 AI 按任务定位相关目录和文件。

## 技术选型

CityLife 使用 Unity 作为游戏引擎，并用 C# 编写游戏逻辑。

## 仓库根目录

| 路径 | 用途 |
| --- | --- |
| [README.md](README.md) | 仓库的目录和文件索引。 |
| [.gitignore](.gitignore) | 排除 Unity 缓存、日志、本机编辑器设置和 Python 字节码。 |
| [ArtSource/](ArtSource/) | 像素画原稿、参考图和 AI 素材生成记录。 |
| [Game/](Game/) | Unity 项目所在目录。 |

## 美术源文件

| 路径 | 用途 |
| --- | --- |
| [ArtSource/Scripts/](ArtSource/Scripts/) | 能重复生成成品的绘图脚本，例如 [咖啡厅生成脚本](ArtSource/Scripts/draw_cafe.py)。 |
| [ArtSource/Originals/](ArtSource/Originals/) | Pixelorama 的 .pxo 等可编辑原稿，可按建筑或道具分子目录存放。 |
| [ArtSource/Drafts/](ArtSource/Drafts/) | 角色草图、配色试稿和动画测试。 |

## Unity 游戏内容

| 路径 | 用途 |
| --- | --- |
| [Game/Assets/CityLife/](Game/Assets/CityLife/) | CityLife 的游戏代码和素材。 |
| [Art/Props/](Game/Assets/CityLife/Art/Props/) | 招牌、售货机和家具等道具素材。 |
| [Art/Props/Cafe/](Game/Assets/CityLife/Art/Props/Cafe/) | 咖啡厅的室内底图和外观覆盖层。两张图使用相同坐标、原点和 16 PPU。角色在外时显示两层，在内时隐藏外观覆盖层。 |
| [Game/Assets/Scenes/](Game/Assets/Scenes/) | Unity 初始化生成的示例场景。 |
| [Game/Assets/Settings/](Game/Assets/Settings/) | 2D 渲染管线、输入动作和场景模板配置。 |
| [Game/Assets/Welcome/](Game/Assets/Welcome/) | Unity 2D 模板的欢迎页资源和脚本。 |
| [Game/Packages/](Game/Packages/) | Unity 包依赖清单和锁定版本。 |
| [Game/ProjectSettings/](Game/ProjectSettings/) | Unity 编辑器版本、构建场景和项目设置。 |

Library、Temp、Logs 和 UserSettings 等本机生成目录不纳入版本控制。
