# Mac天气查询软件

一个基于Python和Tkinter开发的Mac系统天气查询应用。

## 功能特性

- 支持通过城市名称查询天气
- 显示当前天气信息（温度、湿度、风速等）
- 支持摄氏度/华氏度温度单位切换
- 完善的错误处理机制
- 美观易用的GUI界面

## 安装和运行

1. 安装依赖：
```bash
pip install -r requirements.txt
```

2. 配置API密钥：
   - 在OpenWeatherMap注册账号获取API密钥
   - 在main.py中替换`your_openweather_api_key_here`

3. 运行程序：
```bash
python3 main.py
```

## 技术栈

- Python 3.x
- Tkinter (GUI框架)
- Requests (HTTP请求)
- OpenWeatherMap API

## 开发者

由Trae AI自动化系统开发
