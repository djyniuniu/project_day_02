from Page.login_page import Login_Page
import pytest
from Base.get_driver import get_driver
import yaml
from Base.read_data import Op_Data
def get_data():
    data_list = []
    data = Op_Data('data.yaml').read_data().get('Login_in')
    for i in data:
        for o in i.keys():
            data_list.append((o, i.get(o).get('phone'), i.get(o).get('passwd'), i.get(o).get('toast_mess'),
                              i.get(o).get('expect_mess'), i.get(o).get('tag')))
        return data_list

class Test_Log(object):
    def setup_class(self):
        """
        点击我的
        :return:
        """
        self.obj_page = Login_Page(get_driver('com.tpshop.malls', '.SPMainActivity'))
        self.obj_page.click_my_btn_page()
    def teardown_class(self):
        """
        关闭应用
        :return:
        """
        self.obj_page.driver.quit()
    @pytest.mark.parametrize('phone,pwd,toast_mess,expect_mess,tag',get_data())
    def test_login(self,phone,pwd,toast_mess,expect_mess,tag):
        """

        :param phone: 输入账号
        :param pwd:输入密码
        :param toast_mess:获取toast传参
        :param expect_mess:登录后期望toast
        :param tag:标记执行成功测试用例
        :return:
        """

        #点击登录/注册按钮
        self.obj_page.click_login_resi_page()
        #进入到输入手机号和密码的登录页面
        #输入手机号,#输入密码
        self.obj_page.input_user_pwd_page(phone,pwd)
        if tag:
            try:
                #获取登录成功toast消息
                suc_mess = self.obj_page.get_toast(toast_mess)
                #获取登录成功我的订单状态
                order_state = self.obj_page.if_order_page()
                #点击退出登录
                self.obj_page.logout_page()
                assert suc_mess == expect_mess and order_state
            except Exception as e:
                #如果获取获取不到以上信息,就关闭登录信息输入页面
                print(e)
                self.obj_page.person_input_close_page()
        else:
            try:
                #获取登录失败toast消息
                fail_mess = self.obj_page.get_toast(toast_mess)
                if fail_mess:
                    assert fail_mess == expect_mess
                else:
                    return False
            finally:
                self.obj_page.person_input_close_page()



