#-- coding: utf-8 --

# ******
#   __author__ = 'chaoneng'
#   __time__   =2016/12/7 16:33
# *******

import  os
from selenium.webdriver.remote.webdriver import *
from src.run_report.run_report import *
from selenium.common.exceptions import *
import  src.get_selenium.Action_choose  as choose
from src.run_log.runlog import *
from config import config
from src.e_mail.post_email import duqu
class Twice:

    def __init__(self,driver):
        self.driver=driver

    def get_search(self,by,value):
        try :
            if by == 'id':
                by = By.CSS_SELECTOR
                value = '[id="%s"]' % value
            elif by == 'tag_name':
                by = By.CSS_SELECTOR
            elif by == "class_name":
                by = By.CSS_SELECTOR
                value = ".%s" % value
            elif by == "name":
                by = By.CSS_SELECTOR
                value = '[name="%s"]' % value
            return by,value
        except NoSuchElementException:
            print(44);
        finally:
            pass

    def save_screenshot(self,file_adr):
        """
        二次封装保存图片
        """
        return self.driver.save_screenshot(file_adr)

    def click(self,by,value):
        """
        二次封装点击方法
        """
        rs=self.get_search(by,value)
        try:
            return self.driver.find_element( by=rs[0] ,value=rs[1]).click()
        except NoSuchElementException:
            logrun("找不到元素，定位方法为"+by+"定位内容为"+value+'\r\n')

            html=html_base(starttime=config.starttime, endtime=config.endtime,text=u"找不到元素，定位方法为"+by+"定位内容为"+value+'\r\n')
            reportrun(html)
    def send_keys(self,by,value,content):
        """
        二次封装输入方法
        """
        rs=self.get_search(by,value)
        try:
            return self.driver.find_element( by=rs[0] ,value=rs[1]).send_keys(content)
        except NoSuchElementException:
            logrun("找不到元素，定位方法为"+by+"定位内容为"+value+'\r\n')
            html=html_base(starttime=config.starttime, endtime=config.endtime,text=u"异常：找不到元素。定位方法为"+by+"，定位内容为"+value)
            reportrun(html)
            self.driver.quit()
            duqu(config.filename)
            os._exit(0)

    def reset(self,files):
        """
        二次封装重启方法
        """
        return self.driver.reset()
        return False
    def get(self,url):
        """
        再封装访问网站地址的方法
        """
        return self.driver.get(url)
    def openfile(self,adr):
        """
        打开引用文件

        """
        with open(adr,'r') as f:
            filecontent=f.read()
        choose.Choose(self.driver,filecontent)

if __name__=="__main__":
    Twice.reset()