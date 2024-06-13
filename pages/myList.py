import allure, time
from selenium.webdriver.common.by import By
from selenium.common.exceptions import StaleElementReferenceException, NoSuchElementException
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from resources.variables import *
from pathlib import Path
from os import path
import os
import csv


class myListObj:
    my_list_active = (By.XPATH, '//li[@class="menu menu-label"]/a[@id="My Lists"]')
    list_name = (By.XPATH, "//span[@class='view-title']")
    share_button = (By.XPATH, "//button[span[contains(text(),'Email Spreadsheet')]]")
    delete_button = (By.XPATH, "//button/span[contains(text(), 'Delete')]")
    delete_direct_mylist = (By.XPATH, '//div/button[contains(text()," Delete List ")]')
    delete_title_mylist = (By.XPATH, '//div/button[contains(text()," Delete Title ")]')
    delete_1text = (By.XPATH, "//h3[@classs='header-text']")
    share_list_success_text = (By.XPATH, "//span[contains(text(),' Your List Shared Successfully! ')]")
    delete_list = (By.XPATH, "//li[@class='sub-title ng-star-inserted']")
    delete_2text = (By.XPATH, "//p[@class='directions ng-star-inserted']")
    dlt_btn = (By.XPATH, "//div[contains(@class,'delete-btn')]/button[contains(text(), 'Delete List')]")
    cncl_btn = (By.XPATH, "//div[contains(@class,'delete-btn')]/button[contains(text(), 'Cancel')]")
    list_check = (By.XPATH, "//div[contains(@class,'container')]//div[@class='checkbox-shell-dark']/input["
                            "@id='select-all']")
    add_list = (By.XPATH, "//button[@id='dropdownForm1']")
    delete_close = (By.XPATH, "//div[@class='close-x desk-close']//img[@class='close-btn-image']")
    close_popup = (By.XPATH, "//div[@class='share-input']//img[@ class ='close-btn-image']")
    static_topText = (By.XPATH, "//div[@class='share-header']")
    pop_list = (By.XPATH, "//div[@class='share-body ng-star-inserted']")
    static_2Text = (By.XPATH, "//div[@class='share-list']")
    email_textbox = (By.XPATH, '//div[@role="combobox"]/input[@type="text"]')
    share_btn = (By.XPATH, '//div[@class="listing"]//button[contains(@class,"share-btn")]')
    email_address = (By.XPATH, '//span[contains(text(),"Add email")]')
    autoRand_list = (By.XPATH, "//a[contains(text(),'" + new_List_name + "')]")  # new_List_name
    demo_list = (By.XPATH, "//a[contains(text(),'Demo')]")
    addMail = (By.XPATH, '//span[contains(text(),"automation@practicallogix.com")]')
    test2_list = (By.XPATH, "//a[contains(text(),'test2')]")
    test1_list = (By.XPATH, "//a[contains(text(),'test1')]")
    delete_list_confirmation_text = (By.XPATH, '//div/h3[contains(text(),"Delete List")]')
    delete_title_list_confirmation_text = (By.XPATH, '//div/h3[contains(text(),"Delete Title")]')
    download = (By.XPATH, "//button/span[contains(text(),'DOWNLOAD .XLSX')]")
    share_popup = (By.XPATH, "//span[contains(text(),'SHARE LIST')]")
    share_title = (By.XPATH, "//span[contains(text(),'EMAIL .XLSX')]")
    mylist_tab = (By.XPATH, "//ul[@class='menu-items']//a[@id='My Lists']")
    # family_chkvox = (By.XPATH, "//div[a[contains(text(),'Family')]]//parent::div[1]/input[1]")
    # family_chkvox = (By.XPATH, "//div[a[contains(text(),'Blockbusters')]]//parent::div[1]/input[1]")
    family_chkvox = (By.XPATH, "//div[div[p[contains(text(),'Special Lists Made For You')]]]/following-sibling::div["
                               "1]/div[1]//div[@class='checkbox-shell-dark']/input[1]")
    demo_check = (By.XPATH, "//div[p[text()='Your Lists']]/following-sibling::div[1]/div[3]//mgm-checkbox-single["
                            "1]/div[1]/input[1]")
    delete_popup = (By.XPATH, "//button[contains(text(),'DELETE')]")
    movie_1chkbox = (By.XPATH, "//ul[@class='movie-card']/li[1]/div[1]/mgm-checkbox-single/div[1]/input[1]")
    addTOlist = (By.XPATH, "//span[contains(text(),'ADD TO LIST')]")
    newly_name_chkbx = (By.XPATH, "//a[contains(text(),'" + delete_listtt + "')]//parent::div["
                                                                            "1]/preceding-sibling::mgm-checkbox"
                                                                            "-single/div/input[1]")
    # share_confirmation = (By.XPATH, "//div[@class='comfirmation-body']/h5[1]")
    share_confirmation = (By.XPATH, "//span[contains(text(),' Your List Shared Successfully! ')]")
    delete_success = (By.XPATH, "//h3[contains(text(),'Delete List ')]")
    titlesNum_header = (By.XPATH, "//div[@class='list-name']/span[contains(text(),'title')]")
    share_popup_footer = (By.XPATH, "//button/span[contains(text(),'EMAIL SPREADSHEET')]")

    def __init__(self, browser):
        self.browser = browser

    #@allure.step('Verify List name in list table ')
    def verify_listName(self):
        WebDriverWait(self.browser, 15).until(EC.presence_of_element_located(self.list_name))
        return self.browser.find_element(*self.list_name).text

    #@allure.step('Click share button in right top ')
    def click_shareButton(self):
        WebDriverWait(self.browser, 4).until(EC.presence_of_element_located(self.share_button))
        self.browser.find_element(*self.share_button).click()


    #@allure.step('Click on delete button from popup')
    def click_deleteButton(self):
        time.sleep(2)
        self.browser.find_element(*self.delete_button).click()

    #@allure.step('Click on delete button from popup')
    def click_direct_deleteButton(self):
        time.sleep(1.5)
        self.browser.find_element(*self.delete_direct_mylist).click()

    # @allure.step('Click on delete button from popup')
    def click_direct_deleteButton_title(self):
        time.sleep(1.5)
        self.browser.find_element(*self.delete_title_mylist).click()

    #@allure.step('Click on delete button from popup')
    def click_direct_deleteButton_js(self):
        time.sleep(8) # due to un_catch issue
        WebDriverWait(self.browser, 95).until(EC.presence_of_element_located(self.delete_direct_mylist))
        recently = self.browser.find_element(*self.delete_direct_mylist)
        self.browser.execute_script("arguments[0].click();", recently)


    #@allure.step('Click on delete button from popup')
    def click_title_direct_deleteButton(self):
        time.sleep(1.5)
        self.browser.find_element(*self.delete_title_mylist).click()

    #@allure.step('Verify Add to List tab in footer popup')
    def verify_addList(self):
        time.sleep(2)
        return self.browser.find_element(*self.add_list).is_displayed()

    #@allure.step('Verify Add to List tab in footer popup')
    def verify_myList_Active(self):
        time.sleep(1.5)
        class_text = self.browser.find_element(*self.my_list_active).get_attribute('class')
        return class_text

    #@allure.step('Verify Close button in opened Pop after clicking on share button ')
    def verify_closeBtn(self):
        time.sleep(2)
        return self.browser.find_element(*self.close_popup).is_displayed()

    #@allure.step('Verify Static top Text in in share in share popup ')
    def verify_staticToptext(self):
        time.sleep(2)
        return self.browser.find_element(*self.static_topText).is_displayed()

    #@allure.step('Verify List name and numbers of title in it ')
    def verify_lisTitle(self):
        time.sleep(2)
        return self.browser.find_element(*self.pop_list).is_displayed()

    #@allure.step('Verify Static text in middle in share popup ')
    def verify_staticTextmiddle(self):
        time.sleep(2)
        return self.browser.find_element(*self.static_2Text).is_displayed()

    #@allure.step('Verify Email textbox in share popup ')
    def verify_emailTextbox(self):
        time.sleep(2)
        return self.browser.find_element(*self.email_textbox).is_displayed()

    #@allure.step('Verify Share button in share popup ')
    def verify_button(self):
        time.sleep(2)
        return self.browser.find_element(*self.share_btn).is_displayed()

    #@allure.step('Enter email id in share list popup ')
    def enter_email(self, em):
        WebDriverWait(self.browser, 30).until(EC.presence_of_element_located(self.email_textbox))
        time.sleep(1.5)
        self.browser.find_element(*self.email_textbox).clear()
        self.browser.find_element(*self.email_textbox).send_keys(em)

    #@allure.step('Click on button to share list on email')
    def click_add_email_address(self):
        time.sleep(1)
        self.browser.find_element(*self.email_address).click()

    #@allure.step('Click on button to share list on email')
    def click_add_email_address_list(self):
        time.sleep(2)
        self.browser.find_element(*self.addMail).click()

    #@allure.step('Click on button to share list on email')
    def click_buttonToshare(self):
        time.sleep(.5)
        self.browser.find_element(*self.share_btn).click()

    #@allure.step('Verify User can share spreadsheet through click on share button')
    def click_shareList(self):
        time.sleep(.5)
        self.browser.find_element(*self.share_popup_footer).click()

    #@allure.step('Verify Static top Text  in delete popup ')
    def verify_share_list_success(self):
        WebDriverWait(self.browser, 40).until(EC.presence_of_element_located(self.share_list_success_text))
        return self.browser.find_element(*self.share_list_success_text).is_displayed()

    #@allure.step('Verify Static top Text  in delete popup ')
    def verify_deleteToptext(self):
        time.sleep(1.5)
        return self.browser.find_element(*self.delete_1text).is_displayed()

    #@allure.step('Verify List name and numbers of title in delete pop up ')
    def verify_deleteTitle(self):
        time.sleep(1.5)
        return self.browser.find_element(*self.delete_list).is_displayed()

    #@allure.step('Verify Static text in middle in delete popup ')
    def verify_deleteTextmiddle(self):
        time.sleep(2)
        return self.browser.find_element(*self.delete_2text).is_displayed()

    #@allure.step('Verify Delete button in delete popup')
    def verify_deleteBtnPop(self):
        time.sleep(.5)
        return self.browser.find_element(*self.dlt_btn).is_displayed()

    #@allure.step('Click on delete button to delete that list')
    def click_grant_delete(self):
        self.browser.find_element(*self.dlt_btn).click()
        WebDriverWait(self.browser, 18).until(EC.presence_of_element_located(self.delete_success))
        time.sleep(7)

    #@allure.step('Verify Cancel button in delete button popup')
    def verify_cancel_button(self):
        time.sleep(.5)
        return self.browser.find_element(*self.cncl_btn).is_displayed()

    #@allure.step('Verify Close button displayed in Popup after clicking on top delete button ')
    def verify_delete_close(self):
        time.sleep(1)
        return self.browser.find_element(*self.delete_close).is_displayed()

    #@allure.step('Click on cancel button to close popup in my list detailed page')
    def click_cancelButton(self):
        time.sleep(.5)
        self.browser.find_element(*self.cncl_btn).click()

    #@allure.step('Click and verify  newly created list ')
    def click_new_list(self):
        time.sleep(2)
        self.browser.find_element(*self.demo_list).click()

    #@allure.step('Verify Deleted list in User created lists')
    def verify_deletedList(self):
        try:
            WebDriverWait(self.browser, 10).until(EC.presence_of_element_located(self.demo_list))
            return self.browser.find_element(*self.demo_list).is_displayed()
        except:
            return False

    #@allure.step('Verify Deleted list in User created lists')
    def verify_deleted_test2_MyList(self):
        try:
            WebDriverWait(self.browser, 10).until(EC.presence_of_element_located(self.test2_list))
            return self.browser.find_element(*self.test2_list).is_displayed()
        except:
            return False

    #@allure.step('Verify Deleted list in User created lists')
    def verify_deleted_test1_MyList(self):
        try:
            WebDriverWait(self.browser, 10).until(EC.presence_of_element_located(self.test1_list))
            return self.browser.find_element(*self.test1_list).is_displayed()
        except:
            return False

    #@allure.step('Verify Deleted list in User created lists')
    def verify_delete_list_text(self):
        WebDriverWait(self.browser, 40).until(EC.presence_of_element_located(self.delete_list_confirmation_text))
        return self.browser.find_element(*self.delete_list_confirmation_text).is_displayed()

    #@allure.step('Verify Deleted list in list page')
    def verify_delete_title_list_text(self):
        WebDriverWait(self.browser, 20).until(EC.presence_of_element_located(self.delete_title_list_confirmation_text))
        return self.browser.find_element(*self.delete_title_list_confirmation_text).is_displayed()

    #@allure.step('Click on list check box in header')
    def click_headerChkbox(self):
        # WebDriverWait(self.browser, 40).until(EC.presence_of_element_located(self.titlesNum_header))
        time.sleep(5)
        self.browser.find_element(*self.list_check).click()

    #@allure.step('click on download csv file in footer list detailed page')
    def click_csvdownload(self):
        # # time.sleep(2)
        # path_to_download_folder = str(os.path.join(Path.home(), "Downloads"))
        # time.sleep(2)
        # params = {'behavior': 'allow', 'downloadPath': path_to_download_folder}
        # time.sleep(2)
        # self.browser.execute_cdp_cmd('Page.setDownloadBehavior', params)
        # time.sleep(2)
        self.browser.find_element(*self.download).click()

    # #@allure.step('Verify CSV File is downloaded in Download Folder')
    # def verify_csv_downloaded(self):
    #     path_to_download_folder = str(os.path.join(Path.home(), "Downloads"))
    #     ##print(path_to_download_folder)
    #     isExist = path.exists(path_to_download_folder + "\mgm-lions-den-titles.csv")
    #     time.sleep(2)
    #     os.remove(path_to_download_folder + "\mgm-lions-den-titles.csv")
    #     return isExist

    #@allure.step('Click on share button  presented in footer ')
    def click_shareFooter(self):
        time.sleep(2)
        self.browser.find_element(*self.share_popup).click()

    #@allure.step('Click on share title button present in footer')
    def click_shareTitleFooter(self):
        time.sleep(2)
        self.browser.find_element(*self.share_title).click()

    #@allure.step('CLick on myList tab in list detailed page')
    def click_mylistTab(self):
        time.sleep(2)
        self.browser.find_element(*self.mylist_tab).click()

    #@allure.step('Click on Family check box in curated list')
    def click_familyCheck(self):
        time.sleep(2)
        self.browser.find_element(*self.family_chkvox).click()

    #@allure.step('Verify Family check box is selected in curated list')
    def verify_familyChekbox(self):
        time.sleep(2)
        return self.browser.find_element(*self.family_chkvox).is_selected()

    #@allure.step('Clicking on check box in list page for multiple')
    def click_Demo_checkBox(self):
        time.sleep(2)
        chk = self.browser.find_element(*self.demo_check)
        chk.location_once_scrolled_into_view
        time.sleep(2)
        self.browser.find_element(*self.demo_check).click()

    #@allure.step('Verify Delete tab in footer popup ')
    def verify_DeleteFooterpopup(self):
        time.sleep(2)
        try:
            return self.browser.find_element(*self.delete_popup).is_displayed()
        except:
            return False

    #@allure.step('Click on delete in footer to delete the list')
    def deletelist_frmfooter(self):
        time.sleep(2)
        self.browser.find_element(*self.delete_popup).click()

    #@allure.step('click on 1st movie card checkbox')
    def click_1moviechkbox(self):
        time.sleep(2)
        self.browser.find_element(*self.movie_1chkbox).click()

    #@allure.step('clicking on add TO list button from footer ')
    def click_addTolist(self):
        time.sleep(2)
        self.browser.find_element(*self.addTOlist).click()

    #@allure.step('Click on list check box in list page to delete')
    def click_listChkbox(self):
        WebDriverWait(self.browser, 20).until(EC.presence_of_element_located(self.newly_name_chkbx))
        chk = self.browser.find_element(*self.newly_name_chkbx)
        chk.location_once_scrolled_into_view
        time.sleep(2)
        self.browser.find_element(*self.newly_name_chkbx).click()

    #@allure.step('Verify List is deleted successfully ')
    def verify_listDeleted(self):
        time.sleep(2)
        self.browser.refresh()
        time.sleep(4)
        try:
            WebDriverWait(self.browser, 10).until(EC.presence_of_element_located(self.newly_name_chkbx))
            return self.browser.find_element(*self.newly_name_chkbx).is_displayed()
        except:
            return False

    #@allure.step('Verify Share confirmation after clicking on share button')
    def verify_share_confirmation(self):
        #  ignored_exceptions = (NoSuchElementException, StaleElementReferenceException,)
        WebDriverWait(self.browser, 10).until(EC.presence_of_element_located(self.share_confirmation))
        return self.browser.find_element(*self.share_confirmation).is_displayed()

    def do_refresh(self):
        time.sleep(2)
        self.browser.refresh()
        time.sleep(4)
