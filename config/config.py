#-- coding: utf-8 --

# ******
#   __author__ = 'chaoneng'
#   __time__   =2016/12/9 14:06
# *******
import  os,time
#账号信息
to_addr=['969744832@qq.com']                                 #接收方
from_addr="xx.com"                     #邮件显示的来源邮箱，一般跟发送者账号一致
subject ="邮件"                                               #主题
content="已发邮件注意查收"                                      #邮件内容
smtpserver = 'smtp.exmail.qq.com'                            #邮箱服务器地址
username = 'xxx.com'                    #发送者账号
password='xxx'                                           #密码

#项目根地址

ROOT_PATH=os.getcwd()
#报告地址

filename=time.strftime('%Y-%m-%d',time.localtime(time.time()))
filename=ROOT_PATH+'/report/'+filename+'.html'
#脚本开始跟结束时间
starttime=time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))
endtime=time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))
content=''
