
'''

                    _ooOoo_

                   o8888888o

                   88" . "88

                   (| -_- |)

                    O\ = /O

                ____/`---'\____

              .   ' \\| |// `.

               / \\||| : |||// \

             / _||||| -:- |||||- \

               | | \\\ - /// | |

             | \_| ''\---/'' | |

              \ .-\__ `-` ___/-. /

           ___`. .' /--.--\ `. . __

        ."" '< `.___\_<|>_/___.' >'"".

       | | : `- \`.;`\ _ /`;.`/ - ` : | |

         \ \ `-. \_ __\ /__ _/ .-` / /

 ======`-.____`-.___\_____/___.-`____.-'======

                    `=---='



 .............................................

          佛祖保佑             永无BUG



 

 



  佛曰:

          写字楼里写字间，写字间里程序员；

          程序人员写程序，又拿程序换酒钱。

          酒醒只在网上坐，酒醉还来网下眠；

          酒醉酒醒日复日，网上网下年复年。

          但愿老死电脑间，不愿鞠躬老板前；

          奔驰宝马贵者趣，公交自行程序员。

          别人笑我忒疯癫，我笑自己命太贱；

          不见满街漂亮妹，哪个归得程序员？

'''
print("欢迎使用实用Chinglish翻译工具。")

try:
    import requests #尝试导入requests，若库不存在会报错抛出异常
except ImportError: #判断是否抛出异常
    print("requests模块不存在，正在自动安装……")
    import os
    package_name = 'requests' #定义变量package_name（用于下面安装requests模块）
    os.system(f'pip install -i https://pypi.tuna.tsinghua.edu.cn/simple {package_name}')#调用pip安装requests模块
    import requests
try:
    import jieba #尝试导入jieba，若库不存在会报错抛出异常
except ImportError: #判断是否抛出异常
    print("jieba模块不存在，正在自动安装……")
    import os
    package_name = 'jieba' #定义变量package_name（用于下面安装jieba模块）
    os.system(f'pip install -i https://pypi.tuna.tsinghua.edu.cn/simple {package_name}')#调用pip安装jieba模块
    import jieba

def translate(text):#定义翻译函数，接口使用有道翻译
    string = text
    data = {
    'doctype': 'json',
    'type': 'AUTO',
    'i':string
    }
    url = "http://fanyi.youdao.com/translate"
    r = requests.get(url,params=data)
    result = r.json()
    #print(result)
    translate_result = result['translateResult'][0][0]["tgt"]
    #print(translate_result)
    return translate_result

#以下为1.0版本采用的逐字翻译
#import sys
#def translate_one_by_one(text):#将输入文字逐字翻译
#    t=""
#    for c in text:
#        t=t+translate(c)+" "
#    print(t)
#translate_one_by_one(str(input("请输入一段要翻译的文字：")))

#以下为2.0版本采用的逐词翻译

#关闭jieba日志输出
import logging
jieba.setLogLevel(logging.INFO)

def translate_jieba(text):
    t_list=jieba.cut(text,cut_all=False)
    t=""
    for c in t_list:
        t=t+translate(c)+" "
    print(t)
translate_jieba(str(input("请输入一段要翻译的文字：")))