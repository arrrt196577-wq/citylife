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
| [doc/](doc/) | 存放业务文档、玩法设计文档等项目文档。 |
| [Game/](Game/) | Unity 项目所在目录。 |

## 美术源文件

| 路径 | 用途 |
| --- | --- |
| [ArtSource/Scripts/](ArtSource/Scripts/) | 能重复生成成品的绘图脚本。[咖啡厅生成脚本](ArtSource/Scripts/draw_cafe.py)输出室内底图、外观和家具图集，也可用 `--preview` 导出内外对照图。 |
| [ArtSource/Originals/](ArtSource/Originals/) | Pixelorama 的 .pxo 等可编辑原稿，可按建筑或道具分子目录存放。 |
| [ArtSource/Drafts/](ArtSource/Drafts/) | 角色草图、配色试稿和动画测试。 |

## 项目文档

项目文档统一使用 Markdown（`.md`）格式。

| 路径 | 用途 |
| --- | --- |
| [doc/business/](doc/business/) | 项目需求、业务规则和业务流程。 |
| [doc/gameplay/](doc/gameplay/) | 核心玩法、游戏机制和数值设计。 |
| [游戏基座](doc/gameplay/游戏基座.md) | 游戏定位、现有原型与待定义的基础玩法。 |

## Unity 游戏内容

| 路径 | 用途 |
| --- | --- |
| [Game/Assets/CityLife/](Game/Assets/CityLife/) | CityLife 的游戏代码和素材。 |
| [Scripts/PlayerMovement.cs](Game/Assets/CityLife/Scripts/PlayerMovement.cs) | 使用 Player/Move 输入移动角色，并驱动四方向走路与待机动画。 |
| [Scripts/CafeInterior.cs](Game/Assets/CityLife/Scripts/CafeInterior.cs) | 根据角色脚下的位置显示或隐藏咖啡厅外观。 |
| [Art/Characters/](Game/Assets/CityLife/Art/Characters/) | 女主角的正面站姿与四方向走路图集。 |
| [Animations/Player/](Game/Assets/CityLife/Animations/Player/) | 主角 Animator Controller 与四方向走路、待机动画。 |
| [Art/Props/](Game/Assets/CityLife/Art/Props/) | 招牌、售货机和家具等道具素材。 |
| [Art/Props/Cafe/](Game/Assets/CityLife/Art/Props/Cafe/) | 咖啡厅的室内底图、外观覆盖层和独立家具图集。精灵均使用 16 PPU，外观和家具按接地点与角色排序。 |
| [Game/Assets/Scenes/](Game/Assets/Scenes/) | [示例场景](Game/Assets/Scenes/SampleScene.unity)包含主角四方向移动与动画、可步行进出的咖啡厅，以及墙体和家具碰撞。 |
| [Game/Assets/Settings/](Game/Assets/Settings/) | 2D 渲染管线、输入动作和场景模板配置。 |
| [Game/Assets/Welcome/](Game/Assets/Welcome/) | Unity 2D 模板的欢迎页资源和脚本。 |
| [Game/Packages/](Game/Packages/) | Unity 包依赖清单和锁定版本。 |
| [Game/ProjectSettings/](Game/ProjectSettings/) | Unity 编辑器版本、构建场景和项目设置。 |

Library、Temp、Logs 和 UserSettings 等本机生成目录不纳入版本控制。
