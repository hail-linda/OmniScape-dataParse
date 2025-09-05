# 哈尔滨工业大学导航仪器研究所 — 轮式机器人 ROS2 数据解析
## 功能概述

本仓库用于 **哈尔滨工业大学导航仪器研究所轮式机器人** 数据的离线解析与存储。  
其主要目标是将 **ROS 2 的 bag 文件**（rosbag2，SQLite3）通过 **Python 脚本**解析为结构化数据文件（CSV、图片、字典 `.p` 文件），以便后续用于算法研究、可视化和数据集构建。

主要功能包括：
- ✅ 读取 ROS 2 bag 文件并批量导出指定话题数据  
- ✅ 自动将话题数据转换为 **`.p` 文件格式**，并支持保存为 CSV、图片等  
- ✅ 灵活选择话题，支持字段重命名、单位换算与数据插值  
- ✅ 提供基础的 **质量检查与可视化脚本**，包括时间序列一致性、话题频率、丢包率和轨迹绘制  

## 仓库结构

```text
OMNISCAPE-DATAPARSE/
├── __pycache__/                   # Python 缓存文件
├── .vs/                           # VSCode/IDE 配置文件
├── GNSSFeature/                   # GNSS 特征提取模块
│   ├── 02_nb_GNSSeature.ipynb     # GNSS 特征分析 Notebook
│   └── nav_db.json                # GNSS 数据库配置/映射
├── livox_interfaces/              # Livox 激光雷达接口
├── log/                           # 日志目录
├── sensors_interfaces/            # 传感器接口定义
│   └── msg/                       # 接口消息定义
│       ├── GnssFrame.msg
│       ├── MtiFrame.msg
│       ├── MtiGnssFrame.msg
│       ├── MtiStatusFrame.msg
│       ├── OpticalFrame.msg
│       ├── UwbFrame3.msg
│       ├── UwbFrame3Block.msg
│       └── UwbStatusFrame.msg
├── sensors_msg/                   # 自定义传感器消息
│   └── msg/                       
│       ├── CustomMsg.msg
│       ├── CustomPoint.msg
│       ├── GNSS1HPPOSELLHblock.msg
│       ├── GNSS1RAWXblock.msg
│       ├── GNSS1SATblock.msg
│       ├── GnssFrame.msg
│       ├── GNSSmsg.msg
│       ├── Gpfpd.msg / GpfpdNEW.msg
│       ├── Gpio.msg
│       ├── Gtimu.msg / Imu.msg
│       ├── MtiFrame.msg / MtiGnssFrame.msg / MtiStatusFrame.msg
│       ├── OpticalFrame.msg
│       ├── UwbFrame3.msg / UwbFrame3Block.msg / UwbRange.msg
│       └── UwbStatusFrame.msg
├── CMakeLists.txt                 # ROS2 包编译配置
├── package.xml                    # ROS2 包依赖声明
├── 01_OmniScape_nav_DB3_parse.ipynb     # bag 数据解析 Notebook
├── 03_OmniScape_nav_DB3_matching.ipynb  # 数据匹配与对齐 Notebook
├── amapDraw.html                  # 可视化 HTML（高德地图绘制）
├── msgRegister.py                 # ROS2 消息注册脚本
├── name.ros_pickle                # ROS 消息字典序列化文件
├── OmniScape_nav_lint.py          # 数据检查的依赖函数
└── readme.md                      # 项目说明文档（本文件）
```

## 环境依赖

- 依赖管理：Anaconda
- 下载的conda虚拟环境 navDataParse
  
本项目基于 **Anaconda** 管理 Python 环境，已提供完整的 Conda 虚拟环境文件。  
用户只需安装 Anaconda，然后通过提供的环境文件即可快速复现开发环境,推荐的版本号是conda 23.7.2，未测试过其他版本。
👉 [点击这里获取虚拟环境文件](<https://pan.baidu.com/s/1cequWzRHul4318DF0vdpbw?pwd=mgrd>)

虚拟环境配置方法：
```bash
# 1) 下载并解压虚拟环境文件
# 2) 复制导入anaconda安装路径下envs文件夹下
# 3) 激活虚拟环境
conda activate navDataParse
```

## 使用方法

本项目主要通过 **三个 Jupyter Notebook** 完成数据解析与处理，只需依次运行即可：

1. **01_OmniScape_nav_DB3_parse.ipynb**  
   - 用于解析 **ROS2 bag 文件**（SQLite3 格式），提取传感器话题数据，绘制轨迹、卫星状态等。  

2. **02_nb_GNSSeature.ipynb**  
   - 用于分析 **GNSS 卫星特征**，提取可见星、信噪比等特征信息。  

3. **03_OmniScape_nav_DB3_matching.ipynb**  
   - 将前两步结果进行融合与匹配，最终生成 **`.p` 字典文件**，便于后续算法研究与数据使用。  

> 提示：请确保在运行 Notebook 前已激活提供的 Conda 虚拟环境。  

> 提示：如卫星地图无法正确加载，请尝试将火狐浏览器设置为默认浏览器，并信任notebook。 

## 常见问题 FAQ
整理常见报错和解决方法。暂无


## 开发与贡献
本数据分析代码主要由🌸[Xinda Li](<https://github.com/hail-linda>)🌸 开发完成。
