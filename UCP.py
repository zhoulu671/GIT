#
from selenium import webdriver
import time

driver = webdriver.Chrome()  # 调用chrome浏览器
driver.get('https://sit-ccp.uce.cn')
time.sleep(5)
driver.maximize_window()
zhanghao = driver.find_element_by_xpath('/html/body/div/div[2]/div[1]/form/div[2]/div/div[2]/input').send_keys(
    '80239409')
mima = driver.find_element_by_xpath('//*[@id="login-form"]/form/div[3]/div/input[2]').send_keys('zhang_1231212')
dianjidenglu = driver.find_element_by_xpath('/html/body/div/div[2]/div[1]/form/div[4]/div/button').click()
time.sleep(1)

xuanzedingdanguanli = driver.find_element_by_xpath('/html/body/div/div[2]/div[1]/div[2]/ul/li[2]/a/span').click()
time.sleep(1)  # 等待2秒
jinrudingdanguanli = driver.find_element_by_xpath(
    '/html/body/div/div[2]/div[1]/div[2]/ul/li[2]/ul/li[2]/a/span').click()
time.sleep(2)  # 等待2秒
shuruyundanhao = driver.find_element_by_xpath('//*[@id="topBar"]/form/div[1]/div[2]/textarea').send_keys(
    '889900008511503,889900008511497,889900008511481,889900008511480')
time.sleep(1)
chaxunanniu = driver.find_element_by_xpath('//*[@id="topBar"]/form/div[6]/button').click()
time.sleep(1)
xuanzedingdanbianhao = driver.find_element_by_xpath('//*[@id="topBar"]/form/div[1]/div[1]/div[1]/i').click()
time.sleep(1)
zidan = driver.find_element_by_xpath('/html/body/div[2]/div/div[1]/ul/li[4]').click()
time.sleep(1)
qingkongshuruzidanhao = driver.find_element_by_xpath('//*[@id="topBar"]/form/div[1]/div[2]/textarea').clear()
time.sleep(1)
shuruzidanbianhao = driver.find_element_by_xpath('//*[@id="topBar"]/form/div[1]/div[2]/textarea').send_keys(
    '319000350159')
time.sleep(1)
chaxunanniu = driver.find_element_by_xpath('//*[@id="topBar"]/form/div[6]/button').click()
time.sleep(1)
xuanzedigndanbianhao = driver.find_element_by_xpath('//*[@id="topBar"]/form/div[1]/div[1]/div[1]/i').click()
time.sleep(1)
wiabudingdanhao = driver.find_element_by_xpath('/html/body/div[2]/div/div[1]/ul/li[3]').click()
time.sleep(1)
qingkongshuruyundanhao1 = driver.find_element_by_xpath('//*[@id="topBar"]/form/div[1]/div[2]/textarea').clear()
time.sleep(1)
shuruwaibudingdanhao = driver.find_element_by_xpath('//*[@id="topBar"]/form/div[1]/div[2]/textarea').send_keys(
    'WAI1231212')
time.sleep(1)
chaxunanniu = driver.find_element_by_xpath('//*[@id="topBar"]/form/div[6]/button').click()
time.sleep(1)
xuanzedingdanbianhao = driver.find_element_by_xpath('//*[@id="topBar"]/form/div[1]/div[1]/div[1]/i').click()
time.sleep(1)
dingdanbianhao = driver.find_element_by_xpath('/html/body/div[2]/div/div[1]/ul/li[2]').click()
time.sleep(1)
qingkongshuruyundanhao = driver.find_element_by_xpath('//*[@id="topBar"]/form/div[1]/div[2]/textarea').clear()
time.sleep(1)
shurudingdanbianhao2 = driver.find_element_by_xpath('//*[@id="topBar"]/form/div[1]/div[2]/textarea').send_keys(
    'CCP171210165407040053,CCP171214201527000040,CCP171214205118000045,CCP171214193856000020')
time.sleep(1)
chaxunanniu = driver.find_element_by_xpath('//*[@id="topBar"]/form/div[6]/button').click()
time.sleep(1)
qingkongshuruyudanhao = driver.find_element_by_xpath('//*[@id="topBar"]/form/div[1]/div[2]/textarea').clear()
time.sleep(2)
xinzeng = driver.find_element_by_xpath('//*[@id="topBar"]/div/button[1]/span').click()
time.sleep(1)
# yundanbianhao=driver.find_element_by_xpath('//*[@id="addDialog"]/form/div[1]/div/div/input').send_keys('A123121212')
waibudanhao = driver.find_element_by_xpath('//*[@id="addDialog"]/form/div[2]/div/div/input').send_keys('WAI1231212')
jijianren = driver.find_element_by_xpath('//*[@id="addDialog"]/form/div[3]/div/div/input').clear()
jijianren = driver.find_element_by_xpath('//*[@id="addDialog"]/form/div[3]/div/div/input').send_keys('笑1笑')
jijiangongsi = driver.find_element_by_xpath('//*[@id="addDialog"]/form/div[4]/div/div/input').clear()
jijiangongsi = driver.find_element_by_xpath('//*[@id="addDialog"]/form/div[4]/div/div/input').send_keys('无敌幸运星')
jijianshouji = driver.find_element_by_xpath('//*[@id="addDialog"]/form/div[5]/div/div/input').clear()
jijianshouji = driver.find_element_by_xpath('//*[@id="addDialog"]/form/div[5]/div/div/input').send_keys('13888888888')
# jijiandizhi=driver.find_element_by_xpath('//*[@id="addDialog"]/form/div[7]/div/div[1]/div[1]/input').click()
# # 省份=driver.find_element_by_tag_name('上海').click()
# 省份=driver.find_element_by_xpath('/html/body/div[3]/div/div[1]/ul/li[5]').click()
xiangxindizhi = driver.find_element_by_xpath('//*[@id="addDialog"]/form/div[8]/div/div[1]/input').clear()
xiangxindizhi = driver.find_element_by_xpath('//*[@id="addDialog"]/form/div[8]/div/div[1]/input').send_keys(
    '江苏省苏州市姑苏区人民路858号')
