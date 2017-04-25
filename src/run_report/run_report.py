#-- coding: utf-8 --

# ******
#   __author__ = 'chaoneng'
#   __time__   =2017/4/25 9:52
# *******


import time
# from config.config import *
from config import  config
import os

def html_base(starttime,endtime,text):
    #****基础模板
    basehtml=u"""<html>
<head>
<title>ui 测试报告</title>
</head>
<body>
<div>
<h1>ui test</h1>
<P>开始时间<strong>%s</strong></P>
<P>结束时间:<strong>%s</strong></P>
<h2>结果</h2>
</div>
<div>
<p>
%s
</p>
</div>
</body>
</html>
    """%(starttime,endtime,text)
    return  basehtml
def frankreport(c):
    def wrapper(e):
        filename=config.filename
        with open(filename,'a+') as f:
            f.write(c(e))
            f.close()
    return wrapper

@frankreport
def reportrun(e):
    return e
