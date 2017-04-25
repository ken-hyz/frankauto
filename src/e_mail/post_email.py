import  os
import smtplib
from email.mime.multipart import MIMEMultipart

from email.header import Header
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email.mime.application import MIMEApplication
from config.config import *



def getfile(filename):
    (filepath,filename) = os.path.split(filename)


def emailmodel(adr):
    (filepath,filename) = os.path.split(adr)
    print (filename)
    msg = MIMEMultipart()
    # 邮件内容读取
    mime = MIMEApplication(open(adr,"rb").read())
    # 加上必要的头信息:
    mime.add_header('Content-Disposition', 'attachment', filename=("gbk",'',filename))
    #添加到邮件模板
    msg.attach(mime)
    msg.attach(MIMEText('%s'%content))
    msg['From'] = from_addr
    msg['To'] =','.join(to_addr)
    msg['Subject'] = Header('%s'%subject, 'utf-8')
    return  msg

def duqu(adr):
    smtp = smtplib.SMTP(smtpserver) # SMTP协议默认端口是25
    smtp.login(username, password)
    smtp.sendmail(from_addr,to_addr, emailmodel(adr).as_string())
    smtp.quit()


if __name__=="__main__":
    adr="d://index.php"
    duqu(adr)





