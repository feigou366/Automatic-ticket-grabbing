from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import time
from time import sleep
from splinter.browser import Browser
import traceback
from selenium.webdriver import ActionChains


#用户名，密码
username = u"你的用户名"
passwd = u"你的密码"

#输入相应的cookies
starts = u"%u6DF1%u5733%2CSZQ"
ends = u"%u8572%u6625%2CQRN"

#设置时间
dtime = u"你的日期" #2019-01-30

#车次，选择第几趟，0则从上到下依次点击
order = 0

#乘客名
pa = u"你的名字"

"""网址"""
ticket_url = "https://kyfw.12306.cn/otn/leftTicket/init"
login_url = "https://kyfw.12306.cn/otn/login/init"
initmy_url = "https://kyfw.12306.cn/otn/index/initMy12306"

# 前台开启浏览器模式
def openChrome():
    # 加启动配置
    option = webdriver.ChromeOptions()
    option.add_argument('disable-infobars')
    # 打开chrome浏览器
    driver = webdriver.Chrome(chrome_options=option)
    return driver

# 授权操作
def operationAuth(driver):


    url = "https://kyfw.12306.cn/otn/login/init"
    driver.get(url)
    # 找到输入框并输入查询内容
    elem = driver.find_element_by_id("username")
    elem.send_keys(u"你的用户名")
    elem = driver.find_element_by_id("password")
    elem.send_keys(u"你的密码")
    print("请输入验证码，准备登录...")
    sleep(4)
    # 提交表单
    driver.find_element_by_xpath("// *[ @ id = 'loginSub']").click()


    sleep(3)
    ActionChains(driver).move_to_element(driver.find_element_by_link_text("车票")).perform()
    time.sleep(2)
    driver.find_element_by_link_text("单程").click()
    elem = driver.find_element_by_id("fromStationText")

    driver.find_element_by_xpath("// *[@id = 'fromStationText']").click()
    elem.send_keys(u"深圳")
    driver.find_element_by_xpath("//*[@id='citem_0']").click()

    driver.find_element_by_xpath("// *[@id = 'toStationText']").click()
    elem = driver.find_element_by_id("toStationText")
    elem.send_keys(u"江西")
    driver.find_element_by_xpath("//*[@id='citem_0']").click()
    # elem = driver.find_element_by_id("train_date")
    # elem.send_keys(u"江西")

    driver.find_element_by_xpath("//*[@id='date_icon_1']").click()
    sleep(1)

    driver.find_element_by_xpath("/html/body/div[34]/div[1]/div[2]/div[31]/div").click()
    driver.find_element_by_xpath("//*[@id='cc_start_time']").click()
    driver.find_element_by_xpath("//*[@id='cc_start_time']/option[4]").click()

    driver.find_element_by_xpath("//*[@id='_ul_station_train_code']/li[3]/label").click()

    driver.find_element_by_xpath("//*[ @ id = '_ul_station_train_code'] / li[4]/label").click()
    driver.find_element_by_xpath("// *[ @ id = '_ul_station_train_code'] / li[5] / label").click()
    driver.find_element_by_xpath("// *[ @ id = '_ul_station_train_code'] / li[6] / label").click()

    sleep(1)
    driver.find_element_by_xpath("//*[@id='query_ticket']").click()

    print('login success！')
    a = 1
    while a<50:
        sleep(1.5)
        driver.find_element_by_xpath("//*[@id='query_ticket']").click()
        a+=1
