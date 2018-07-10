#页面中的元素
from selenium.webdriver.common.by import By

#定位我的按钮
my_btn_xpath = (By.ID,"//*[contains(@text,'我的') and contains(@resource-id,'com.tpshop.malls:id/tab_txtv')]")
"""
登录输入信息页面
"""
#登录注册按钮
login_resign_id = (By.ID,'com.tpshop.malls:id/nickname_txtv')
#账号输入框
input_phone_id = (By.ID,'com.tpshop.malls:id/edit_phone_num')
#密码输入框
input_pwd_id = (By.ID,'com.tpshop.malls:id/edit_password')
#登录按钮
sign_btn_id = (By.ID,'com.tpshop.malls:id/btn_login')
#登录输入信息点击关闭按钮
log_close_id = (By.ID,'com.tpshop.malls:id/titlebar_back_rl')

"""
个人中心设置按钮
"""
#我的订单按钮定位
my_order_btn = (By.XPATH, "//*[contains(@text,'我的订单') and contains(@resource-id,'com.tpshop.malls:id/title_txtv')]")
"""
设置页面
"""
#登录成功后，个人中心设置页面的设置按钮
person_set_id = (By.ID,'com.tpshop.malls:id/setting_btn')
#设置页面的安全退出
person_logout_id = (By.ID,'com.tpshop.malls:id/setting_btn')

