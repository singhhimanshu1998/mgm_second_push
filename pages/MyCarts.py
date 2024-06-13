import allure, time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import StaleElementReferenceException
from resources.variables import *


class MyCartsPage:
    headerMyCarts = (By.XPATH, '//body//mgm-app-root//mgm-header//a[2]')
    yourCartTitle = (By.XPATH, '//div/p[contains(text(),"Your Carts")]')
    firstCartDeleteButton = (By.XPATH, '//div[contains(@class,"container-content")]//div[contains(@class,"row racks")]'
                                       '[1]//span[contains(text(), "Delete")]')
    firstCartName = (By.XPATH, '//div[contains(@class,"container-content")]//div[contains(@class,"row racks")][1]//a')
    cartCountText = (By.XPATH, '//a[contains(text(),"testingCart2")]/parent::div/span[contains(text(),"1")]')
    testingCart2 = (By.XPATH, '//a[contains(text(),"testingCart2")]')
    cartTableTitle = (By.XPATH, '//div[@class="list-name"]/div[@id="top-title"]')
    deletePopupCloseButton = (By.XPATH, '(//div[contains(@class,"desk-close")]/img[contains(@class,"close-btn-image")])[2]')
    deletePopupDeleteCartButton = (By.XPATH, '//div[@class="ltcc-modal"]//div/button[contains(text()," Delete Cart ")]')
    deleteCartConfirmationText = (By.XPATH, '//h3[contains(text(),"Delete Cart ")]')
    tabularRowButton = (By.XPATH, '//div[contains(@class,"modebtn")]/div[contains(@class,"list-icons")]/div')
    tabularRowTitleName = (By.XPATH, '(//div[contains(@class,"row")]//div[contains(@class,"ile-titles")])[1]')
    deletePopupCancelButton = (By.XPATH, '//div[contains(@class,"modal-content")]//div/button[contains(text()," Cancel ")]')
    startDownloadCartButton = (By.XPATH, '//div[contains(@class,"modal-content")]//div/button[contains(text()," Start Download ")]')
    downloadingStartText = (By.XPATH, '//div[@class="modal-content"]//p[contains(@class,"directions")]')
    deletePopupStaticText = (By.XPATH, '//h3[@classs="header-text"]')
    testingCart2DeleteButton = (By.XPATH, '//a[contains(text(),"testingCart2")]/parent::div/parent::div/div'
                                          '//span[contains(text(),"Delete")]')
    testElementsCart = (By.XPATH, '//a[contains(text(),"testElements")]')
    testingCartFirst = (By.XPATH, '//a[contains(text(),"testingCart")]')
    cartNameTitle = (By.XPATH, '//h1[contains(@class,"ld-title")]')
    editCartButton = (By.XPATH, '//img[contains(@class,"edit-btn")]')
    cartPageDeleteButton = (By.XPATH, '//div[contains(@class,"dlt-btn")]/button/i[contains(@class,"delete-icon")]')
    allAssetsButton = (By.XPATH,'//div[contains(@class,"row main-content")]//p[contains(text(),"ALL ASSETS")]')
    cartDownloadButton = (By.XPATH, '//button[contains(text(),"DOWNLOAD CART")]')
    cartSortingButton = (By.XPATH, '//div[contains(@class,"sort-dropdown")]//div[contains(@class,"sort-filter")]/div[contains(@class,"dropdown-filter")]')
    sortingFileSizeDown = (By.XPATH, '//div[contains(@class,"dropdown-defaults")]//span[contains(text()," FILE SIZE ")]//img[@src="/assets/images/down-arrow-icon.png"]')
    sortingFileSizeUp = (By.XPATH, '//div[contains(@class,"dropdown-defaults")]//span[contains(text()," FILE SIZE ")]//img[@src="/assets/images/up-arrow-icon.png"]')
    sortingAtoZ = (By.XPATH, '//div[contains(@class,"dropdown-defaults")]//span[contains(text()," FILE NAME A-Z ")]//img[@src="/assets/images/down-arrow-icon.png"]')
    sortingZtoA = (By.XPATH, '//div[contains(@class,"dropdown-defaults")]//span[contains(text()," FILE NAME Z-A ")]//img[@src="/assets/images/up-arrow-icon.png"]')
    firstRowFileSize = (By.XPATH, '(//div[contains(@class,"asset-list-row")]/div[4])[1]')
    secondRowFileSize = (By.XPATH, '(//div[contains(@class,"asset-list-row")]/div[4])[2]')
    firstFileName = (By.XPATH, '(//div[contains(@class,"asset-list-row")]/div[3])[1]')
    lastFileName = (By.XPATH, '(//div[contains(@class,"asset-list-row")]/div[3])[4]')
    titleColumn = (By.XPATH, '//div[contains(@class,"asset-list-row")]/div[2]')
    fileNameColumn = (By.XPATH, '//div[contains(@class,"asset-list-row")]/div[3]')
    fileSizeColumn = (By.XPATH, '//div[contains(@class,"asset-list-row")]/div[4]')
    assetTypeColumn = (By.XPATH, '//div[contains(@class,"asset-list-row")]/div[5]')
    cartDetailsTableTitle = (By.XPATH, '//div[contains(@class,"list-icons")]/div')
    cartTitleNameText = (By.XPATH, '//h1[contains(@class,"ld-title")]//input[@id="top-title"]')
    # cartRowCount = (By.XPATH, '//div[contains(@class,"carts-lists")]/div')
    cartRowCount = (By.XPATH, '//div[@class="result-count"]')
    cartAssetsCount = (By.XPATH, '//div[contains(@class,"ld-title-data")]/div[@class="carts-title"]')
    cartDetailPageDeleteButton = (By.XPATH, '//button[contains(text(), " DELETE CART ")]')
    cartDetailPageDownloadButton = (By.XPATH, '//button[contains(text(),"DOWNLOAD CART ")]')
    assetDeleteButton = (By.XPATH, '//div[contains(@class,"carts-lists")]//button/i')
    removeAssetButton = (By.XPATH, '//div/button[contains(text(), " Remove Asset ")]')
    deleteAssetButton = (By.XPATH, '(//div[contains(@class,"asset-list-row")]//div[contains(@class,"delete-icon")]//img)[1]')
    removingAssetText = (By.XPATH, '//p[contains(text(), "Removing Cart")]')
    firstRowDeleteButton = (By.XPATH, '(//button[contains(@class,"cui-delete-btn")])[1]')
    firstFileNameColumn = (By.XPATH, '(//div[contains(@class,"asset-list-row")]/div[3])[1]')

    delete_button = (By.XPATH, "//a[text()='TestCart']/parent::div/following-sibling::div//span[text()='Delete']")
    popup_delete_cart = (By.XPATH, "//button[text()=' Delete Cart ']")
    popup_cancel = (By.XPATH, "//button[text()=' Cancel ']")
    popup_close = (By.XPATH, "//div[@class='close-x desk-close']/img[@class='close-btn-image']")
    delete_sucess_text = (By.XPATH, "//div[text()='TestCart cart has been deleted ']")
    shared_by_mgm_tab = (By.XPATH, "//p[text()='Shared by MGM']")
    test_cart = (By.XPATH, "//p[text()='Shared by MGM']")
    documents = (By.XPATH, "//p[text()='DOCUMENTS']")


    def __init__(self, browser):
        self.browser = browser

    #@allure.step('Verify User can open My-Cart page')
    def click_my_carts_header_title(self):
        WebDriverWait(self.browser, 98).until(EC.presence_of_element_located(self.headerMyCarts))
        self.browser.find_element(*self.headerMyCarts).click()
        WebDriverWait(self.browser, 90).until(EC.presence_of_element_located(self.yourCartTitle))
        # your_title = self.browser.find_element(*self.yourCartTitle).is_displayed()
        self.browser.find_element(*self.yourCartTitle).click()
        WebDriverWait(self.browser, 90).until(EC.element_to_be_clickable(self.yourCartTitle))
        WebDriverWait(self.browser, 300).until(EC.element_to_be_clickable(self.firstRowDeleteButton))
        return self.browser.find_element(*self.firstRowDeleteButton).is_displayed()

    #@allure.step('Verify Download cart button is clickable in cart Detail page')
    def click_download_cart_detail_page(self):
        WebDriverWait(self.browser, 20).until(EC.presence_of_element_located(self.cartDetailPageDownloadButton))
        time.sleep(2)
        self.browser.find_element(*self.cartDetailPageDownloadButton).click()

    #@allure.step('Verify cart name is clickable in My Cart page')
    def click_test_elements_cart(self):
        WebDriverWait(self.browser, 90).until(EC.presence_of_element_located(self.testElementsCart))
        self.browser.find_element(*self.testElementsCart).click()
        WebDriverWait(self.browser, 75).until(EC.element_to_be_clickable(self.allAssetsButton))
        time.sleep(5.5)
        all_assets_button = self.browser.find_element(*self.allAssetsButton)
        self.browser.execute_script("arguments[0].click();", all_assets_button)
        WebDriverWait(self.browser, 55).until(EC.presence_of_element_located(self.cartPageDeleteButton))
        # return self.browser.find_element(*self.cartPageDeleteButton).is_displayed()

    #@allure.step('Verify cart name is clickable in My Cart page')
    def click_testing_first_cart(self):
        WebDriverWait(self.browser, 80).until(EC.presence_of_element_located(self.testingCartFirst))
        self.browser.find_element(*self.testingCartFirst).click()
        WebDriverWait(self.browser, 75).until(EC.element_to_be_clickable(self.allAssetsButton))
        time.sleep(5.5)
        all_assets_button = self.browser.find_element(*self.allAssetsButton)
        self.browser.execute_script("arguments[0].click();", all_assets_button)
        WebDriverWait(self.browser, 55).until(EC.presence_of_element_located(self.cartPageDeleteButton))

    # @allure.step('Verify cart name is clickable in My Cart page')
    def verify_first_testing_first_cart_not_present(self):
        try:
            WebDriverWait(self.browser, 5).until(EC.presence_of_element_located(self.testingCartFirst))
            testing_cart = self.browser.find_element(*self.testingCartFirst).is_displayed()
            if testing_cart:
                return True
            else:
                return False
        except:
            return False



    # @allure.step('Verify cart name is clickable in My Cart page')
    def click_delete_remove_asset_button(self):
        WebDriverWait(self.browser, 70).until(EC.presence_of_element_located(self.deleteAssetButton))
        time.sleep(1.5)
        self.browser.find_element(*self.deleteAssetButton).click()

    #@allure.step('Verify cart name is clickable in My Cart page')
    def click_remove_asset_button(self):
        WebDriverWait(self.browser, 70).until(EC.element_to_be_clickable(self.removeAssetButton))
        time.sleep(1.5)
        self.browser.find_element(*self.removeAssetButton).click()
        time.sleep(10)


    #@allure.step('Verify user is able to delete cart asset')
    def click_asset_delete_button_testing_first_cart(self):
        WebDriverWait(self.browser, 20).until(EC.presence_of_element_located(self.assetDeleteButton))
        self.browser.find_element(*self.assetDeleteButton).click()

    #@allure.step('Verify Start download button present in download cart popup')
    def verify_start_download_Button_cart_detail_page(self):
        WebDriverWait(self.browser, 30).until(EC.presence_of_element_located(self.startDownloadCartButton))
        time.sleep(2.5)
        return self.browser.find_element(*self.startDownloadCartButton).is_displayed()

    #@allure.step('Verify user can download cart assets')
    def click_start_download_Button_cart_detail_page(self):
        WebDriverWait(self.browser, 20).until(EC.presence_of_element_located(self.startDownloadCartButton))
        self.browser.find_element(*self.startDownloadCartButton).click()
        WebDriverWait(self.browser, 10).until(EC.presence_of_element_located(self.downloadingStartText))
        downloading_text = self.browser.find_element(*self.downloadingStartText).text
        time.sleep(20)
        return downloading_text

    # @allure.step('Verify user can download cart assets')
    def verify_first_asset_file_name(self):
        try:
            time.sleep(1.5)
            WebDriverWait(self.browser, 20).until(EC.presence_of_element_located(self.firstFileNameColumn))
            first_file_name_text = self.browser.find_element(*self.firstFileNameColumn).text
            time.sleep(1.5)
            return first_file_name_text
        except:
            return "movie not present"

    #@allure.step('Verify delete button is clickable in Cart detail page')
    def click_delete_button_test_elements_cart(self):
        WebDriverWait(self.browser, 40).until(EC.presence_of_element_located(self.cartDetailPageDeleteButton))
        self.browser.find_element(*self.cartDetailPageDeleteButton).click()

    #@allure.step('Verify cart name is clickable in My Cart page')
    def verify_assets_count_cart_detail_page(self):
        WebDriverWait(self.browser, 20).until(EC.presence_of_element_located(self.cartRowCount))
        whole_text = self.browser.find_element(*self.cartRowCount).text
        asset_count = whole_text.split(" ")
        return asset_count[0]

    #@allure.step('Verify Delete Button present in My Cart page')
    def verify_delete_button(self):
        WebDriverWait(self.browser, 300).until(EC.presence_of_element_located(self.firstCartDeleteButton))
        return self.browser.find_element(*self.firstCartDeleteButton).is_displayed()

    #@allure.step('Verify Title Column present in cart detail page')
    def verify_title_name_column(self):
        time.sleep(1)
        title_column = self.browser.find_elements(*self.titleColumn)
        time.sleep(2)
        return len(title_column)

    #@allure.step('Verify File Name Column present in cart detail page')
    def verify_file_name_column(self):
        time.sleep(1)
        title_column = self.browser.find_elements(*self.fileNameColumn)
        time.sleep(2)
        return len(title_column)

    #@allure.step('Verify File Size Column present in cart detail page')
    def verify_file_size_column(self):
        time.sleep(1)
        title_column = self.browser.find_elements(*self.fileSizeColumn)
        time.sleep(2)
        return len(title_column)

    #@allure.step('Verify Asset Type Column present in cart detail page')
    def verify_asset_type_column(self):
        time.sleep(1)
        title_column = self.browser.find_elements(*self.assetTypeColumn)
        time.sleep(2)
        return len(title_column)

    #@allure.step('Verify cart name present in My Cart page')
    def verify_cart_title_name(self):
        WebDriverWait(self.browser, 14).until(EC.presence_of_element_located(self.cartTableTitle))
        return self.browser.find_element(*self.cartTableTitle).is_displayed()

    #@allure.step('Verify cart name present in My Cart page')
    def verify_cart_title_name_text(self):
        WebDriverWait(self.browser, 14).until(EC.presence_of_element_located(self.cartTableTitle))
        # self.browser.find_element(*self.editCartButton).click()
        # return self.browser.find_element(*self.cartTableTitle).get_attribute('value')
        return self.browser.find_element(*self.cartTableTitle).text

    #@allure.step('Verify cart name present in My Cart page')
    def type_new_cart_title_name(self, cartName):
        time.sleep(2)
        self.browser.find_element(*self.editCartButton).click()
        self.browser.find_element(*self.cartTitleNameText).clear().send_keys(cartName)

    #@allure.step('Verify cart name present in My Cart page')
    def verify_new_cart_title_name_save(self, cartName):
        time.sleep(2)
        self.browser.find_element(*self.cartTitleNameText).send_keys(Keys.ENTER)

    #@allure.step('Verify cart edit button present in Cart page')
    def verify_cart_edit_name(self):
        return self.browser.find_element(*self.editCartButton).is_displayed()

    #@allure.step('Verify cart delete button present in Cart page')
    def verify_cart_page_delete_button(self):
        WebDriverWait(self.browser, 7).until(EC.presence_of_element_located(self.cartPageDeleteButton))
        return self.browser.find_element(*self.cartPageDeleteButton).is_displayed()

    #@allure.step('Verify cart Download button present in Cart page')
    def verify_cart_page_download_button(self):
        return self.browser.find_element(*self.cartDownloadButton).is_displayed()

    #@allure.step('Verify cart Sorting button present in Cart page')
    def verify_cart_page_sorting_button(self):
        return self.browser.find_element(*self.cartSortingButton).is_displayed()

    #@allure.step('Verify cart Sorting button is clickable in Cart detail page page')
    def click_cart_page_sorting_button(self):
        WebDriverWait(self.browser, 24).until(EC.element_to_be_clickable(self.cartSortingButton))
        filter_button = self.browser.find_element(*self.cartSortingButton)
        self.browser.execute_script("arguments[0].click();", filter_button)

    #@allure.step('Verify cart Sorting file Size Down button is clickable in Cart detail page page')
    def click_file_down_size_sorting_button(self):
        time.sleep(1)
        self.browser.find_element(*self.sortingFileSizeDown).click()
        time.sleep(10)
        first_whole_size = self.browser.find_element(*self.firstRowFileSize).text
        first_file_size_mb = first_whole_size.split(".")
        first_file = int(first_file_size_mb[0])
        second_whole_size = self.browser.find_element(*self.secondRowFileSize).text
        second_file_size_mb = second_whole_size.split(".")
        second_file = int(second_file_size_mb[0])
        return first_file, second_file

    #@allure.step('Verify cart Sorting file Size Down button is clickable in Cart detail page page')
    def click_file_up_size_sorting_button(self):
        time.sleep(1)
        self.browser.find_element(*self.sortingFileSizeUp).click()
        time.sleep(10)
        first_whole_size = self.browser.find_element(*self.firstRowFileSize).text
        first_file_size_mb = first_whole_size.split(".")
        first_file = int(first_file_size_mb[0])
        second_whole_size = self.browser.find_element(*self.secondRowFileSize).text
        second_file_size_mb = second_whole_size.split(".")
        second_file = int(second_file_size_mb[0])
        return first_file, second_file

    #@allure.step('Verify user can click apply A-Z')
    def verify_sorting_a_to_z(self):
        self.browser.find_element(*self.sortingAtoZ).click()
        time.sleep(5)
        first_asset_name = self.browser.find_element(*self.firstFileName)
        movies_name = first_asset_name.text
        first_name = movies_name[0]
        last_asset_name = self.browser.find_element(*self.lastFileName)
        movie_name = last_asset_name.text
        last_name = movie_name[0]
        return first_name, last_name

    #@allure.step('Verify user can click apply A-Z')
    def verify_sorting_z_to_a(self):
        self.browser.find_element(*self.sortingZtoA).click()
        time.sleep(5)
        first_asset_name = self.browser.find_element(*self.firstFileName)
        movies_name = first_asset_name.text
        first_name = movies_name[0]
        last_asset_name = self.browser.find_element(*self.lastFileName)
        movie_name = last_asset_name.text
        last_name = movie_name[0]
        return first_name, last_name

    #@allure.step('Verify cart Sorting button present in My Cart page')
    def verify_cart_tabular_structure(self):
        return self.browser.find_element(*self.cartDetailsTableTitle).is_displayed()

    #@allure.step('Verify Delete Button clickable in My-Cart page')
    def click_delete_button(self):
        WebDriverWait(self.browser, 14).until(EC.presence_of_element_located(self.firstCartDeleteButton))
        self.browser.find_element(*self.firstCartDeleteButton).click()

    #@allure.step('Verify Delete Button clickable in My-Cart page')
    def click_delete_button_testing_cart2(self):
        WebDriverWait(self.browser, 14).until(EC.presence_of_element_located(self.testingCart2DeleteButton))
        self.browser.find_element(*self.testingCart2DeleteButton).click()

    #@allure.step('Verify cart name present in My Cart page')
    def verify_cart_name(self):
        WebDriverWait(self.browser, 14).until(EC.presence_of_element_located(self.firstCartName))
        return self.browser.find_element(*self.firstCartName).is_displayed()

    #@allure.step('Verify cart name present in My Cart page')
    def verify_cart_count_text(self):
        WebDriverWait(self.browser, 14).until(EC.presence_of_element_located(self.cartCountText))
        return self.browser.find_element(*self.cartCountText).is_displayed()

    #@allure.step('Verify cart name is clickable')
    def click_cart_title_text(self):
        WebDriverWait(self.browser, 48).until(EC.presence_of_element_located(self.testingCart2))
        self.browser.find_element(*self.testingCart2).click()
        WebDriverWait(self.browser, 48).until(EC.presence_of_element_located(self.cartTableTitle))
        return self.browser.find_element(*self.cartTableTitle).is_displayed()

    #@allure.step('Verify cart delete button is present')
    def verify_delete_popup_delete_cart_button(self):
        WebDriverWait(self.browser, 180).until(EC.presence_of_element_located(self.deletePopupDeleteCartButton))
        return self.browser.find_element(*self.deletePopupDeleteCartButton).is_displayed()

    #@allure.step('Verify cart delete button is Clickable')
    def verify_click_delete_cart_button_delete_popup(self):
        WebDriverWait(self.browser, 18).until(EC.presence_of_element_located(self.deletePopupDeleteCartButton))
        self.browser.find_element(*self.deletePopupDeleteCartButton).click()
        WebDriverWait(self.browser, 18).until(EC.presence_of_element_located(self.deleteCartConfirmationText))
        return self.browser.find_element(*self.deleteCartConfirmationText).is_displayed()

    #@allure.step('Verify testing cart is not present after preform delete operation')
    def verify_testing_cart2_delete(self):
        time.sleep(5)
        try:
            testing_cart = self.browser.find_element(*self.deletePopupDeleteCartButton).is_displayed()
            if testing_cart:
                return False
        except:
            return True

    #@allure.step('Verify cancel button is present in delete cart popup')
    def verify_delete_popup_cancel_button(self):
        time.sleep(1)
        return self.browser.find_element(*self.deletePopupCancelButton).is_displayed()

    #@allure.step('Verify close button present in delete cart popup')
    def verify_delete_popup_close_button(self):
        return self.browser.find_element(*self.deletePopupCloseButton).is_displayed()

    #@allure.step('Verify close button is clickable in delete cart popup')
    def click_close_button_delete_popup(self):
        close_button = self.browser.find_element(*self.deletePopupCloseButton)
        self.browser.execute_script("arguments[0].click();", close_button)
        try:
            time.sleep(15)
            close_button = self.browser.find_element(*self.deletePopupCloseButton).is_displayed()
            if close_button:
                return False
        except:
            return True

    #@allure.step('Verify cancel button is clickable in delete cart popup')
    def click_cancel_button_delete_popup(self):
        cancel_button = self.browser.find_element(*self.deletePopupCancelButton)
        self.browser.execute_script("arguments[0].click();", cancel_button)
        try:
            time.sleep(3)
            close_button = self.browser.find_element(*self.deletePopupCancelButton).is_displayed()
            if close_button:
                return False
        except:
            return True

    # @allure.step('Verify cancel button is clickable in delete cart popup')
    def click_list_tabular_row_button(self):
        cancel_button = self.browser.find_element(*self.tabularRowButton)
        self.browser.execute_script("arguments[0].click();", cancel_button)
        time.sleep(1.5)
        WebDriverWait(self.browser, 28).until(EC.presence_of_element_located(self.tabularRowTitleName))
        time.sleep(2.5)


    #@allure.step('Verify static text present in delete cart popup')
    def verify_delete_popup_static_text(self):
        return self.browser.find_element(*self.deletePopupStaticText).is_displayed()

    #@allure.step('Verify static text present in Download cart popup')
    def verify_download_popup_static_text(self):
        time.sleep(2)
        return self.browser.find_element(*self.deletePopupStaticText).text

    def click_delete_button(self):
        time.sleep(2)
        self.browser.find_element(*self.deletePopupDeleteCartButton).click()


