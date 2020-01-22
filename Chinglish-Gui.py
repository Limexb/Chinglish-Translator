try:
    import requests #尝试导入requests，若库不存在会报错抛出异常
except ImportError: #判断是否抛出异常
    print("requests模块不存在，正在自动安装……")
    import os
    package_name = 'requests' #定义变量package_name（用于下面安装requests模块）
    os.system(f'pip install -i https://pypi.tuna.tsinghua.edu.cn/simple {package_name}')#调用pip安装requests模块
    import requests
try:
    import tkinter #尝试导入requests，若库不存在会报错抛出异常
except ImportError: #判断是否抛出异常
    print("tkinter模块不存在，正在自动安装……")
    import os
    package_name = 'tkinter' #定义变量package_name（用于下面安装tkinter模块）
    os.system(f'pip install -i https://pypi.tuna.tsinghua.edu.cn/simple {package_name}')#调用pip安装tkinter模块
    import requests
try:
    import jieba #尝试导入jieba，若库不存在会报错抛出异常
except ImportError: #判断是否抛出异常
    print("jieba模块不存在，正在自动安装……")
    import os
    package_name = 'jieba' #定义变量package_name（用于下面安装jieba模块）
    os.system(f'pip install -i https://pypi.tuna.tsinghua.edu.cn/simple {package_name}')#调用pip安装jieba模块
    import jieba

import requests
from requests.exceptions import RequestException
import tkinter as tk
import sys
class Translate():
    def __init__(self):
        self.window = tk.Tk()  #创建window窗口
        self.window.geometry("420x270")
        self.window.title("Chinglish翻译器")  # 定义窗口名称
        self.window.resizable(0,0)  # 禁止调整窗口大小
        self.input = tk.Entry(self.window, width=50)  # 创建一个输入框,并设置尺寸
        self.info = tk.Text(self.window, height=18,width=59)   # 创建一个文本展示框，并设置尺寸
        # 添加一个按钮，用于触发翻译功能
        self.t_button = tk.Button(self.window, text='翻译', relief=tk.RAISED, width=8, height=1, command=self.fanyi)

    def gui_arrang(self):
        """完成页面元素布局，设置各部件的位置"""
        self.input.place(x=0, y=5)
        self.info.place(x=0, y=30)
        self.t_button.place(x=355, y=0)

    def fanyi(self):
        """定义一个函数，完成翻译功能"""
        original_str = self.input.get()  # 定义一个变量，用来接收输入框输入的值
        #关闭jieba日志输出
        import logging
        jieba.setLogLevel(logging.INFO)
        t=""
        t_list=jieba.cut(original_str,cut_all=False)
        #for c in original_str:
        for c in t_list:
            string = c
            data = {
            'doctype': 'json',
            'type': 'AUTO',
            'i':string
            }
            url = "http://fanyi.youdao.com/translate"
            r = requests.get(url,params=data)
            result = r.json()
            translate_result = result['translateResult'][0][0]["tgt"]
            t=t+translate_result+" "
        translate_jg = t
        self.info.delete(1.0, "end")  # 输出翻译内容前，先清空输出框的内容
        self.info.insert('end',translate_jg)  # 将翻译结果添加到输出框中
    def cle(self):
        """定义一个函数，用于清空输出框的内容"""
        self.info.delete(1.0,"end")  # 从第一行清除到最后一行

    def cle_e(self):
        """定义一个函数，用于清空输入框的内容"""
        self.input.delete(0,"end")

def main():
    t = Translate()
    t.gui_arrang()
    tk.mainloop()

if __name__ == '__main__':
    main()