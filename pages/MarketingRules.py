import allure, time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import StaleElementReferenceException
from resources.variables import *


class MarketingRulesPage:
    headerMarketingRules = (By.XPATH, '//li[@class="menu menu-label"]//a[@id="Marketing Rules"]')
    bannerImage = (By.XPATH, '//div[@class="header"]/img')
    bannerText = (By.XPATH, '//div[@class="container"]/h2')
    downloadButton = (By.XPATH, '//p/a[contains(text(),"Download PDF")]')
    staticText = (By.XPATH, '//ul[@class="privacy-policy-list"]')

    def __init__(self, browser):
        self.browser = browser

    #@allure.step('Verify Marketing Rules page get open')
    def verify_marketing_rules_page(self):
        WebDriverWait(self.browser, 80).until(EC.presence_of_element_located(self.headerMarketingRules))
        self.browser.find_element(*self.headerMarketingRules).click()
        WebDriverWait(self.browser, 80).until(EC.presence_of_element_located(self.bannerImage))
        banner_image = self.browser.find_element(*self.bannerImage).is_displayed()
        return banner_image

    #@allure.step('Verify Marketing banner-image is present')
    def verify_banner_image(self):
        banner_image = self.browser.find_element(*self.bannerImage).is_displayed()
        return banner_image

    #@allure.step('Verify Marketing banner-text is present')
    def verify_banner_text(self):
        banner_text = self.browser.find_element(*self.bannerText).is_displayed()
        return banner_text

    #@allure.step('Verify download pdf button')
    def verify_download_button(self):
        time.sleep(1)
        download_pdf_button = self.browser.find_elements(*self.downloadButton)
        time.sleep(2)
        return len(download_pdf_button)

    #@allure.step('Verify static-text is present')
    def verify_static_text(self):
        static_text = self.browser.find_element(*self.staticText).is_displayed()
        return static_text




