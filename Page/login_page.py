from Base.Base import Base_Class
import pytest
import Page,allure
class Login_Page(Base_Class):
    def __init__(self,driver):
        Base_Class.__init__(self,driver)
    @allure.step(title='点击我的按钮')
    def click_my_btn_page(self):
        """
        点击我的
        :return:
        """
        self.click_element(Page.my_btn_xpath)
    @allure.step(title='点击登录注册按钮')
    def click_login_resi_page(self):
        """
        点击登录/注册按钮
        :return:
        """
        self.click_element(Page.login_resign_id)
    @allure.step(title = '输入用户名和密码')
    def input_user_pwd_page(self,phone,passwd):
        """
        输入用户名和密码，并点击登录
        :param username:
        :param pwd:
        :return:
        """
        #输入手机号码
        allure.attach('输入用户信息','账户：%s'% phone)
        self.send_text(Page.input_phone_id,phone)
        #输入密码
        allure.attach('输入用户信息','密码:%s' %passwd)
        self.send_text(Page.input_pwd_id,passwd)
        #点击登录
        self.click_element(Page.sign_btn_id)
    @allure.step(title='退出登录')
    def logout_page(self):
        """
        退出登录按钮
        :return:
        """
        #点击设置按钮
        self.click_element(Page.person_set_id)
        #点击安全退出按钮
        self.click_element(Page.person_logout_id)
    @allure.step(title='关闭登录信息页面')
    def person_input_close_page(self):
        #点击登录信息输入页面的关闭按钮
        self.click_element(Page.log_close_id)
    @allure.step(title='判断我的订单是否存在')
    def if_order_page(self):
        """
        判断我的订单按钮是否存在
        :return:
        """

        try:
            self.search_element(Page.my_order_btn)
            allure.attach('订单状态','存在')
            assert True
        except Exception as e:
            print(e)
            allure.attach('订单状态','不存在')
            assert False







