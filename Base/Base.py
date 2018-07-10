from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
class Base_Class(object):
    def __init__(self,driver):
        self.driver = driver
    def search_element(self,loc,timeout = 10,poll = 1):
        """定位单个元素

        :param loc: 传入的是一个元组格式比如：（ID,'ID值'）
        :param timeout: 显示等待方法中的超时时间设置
        :param poll: 显示等待方法中间隔时间进行请求设置
        :return:
        """
        #使用显示等待进行查找元素
        WebDriverWait(self.driver,timeout,poll).until(lambda x : x.find_element(*loc))
    def search_elements(self,loc,timeout = 10,poll = 1):
        """
        定位多个元素
        :param loc:
        :param timeout:
        :param poll:
        :return:
        """
        WebDriverWait(self.driver,timeout,poll).until(lambda x :x.find_elemts(*loc))
    def click_element(self,loc):
        """
        对定位到的元素进行点击操作
        :param loc:
        :return:
        """
        #点击查找到的元素
        self.search_element(loc).click()
    def send_text(self,loc,text):
        """
        定位到元素后进行输入内容操作
        :param loc:
        :param text:
        :return:
        """
        #定位到元素，并存放到一个变量中
        input_text = self.search_element(loc)
        #对定位到的元素进行清空操作
        input_text.clear()
        #对定位到的元素进行输入操作
        input_text.send_text(text)
    def get_toast(self,message):
        #获取toast消息
        #如果获取不到，就会返回False
        try:
            xpath = "//*[contains(@text,{})]".format(message)
            toast_message = self.search_element((By.ID,xpath),timeout=5,poll=0.1)
            return  toast_message.text
        except Exception as e:
            return False
