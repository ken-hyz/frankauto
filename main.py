#-- coding: utf-8 --

# ******
#   __author__ = 'chaoneng'
#   __time__   =2017/4/24 16:19
# *******
import os,time
from src.run_log.runlog import  logrun
from src.run_report.run_report import *
from  src.get_selenium import MobileGettest ,Driverrun
from config import  config

logrun('beign time :'+config.starttime+'\r\n')
content=MobileGettest.get_testfile(config.ROOT_PATH+"/data")
f_rs=[]
th=[]
for i in range(1):
    text=content.get()
    th.append(Driverrun.web(text,content,f_rs))
for i in range(1)  :
    th[i].start()
    th[i].join()


logrun('end  time :'+config.endtime+'\r\n')
reportrun(html_base(starttime=config.starttime,endtime=config.endtime,text="一切正常"))
