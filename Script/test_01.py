import allure
class Test_Png:

    def test_001(self):

        assert 0
    def test_002(self):
        assert 1
with open('./Screen/appium.png','rb') as f:
    allure.attach('图片名字',f.read(),allure.attach_type.PNG)
