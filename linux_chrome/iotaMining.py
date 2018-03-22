#!/usr/bin/env python
#-*- coding: utf-8 -*-
import os
import sys
import time

# reload(sys)
# sys.setdefaultencoding( "utf-8" )

class IOTAMiningTool(object):
    """docstring for ClassName"""
    def __init__(self, isCmdMode = True):

        self.isCmdMode = isCmdMode
        
        self.wdriver = None
        self.mineiotaURL = 'https://mineiota.com'
        self.reciveAddr = 'YRNKFDZDOECCMKTORLXJTJRVAMAPKVKEWI9QKRHCYJLBCGTFQBAPWSDBAPETELCJHNMJV9CAJVKTONLIXTD9IJIYH9'

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
                # linux上安装chrome要安装这两个库libgconf2-4 libnss3-1d
                #https://jiayi.space/post/zai-ubuntufu-wu-qi-shang-shi-yong-chrome-headless
                #chrome drvier下载：https://sites.google.com/a/chromium.org/chromedriver/downloads
                #

                from selenium import webdriver
                # from pyvirtualdisplay import Display
                # display = Display(visible=0, size=(800, 800))  
                # display.start()
                # time.sleep(1)
                chrome_options = webdriver.ChromeOptions()
                chrome_options.add_argument('--headless')
                chrome_options.add_argument('--disable-gpu')
                chrome_options.add_argument("user-agent='Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36'")
                self.wdriver = webdriver.Chrome(chrome_options=chrome_options,executable_path='/root/chrome/chromedriver')
                print('used chrome')

        self.wdriver.get(self.mineiotaURL)

        outdic = {} 

        #企业高管信息
        self.startMining(self.wdriver)                                                #获取高管信息

    def startMining(self,browser):

        #输入地址//*[@id="iotaAddress"]
        print('start mining')
        addrInput = browser.find_element_by_id('iotaAddress')

        time.sleep(1)
        addrInput.send_keys(self.reciveAddr)
        print('start input')
        time.sleep(5)
        #提交地址
        submitBtn = browser.find_element_by_id('setAddress')
        submitBtn.click()
        print('wait allowbtn')
        time.sleep(20)

        try:
            #//*[@id="mineLog"]
            logtxt = browser.find_element_by_id('mineLog')
            print(logtxt.text)
        except Exception as e:
            print('no logtxt')
        
        
        try:
            isNoHeaveFram = True
            sleeptimes = 1
            #//*[@id="accept"]
            while isNoHeaveFram:
                try:
                    browser.switch_to.frame(0)
                    allowBtn = browser.find_element_by_id('accept')
                    if allowBtn:
                        allowBtn.click()
                        print('allow button is click')
                        browser.switch_to.parent_frame()
                        isNoHeaveFram = False
                    print('heave frame but not allowbtn')
                except Exception as e:
                    print('not allow %d'%(sleeptimes))
                time.sleep(10)
        except Exception as e:
            print('--------not heave allow button')
        #//*[@id="accept"]
        
        time.sleep(1)
        #挖矿情况//*[@id="mineStats"]
        try:
            minieShow = browser.find_element_by_id('mineStats')
            print(minieShow.text)
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
    input('input enter for end.')
    # runtime = 60*60*24
    # while True:
    #     time.sleep(runtime)
    #     break
    companytool.stopWork()

#测试
if __name__ == '__main__':
    main()




