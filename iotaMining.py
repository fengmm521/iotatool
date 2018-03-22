#!/usr/bin/env python
#-*- coding: utf-8 -*-
import os
import sys
import time
import chardet  #中文编码判断

reload(sys)
sys.setdefaultencoding( "utf-8" )

class IOTAMiningTool(object):
    """docstring for ClassName"""
    def __init__(self, isCmdMode = True):

        self.isCmdMode = isCmdMode
        
        self.wdriver = None
        self.mineiotaURL = 'https://mineiota.com'
        self.reciveAddr = 'YRNKFDZDOECCMKTORLXJTJRVAMAPKVKEWI9QKRHCYJLBCGTFQBAPWSDBAPETELCJHNMJV9CAJVKTONLIXTD9IJIYH9'
    #获取高官信息
    # def getManager(wdriver,tid):
    def conventStrTOUtf8(self,oldstr):
        try:
            nstr = oldstr.encode("utf-8")
            return nstr
        except Exception as e:
            print 'nstr do not encode utf-8'
        cnstrtype = chardet.detect(oldstr)['encoding']
        utf8str =  oldstr.decode(cnstrtype).encode('utf-8')
        return utf8str

    #获取公司资料
    def runWork(self,isCmdMode = True):
        self.isCmdMode = isCmdMode
        if not self.wdriver:
            if self.isCmdMode:
                import selenium.webdriver.phantomjs.webdriver as wd
                self.wdriver = wd.WebDriver('/usr/local/bin/phantomjs')       #test
                self.wdriver.maximize_window()
                print('used phantomjs')
            else:
                # import selenium.webdriver.chrome.webdriver as  wd
                # chrome_options = wd.ChromeOptions()
                # chrome_options.add_argument('--headless')
                # chrome_options.add_argument('--disable-gpu')
                # self.wdriver = wd.WebDriver('/Users/mage/Documents/tool/cmdtool/chromedriver')       #test
                # self.wdriver.maximize_window()
                from selenium import webdriver
                chrome_options = webdriver.ChromeOptions()
                chrome_options.add_argument('--headless')
                chrome_options.add_argument('--disable-gpu')
                chrome_options.add_argument("user-agent='Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36'")
                self.wdriver = webdriver.Chrome(chrome_options=chrome_options,executable_path='/Users/mage/Documents/tool/cmdtool/chromedriver')

        self.wdriver.get(self.mineiotaURL)

        outdic = {} 

        #企业高管信息
        self.startMining(self.wdriver)                                                #获取高管信息

    def startMining(self,browser):

        #输入地址//*[@id="iotaAddress"]
        addrInput = browser.find_element_by_id('iotaAddress')

        time.sleep(1)
        addrInput.send_keys(self.reciveAddr)
        time.sleep(5)
        #提交地址
        submitBtn = browser.find_element_by_id('setAddress')
        submitBtn.click()
        print('wait allowbtn')
        time.sleep(25)



        #//*[@id="mineLog"]
        logtxt = browser.find_element_by_id('mineLog')
        print(logtxt.text)
        try:
            #//*[@id="accept"]
            browser.switch_to.frame(0)
            allowBtn = browser.find_element_by_id('accept')
            if allowBtn:
                allowBtn.click()
                print('allow button is click')
                browser.switch_to.parent_frame()
        except Exception as e:
            print('--------not heave allow button')
        #//*[@id="accept"]
        
        time.sleep(1)
        #挖矿情况//*[@id="mineStats"]
        try:
            minieShow = browser.find_element_by_id('mineStats')
            print minieShow.text
        except Exception as e:
            print('no minieShow')
        try:
            #恢复按钮//*[@id="resumeMining"]
            resumeBtn = browser.find_element_by_id('resumeMining')
            #停止按钮//*[@id="stopMining"]
            stopBtn = browser.find_element_by_id('stopMining')
            #提现按钮//*[@id="withdraw"]
            withdrawBtn = browser.find_element_by_id('withdraw')
        except Exception as e:
            print('init resume btn erro')
        try:
            logtxt = browser.find_element_by_id('mineLog')
            print(logtxt.text)
        except Exception as e:
            print('no logtxt')
        
        
    def stopWork(self):
        self.wdriver.quit()


def main():
    companytool = IOTAMiningTool()
    companytool.runWork(False)
    # companytool.runWork()
    raw_input('input enter for end.')
    companytool.stopWork()

#测试
if __name__ == '__main__':
    main()




