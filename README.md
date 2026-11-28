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
| [ArtSource/Drafts/](ArtSource/Drafts/) | 角色草图、配色试稿、动画测试和场景规划草图。[小超市室内规划草稿](ArtSource/Drafts/supermarket-interior-layout-v1.png)展示货架和购物动线。[小超市室内外对照](ArtSource/Drafts/supermarket-inside-outside-v1.png)展示进店前后的画面。[第二版外观](ArtSource/Drafts/supermarket-exterior-v2.png)采用砖红平顶和沿街生鲜橱窗。[第二版室内预览](ArtSource/Drafts/supermarket-interior-layout-v2.png)展示浅色砖墙、地砖和六色选品地毯。 |

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
| [Scripts/CameraFollow.cs](Game/Assets/CityLife/Scripts/CameraFollow.cs) | 镜头跟随主角移动，保留初始取景偏移与相机深度，可从咖啡厅走向右侧超市。 |
| [Scripts/CafeInterior.cs](Game/Assets/CityLife/Scripts/CafeInterior.cs) | 根据角色脚下的位置显示或隐藏建筑外观，供 Cafe 和 Market 使用。 |
| [Art/Characters/](Game/Assets/CityLife/Art/Characters/) | 女主角的正面站姿与四方向走路图集。 |
| [Animations/Player/](Game/Assets/CityLife/Animations/Player/) | 主角 Animator Controller 与四方向走路、待机动画。 |
| [Art/Props/](Game/Assets/CityLife/Art/Props/) | 招牌、售货机和家具等道具素材。 |
| [Art/Props/Cafe/](Game/Assets/CityLife/Art/Props/Cafe/) | 咖啡厅的室内底图、外观覆盖层和独立家具图集。精灵均使用 16 PPU，外观和家具按接地点与角色排序。 |
| [Art/Props/Supermarket/](Game/Assets/CityLife/Art/Props/Supermarket/) | 小超市的室内底图、外观覆盖层和家具图集。三张图共用 448 × 384 px 画布和 16 PPU，家具按草稿原位切片。以底图中心为原点，外观覆盖层的局部 Y 为 `-5.8125`。 |
| [Art/Props/Supermarket/V2/](Game/Assets/CityLife/Art/Props/Supermarket/V2/) | 第二版室内底图、外观覆盖层、购物车和选品地毯图集，均为 16 PPU。每块地毯为 104 × 15 px，轴心在下边中央。以底图中心为原点，左右列局部 X 为 `-5`、`5`，后、中、前排局部 Y 为 `4`、`0.75`、`-2.625`。 |
| [Market.prefab](Game/Assets/CityLife/Art/Props/Supermarket/V2/Market.prefab) | 已组装第二版室内外、家具、六块独立地毯和墙体碰撞。拖入场景后调整 `Market` 父物体的 `Transform`，再将场景中的 `Player` 拖入 `Cafe Interior` 组件的 `Player` 槽，即可随进出切换外观。 |
| [Game/Assets/Scenes/](Game/Assets/Scenes/) | [示例场景](Game/Assets/Scenes/SampleScene.unity)包含主角四方向移动与动画、跟随镜头、可步行进出的咖啡厅和右侧超市，以及墙体和家具碰撞。超市从南面正门进入，从咖啡厅出发需先向下绕过超市左墙，再向右走到门口。 |
| [Game/Assets/Settings/](Game/Assets/Settings/) | 2D 渲染管线、输入动作和场景模板配置。 |
| [Game/Assets/Welcome/](Game/Assets/Welcome/) | Unity 2D 模板的欢迎页资源和脚本。 |
| [Game/Packages/](Game/Packages/) | Unity 包依赖清单和锁定版本。 |
| [Game/ProjectSettings/](Game/ProjectSettings/) | Unity 编辑器版本、构建场景和项目设置。 |

Library、Temp、Logs 和 UserSettings 等本机生成目录不纳入版本控制。
