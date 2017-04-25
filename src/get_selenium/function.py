#-- coding: utf-8 --

# ******
#   __author__ = 'chaoneng'
#   __time__   =2017/4/25 10:24
# *******

#***
#*  异常退出时，写入结束时间
#*
#***
import time
from src.run_report.reportbase import  html_base
from src.run_log.runlog import  logrun
def endtime():
    endtime=time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))
    logrun('end  time :'+endtime+'\r\n')
    html_base(endtime=endtime)