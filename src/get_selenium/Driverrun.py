#-- coding: utf-8 --

# ******
#   __author__ = 'chaoneng'
#   __time__   =2016/12/14 15:59
# *******

from    selenium import webdriver
import  threading,time,queue
from    src.get_selenium.Twice_element import Twice
from    src.get_selenium.Action_choose import Choose
from    selenium.webdriver.common.action_chains import ActionChains
class web(threading.Thread):
    def __init__(self,text,content,rs):
        threading.Thread.__init__(self)

        self.text=text
        self.content=content
        self.rs=rs
    def run (self):
        driver=webdriver.Chrome()
        driver.get(" http://www.baidu.com/")
        if not Choose(driver,self.text).get_action():
            self.rs.append(self.text)

        while self.content.qsize() !=0:
            # print (content.qsize())
            text=self.content.get()
            # print (text)
            if not Choose(driver,text).get_action():
                self.rs.append(text)


        else:
            driver.close()



if __name__=="__main__":
    content=MobileGettest.get_testfile('D:\python_project\mobileauto')
    f_rs=[]
    th=[]
    for i in range(1):
        text=content.get()
        # print (text)
        # web(text,content,f_rs).setDaemon(True)
        th.append(web(text,content,f_rs))
    for i in range(1)  :
       th[i].start()
    for i in range(1)  :
       th[i].join()
    print (1)
