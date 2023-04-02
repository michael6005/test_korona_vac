from appium.webdriver.common.appiumby import AppiumBy
from appium import webdriver

class Login:
    def __init__(self, driver: webdriver):
        self.driver = driver

    def btn_transition_otp(self):
        return self.driver.find_element(AppiumBy.ID, "com.ideomobile.maccabi:id/btn_negative")

    def tab_enter_with_password(self):
        return self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "התחברות באמצעות סיסמה")

    def entering_member_id(self):
        return self.driver.find_element(AppiumBy.ID, "com.ideomobile.maccabi:id/textInputEditText")

    def entering_password(self):
        return self.driver.find_element(AppiumBy.ID, "com.ideomobile.maccabi:id/textInputEditTextPassword")

    def btn_enter(self):
        return self.driver.find_element(AppiumBy.ID, "com.ideomobile.maccabi:id/enterButton")

