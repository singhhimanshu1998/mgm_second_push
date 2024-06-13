"""
This module contains the page object
for the homepage.
"""

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from appium.webdriver.webdriver import WebDriver
import allure
from pathlib import Path
import csv
import time
from pages.testrail import APIClient
import datetime


class loginpage:
    """
    Define all web element locators and test steps
    in this class for homepage
    """

    verify_login_title = (By.XPATH, "//h1[@class='login-text']")
    carousal_image = (By.XPATH, "//div[@class='auth-component']")
    accept_cookies = (By.XPATH, '//button[@id="onetrust-accept-btn-handler"]')
    email_textbox = (By.XPATH, "//input[@name='username']")
    next_button = (By.XPATH, "//div/input[@value='Next']")
    verify_button = (By.XPATH, '//div/input[@value="Verify"]')
    remember_me = (By.XPATH, '//div[@class="custom-checkbox"]')
    remember_me_selected = (By.XPATH, '//*[contains(text(),"Remember me")]')

    email_empty = (By.XPATH, '//p[@role="alert"]')
    request_an_account = (By.XPATH, '//div/a[contains(text(),"Create an account")]')
    enter_password = (By.XPATH, "//input[@type='password']")
    # logout_button = (By.XPATH, "//li[@class='col col-lg-2']//button[@class='user-logout-btn']")
    logout_button = (By.XPATH, "//span[contains(text(),'log out')]")
    dropdown_logout_toggle = (By.XPATH, "//button[contains(@class,'dropdown-toggle btn')]")
    continue_button = (By.XPATH, "//button[normalize-space()='CONTINUE']")
    cancel_button = (By.XPATH, "//button[text()='CANCEL']")
    today = datetime.datetime.now()
    global today_date
    current_date = today.strftime("%d")
    current_month = today.strftime("%m")
    current_year = today.year
    current_hour = today.strftime("%I")
    currnt_minute = today.strftime("%M")
    current_time = today.strftime("%p")
    today_date = current_date + "/" + current_month + "/" + str(current_year) + " - " + current_hour + ":" + currnt_minute + " " + current_time


    def get_url(self, new_url):
        URL = new_url
        print("from page file",URL)


    def __init__(self, browser):
        self.browser = browser
        #self.browser = WebDriver

    global client
    global run_id
    run_id = None
    client = APIClient('https://mgmstudios.testrail.io/')
    client.user = 'digadmin@mgm.com'
    client.password = 'MGMstudios4eva!'



    # def createTestRun(self,test_ids=[]):
    #     response = client.send_post(
    #         'add_run/1',
    #         {'name': "MGM ROAR - Home Page and My list  - " + today_date,
    #          'include_all': False,
    #          # 'status_id': 1, 'comment': 'This test worked fine!',
    #          'case_ids': test_ids
    #          }
    #     )
    #     global run_id
    #     run_id = str(response["id"])
    #
    # def createTestRunAssets(self, test_ids=[]):
    #     response = client.send_post(
    #         'add_run/1',
    #         {'name': "MGM ROAR - Assets and My Cart  - " + today_date,
    #          'include_all': False,
    #          # 'status_id': 1, 'comment': 'This test worked fine!',
    #          'case_ids': test_ids
    #          }
    #     )
    #     global run_id
    #     run_id = str(response["id"])
    #
    # def createTestRun3(self, test_ids=[]):
    #     response = client.send_post(
    #         'add_run/1',
    #         {'name': "MGM ROAR - Film & Series and Marketing Rules  - " + today_date,
    #          'include_all': False,
    #          # 'status_id': 1, 'comment': 'This test worked fine!',
    #          'case_ids': test_ids
    #          }
    #     )
    #     global run_id
    #     run_id = str(response["id"])

    def createTestRun(self, test_ids=[]):
        response = client.send_post(
            'add_run/1',
            {'name': "MGM ROAR - " + today_date,
             'include_all': False,
             # 'status_id': 1, 'comment': 'This test worked fine!',
             'case_ids': test_ids
             }
        )
        global run_id
        run_id = str(response["id"])

    def closeTestRun(self):
        global run_id
        response = client.send_post(
            'close_run/' + run_id,
            {}
        )

    def updateTestCase(self, testCaseId, my_comment, result):
        global run_id
        if result == "pass":
            status = 1
        elif result == "fail":
            status = 5
        # else:
        # self.log.failed("Unknows Status ID for TestRail test update. Please use 'pass' or 'fail' for the tests.")
        # print(testCaseId)
        # print(run_id)
        response = client.send_post(
            'add_result_for_case/' + str(run_id) + '/' + str(testCaseId),
            {
                'status_id': status,
                'comment': my_comment
            }
        )


    def case_fields(self, testid):
        print("test id-------------------------->", testid)
        global run_id
        response = client.send_get(
            'get_case/' + testid
        )
        print("printing response.")
        # print json.dumps(response, sort_keys=True, indent=4)
        print("Title")
        print
        response["title"]
        print("Steps:-")
        print
        response["custom_steps"]
        print("Expected Output:")
        print
        response["custom_expected"]

    #@allure.step('Load Login page When user hit ROAR app url ')
    def load_url(self, URL):
        self.browser.get(URL)
        WebDriverWait(self.browser, 300).until(EC.presence_of_element_located(self.verify_login_title))
        verify = self.browser.find_element(*self.verify_login_title).text
        return verify

    #@allure.step('verify carousel image set by admin')
    def CarouselImage(self):
        WebDriverWait(self.browser, 10).until(EC.presence_of_element_located(self.carousal_image))
        verify_image = self.browser.find_element(*self.carousal_image).is_displayed()
        WebDriverWait(self.browser, 10).until(EC.presence_of_element_located(self.accept_cookies))
        time.sleep(2) #5
        self.browser.find_element(*self.accept_cookies).click()
        return verify_image

    #@allure.step('On each visit user see different carousel image ')
    def DifferentCarouselImage(self):
        time.sleep(2)
        FirstImage = self.browser.find_element(*self.carousal_image).get_attribute("style")
        self.browser.refresh()
        time.sleep(2)
        SecondImage = self.browser.find_element(*self.carousal_image).get_attribute("style")
        self.browser.refresh()
        time.sleep(2)
        ThirdImage = self.browser.find_element(*self.carousal_image).get_attribute("style")


        if(FirstImage == SecondImage and SecondImage == ThirdImage):
            return False
        else:
            return True

    #@allure.step('Verify Email box present in login model')
    def VerifyEmail(self):
        WebDriverWait(self.browser, 5).until(EC.presence_of_element_located(self.email_textbox))
        return self.browser.find_element(*self.email_textbox).is_displayed()

    #@allure.step('Verify Next button present in login model')
    def VerifyNextButton(self):
        WebDriverWait(self.browser, 5).until(EC.presence_of_element_located(self.next_button))
        return self.browser.find_element(*self.next_button).is_displayed()

    #@allure.step('Verify Request an account button present in login model')
    def VerifyRequestAnAccount(self):
        WebDriverWait(self.browser, 5).until(EC.presence_of_element_located(self.request_an_account))
        return self.browser.find_element(*self.request_an_account).is_displayed()

    #@allure.step('Verify remember-me checkbox present in login model')
    def VerifyRememberMe(self):
        WebDriverWait(self.browser, 5).until(EC.presence_of_element_located(self.remember_me))
        return self.browser.find_element(*self.remember_me).is_displayed()

    #@allure.step('Verify user is able to enter Email in email field')
    def EnterEmail(self, username):
        WebDriverWait(self.browser, 10).until(EC.presence_of_element_located(self.email_textbox))
        self.browser.find_element(*self.email_textbox).clear()
        time.sleep(1)
        self.browser.find_element(*self.email_textbox).send_keys(username)

    #@allure.step('Verify user is able to enter Email in email field')
    def ClickOnAcceptCookies(self):
        time.sleep(3)
        try:
            accept_cookies = self.browser.find_element(*self.accept_cookies).is_displayed()
            if accept_cookies:
                self.browser.find_element(*self.accept_cookies).click()
        except:
            print('cookies popup not present')


    #@allure.step('Verify user is able to enter Email in email field')
    def ClickOnRememberMe(self):
        self.browser.find_element(*self.remember_me).click()
        time.sleep(1.5)
        remember_checkbox = self.browser.find_element(*self.remember_me_selected).get_attribute("class")
        return remember_checkbox

    #@allure.step('reload the login page')
    def LoginPage(self, URL):
        self.browser.get(URL)
        # time.sleep(5)
        WebDriverWait(self.browser, 300).until(EC.presence_of_element_located(self.email_textbox))

    #@allure.step('Verify user without email-Id can not proceed to next step ')
    def ClickNextValidation(self):
        self.browser.find_element(*self.next_button).click()
        WebDriverWait(self.browser, 5).until(EC.presence_of_element_located(self.email_empty))
        email_validation = self.browser.find_element(*self.email_empty).text
        return email_validation

    #@allure.step('Verify user with valid email id can proceed to next step')
    def ClickNext(self):
        WebDriverWait(self.browser, 30).until(EC.presence_of_element_located(self.next_button))
        self.browser.find_element(*self.next_button).click()
        WebDriverWait(self.browser, 30).until(EC.presence_of_element_located(self.enter_password))
        return self.browser.find_element(*self.enter_password).is_displayed()

    #@allure.step('Verify user with valid email id can proceed to next step')
    def verifyButton(self):
        WebDriverWait(self.browser, 8).until(EC.presence_of_element_located(self.verify_button))
        self.browser.find_element(*self.verify_button).click()


    #@allure.step('verify user is successfully logged in')
    def EnterPassword(self, password):
        time.sleep(1)
        WebDriverWait(self.browser, 30).until(EC.presence_of_element_located(self.enter_password))
        self.browser.find_element(*self.enter_password).send_keys(password)
        # time.sleep(3)

    #@allure.step('verify user is successfully logged in')
    def ValidateUrlForNextPage(self):
        time.sleep(4)
        url = self.browser.current_url
        print('urllll', url)
        return url

    #@allure.step('Verify confirmation page ')
    def confrimation_page_without_elements(self):
        print("before sec")
        time.sleep(120)
        print("after sec")
        try:
            url = self.browser.current_url
            if 'home' in url:
                return
            else:
                continueButton = self.browser.find_element(*self.continue_button)
                continueButton.click()
                print("clicked on continue button")
        except:
            try:
                self.browser.refresh()
                time.sleep(30)
                url = self.browser.current_url
                if 'home' in url:
                    return
                else:
                    continueButton = self.browser.find_element(*self.continue_button)
                    continueButton.click()
                    print("clicked on continue button")
            except:
                try:
                    self.browser.refresh()
                    time.sleep(30)
                    url = self.browser.current_url
                    if 'home' in url:
                        return
                    else:
                        continueButton = self.browser.find_element(*self.continue_button)
                        continueButton.click()
                        print("clicked on continue button")
                except:
                    self.browser.refresh()
                    time.sleep(30)
                    print("Page Reloded")


    #@allure.step('verify user can click on confrimation page')
    def confrimation_page_elements(self):
        try:
            time.sleep(1)
            continueButton = self.browser.find_element(*self.continue_button)
            if continueButton.is_displayed():
                continueButton.click()
                print("already login")
        except:
            print("new login")


    #@allure.step('verify user is successfully logged in')
    def VerifyLogin(self):
        WebDriverWait(self.browser, 45).until(EC.presence_of_element_located(self.dropdown_logout_toggle))
        time.sleep(1.5)
        return self.browser.find_element(*self.dropdown_logout_toggle).is_displayed()

        '''with open(self.license_file, mode='a', newline='') as csvFile:
            csv_writer = csv.writer(csvFile)
            csv_writer.writerow([abc])
        ##print(len(jobs))
        ##print(abc)'''

