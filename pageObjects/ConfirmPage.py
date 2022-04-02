from selenium.webdriver.common.by import By


class ConfirmPage:

    def __init__(self, driver):
        self.driver = driver

    location = (By.ID, "country")
    clickIndia = (By.LINK_TEXT,'India')
    agree = (By.XPATH, "//div[@class='checkbox checkbox-primary']")
    purchase = (By.CSS_SELECTOR, "[type='submit']")
    alert = (By.CSS_SELECTOR, "[class*='alert-success']")

    def sendLocValue(self):
        return self.driver.find_element(*ConfirmPage.location)

    def confirmLocVal(self):
        return self.driver.find_element(*ConfirmPage.clickIndia)

    def checktoAgree(self):
        return self.driver.find_element(*ConfirmPage.agree)

    def submittoPurchase(self):
        return self.driver.find_element(*ConfirmPage.purchase)

    def grabAlert(self):
        return self.driver.find_element(*ConfirmPage.alert)