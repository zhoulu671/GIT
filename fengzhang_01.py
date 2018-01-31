from selenium import webdriver
# from time import sleep
import time
class TEST:000
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.driver.get('https://sit-ccp.uce.cn')
        time.sleep(5)
    def login(self):
        self.driver.find_element_by_xpath('/html/body/div/div[2]/div[1]/form/div[2]/div/div[2]/input').send_keys('80239409')
        self.driver.find_element_by_xpath('//*[@id="login-form"]/form/div[3]/div/input[2]').send_keys('zhang_1231212')
        self.driver.find_element_by_xpath('/html/body/div/div[2]/div[1]/form/div[4]/div/button').click()
    def track(self):
        xuanzedingdanguanli = self.driver.find_element_by_xpath(
            '/html/body/div/div[2]/div[1]/div[2]/ul/li[2]/a/span').click()
        time.sleep(1)  # 等待2秒
        jinrudingdanguanli = self.driver.find_element_by_xpath(
            '/html/body/div/div[2]/div[1]/div[2]/ul/li[2]/ul/li[2]/a/span').click()
        time.sleep(2)  # 等待2秒
        shuruyundanhao = self.driver.find_element_by_xpath('//*[@id="topBar"]/form/div[1]/div[2]/textarea').send_keys(
            '889900008511503,889900008511497,889900008511481,889900008511480')
        time.sleep(1)
        chaxunanniu = self.driver.find_element_by_xpath('//*[@id="topBar"]/form/div[6]/button').click()
        time.sleep(1)
        xuanzedingdanbianhao = self.driver.find_element_by_xpath('//*[@id="topBar"]/form/div[1]/div[1]/div[1]/i').click()
        time.sleep(1)
        zidan = self.driver.find_element_by_xpath('/html/body/div[2]/div/div[1]/ul/li[4]').click()
        time.sleep(1)
        qingkongshuruzidanhao = self.driver.find_element_by_xpath('//*[@id="topBar"]/form/div[1]/div[2]/textarea').clear()
        time.sleep(1)
        shuruzidanbianhao =self.driver.find_element_by_xpath('//*[@id="topBar"]/form/div[1]/div[2]/textarea').send_keys(
            '319000350159')
        time.sleep(1)
        chaxunanniu = self.driver.find_element_by_xpath('//*[@id="topBar"]/form/div[6]/button').click()
        time.sleep(1)
        xuanzedigndanbianhao = self.driver.find_element_by_xpath('//*[@id="topBar"]/form/div[1]/div[1]/div[1]/i').click()
        time.sleep(1)
        wiabudingdanhao = self.driver.find_element_by_xpath('/html/body/div[2]/div/div[1]/ul/li[3]').click()
        time.sleep(1)
        qingkongshuruyundanhao1 = self.driver.find_element_by_xpath('//*[@id="topBar"]/form/div[1]/div[2]/textarea').clear()
        time.sleep(1)
        shuruwaibudingdanhao = self.driver.find_element_by_xpath('//*[@id="topBar"]/form/div[1]/div[2]/textarea').send_keys(
            'WAI1231212')
        time.sleep(1)
        chaxunanniu = self.driver.find_element_by_xpath('//*[@id="topBar"]/form/div[6]/button').click()
        time.sleep(1)
        xuanzedingdanbianhao = self.driver.find_element_by_xpath('//*[@id="topBar"]/form/div[1]/div[1]/div[1]/i').click()
        time.sleep(1)
        dingdanbianhao = self.driver.find_element_by_xpath('/html/body/div[2]/div/div[1]/ul/li[2]').click()
        time.sleep(1)
        qingkongshuruyundanhao = self.driver.find_element_by_xpath('//*[@id="topBar"]/form/div[1]/div[2]/textarea').clear()
        time.sleep(1)
        shurudingdanbianhao2 = self.driver.find_element_by_xpath('//*[@id="topBar"]/form/div[1]/div[2]/textarea').send_keys(
            'CCP171210165407040053,CCP171214201527000040,CCP171214205118000045,CCP171214193856000020')
        time.sleep(1)
        chaxunanniu = self.driver.find_element_by_xpath('//*[@id="topBar"]/form/div[6]/button').click()
        time.sleep(1)
