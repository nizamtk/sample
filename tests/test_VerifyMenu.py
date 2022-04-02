import pytest
from selenium.webdriver.common.by import By

from TestData.HomePageData import HomePageData
from utilities.BaseClass import BaseClass
from selenium.webdriver import ActionChains


class TestVerifyMenu(BaseClass):

    def test_submenu(self, getData):
        log = self.getLogger()
        action = ActionChains(self.driver)
        log.info("Moving cursor to parent menu" + getData["MainMenu"])
        action.move_to_element(self.driver.find_element(By.LINK_TEXT, getData['MainMenu'])).perform()
        log.info("Find child menu and click" + getData["SubMenu"])
        self.driver.find_element(By.LINK_TEXT, getData['SubMenu']).click()



    @pytest.fixture(params=HomePageData.test_HomePage_data)
    def getData(self, request):
        return request.param



