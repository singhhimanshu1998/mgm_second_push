import os

import allure, time
from os import path
from pathlib import Path
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import StaleElementReferenceException
from resources.variables import *
import random


class ListDetails():
    movieheader = (By.XPATH, "//ul[@class='menu-items']//a[@id='Movies']")
    searchmovie = (By.XPATH, "//input[@placeholder='Search Movie Title, Actor, or Genre']")
    moviedetail = (
        By.XPATH,
        "//li[1]//div[2]//mgm-list-poster[1]//div[1]//div[1]//div[1]//div[1]//div[1]//div[1]")
    addtolistmovie = (
        By.XPATH,
        "//li[1]//div[2]//mgm-list-poster[1]//div[1]//div[1]//div[1]//div[1]//div[2]//ul[1]//li[1]//button[1]")
    toggledemo = (By.XPATH, "//span[contains(text(),'movietest')]/preceding-sibling::span[1]")
    mylist = (By.XPATH, "//ul[@class='menu-items']//a[@id='My Lists']")
    listele = (By.XPATH, "//a[contains(text(),'movietest')]")
    listchkbox = (By.XPATH, "//input[@id='select-all']")
    listtitle = (By.XPATH, "//input[@id='top-title']")
    listgrid = (By.XPATH, "//div[@class='white-grid']")
    listedbutton = (By.XPATH, "//div[@class='list-icon toggle-icon list']")
    sharebutton = (By.XPATH, "//span[contains(@class,'share-icon')]")
    deletebutton = (
        By.XPATH,
        "//span[contains(text(), 'Delete')]")
    success_created_list = (By.XPATH, "//div[@class='createdListItem ng-star-inserted']//span[@class='ie11fix uppercase']")
    moviecheck = (By.XPATH,
                  "//div[@class='movie-detail']/p[contains(text(),'Spectre')]/ancestor::mgm-list-poster/ancestor::div[@class='poster']/preceding-sibling::div[@class='checkBox']/mgm-checkbox-single")
    moviedet = (
        By.XPATH,
        "//div[@class='desk-on']//div[@class='movie-detail']/p[contains(text(),'Spectre')]")
    overlaypanel = (By.XPATH,
                    "//div[@class='movie-detail']/p[contains(text(),'Spectre')]/ancestor::div[@class='movie-detail']/preceding-sibling::div[1]/div/div/div")
    addtolist = (
        By.XPATH,
        "//div[@class='movie-detail']/p[contains(text(),'Spectre')]/ancestor::div[@class='movie-detail']/preceding-sibling::div[1]/div/div[2]/ul/li[1]")
    watchmovie = (
        By.XPATH,
        "//div[@class='movie-detail']/p[contains(text(),'Spectre')]/ancestor::div[@class='movie-detail']/preceding-sibling::div[1]/div/div[2]/ul/li[2]")
    watchtrailer = (
        By.XPATH,
        "//div[@class='movie-detail']/p[contains(text(),'Spectre')]/ancestor::div[@class='movie-detail']/preceding-sibling::div[1]/div/div[2]/ul/li[3]")
    viewdetails = (
        By.XPATH,
        "//div[@class='movie-detail']/p[contains(text(),'Spectre')]/ancestor::div[@class='movie-detail']/preceding-sibling::div[1]/div/div[2]/ul/li[4]")
    titlelist = (By.XPATH, "//div[@class='col-lg-3 inner-container']")
    directedby = (By.XPATH, "//div[contains(text(),'Directed By')]")
    maincast = (By.XPATH, "//div[@class='col-lg-3']")
    synopsis = (By.XPATH, "//div[@class='col-lg-4']")
    selecttitle = (By.XPATH,
                   "//p[contains(text(),'Spectre')]/ancestor::div[@class='poster']/preceding-sibling::div/mgm-checkbox-single/div/input")
    checkedtitle = (By.XPATH, "//span[contains(text(),'Item Selected')]")
    footerlist = (By.XPATH, "//div[@class='item-actions']/span[1]")
    addtolisdtfooter = (By.XPATH, "//span[contains(text(),'ADD TO LIST')]")
    autotestlist = (By.XPATH, "//span[contains(text(),'autotest')]/preceding-sibling::span[1]")
    addtolistbutton = (By.XPATH, "//div[@class='atl-add-btn']/div/button")
    titleinlist = (By.XPATH, "//a[contains(text(),'autotest')]")
    verifytitlelist = (
        By.XPATH, "//div[@class='desk-on']//p[contains(text(),'Spectre')]")
    mylistname = (By.XPATH, "//input[@placeholder='My New List Name']")
    createlistbutton = (By.XPATH, "//button[@class='cui-btn cui-btn-flat cui-btn-o-1 on-light']")
    autoselect = (By.XPATH, "//span[contains(text(),'autodetailtest')]/preceding-sibling::input[1]")
    createdlist = (By.XPATH, "//a[contains(text(),'autodetailtest')]")
    sharemoviecheck = (By.XPATH, "//li[1]//div[1]//mgm-checkbox-single[1]")
    sharetitle = (By.XPATH, "//span[contains(text(),'EMAIL .XLSX')]")
    sharelistpopup = (By.XPATH, "//button[@class='share-btn']")
    shareemail = (By.XPATH, "//input[@id='email']")
    shareemailbutton = (By.XPATH, "//button[@class='share-btn']")
    csvbutton = (By.XPATH, "//div[@class='item-list']/div[2]/div[@class='item-action']/button")
    csvclick = (By.XPATH, "//div[@class='share-popup']//div[2]//div[1]")
    selectall = (By.XPATH, "//div[@class='checkbox-shell-dark']/input[@id='select-all']")
    deletecreatelist = (By.XPATH,
                        "//a[contains(text(),'autodetailtest')]/ancestor::div[@class='col-lg-5 listData']/following-sibling::div[2]/button[2]")
    shareheader = (By.XPATH, "//button[@class='cui-btn cui-btn-flat']/span[contains(text(),'Share List')]")
    deleteheader = (By.XPATH, "//button[@class='cui-btn cui-btn-flat']/span[contains(text(),'Delete')]")
    deletelistbutton = (By.XPATH, "//div[@class='delete-btn ng-star-inserted']/button[contains(text(),'Delete List')]")
    deletefooterbutton = (By.XPATH, "//div[@class='item-actions']/following-sibling::div[1]/div[4]/button")
    delete_button_footer = (By.XPATH, "//button[contains(text(),'DELETE')]")
    deletetitle = (By.XPATH, "//button[@class='cui-btn cui-btn-primary ng-star-inserted']")
    listunderline = (By.XPATH, "//ul[@class='menu-items']//a[@id='My Lists']")
    televisionclick = (By.XPATH, "//ul[@class='menu-items']//a[@id='Television']")
    tvcheck = (By.XPATH,
               "//div[mgm-list-poster[div[@class='desk-on']//p[@class='movie-title light-color'][contains(text(),'Mr. Mom (series)')]]]/preceding-sibling::div[1]/mgm-checkbox-single")
    deletemovie = (By.XPATH,
                   "//div[@class='movie-detail']/p[contains(text(),'Spectre')]/ancestor::mgm-list-poster/ancestor::div[@class='poster']/preceding-sibling::div[@class='checkBox']/mgm-checkbox-single")
    watchmovieintv = (By.XPATH, "//button[contains(text(),'Watch movie')]")
    verifytvpanel = (By.XPATH,
                     "//p[contains(text(),' Mr. Mom (series) ')]/ancestor::div[@class='movie-detail']/preceding-sibling::div/div/div/div")
    added_movie = (By.XPATH, "//span[contains(text(),'movietest')]")
    added_movie_list = (By.XPATH, "//span[contains(text(),'autodetailtest')]")
    success_created = (By.XPATH, "//div[@class='atl-add-btn']//span[@class='ie11fix uppercase']")
    titlesNum_header = (By.XPATH, "//div[@class='list-name']/span[contains(text(),'title')]")
    share_confirmation = (By.XPATH, "//span[contains(text(),' Your List Shared Successfully! ')]")
    delete_success_msg = (By.XPATH, "//h3[contains(text(),'Delete Title ')]")
    delete_success = (By.XPATH, "//h3[contains(text(),'Delete List ')]")
    results_found = (By.XPATH, "//h2[@class='count-text ng-star-inserted']")
    header_search = (By.XPATH, "//input[@placeholder='Search Movie Title, Actor, or Genre']")

    def __init__(self, browser):
        self.browser = browser

    """list details-35"""

    #@allure.step('To verify movie detail page')
    def verify_addmovietolist(self):
        actionchains = ActionChains(self.browser)
        WebDriverWait(self.browser, 30).until(EC.presence_of_element_located(self.movieheader))
        self.browser.find_element(*self.movieheader).click()
        WebDriverWait(self.browser, 30).until(EC.presence_of_element_located(self.searchmovie))
        time.sleep(5)
        self.browser.find_element(*self.searchmovie).send_keys("spectre")
        actionchains.send_keys(Keys.ENTER).perform()
        time.sleep(2)
        lst = self.browser.find_element(*self.moviedetail)
        WebDriverWait(self.browser, 30).until(EC.presence_of_element_located(self.moviedetail))
        self.browser.execute_script("arguments[0].scrollIntoView();", lst)
        verifyoverlay = self.browser.find_element(*self.moviedetail)
        ActionChains(self.browser).move_to_element(verifyoverlay).perform()
        time.sleep(2)
        self.browser.find_element(*self.addtolistmovie).click()
        time.sleep(2)
        WebDriverWait(self.browser, 10).until(EC.presence_of_element_located(self.mylistname))
        self.browser.find_element(*self.mylistname).click()
        time.sleep(1)
        self.browser.find_element(*self.mylistname).send_keys("movietest")
        self.browser.find_element(*self.createlistbutton).click()
        WebDriverWait(self.browser, 50).until(EC.presence_of_element_located(self.success_created_list))
        WebDriverWait(self.browser, 40).until(EC.presence_of_element_located(self.added_movie))
        time.sleep(4)
        self.browser.find_element(*self.addtolistbutton).click()
        WebDriverWait(self.browser, 55).until(EC.presence_of_element_located(self.success_created))

    #@allure.step('To verify mylist details page is displayed')
    def verify_mylist(self):
        WebDriverWait(self.browser, 30).until(EC.presence_of_element_located(self.mylist))
        self.browser.find_element(*self.mylist).click()
        time.sleep(3)
        self.browser.refresh()
        WebDriverWait(self.browser, 30).until(EC.presence_of_element_located(self.listele))
        lst = self.browser.find_element(*self.listele)
        self.browser.execute_script("arguments[0].scrollIntoView();", lst)
        self.browser.find_element(*self.listele).click()

    #@allure.step('Verify header title in mylistdetails page')
    def verify_listcheckbox(self):
        WebDriverWait(self.browser, 30).until(EC.presence_of_element_located(self.listchkbox))
        verifychkbx = self.browser.find_element(*self.listchkbox).is_displayed()
        return verifychkbx

    #@allure.step('Verify header title in mylistdetails page')
    def verify_listheadername(self):
        WebDriverWait(self.browser, 40).until(EC.presence_of_element_located(self.titlesNum_header))
        verifytitle = self.browser.find_element(*self.listtitle).is_displayed()
        print(verifytitle)
        return verifytitle

    #@allure.step('Verify grid button in mylistdetails page')
    def verify_listgridbutton(self):
        time.sleep(2)
        verifygrid = self.browser.find_element(*self.listgrid).is_displayed()
        return verifygrid

    #@allure.step('Verify list button in mylistdetails page')
    def verify_listbutton(self):
        time.sleep(2)
        listbutton = self.browser.find_element(*self.listedbutton).is_displayed()
        return listbutton

    #@allure.step('Verify list button in mylistdetails page')
    def verify_sharebutton(self):
        shrebutton = self.browser.find_element(*self.sharebutton).is_displayed()
        return shrebutton

    #@allure.step('Verify list button in mylistdetails page')
    def verify_deletebutton(self):
        time.sleep(2)
        deltebutton = self.browser.find_element(*self.deletebutton).is_displayed()
        return deltebutton

    #@allure.step('Verify moviecheck in mylistdetails page')
    def verify_moviecheckbox(self):
        time.sleep(2)
        moviechck = self.browser.find_element(*self.moviecheck).is_displayed()
        return moviechck

    #@allure.step('Verify moviedetail in mylistdetails page')
    def verify_moviedetail(self):
        time.sleep(2)
        moviedtl = self.browser.find_element(*self.moviedet).is_displayed()
        return moviedtl

    """list details-36"""

    #@allure.step('To verify overlay for movie card')
    def verify_overlaypanel(self):
        self.browser.implicitly_wait(7)
        verifyoverlay = self.browser.find_element(*self.overlaypanel)
        ActionChains(self.browser).move_to_element(verifyoverlay).perform()

    #@allure.step('To verify add to list element in overlay for movie card')
    def verify_addolist(self):
        time.sleep(2)
        addtolst = self.browser.find_element(*self.addtolist).is_displayed()
        return addtolst

    #@allure.step('To verify watch movie element in overlay for movie card')
    def verify_watchmovie(self):
        time.sleep(2)
        wtch = self.browser.find_element(*self.watchmovie).is_displayed()
        return wtch

    #@allure.step('To verify watch trailer element in overlay for movie card')
    def verify_watchtrailer(self):
        time.sleep(2)
        wtch = self.browser.find_element(*self.watchtrailer).is_displayed()
        return wtch

    #@allure.step('To verify view details element in overlay for movie card')
    def verify_viewdetails(self):
        time.sleep(2)
        wtchdet = self.browser.find_element(*self.viewdetails).is_displayed()
        return wtchdet

    """list details-38"""

    #@allure.step('To verify list view is displayed')
    def verify_listview(self):
        time.sleep(2)
        self.browser.find_element(*self.listedbutton).click()

    """list details-39"""

    #@allure.step('To verify list view elements in mylist details page')
    def verify_listelements(self):
        WebDriverWait(self.browser, 20).until(EC.presence_of_element_located(self.titlelist))
        verifytitle = self.browser.find_element(*self.titlelist).text
        print(verifytitle)
        return verifytitle

    #@allure.step('To verify directedby elements in mylist details page')
    def verify_directedelements(self):
        verifydirected = self.browser.find_element(*self.directedby).text
        print(verifydirected)
        return verifydirected

    #@allure.step('To verify main cast elements in mylist details page')
    def verify_maincastelements(self):
        cast = self.browser.find_element(*self.maincast).text
        print(cast)
        return cast

    #@allure.step('To verify synop elements in mylist details page')
    def verify_synopsiselements(self):
        synop = self.browser.find_element(*self.synopsis).text
        print(synop)
        return synop

    """list details-40"""

    #@allure.step('To verify user is able to select title using checkbox')
    def verify_titleselect(self):
        WebDriverWait(self.browser, 30).until(EC.presence_of_element_located(self.selecttitle))
        lst = self.browser.find_element(*self.selecttitle)
        self.browser.execute_script("arguments[0].scrollIntoView();", lst)
        self.browser.find_element(*self.selecttitle).click()
        WebDriverWait(self.browser, 30).until(EC.presence_of_element_located(self.selecttitle))
        verifytitle = self.browser.find_element(*self.selecttitle).is_selected()
        return verifytitle

    """list details-41"""

    #@allure.step('To verify footer section when selected a title')
    def verify_footersection(self):
        WebDriverWait(self.browser, 20).until(EC.presence_of_element_located(self.footerlist))
        footer = self.browser.find_element(*self.footerlist).is_displayed()
        return footer

    """list details-42"""

    #@allure.step('To verify added title to the list')
    def verify_addtitletolist(self):
        self.browser.find_element(*self.addtolisdtfooter).click()
        time.sleep(2)
        lsst = self.browser.find_element(*self.autotestlist)
        self.browser.execute_script("arguments[0].scrollIntoView();", lsst)
        WebDriverWait(self.browser, 20).until(EC.presence_of_element_located(self.autotestlist))
        self.browser.find_element(*self.autotestlist).click()
        time.sleep(2)
        self.browser.find_element(*self.addtolistbutton).click()
        WebDriverWait(self.browser, 50).until(EC.presence_of_element_located(self.success_created)) #ignored_exceptions
        WebDriverWait(self.browser, 20).until(EC.presence_of_element_located(self.mylist))
        self.browser.find_element(*self.mylist).click()
        time.sleep(8)
        self.browser.refresh()
        WebDriverWait(self.browser, 40).until(EC.presence_of_element_located(self.titleinlist))
        self.browser.find_element(*self.titleinlist).click()
        WebDriverWait(self.browser, 40).until(EC.presence_of_element_located(self.titlesNum_header))
        WebDriverWait(self.browser, 10).until(EC.presence_of_element_located(self.verifytitlelist))
        time.sleep(2)
        footer = self.browser.find_element(*self.verifytitlelist).is_displayed()
        return footer

    """list details-43"""

    #@allure.step('To verify added title to the list')
    def verify_createlist(self):
        self.browser.find_element(*self.selecttitle).click()
        time.sleep(2)
        self.browser.find_element(*self.addtolisdtfooter).click()
        time.sleep(2)
        WebDriverWait(self.browser, 10).until(EC.presence_of_element_located(self.mylistname))
        self.browser.find_element(*self.mylistname).click()
        time.sleep(1)
        self.browser.find_element(*self.mylistname).send_keys("autodetailtest")
        self.browser.find_element(*self.createlistbutton).click()
        WebDriverWait(self.browser, 50).until(EC.presence_of_element_located(self.success_created_list))
        WebDriverWait(self.browser, 40).until(EC.presence_of_element_located(self.added_movie_list))
        lst = self.browser.find_element(*self.autoselect)
        self.browser.execute_script("arguments[0].scrollIntoView();", lst)
        elem = self.browser.find_element(*self.autoselect)
        if elem.is_selected():
            return True
        else:
            return False

    """list details-44"""

    #@allure.step('To verify added title to the list')
    def verify_createdlist(self):
        self.browser.find_element(*self.addtolistbutton).click()
        WebDriverWait(self.browser, 50).until(EC.presence_of_element_located(self.success_created))
        WebDriverWait(self.browser, 20).until(EC.presence_of_element_located(self.mylist))
        lst = self.browser.find_element(*self.mylist)
        self.browser.execute_script("arguments[0].scrollIntoView();", lst)
        self.browser.find_element(*self.mylist).click()
        time.sleep(6)
        self.browser.refresh()
        WebDriverWait(self.browser, 45).until(EC.presence_of_element_located(self.createdlist))
        footer = self.browser.find_element(*self.createdlist).is_displayed()
        return footer

    #@allure.step('To verify added title to the list')
    def verify_titleincreatedlist(self):
        self.browser.find_element(*self.createdlist).click()
        WebDriverWait(self.browser, 40).until(EC.presence_of_element_located(self.titlesNum_header))
        time.sleep(2)
        verifytitle = self.browser.find_element(*self.verifytitlelist).is_displayed()
        return verifytitle

    """list details-45"""

    #@allure.step('To verify user is able to share title')
    def verify_sharewindow(self):
        self.browser.find_element(*self.sharemoviecheck).click()
        time.sleep(2)
        self.browser.find_element(*self.sharetitle).click()
        time.sleep(2)
        verifysharepopup = self.browser.find_element(*self.sharelistpopup).is_displayed()
        return verifysharepopup

    #@allure.step('To verify user is able to share title in email')
    def verify_shareemail(self):
        self.browser.find_element(*self.shareemail).send_keys('hiteshsingh564@gmail.com')
        self.browser.find_element(*self.shareemailbutton).click()

    #@allure.step('Verify Share confirmation after clicking on share button')
    def verify_share_confirmation(self):
        #  ignored_exceptions = (NoSuchElementException, StaleElementReferenceException,)
        WebDriverWait(self.browser, 10).until(EC.presence_of_element_located(self.share_confirmation))
        return self.browser.find_element(*self.share_confirmation).is_displayed()

    """list details-47"""

    #@allure.step('To verify user is able to download csv')
    def verify_downloadcsv(self):
        downloads = str(os.path.join(Path.home(), "Downloads"))
        self.browser.refresh()
        WebDriverWait(self.browser, 40).until(EC.presence_of_element_located(self.titlesNum_header))
        time.sleep(2)
        self.browser.find_element(*self.moviecheck).click()
        time.sleep(2)
        params = {'behavior': 'allow', 'downloadPath': downloads}
        time.sleep(1)
        self.browser.execute_cdp_cmd('Page.setDownloadBehavior', params)
        time.sleep(1)
        self.browser.find_element(*self.csvclick).click()

    #@allure.step('Verify CSV File is downloaded in Download Folder')
    def verify_csv_downloaded(self):
        path_to_download_folder = str(os.path.join(Path.home(), "Downloads"))
        print(path_to_download_folder)
        isExist = path.exists(path_to_download_folder + "\mgm-lions-den-titles.csv")
        time.sleep(3)
        os.remove(path_to_download_folder + "\mgm-lions-den-titles.csv")
        return isExist

    """list details-48"""

    #@allure.step('To verify select all titile checkbox')
    def verify_selectalltitle(self):
        self.browser.refresh()
        WebDriverWait(self.browser, 40).until(EC.presence_of_element_located(self.titlesNum_header))
        time.sleep(2)
        WebDriverWait(self.browser, 30).until(EC.presence_of_element_located(self.selectall))
        self.browser.find_element(*self.selectall).click()
        time.sleep(2)
        verify = self.browser.find_element(*self.footerlist).is_displayed()
        return verify

    """list details-50"""

    #@allure.step('To Verify User is able to share list by clicking on Sahre button in header')
    def verify_sharelistheader(self):
        self.browser.find_element(*self.shareheader).click()
        time.sleep(3)
        self.browser.find_element(*self.shareemail).send_keys('hiteshsingh564@gmail.com')
        self.browser.find_element(*self.shareemailbutton).click()

    """list details-46"""

    #@allure.step('To verify delete title in the list')
    def verify_deletetitle(self):
        self.browser.refresh()
        WebDriverWait(self.browser, 45).until(EC.presence_of_element_located(self.titlesNum_header))
        time.sleep(3)
        self.browser.find_element(*self.selecttitle).click()
        time.sleep(2)
        self.browser.find_element(*self.delete_button_footer).click()
        time.sleep(2)
        self.browser.find_element(*self.deletetitle).click()
        WebDriverWait(self.browser, 65).until(EC.presence_of_element_located(self.delete_success_msg))
        try:
            WebDriverWait(self.browser, 10).until(EC.presence_of_element_located(self.selecttitle))
            verify = self.browser.find_element(*self.selecttitle)
            if (verify.is_displayed()):
                return True
            else:
                return False
        except:
            return False

    """list details-49"""

    #@allure.step('To Verify user is able to Delete Title(s) of a list')
    def verify_deletelist(self):
        WebDriverWait(self.browser, 20).until(EC.presence_of_element_located(self.mylist))
        self.browser.find_element(*self.mylist).click()
        time.sleep(6)
        WebDriverWait(self.browser, 30).until(EC.presence_of_element_located(self.deletecreatelist))
        dlt_lst = self.browser.find_element(*self.deletecreatelist)
        self.browser.execute_script("arguments[0].scrollIntoView();", dlt_lst)
        time.sleep(2)
        self.browser.find_element(*self.deletecreatelist).click()
        time.sleep(2)
        self.browser.find_element(*self.deletelistbutton).click()
        WebDriverWait(self.browser, 60).until(EC.presence_of_element_located(self.delete_success))
        time.sleep(7)
        self.browser.refresh()
        try:
            WebDriverWait(self.browser, 30).until(EC.presence_of_element_located(self.createdlist))
            verify = self.browser.find_element(*self.createdlist)
            if (verify.is_displayed()):
                return True
        except:
            return False

    """list details-4"""

    #@allure.step('Verify My List is underlined in Menu')
    def verify_listunderline(self):
        clas = self.browser.find_element(*self.listunderline).get_attribute('class')
        print(clas)
        return clas

    """list details-37"""

    #@allure.step("To verify Watch Movie should not be shown in case of a TV entity")
    def verify_watchmovieintv(self):
        WebDriverWait(self.browser, 30).until(EC.presence_of_element_located(self.televisionclick))
        self.browser.find_element(*self.televisionclick).click()
        WebDriverWait(self.browser, 20).until(EC.presence_of_element_located(self.results_found))
        self.browser.find_element(*self.header_search).send_keys(" Mr. Mom (series) ")
        ActionChains(self.browser).send_keys(Keys.ENTER).perform()
        time.sleep(4)
        self.browser.find_element(*self.tvcheck).click()
        time.sleep(2)
        self.browser.find_element(*self.addtolisdtfooter).click()
        time.sleep(2)
        self.browser.find_element(*self.autotestlist).click()
        time.sleep(2)
        self.browser.find_element(*self.addtolistbutton).click()
        WebDriverWait(self.browser, 50).until(EC.presence_of_element_located(self.success_created))
        self.browser.refresh()
        WebDriverWait(self.browser, 20).until(EC.presence_of_element_located(self.mylist))
        lst = self.browser.find_element(*self.mylist)
        self.browser.execute_script("arguments[0].scrollIntoView();", lst)
        self.browser.find_element(*self.mylist).click()
        WebDriverWait(self.browser, 25).until(EC.presence_of_element_located(self.titleinlist))
        self.browser.find_element(*self.titleinlist).click()
        WebDriverWait(self.browser, 45).until(EC.presence_of_element_located(self.titlesNum_header))
        self.browser.find_element(*self.deletemovie).click()
        time.sleep(2)
        self.browser.find_element(*self.deletefooterbutton).click()
        time.sleep(2)
        self.browser.find_element(*self.deletetitle).click()
        WebDriverWait(self.browser, 65).until(EC.presence_of_element_located(self.delete_success_msg))
        self.browser.refresh()
        WebDriverWait(self.browser, 40).until(EC.presence_of_element_located(self.titlesNum_header))
        verifyoverlay = self.browser.find_element(*self.verifytvpanel)
        ActionChains(self.browser).move_to_element(verifyoverlay).perform()
        time.sleep(6)
        try:
            verify = self.browser.find_element(*self.watchmovieintv)
            if (verify.is_displayed()):
                return True
            else:
                return False
        except:
            return False
