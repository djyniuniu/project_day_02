from appium import webdriver
def get_driver(pac,act):
    desired_caps = {}
    desired_caps['platformName'] = 'Android'
    desired_caps['platformVersion'] = '5.1'
    desired_caps['deviceName'] = '192.168.26.101:5555'
    desired_caps['appActivity'] = act
    desired_caps['appPackage'] = pac
    #允许输入中文
    desired_caps['unicodeKeyboard'] = True
    desired_caps['resetKeyboard'] = True
    #获取toast消息
    desired_caps['automationName'] = 'Uiautomator2'
    #返回driver
    return webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)