shoujianren = driver.find_element_by_xpath('//*[@id="addDialog"]/form/div[9]/div/div/input').clear()
shoujianren = driver.find_element_by_xpath('//*[@id="addDialog"]/form/div[9]/div/div/input').send_keys('小白')
shoujiangongsi = driver.find_element_by_xpath('//*[@id="addDialog"]/form/div[10]/div/div/input').send_keys('优速快递')
shoujiandianhua = driver.find_element_by_xpath('//*[@id="addDialog"]/form/div[11]/div/div/input').send_keys(
    '13666666666')
shoujianxiangxindizhi = driver.find_element_by_xpath('//*[@id="addDialog"]/form/div[14]/div/div/input').send_keys(
    '上海市浦东新区世博大道2820号')
jianshu = driver.find_element_by_xpath('//*[@id="addDialog"]/form/div[15]/div/div/input').clear()
jianshu1 = driver.find_element_by_xpath('//*[@id="addDialog"]/form/div[15]/div/div/input').send_keys('1')
zhongliang = driver.find_element_by_xpath('//*[@id="addDialog"]/form/div[16]/div/div/input').clear()
zhongliang = driver.find_element_by_xpath('//*[@id="addDialog"]/form/div[16]/div/div/input').send_keys('2')
daishoukuai = driver.find_element_by_xpath('//*[@id="addDialog"]/form/div[17]/div/div/input').send_keys('10')
daofukuan = driver.find_element_by_xpath('//*[@id="addDialog"]/form/div[18]/div/div/input').send_keys('66')
qianhuidan = driver.find_element_by_xpath('//*[@id="addDialog"]/form/div[20]/div/label/span/span').click()
wupinjiazhi = driver.find_element_by_xpath('//*[@id="addDialog"]/form/div[21]/div/div/input').send_keys('888')
beizhu = driver.find_element_by_xpath('//*[@id="addDialog"]/form/div[22]/div/div/textarea').send_keys('测试数据随便删！！')
xinzenganniiu = driver.find_element_by_xpath(
    '/html/body/div[1]/div[2]/div[2]/div[2]/div/div/div[4]/div[1]/div/div[3]/div/button[2]/span').click()
time.sleep(1)
qingkongshuruyundanhao = driver.find_element_by_xpath('//*[@id="topBar"]/form/div[1]/i').click()
time.sleep(2)
chaxunanniu = driver.find_element_by_xpath('//*[@id="topBar"]/form/div[6]/button').click()
time.sleep(2)
xiugai = driver.find_element_by_css_selector(
    'body > div.app.default > div.uce-layout.flexbox > div.flexbox.right-slide > div.uce-view > div > div > div.el-tabl-flex > div > div.el-table__fixed-right > div.el-table__fixed-body-wrapper > table > tbody > tr:nth-child(1) > td.el-table_1_column_14.is-center > div > a:nth-child(1) > button > span > i').click()
time.sleep(1)
jianshu = driver.find_element_by_xpath('//*[@id="addDialog"]/form/div[15]/div/div/input').clear()
jianshu1 = driver.find_element_by_xpath('//*[@id="addDialog"]/form/div[15]/div/div/input').send_keys('2')
time.sleep(1)
zhongliang = driver.find_element_by_xpath('//*[@id="addDialog"]/form/div[16]/div/div/input').clear()
zhongliang = driver.find_element_by_xpath('//*[@id="addDialog"]/form/div[16]/div/div/input').send_keys('2')
time.sleep(1)
baocun = driver.find_element_by_xpath(
    '/html/body/div[1]/div[2]/div[2]/div[2]/div/div/div[4]/div[1]/div/div[3]/div/button[2]/span').click()
time.sleep(1)
chaxunanniu = driver.find_element_by_xpath('//*[@id="topBar"]/form/div[6]/button').click()
time.sleep(1)
jietu = driver.get_screenshot_as_file("D:\\123.png")
shanchu = driver.find_element_by_xpath(
    '/html/body/div[1]/div[2]/div[2]/div[2]/div/div/div[2]/div/div[4]/div[2]/table/tbody/tr[1]/td[14]/div/a[2]/button/span/i').click()
time.sleep(1)
shanchuqueding = driver.find_element_by_css_selector(
    'body > div.el-message-box__wrapper > div > div.el-message-box__btns > button.el-button.el-button--default.el-button--primary > span').click()
jietu = driver.get_screenshot_as_file("D:\\shanchu.png")
time.sleep(5)
driver.quit()
