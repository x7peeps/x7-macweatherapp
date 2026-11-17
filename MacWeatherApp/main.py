#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Mac天气查询软件
主程序入口
"""

import tkinter as tk
from tkinter import ttk, messagebox
import requests
import json
from datetime import datetime

class WeatherApp:
    """天气查询应用主类"""
    
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Mac天气查询软件")
        self.root.geometry("600x500")
        self.root.resizable(False, False)
        
        # API配置
        self.api_key = "your_openweather_api_key_here"
        self.base_url = "http://api.openweathermap.org/data/2.5/weather"
        
        # 温度单位
        self.temp_unit = "celsius"
        
        self.create_widgets()
        
    def create_widgets(self):
        """创建界面组件"""
        # 主框架
        main_frame = ttk.Frame(self.root, padding="20")
        main_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        
        # 标题
        title_label = ttk.Label(main_frame, text="Mac天气查询软件", 
                               font=("Arial", 18, "bold"))
        title_label.grid(row=0, column=0, columnspan=3, pady=(0, 20))
        
        # 城市输入
        ttk.Label(main_frame, text="城市名称:").grid(row=1, column=0, sticky=tk.W)
        self.city_entry = ttk.Entry(main_frame, width=30)
        self.city_entry.grid(row=1, column=1, padx=(10, 0))
        
        # 查询按钮
        query_btn = ttk.Button(main_frame, text="查询天气", command=self.query_weather)
        query_btn.grid(row=1, column=2, padx=(10, 0))
        
        # 温度单位选择
        unit_frame = ttk.Frame(main_frame)
        unit_frame.grid(row=2, column=0, columnspan=3, pady=10)
        
        self.unit_var = tk.StringVar(value="celsius")
        ttk.Radiobutton(unit_frame, text="摄氏度(°C)", variable=self.unit_var, 
                       value="celsius").pack(side=tk.LEFT, padx=(0, 20))
        ttk.Radiobutton(unit_frame, text="华氏度(°F)", variable=self.unit_var, 
                       value="fahrenheit").pack(side=tk.LEFT)
        
        # 天气信息显示区域
        self.info_text = tk.Text(main_frame, width=70, height=20, 
                                font=("Courier", 11))
        self.info_text.grid(row=3, column=0, columnspan=3, pady=(20, 0))
        
        # 滚动条
        scrollbar = ttk.Scrollbar(main_frame, orient="vertical", command=self.info_text.yview)
        scrollbar.grid(row=3, column=3, sticky=(tk.N, tk.S))
        self.info_text.configure(yscrollcommand=scrollbar.set)
        
    def query_weather(self):
        """查询天气信息"""
        city = self.city_entry.get().strip()
        if not city:
            messagebox.showwarning("警告", "请输入城市名称")
            return
            
        try:
            # 构建API请求
            params = {
                'q': city,
                'appid': self.api_key,
                'units': 'metric' if self.unit_var.get() == 'celsius' else 'imperial',
                'lang': 'zh_cn'
            }
            
            # 发送请求
            response = requests.get(self.base_url, params=params, timeout=10)
            
            if response.status_code == 200:
                data = response.json()
                self.display_weather_info(data)
            elif response.status_code == 404:
                messagebox.showerror("错误", "未找到该城市，请检查城市名称")
            else:
                messagebox.showerror("错误", f"API请求失败: {response.status_code}")
                
        except requests.exceptions.Timeout:
            messagebox.showerror("错误", "请求超时，请检查网络连接")
        except requests.exceptions.ConnectionError:
            messagebox.showerror("错误", "网络连接失败")
        except Exception as e:
            messagebox.showerror("错误", f"查询失败: {str(e)}")
            
    def display_weather_info(self, data):
        """显示天气信息"""
        self.info_text.delete(1.0, tk.END)
        
        # 基本信息
        city_name = data['name']
        country = data['sys']['country']
        temp = data['main']['temp']
        feels_like = data['main']['feels_like']
        humidity = data['main']['humidity']
        pressure = data['main']['pressure']
        description = data['weather'][0]['description']
        wind_speed = data['wind']['speed']
        
        # 温度单位
        unit_symbol = "°C" if self.unit_var.get() == "celsius" else "°F"
        
        # 格式化显示
        info = f"""
╔══════════════════════════════════════════════════════════════╗
║                        天气查询结果                          ║
╠══════════════════════════════════════════════════════════════╣
║ 城市: {city_name}, {country}
║ 查询时间: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}
║
║ 当前天气: {description}
║ 温度: {temp}{unit_symbol}
║ 体感温度: {feels_like}{unit_symbol}
║ 湿度: {humidity}%
║ 气压: {pressure} hPa
║ 风速: {wind_speed} m/s
╚══════════════════════════════════════════════════════════════╝
"""
        
        self.info_text.insert(tk.END, info)
        
    def run(self):
        """运行应用"""
        self.root.mainloop()

if __name__ == "__main__":
    app = WeatherApp()
    app.run()
