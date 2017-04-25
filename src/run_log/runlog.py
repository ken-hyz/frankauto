#-- coding: utf-8 --

# ******
#   __author__ = 'chaoneng'
#   __time__   =2017/4/24 17:42
# *******
import time
# from config.config import *

import os
ROOT_PATH=os.getcwd()
def franklog(c):
    def wrapper(e):

        filename=time.strftime('%Y-%m-%d ',time.localtime(time.time()))
        print (ROOT_PATH+'/log/'+filename+'.log')
        with open(ROOT_PATH+'/log/'+filename+'.log','a+') as f:
            f.write(c(e))
            f.close()
    return wrapper

@franklog
def logrun(e):
    return e
