# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re

class BookingcomNextPage(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.base_url = "https://www.booking.com/"
        self.verificationErrors = []
        self.accept_next_alert = True
    
    def test_bookingcom_next_page(self):
        driver = self.driver
        driver.get(self.base_url + "/index.zh-tw.html?label=gen173nr-1DCAEoggJCAlhYSDNiBW5vcmVmaOcBiAEBmAEwuAEHyAEP2AED6AEBkgIBeagCAw;sid=869c62621e3d43712c1fbc29cfed3288;sb_price_type=total&")
        driver.find_element_by_id("ss").click()
        driver.find_element_by_id("ss").clear()
        driver.find_element_by_id("ss").send_keys("hk")
        driver.find_element_by_xpath("//form[@id='frm']/div[2]/div/div/ul/li").click()
        driver.find_element_by_css_selector("button.sb-searchbox__button.").click()
        driver.find_element_by_id("close_map_lightbox").click()
        driver.find_element_by_link_text(u"下一頁").click()
        driver.find_element_by_link_text(u"下一頁").click()
        driver.find_element_by_link_text(u"下一頁").click()
    
    def is_element_present(self, how, what):
        try: self.driver.find_element(by=how, value=what)
        except NoSuchElementException as e: return False
        return True
    
    def is_alert_present(self):
        try: self.driver.switch_to_alert()
        except NoAlertPresentException as e: return False
        return True
    
    def close_alert_and_get_its_text(self):
        try:
            alert = self.driver.switch_to_alert()
            alert_text = alert.text
            if self.accept_next_alert:
                alert.accept()
            else:
                alert.dismiss()
            return alert_text
        finally: self.accept_next_alert = True
    
    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()
