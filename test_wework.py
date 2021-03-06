from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class TestWework:
    def setup(self):
        desired_caps = {}
        desired_caps['platformName'] = 'Android'
        desired_caps['platformVersion'] = '6.0'
        desired_caps['deviceName'] = 'emulator-5554'
        desired_caps['appPackage'] = 'com.tencent.wework'
        desired_caps['appActivity'] = '.launch.WwMainActivity'
        desired_caps['noReset'] = 'true'
        # desired_caps['dontStopAppOnReset'] = 'true'
        desired_caps['skipDeviceInitialization'] = 'true'
        desired_caps['unicodeKeyBoard'] = 'true'  # 输入中文
        desired_caps['resetKeyBoard'] = 'true'
        desired_caps['settings[waitForIdleTimeout]']= 0 # 取消定位动态页面等待时间
        self.driver = webdriver.Remote('http://0.0.0.0:4723/wd/hub', desired_caps)
        self.driver.implicitly_wait(10)

    def teardown(self):
        self.driver.quit()

    def test_daka(self):
        self.driver.find_element_by_xpath('//*[@resource-id="com.tencent.wework:id/dqn" and @text="工作台"]').click()
        self.driver.find_element_by_android_uiautomator('new UiScrollable(new UiSelector().'
                                                        'scrollable(true).instance(0)).'
                                                        'scrollIntoView(new UiSelector().text("打卡").'
                                                        'instance(0));').click()

        self.driver.find_element_by_xpath('//*[@text="外出打卡"]').click()

    def test_addconnect(self):
        self.driver.find_element_by_xpath('//*[@text="通讯录"]').click()
        self.driver.find_element_by_android_uiautomator('new UiScrollable(new UiSelector().'
                                                        'scrollable(true).instance(0)).'
                                                        'scrollIntoView(new UiSelector().text("添加成员").'
                                                        'instance(0));').click()
        self.driver.find_element(MobileBy.XPATH, '//*[@text="手动输入添加"]').click()
        self.driver.find_element(MobileBy.XPATH, '//*[@resource-id="com.tencent.wework:id/au0" and @text="必填"]').send_keys("Test1")
        self.driver.find_element(MobileBy.XPATH, '//*[@resource-id="com.tencent.wework:id/aut" and @text="男"]').click()

        locator = (MobileBy.XPATH, '//*[@resource-id="com.tencent.wework:id/dqn" and @text="男"]')
        ele = WebDriverWait(self.driver, 10).until(expected_conditions.element_to_be_clickable(locator))
        ele.click()
        self.driver.find_element_by_xpath('//*[@text="手机号"]').send_keys(13388889999)
        self.driver.find_element_by_xpath('//*[@text="保存"]').click()

