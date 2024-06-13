import allure, time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import StaleElementReferenceException
from resources.variables import *
import datetime


class AssetsPage:
    firstTitleCard = (By.XPATH, '//ul[contains(@class,"search-list")]/li[1]//div[@class="desk-on"]'
                                '//div[@class="movie"]')
    bannerImage = (By.XPATH, '//div[@class="header"]/div/img')
    bannerText = (By.XPATH, '//div[@class="banner-text"]/h2[contains(text(),"Our Titles")]')
    searchInputField = (By.XPATH, '//div[@class="search-content"]/input[@placeholder="Search Movie or TV Titles"]')
    actionCrossButton = (By.XPATH, '//li/span[contains(text(),"Action")]/parent::li/span[2]')
    paginationLastPageNumber = (By.XPATH, '//nav[@aria-label="Pagination"]//ul/li[last()-1]/a/span')
    assetsActive = (By.XPATH, '//li[@class="menu menu-label"]/a[@id="Assets"]')
    howItEndsMovieCard = (By.XPATH, '//div[@class="desk-on"]//div[@class="movie-detail"]/p[contains(text(),'
                                    '" How It Ends ")]/parent::div/parent::div//div[@class="poster"]')
    respectMovie = (By.XPATH, '//div[@class="desk-on"]//div[@class="movie-detail"]/p[contains(text()," Respect ")]'
                              '/parent::div/parent::div//div[@class="poster"]')
    searchResultCount = (
        By.XPATH, '//div[contains(@class,"count-section")]/div[contains(@class,"search-counts")]/h2/span[1]')
    synopsisTitle = (By.XPATH, '//div[contains(@class,"synopsis-title")]')
    cardBannerImage = (By.XPATH, '//div[contains(@class,"header")]//div[@class="overlay"]')
    cardTabs = (By.XPATH, '//div[contains(@class,"row sub-menu-lis")]')
    cardBackButton = (By.XPATH, '//div[contains(@class,"back-btn")]/a/span[contains(text(),BACK)]')
    tabTitleOverview = (By.XPATH, '//div[contains(@class,"row sub-menu-lis")]//p[contains(text(),"TITLE OVERVIEW")]')
    tabAllAssets = (By.XPATH, '//div[contains(@class,"row sub-menu-lis")]//p[contains(text(),"ALL ASSETS")]')
    tabImagesPhotos = (By.XPATH, '//div[contains(@class,"row sub-menu-lis")]//p[contains(text(),"IMAGES/PHOTOS")]')
    tabDocuments = (By.XPATH, '//div[contains(@class,"row sub-menu-lis")]//p[contains(text(),"DOCUMENTS")]')
    tabPaidAdMemo = (By.XPATH, '//div[contains(@class,"row sub-menu-lis")]//p[contains(text(),"PAID AD MEMO")]')
    tabVideo = (By.XPATH, '//div[contains(@class,"row sub-menu-lis")]//p[contains(text(),"VIDEOS")]')
    resetFiltersButton = (By.XPATH, '//ul/li/span[contains(text(),"RESET FILTERS")]')
    collapseAll = (By.XPATH, '//ul//span[contains(text(),"COLLAPSE ALL ")]')
    # selectAll = (By.XPATH, '//ul//label[contains(text(),"Select All")]')
    selectAll = (By.XPATH, '//ul//label[contains(text(),"SELECT ALL ASSETS")]')
    gridViewButton = (By.XPATH, '//div[contains(@class,"grid-icon")]')
    listViewButton = (By.XPATH, '//div[contains(@class,"list-icon")]')
    sortingFilterButton = (By.XPATH, '//div[contains(@class,"sort-dropdown")]//div[contains'
                                     '(@class,"sort-filter")]/div[1]')
    fileTypeFilterText = (By.XPATH, '//h5[contains(text(),"File Type")]')
    videoPropertiesText = (By.XPATH, '//h5[contains(text(), "Video Properties")]')
    assetTypeText = (By.XPATH, '//h5[contains(text(), "Asset Type")]')
    fileSizeHeadingText = (By.XPATH, '//h5[contains(text(), "File Size")]')
    fileSizeLeftPoint = (By.XPATH, '//div[contains(@class, "slider")]//span[5]')
    fileSizeRangeText = (By.XPATH, '//div[contains(@class, "slider")]//span[contains(text(),"1 GB")]')
    fileSizeRangeMb = (By.XPATH, '//div[contains(@class, "slider")]//span[contains(text(),"1 MB")]')
    assetTypeDocuments = (By.XPATH, '//span[contains(text(), " Documents ")]')
    assetTypePhotoImages = (By.XPATH, '//span[contains(text(), " Photos/Images ")]')
    assetTypeAds = (By.XPATH, '//span[contains(text(), " Ads ")]')
    assetTypeVideos = (By.XPATH, '//span[contains(text(), " Videos ")]')

    resolutionCheckbox = (By.XPATH, '//span[contains(text(), " Resolution ")]/parent::div/div//input'
                                    '[@type ="checkbox"][1]')
    resolutionText = (By.XPATH, '//span[contains(text(), " Resolution ")]')
    frameRateCheckbox = (By.XPATH, '(//span[contains(text(), " Frame Rate ")]/parent::div/div//span)[1]')
    scriptCheckbox = (By.XPATH, '//span[contains(text(), " Documents ")]/parent::div/div[1]/label/'
                                'input[@type ="checkbox"]')
    videoCheckbox = (By.XPATH, '//span[contains(text(), " Videos ")]/parent::div/div[1]/label/input[@type ="checkbox"]')
    paidAdMemoCheckbox = (By.XPATH, '//span[contains(text(), " Documents ")]/parent::div/div[2]/label'
                                    '/input[@type ="checkbox"]')
    paidTabPaidAdMemoCheckbox = (By.XPATH, '//span[contains(text(), " Documents ")]'
                                           '/parent::div/div/label/input[@type ="checkbox"]')
    paidTabAdsPaidAdMemoCheckbox = (By.XPATH, '//span[contains(text(), " Ads ")]/parent::'
                                              'div/div/label/input[@type ="checkbox"]')
    photoImagesCheckbox = (By.XPATH, '//span[contains(text(), " Photos/Images ")]/parent::div/div[1]/label/span')
    photoKeyArtCheckbox = (By.XPATH, '//div[contains(text(), "Key Art: Main")]/parent::div/label/span')
    frameRateText = (By.XPATH, '//span[contains(text(), " Frame Rate ")]')
    selectedOne = (By.XPATH, '//span[contains(@class,"number")]')
    videoPropertiesClearButton = (By.XPATH, '//h5[contains(text(),"Video Properties")]/parent::div/parent::div/parent::'
                                            'div//span[contains(text(),"CLEAR")]')
    assetTypeClearButton = (By.XPATH, '//h5[contains(text(),"Asset Type")]/parent::div/parent::div/parent::'
                                      'div//span[contains(text(),"CLEAR")]')
    fileSizeResetButton = (By.XPATH, '//h5[contains(text(),"File Size")]/parent::div/parent::div/parent::div//'
                                     'span[contains(text(),"RESET ")]')
    allAssetsFirstCard = (By.XPATH, '//div[contains(@class,"movie-poster")]//div[@class="row movie-asset"]/div[1]/div')
    allAssetsResult = (By.XPATH, '//div/p[contains(text(),"Results")]')
    paginationNextButton = (By.XPATH, '//li[contains(@class,"pagination-next")]/a')
    paginationVerify = (By.XPATH, '//li[contains(@class,"pagination-next")]')
    fileTypePdfText = (By.XPATH, '//div[contains(text(),"PDF (.pdf )")]')
    fileTypeJpegPhoto = (By.XPATH, '//div[contains(text(),"JPEG Image (.jpg, .jpeg )")]')
    fileTypeVideo = (By.XPATH, '//div[contains(text(),"Video (.3gpp, .mov, .mp4 )")]')
    itemsSelectedText = (By.XPATH, "//div[contains(@class,'asset-body' )]//div[contains(@class,'share-popup' )]//"
                                   "div[contains(@class,'item-actions' )][1]/span[contains(text(),'Items Selected')]")
    itemSelectedText = (By.XPATH, "//div[contains(@class,'asset-body' )]//div[contains(@class,'share-popup' )]//div"
                                  "[contains(@class,'item-actions' )][1]/span[contains(text(),'1 Item Selected')]")
    twoItemsSelectedText = (By.XPATH, "//div[contains(@class,'asset-body' )]//div[contains(@class,'share-popup' )]//div"
                                      "[contains(@class,'item-actions' )][1]/span[contains(text(),'2 Items Selected')]")
    threeItemsSelectedText = (By.XPATH, "//div[contains(@class,'asset-body' )]//div[contains(@class,'share-popup' )]//div"
                                      "[contains(@class,'item-actions' )][1]/span[contains(text(),'3 Items Selected')]")
    startDownloadButton = (By.XPATH, '//div/button[contains(text()," Start Download ")]')
    downloadInProgressText = (By.XPATH, '//p[contains(text(),"Download in progress")]')
    cancelButton = (By.XPATH, '//div[contains(@class,"delete-btn")]/button[contains(text()," Cancel ")]')
    downloadFooterCloseButton = (By.XPATH, '(//div[@class="modal-content"]//div[contains(@class,"ltcc-modal")]//div[@aria-label="Close"]/img[@class="close-btn-image"])[2]')
    downloadPopupDescription = (By.XPATH, '//div[contains(@class,"sm-top")]//h3')
    singleItemSelected = (By.XPATH, "//div[contains(@class,'asset-body' )]//div[contains(@class,'share-popup' )]//div"
                                    "[contains(@class,'item-actions' )][1]/span[contains(text(),'1 Item Selected')]")
    listHeaderFileNameText = (By.XPATH, '//div[contains(@class,"file-name")]')
    listHeaderFileSizeText = (By.XPATH, '//div[contains(@class,"file-size")]')
    listHeaderFileAssetTypeText = (By.XPATH, '//div[contains(@class,"asset-type")]')
    listFirstCheckBox = (By.XPATH, '//div[contains(@class,"row asset-list-row")][1]/div[contains(@class,"checkBox")]')
    listFirstAddCartButton = (By.XPATH, '//div[contains(@class,"row asset-list-row")][1]'
                                        '//img[contains(@class,"asset-addcart")]')
    addToCartPopup = (By.XPATH, '//div/span[contains(text(),"CREATE A NEW CART")]')
    sortingFileSizeUp = (By.XPATH, '//span[contains(text(),"FILE SIZE")]/div[contains(@class,"custom-up-arrow")]')
    sortingFileSizeDown = (By.XPATH, '//span[contains(text(),"FILE SIZE")]/div[contains(@class,"custom-down-arrow")]')
    firstFileSizeDimension = (By.XPATH, '//div[contains(@class,"row asset-list-row")][1]//div[contains(@class,'
                                        '"dimension")]')
    secondFileSizeDimension = (By.XPATH, '//div[contains(@class,"row asset-list-row")][2]//div[contains(@class,'
                                         '"dimension")]')
    thirdFileSizeDimension = (By.XPATH, '//div[contains(@class,"row asset-list-row")][3]//div[contains(@class,'
                                        '"dimension")]')
    sortingFileAtoZButton = (By.XPATH, '//span[contains(text(),"FILE NAME A-Z")]')
    sortingFileZtoAButton = (By.XPATH, '//span[contains(text(),"FILE NAME Z-A")]')
    allAssetTitleText = (By.XPATH, '//div[contains(@class,"file-titles")]')
    sortingFileByDateUp = (By.XPATH, '//span[contains(text(),"SORT BY DATE")]/div[contains(@class,"custom-up-arrow")]')
    sortingFileByDateDown = (By.XPATH, '//span[contains(text(),"SORT BY DATE")]/div'
                                       '[contains(@class,"custom-down-arrow")]')
    assetsFirstCardImage = (By.XPATH, '//div[contains(@class,"row asset-list-row")][1]//div/img')
    footerDownloadButton = (By.XPATH, '//div[contains(@class,"item-actions")]//button[contains(text(),"DOWNLOAD")]')
    footerAddToCartButton = (
        By.XPATH, '//div[contains(@class,"item-actions")]//button[contains(text(),"ADD TO CART ")]')
    assetsSecondCardImage = (By.XPATH, '//div[contains(@class,"row asset-list-row")][2]//div/img')
    assetFileUploadDate = (By.XPATH, '//span[contains(text(),"Updated At")]/parent::div/div')
    previewCloseButton = (By.XPATH, '//div[contains(@class,"modal-header-popup")]/'
                                    'div/img[contains(@class,"close-btn-image")]')
    enterUniqueCartNameText = (By.XPATH, '//span[contains(text(),"Please enter a unique cart name.")]')
    previewLeftImage = (By.XPATH, '//div[contains(@class,"left-panel")]/div/img[contains(@default,"/assets/images")]')
    previewDownloadButton = (By.XPATH, '//a/img[contains(@class,"preview-asset-icon")]')
    previewAddToCartButton = (By.XPATH, '//div/img[contains(@class,"preview-asset-icon")]')
    previewNextIconButton = (By.XPATH, '//div/i[contains(@class,"next")]')
    previewRightDescription = (By.XPATH, '//div[contains(@class,"right-panel")]/div[contains(@class,"right-panel")]')
    previewPreviousButton = (By.XPATH, '//div/i[contains(@class,"previous")]')
    videoPropertiesDropdown = (By.XPATH, '//div/h5[contains(text(),"Video Properties")]')
    fileTypeFilterDropdown = (By.XPATH, '//div/h5[contains(text(),"File Type")]')
    assetTypeFilterDropdown = (By.XPATH, '//div/h5[contains(text(),"Asset Type")]')
    fileSizeTypeFilterDropdown = (By.XPATH, '//div/h5[contains(text(),"File Size")]')
    video3gpMovMp4Checkbox = (By.XPATH, '//div[contains(text(),"Video (.3gpp, .mov, .mp4 )")]/parent::div/label/span[contains(@class ,"checkmark checked")]')
    pdfCheckbox = (By.XPATH, '//div[contains(text(),"PDF (.pdf )")]/parent::div/label/span[contains(@class ,"checkmark checked")]')
    jpegImageCheckbox = (By.XPATH, '//div[contains(text(),"JPEG Image (.jpg, .jpeg )")]/parent::div/label/span[contains(@class ,"checkmark checked")]')
    resultCount = (By.XPATH, '//div/p[contains(text(),"Result")]/parent::div/p')
    fileTypeClearButton = (By.XPATH, '//div[contains(@id,"flt-content_type")]//span[contains(text(),"CLEAR")]')

    firstCardPreviewButton = (By.XPATH, '//div[contains(@class,"row movie")]/div[1]/div[contains(@class,"poster")]'
                                        '//ul/li/button[contains(text(),"Preview")]')
    firstCardDownloadButton = (By.XPATH, '//div[contains(@class,"row movie")]/div[1]/div[contains(@class,"poster")]'
                                         '//ul//button[contains(text(),"Download")]')
    firstCardAddToCartButton = (By.XPATH, '//div[contains(@class,"row movie")]/div[1]/div[contains(@class,"poster")]'
                                          '//ul//button[contains(text(),"Add to cart")]')
    previewButton = (By.XPATH, '//button[contains(text(),"Preview")]')
    firstGridCardImage = (By.XPATH, '//div[contains(@class,"row movie")]/div[1]/div[contains(@class,"poster")]//img')
    firstGridCardCheckbox = (By.XPATH, '//div[contains(@class,"row movie")]/div[1]/div[contains(@class,"poster")]'
                                       '//div[contains(@class,"checkbox")]/input')
    firstGridCardCheckbox1 = (By.XPATH, '//div[contains(@class,"row movie")]/div[1]/div[contains(@class,"poster")]'
                                        '//div[contains(@class,"checkbox")]')
    secondGridCardCheckbox = (By.XPATH, '//div[contains(@class,"row movie")]/div[2]/div[contains(@class,"poster")]'
                                        '//div[contains(@class,"checkbox")]/input[contains(@class,"inputBox")]')
    cartNameInputField = (By.XPATH, '//input[@placeholder="My New Cart Name"]')
    createCartButton = (By.XPATH, "//div[@class='atl-newlistadd']/button")
    createdText = (By.XPATH, '//span[text()=" Created! "]')
    creatingText = (By.XPATH, '//div[text()="Creating..."]')
    testingCartName = (By.XPATH, "//div[contains(@class,'toggle-btn-item')]//span[text() = ' testingCart ']")
    testingCart2Name = (By.XPATH, "//div[contains(@class,'toggle-btn-item')]//span[text() = ' testingCart2 ']")
    testingCartToggleButton = (By.XPATH, "//span[text()=' testingCart ']/ancestor::label/input")
    testingCart2ToggleButton = (By.XPATH, "//span[text()=' testingCart2 ']/ancestor::label/input")
    cartTestingCart = (By.XPATH, '//span[text()=" testingCart "]')
    cartTestingCart2 = (By.XPATH, '//span[text()=" testingCart2 "]')

    def __init__(self, browser):
        self.browser = browser

    #@allure.step('verify user can create new cart')
    def click_create_cart(self):
        time.sleep(1)
        create_list = self.browser.find_element(*self.createCartButton)
        time.sleep(1.5)
        self.browser.execute_script("arguments[0].click();", create_list)
        WebDriverWait(self.browser, 80).until(EC.presence_of_element_located(self.creatingText))
        return True

    #@allure.step('verify user can create new cart')
    def click_create_cart_duplicate(self):
        time.sleep(1)
        create_list = self.browser.find_element(*self.createCartButton)
        time.sleep(1)
        self.browser.execute_script("arguments[0].click();", create_list)

    #@allure.step('Verify new cart should be present in add to cart popup')
    def verify_cart_created(self):
        return self.browser.find_element(*self.testingCartName).is_displayed()

    #@allure.step('Verify new cart should be present in add to cart popup')
    def verify_second_cart_created(self):
        return self.browser.find_element(*self.testingCart2Name).is_displayed()

    #@allure.step('verify user can search any cart name in cart search box')
    def verify_search_testing_cart_name(self):
        time.sleep(1)
        return self.browser.find_element(*self.cartTestingCart).is_displayed()

    #@allure.step('verify user can select cart')
    def verify_cart_selectable(self):
        WebDriverWait(self.browser, 140).until(EC.presence_of_element_located(self.cartTestingCart))
        time.sleep(1.5)
        cart_toggle_button = self.browser.find_element(*self.cartTestingCart)
        time.sleep(.5)
        self.browser.execute_script("arguments[0].click();", cart_toggle_button)
        time.sleep(1.5)
        return self.browser.find_element(*self.testingCartToggleButton).is_selected()

    #@allure.step('Verify Created cart is auto-selected')
    def verify_cart_is_auto_select(self):
        time.sleep(3)
        try:

            if self.browser.find_element(*self.testingCartToggleButton).is_selected():
                print('If is working')
                return True
            else:
                cart_toggle_button = self.browser.find_element(*self.cartTestingCart)
                time.sleep(1)
                self.browser.execute_script("arguments[0].click();", cart_toggle_button)
                time.sleep(2)
                print('else is working')
                return self.browser.find_element(*self.testingCartToggleButton).is_selected()
        except:
            cart_toggle_button = self.browser.find_element(*self.cartTestingCart)
            time.sleep(1)
            self.browser.execute_script("arguments[0].click();", cart_toggle_button)
            time.sleep(2)
            print('cart auto Selecting Functionality is not working')
            return self.browser.find_element(*self.testingCartToggleButton).is_selected()

    #@allure.step('Verify Created cart is auto-selected')
    def verify_second_cart_is_auto_select(self):
        time.sleep(5)
        try:

            if self.browser.find_element(*self.testingCart2ToggleButton).is_selected():
                print('If is working')
                return True
            else:
                cart_toggle_button = self.browser.find_element(*self.cartTestingCart2)
                time.sleep(1)
                self.browser.execute_script("arguments[0].click();", cart_toggle_button)
                time.sleep(2)
                print('else is working')
                return self.browser.find_element(*self.testingCart2ToggleButton).is_selected()
        except:
            cart_toggle_button = self.browser.find_element(*self.cartTestingCart2)
            time.sleep(1)
            self.browser.execute_script("arguments[0].click();", cart_toggle_button)
            time.sleep(2)
            print('cart auto Selecting Functionality is not working')
            return self.browser.find_element(*self.testingCart2ToggleButton).is_selected()

    #@allure.step('Verify Created text should be visible when cart created')
    def created_cart_text(self):
        WebDriverWait(self.browser, 20).until(EC.presence_of_element_located(self.createdText))
        return self.browser.find_element(*self.createdText).is_displayed()

    #@allure.step('Verify close button present in preview page')
    def verify_preview_close_button(self):
        return self.browser.find_element(*self.previewCloseButton).is_displayed()

    #@allure.step('verify user is not able to create duplicate cart')
    def verify_duplicate_cart_name(self):
        time.sleep(2.5)
        return self.browser.find_element(*self.enterUniqueCartNameText).is_displayed()

    #@allure.step('verify user can type new cart name')
    def enter_cart_name(self, name):
        time.sleep(1)
        self.browser.find_element(*self.cartNameInputField).send_keys(name)

    #@allure.step('Verify close button is clickable in preview page')
    def click_preview_close_button(self):
        close_button = self.browser.find_element(*self.previewCloseButton)
        self.browser.execute_script("arguments[0].click();", close_button)
        time.sleep(4)
        try:
            close_button = self.browser.find_element(*self.previewCloseButton).is_displayed()
            if close_button:
                return True
        except:
            return False

    #@allure.step('Verify Next-Icon button present in preview page')
    def verify_preview_next_icon_button(self):
        return self.browser.find_element(*self.previewNextIconButton).is_displayed()

    #@allure.step('Verify previous-Icon button present in preview page')
    def verify_previous_icon_button(self):
        self.browser.find_element(*self.previewNextIconButton).click()
        WebDriverWait(self.browser, 30).until(EC.element_to_be_clickable(self.previewPreviousButton))
        return self.browser.find_element(*self.previewPreviousButton).is_displayed()

    #@allure.step('Verify previous-Icon button present in preview page')
    def verify_previous_icon_button_clickable(self):
        self.browser.find_element(*self.previewNextIconButton).click()
        time.sleep(15)
        # WebDriverWait(self.browser, 50).until(EC.element_to_be_clickable(self.previewPreviousButton))
        self.browser.find_element(*self.previewPreviousButton).click()
        time.sleep(15)
        try:
            # WebDriverWait(self.browser, 15).until(EC.presence_of_element_located(self.previewPreviousButton))
            previous_button = self.browser.find_element(*self.previewPreviousButton).is_displayed()
            if previous_button:
                return True
        except:
            return False

    #@allure.step('Verify Next-Icon button present in preview page')
    def verify_preview_page_description(self):
        return self.browser.find_element(*self.previewRightDescription).is_displayed()

    #@allure.step('Verify Add to cart button present in preview page')
    def verify_preview_add_to_cart_button(self):
        return self.browser.find_element(*self.previewAddToCartButton).is_displayed()

    #@allure.step('Verify Add to cart button clickable in preview page')
    def click_preview_add_to_cart_button(self):
        self.browser.find_element(*self.previewAddToCartButton).click()
        WebDriverWait(self.browser, 5).until(EC.presence_of_element_located(self.addToCartPopup))
        return self.browser.find_element(*self.addToCartPopup).is_displayed()

    #@allure.step('Verify download button present in preview page')
    def verify_preview_download_button(self):
        return self.browser.find_element(*self.previewDownloadButton).is_displayed()

    #@allure.step('Verify image or pdf present in preview page')
    def verify_preview_image_pdf(self):
        return self.browser.find_element(*self.previewLeftImage).is_displayed()

    #@allure.step('Verify checkbox present in card elements')
    def verify_grid_card_checkbox(self):
        return self.browser.find_element(*self.firstGridCardCheckbox1).is_displayed()

    #@allure.step('Verify Add To Cart button is present in Footer popup')
    def verify_footer_add_to_cart(self):
        return self.browser.find_element(*self.footerAddToCartButton).is_displayed()

    #@allure.step('Verify Add To Cart button is clickable in Footer popup')
    def click_footer_add_to_cart_button(self):
        self.browser.find_element(*self.footerAddToCartButton).click()
        WebDriverWait(self.browser, 5).until(EC.presence_of_element_located(self.addToCartPopup))
        return self.browser.find_element(*self.addToCartPopup).is_displayed()

    # @allure.step('Verify Add To Cart popup is not present')
    def verify_add_to_cart_footer_not_present(self):
        time.sleep(4.5)
        try:
            add_to_cart = self.browser.find_element(*self.itemSelectedText).is_displayed()
            if add_to_cart:
                return True
            else:
                return False
        except:
            return False

    #@allure.step('Verify Add To Cart popup is not present')
    def verify_add_to_cart_not_present(self):
        time.sleep(3)
        try:
            add_to_cart = self.browser.find_element(*self.addToCartPopup).is_displayed()
            if add_to_cart:
                return True
            else:
                return False
        except:
            return False

    #@allure.step('Verify Download button is present in Footer popup')
    def verify_footer_download(self):
        return self.browser.find_element(*self.footerDownloadButton).is_displayed()

    #@allure.step('Verify Download button is clickable in Footer popup')
    def verify_footer_download_clickable(self):
        time.sleep(3)
        start_download = self.browser.find_element(*self.startDownloadButton).is_displayed()
        return start_download

    #@allure.step('Verify Download button is clickable in Footer popup')
    def click_footer_start_download_button(self):
        time.sleep(2)
        self.browser.find_element(*self.startDownloadButton).click()
        WebDriverWait(self.browser, 8).until(EC.presence_of_element_located(self.downloadInProgressText))
        return self.browser.find_element(*self.downloadInProgressText).is_displayed()

    #@allure.step('Verify card checkbox is clickable')
    def click_first_grid_card_checkbox(self):
        self.browser.find_element(*self.secondGridCardCheckbox).click()

    #@allure.step('Verify card checkbox is clickable')
    def click_second_grid_card_checkbox(self):
        time.sleep(1.5)
        # self.browser.find_element(*self.secondGridCardCheckbox).click()
        second_checkbox = self.browser.find_element(*self.firstGridCardCheckbox)
        time.sleep(1.5)
        self.browser.execute_script("arguments[0].scrollIntoView();", second_checkbox)
        time.sleep(2.5)
        self.browser.execute_script("arguments[0].click();", second_checkbox)
        time.sleep(3)
        try:
            second_click = self.browser.find_element(*self.twoItemsSelectedText).is_displayed()
            if second_click:
                print('second click already selected')
        except:
            second_checkbox = self.browser.find_element(*self.firstGridCardCheckbox)
            time.sleep(1)
            self.browser.execute_script("arguments[0].click();", second_checkbox)

    #@allure.step('Verify card checkbox is clickable')
    def click_first_grid_card_checkbox_download(self):
        WebDriverWait(self.browser, 15).until(EC.presence_of_element_located(self.firstGridCardCheckbox))
        time.sleep(1)
        second_checkbox = self.browser.find_element(*self.firstGridCardCheckbox)
        time.sleep(1)
        self.browser.execute_script("arguments[0].scrollIntoView();", second_checkbox)
        time.sleep(1.5)
        self.browser.execute_script("arguments[0].click();", second_checkbox)
        time.sleep(2.5)

    #@allure.step('Verify File-Type dropdown is present dropdown is present in left side Navigation ')
    def verify_file_type_filter_dropdown(self):
        return self.browser.find_element(*self.fileTypeFilterDropdown).is_displayed()

    #@allure.step('Verify Video Properties dropdown is present in left side Navigation ')
    def verify_video_properties_dropdown(self):
        return self.browser.find_element(*self.videoPropertiesDropdown).is_displayed()

    #@allure.step('Verify Resolution checkbox is present in Video-Properties')
    def verify_video_resolution_text(self):
        return self.browser.find_element(*self.resolutionText).is_displayed()

    #@allure.step('Verify Frame-Rate checkbox is present in Video-Properties')
    def verify_video_frame_rate_text(self):
        return self.browser.find_element(*self.frameRateText).is_displayed()

    #@allure.step('Verify File-Size is present in heading in list view')
    def verify_asset_type_filter_dropdown(self):
        return self.browser.find_element(*self.assetTypeFilterDropdown).is_displayed()

    #@allure.step('Verify File-Size is present in heading in list view')
    def verify_file_size_filter_dropdown(self):
        return self.browser.find_element(*self.fileSizeTypeFilterDropdown).is_displayed()

    def assets_page_refresh(self):
        time.sleep(1)
        self.browser.refresh()
        WebDriverWait(self.browser, 300).until(EC.presence_of_element_located(self.tabTitleOverview))
        time.sleep(2.5)

    #@allure.step('Verify Sorting Filter button is Clickable')
    def click_sorting_filter(self):
        time.sleep(1.5)
        sorting_filter = self.browser.find_element(*self.sortingFilterButton)
        time.sleep(1)
        self.browser.execute_script("arguments[0].click();", sorting_filter)
        time.sleep(1)

    #@allure.step('Verify file-type clear button is Clickable')
    def click_file_type_clear_button(self):
        file_type = self.browser.find_element(*self.fileTypeClearButton)
        self.browser.execute_script("arguments[0].click();", file_type)
        time.sleep(6)

    #@allure.step('Click on Frame rate checkbox field')
    def click_video_frame_rate_checkbox(self):
        frame_rate = self.browser.find_element(*self.frameRateCheckbox)
        self.browser.execute_script("arguments[0].click();", frame_rate)
        time.sleep(7)

    #@allure.step('Click on Script checkbox in Asset-Type')
    def click_document_script_checkbox(self):
        frame_rate = self.browser.find_element(*self.scriptCheckbox)
        self.browser.execute_script("arguments[0].click();", frame_rate)
        time.sleep(7)

    #@allure.step('Click on Video Trailer checkbox in Asset-Type')
    def click_video_trailer_checkbox(self):
        video_trailer = self.browser.find_element(*self.videoCheckbox)
        self.browser.execute_script("arguments[0].click();", video_trailer)
        time.sleep(7)

    #@allure.step('Click on Asset type images checkbox')
    def click_photo_images_checkbox(self):
        photo_images = self.browser.find_element(*self.photoImagesCheckbox)
        self.browser.execute_script("arguments[0].click();", photo_images)
        time.sleep(7)


    #@allure.step('Click on Asset type key-Art checkbox')
    def click_key_art_checkbox(self):
        key_art = self.browser.find_element(*self.photoKeyArtCheckbox)
        self.browser.execute_script("arguments[0].click();", key_art)
        time.sleep(7)

    #@allure.step('Click on Paid-Ad-Memo checkbox in Asset-Type')
    def click_document_paid_ad_memo_checkbox(self):
        frame_rate = self.browser.find_element(*self.paidAdMemoCheckbox)
        self.browser.execute_script("arguments[0].click();", frame_rate)
        time.sleep(7)

    #@allure.step('Click on Paid-Ad-Memo checkbox in Asset-Type')
    def click_paid_tab_paid_ad_memo_checkbox(self):
        frame_rate = self.browser.find_element(*self.paidTabPaidAdMemoCheckbox)
        self.browser.execute_script("arguments[0].click();", frame_rate)
        time.sleep(7)

    #@allure.step('Click on Paid-Ad-Memo checkbox in Asset-Type')
    def click_paid_tab_ads_paid_ad_memo_checkbox(self):
        frame_rate = self.browser.find_element(*self.paidTabAdsPaidAdMemoCheckbox)
        self.browser.execute_script("arguments[0].click();", frame_rate)
        time.sleep(7)

    #@allure.step('Click on Resolution checkbox field')
    def click_video_resolution_checkbox(self):
        frame_rate = self.browser.find_element(*self.resolutionCheckbox)
        self.browser.execute_script("arguments[0].click();", frame_rate)
        time.sleep(7)

    #@allure.step('Verify Checkbox count in Video Properties Section')
    def verify_selected_checkbox_count(self):
        return self.browser.find_element(*self.selectedOne).text

    #@allure.step('Verify Checkbox count in Video Properties Section')
    def verify_click_clear_selected_checkbox_count(self):
        try:
            time.sleep(5)
            selecet_item = self.browser.find_element(*self.selectedOne).is_displayed()
            if selecet_item:
                return True
        except:
            return False

    #@allure.step('Verify date filter (up) functionality')
    def mouse_hover_on_first_file_image(self):
        self.browser.find_element(*self.sortingFileByDateUp).click()
        time.sleep(8)
        movie_card = self.browser.find_element(*self.assetsFirstCardImage)
        time.sleep(2)
        self.browser.execute_script("arguments[0].scrollIntoView();", movie_card)
        time.sleep(2)
        ActionChains(self.browser).move_to_element(movie_card).perform()
        time.sleep(2)
        upload_time = self.browser.find_element(*self.assetFileUploadDate).text
        year_date_month_time = upload_time.split("T")
        # print(year_date_month_time)
        year_date_month = year_date_month_time[0].split("-")
        # print(year_date_month_time[0])
        year_text = int(year_date_month[0])
        month_text = int(year_date_month[1])
        date_text = int(year_date_month[2])
        # print(year_text, date_text, month_text)
        first_card_date = datetime.datetime(year_text, month_text, date_text)

        movie_card2 = self.browser.find_element(*self.assetsSecondCardImage)
        ActionChains(self.browser).move_to_element(movie_card2).perform()
        time.sleep(2)
        upload_time = self.browser.find_element(*self.assetFileUploadDate).text
        year_date_month_time2 = upload_time.split("T")
        year_date_month2 = year_date_month_time2[0].split("-")
        year_text1 = int(year_date_month2[0])
        month_text1 = int(year_date_month2[1])
        date_text1 = int(year_date_month2[2])
        # print(year_text1, date_text1, month_text1)
        second_card_date = datetime.datetime(year_text1, month_text1, date_text1)
        try:
            if first_card_date >= second_card_date:
                return True
        except:
            return False

    #@allure.step('Verify date filter (Down) functionality')
    def mouse_hover_on_Second_file_image(self):
        self.browser.find_element(*self.sortingFileByDateDown).click()
        time.sleep(8)
        movie_card = self.browser.find_element(*self.assetsFirstCardImage)
        time.sleep(2)
        self.browser.execute_script("arguments[0].scrollIntoView();", movie_card)
        time.sleep(2)
        ActionChains(self.browser).move_to_element(movie_card).perform()
        time.sleep(2)
        upload_time = self.browser.find_element(*self.assetFileUploadDate).text
        year_date_month_time = upload_time.split("T")
        # print(year_date_month_time)
        year_date_month = year_date_month_time[0].split("-")
        # print(year_date_month_time[0])
        year_text = int(year_date_month[0])
        month_text = int(year_date_month[1])
        date_text = int(year_date_month[2])
        # print(year_text, date_text, month_text)
        first_card_date = datetime.datetime(year_text, month_text, date_text)

        movie_card2 = self.browser.find_element(*self.assetsSecondCardImage)
        ActionChains(self.browser).move_to_element(movie_card2).perform()
        time.sleep(2)
        upload_time = self.browser.find_element(*self.assetFileUploadDate).text
        year_date_month_time2 = upload_time.split("T")
        year_date_month2 = year_date_month_time2[0].split("-")
        year_text1 = int(year_date_month2[0])
        month_text1 = int(year_date_month2[1])
        date_text1 = int(year_date_month2[2])
        # print(year_text1, date_text1, month_text1)
        second_card_date = datetime.datetime(year_text1, month_text1, date_text1)
        try:
            if second_card_date >= first_card_date:
                return True
        except:
            return False

    #@allure.step('Verify Preview button present on first card')
    def mouse_hover_first_card_preview_button(self):
        WebDriverWait(self.browser, 15).until(EC.presence_of_element_located(self.firstGridCardImage))
        first_card = self.browser.find_element(*self.firstGridCardImage)
        time.sleep(2)
        self.browser.execute_script("arguments[0].scrollIntoView();", first_card)
        time.sleep(2)
        ActionChains(self.browser).move_to_element(first_card).perform()
        time.sleep(2)
        preview_button = self.browser.find_element(*self.firstCardPreviewButton)
        ActionChains(self.browser).move_to_element(preview_button).perform()
        time.sleep(2)
        return preview_button.is_displayed()

    #@allure.step('Verify Preview button is clickable on first card')
    def click_first_card_preview_button(self):
        WebDriverWait(self.browser, 15).until(EC.presence_of_element_located(self.firstGridCardImage))
        time.sleep(4)
        first_card = self.browser.find_element(*self.firstGridCardImage)
        time.sleep(2)
        self.browser.execute_script("arguments[0].scrollIntoView();", first_card)
        time.sleep(2)
        ActionChains(self.browser).move_to_element(first_card).perform()
        time.sleep(2)
        preview_button = self.browser.find_element(*self.firstCardPreviewButton)
        ActionChains(self.browser).move_to_element(preview_button).perform()
        time.sleep(2)
        preview_button.click()

    #@allure.step('Verify date elements are present on Preview Page')
    def verify_date_preview_page(self):
        time.sleep(2)
        return self.browser.find_element(*self.assetFileUploadDate).is_displayed()

    #@allure.step('Verify download button present on first card')
    def mouse_hover_first_card_download_button(self):
        download_button = self.browser.find_element(*self.firstCardDownloadButton)
        ActionChains(self.browser).move_to_element(download_button).perform()
        time.sleep(2)
        return download_button.is_displayed()

    #@allure.step('click download button present on first card')
    def click_first_card_download_button(self):
        WebDriverWait(self.browser, 16).until(EC.presence_of_element_located(self.resetFiltersButton))
        download_button = self.browser.find_element(*self.firstCardDownloadButton)
        ActionChains(self.browser).move_to_element(download_button).perform()
        time.sleep(2)
        download_button.click()

    #@allure.step('Verify Add to cart button present on first card')
    def mouse_hover_first_card_add_to_cart_button(self):
        add_cart_button = self.browser.find_element(*self.firstCardAddToCartButton)
        ActionChains(self.browser).move_to_element(add_cart_button).perform()
        time.sleep(2)
        return add_cart_button.is_displayed()

    #@allure.step('Verify Add to cart button is clickable in card')
    def click_first_card_add_to_cart_button(self):
        WebDriverWait(self.browser, 15).until(EC.presence_of_element_located(self.firstGridCardImage))
        time.sleep(4)
        first_card = self.browser.find_element(*self.firstGridCardImage)
        time.sleep(2)
        self.browser.execute_script("arguments[0].scrollIntoView();", first_card)
        time.sleep(2)
        ActionChains(self.browser).move_to_element(first_card).perform()
        time.sleep(2)
        add_cart_button = self.browser.find_element(*self.firstCardAddToCartButton)
        ActionChains(self.browser).move_to_element(add_cart_button).perform()
        time.sleep(2)
        add_cart_button.click()
        WebDriverWait(self.browser, 5).until(EC.presence_of_element_located(self.addToCartPopup))
        return self.browser.find_element(*self.addToCartPopup).is_displayed()

    #@allure.step('Verify User can click on Video checkbox in file type section  ')
    def click_video_mp4_3gp_checkbox_file_type(self):
        WebDriverWait(self.browser, 10).until(EC.presence_of_element_located(self.video3gpMovMp4Checkbox))
        video_checkbox = self.browser.find_element(*self.video3gpMovMp4Checkbox)
        self.browser.execute_script("arguments[0].scrollIntoView();", video_checkbox)
        time.sleep(1)
        self.browser.execute_script("arguments[0].click();", video_checkbox)
        time.sleep(6)

    #@allure.step('Verify User can click on PDF checkbox in file type section  ')
    def click_pdf_checkbox_file_type(self):
        WebDriverWait(self.browser, 10).until(EC.presence_of_element_located(self.pdfCheckbox))
        pdf_checkbox = self.browser.find_element(*self.pdfCheckbox)
        self.browser.execute_script("arguments[0].scrollIntoView();", pdf_checkbox)
        time.sleep(1)
        self.browser.execute_script("arguments[0].click();", pdf_checkbox)
        time.sleep(6)

    #@allure.step('Verify User can click on JPEG checkbox in file type section  ')
    def click_jpeg_checkbox_file_type(self):
        WebDriverWait(self.browser, 10).until(EC.presence_of_element_located(self.jpegImageCheckbox))
        jpeg_checkbox = self.browser.find_element(*self.jpegImageCheckbox)
        self.browser.execute_script("arguments[0].scrollIntoView();", jpeg_checkbox)
        time.sleep(1)
        self.browser.execute_script("arguments[0].click();", jpeg_checkbox)
        time.sleep(6)

    #@allure.step('Verify Result count in asset page')
    def verify_total_count_asset(self):
        time.sleep(1)
        result_text = self.browser.find_element(*self.resultCount).text
        result_count = result_text.split(" ")
        return int(result_count[0])

    #@allure.step('Verify Result text is present in assets page')
    def verify_total_result_text(self):
        time.sleep(1)
        return self.browser.find_element(*self.resultCount).is_displayed()

    #@allure.step('Verify User can sort in larger to smaller size')
    def click_sorting_file_size_up_filter(self):
        time.sleep(2)
        self.browser.find_element(*self.sortingFileSizeUp).click()
        WebDriverWait(self.browser, 20).until(EC.presence_of_element_located(self.secondFileSizeDimension))
        time.sleep(7)
        first_file_size = self.browser.find_element(*self.secondFileSizeDimension).text
        first_file = first_file_size.split(".")
        file_name = int(first_file[0])
        print(file_name)
        second_file_size = self.browser.find_element(*self.thirdFileSizeDimension).text
        second_file = second_file_size.split(".")
        file_name_two = int(second_file[0])
        print(file_name_two)
        return file_name, file_name_two

    #@allure.step('Verify User can sort in larger to smaller size')
    def click_sorting_file_size_up_filter_documents(self):
        self.browser.find_element(*self.sortingFileSizeUp).click()
        WebDriverWait(self.browser, 20).until(EC.presence_of_element_located(self.firstFileSizeDimension))
        time.sleep(7)
        first_file_size = self.browser.find_element(*self.firstFileSizeDimension).text
        first_file = first_file_size.split(".")
        file_name = int(first_file[0])
        print(file_name)
        second_file_size = self.browser.find_element(*self.secondFileSizeDimension).text
        second_file = second_file_size.split(".")
        file_name_two = int(second_file[0])
        print(file_name_two)
        return file_name, file_name_two

    #@allure.step('Verify User can sort in smaller to larger file')
    def click_sorting_file_size_down_filter(self):
        time.sleep(2)
        self.browser.find_element(*self.sortingFileSizeDown).click()
        WebDriverWait(self.browser, 20).until(EC.presence_of_element_located(self.secondFileSizeDimension))
        time.sleep(7)
        first_file_size = self.browser.find_element(*self.secondFileSizeDimension).text
        first_file = first_file_size.split(".")
        file_name = int(first_file[0])
        print(file_name)
        second_file_size = self.browser.find_element(*self.thirdFileSizeDimension).text
        second_file = second_file_size.split(".")
        file_name_two = int(second_file[0])
        print(file_name_two)
        return file_name, file_name_two

    # @allure.step('Verify User can sort in smaller to larger file')
    def click_sorting_file_size_down_filter_respect(self):
        time.sleep(2)
        self.browser.find_element(*self.sortingFileSizeDown).click()
        WebDriverWait(self.browser, 20).until(EC.presence_of_element_located(self.secondFileSizeDimension))
        time.sleep(7)
        first_file_size = self.browser.find_element(*self.firstFileSizeDimension).text
        first_file = first_file_size.split(".")
        file_name = int(first_file[0])
        print(file_name)
        second_file_size = self.browser.find_element(*self.secondFileSizeDimension).text
        second_file = second_file_size.split(".")
        file_name_two = int(second_file[0])
        print(file_name_two)
        return file_name, file_name_two


    #@allure.step('Verify User can sort in smaller to larger file')
    def click_sorting_file_size_down_filter_documents(self):
        time.sleep(2)
        self.browser.find_element(*self.sortingFileSizeDown).click()
        WebDriverWait(self.browser, 20).until(EC.presence_of_element_located(self.firstFileSizeDimension))
        time.sleep(7)
        first_file_size = self.browser.find_element(*self.firstFileSizeDimension).text
        first_file = first_file_size.split(".")
        file_name = int(first_file[0])
        print(file_name)
        second_file_size = self.browser.find_element(*self.secondFileSizeDimension).text
        second_file = second_file_size.split(".")
        file_name_two = int(second_file[0])
        print(file_name_two)
        return file_name, file_name_two

    # @allure.step('Verify User can sort in smaller to larger file')
    def click_sorting_file_size_respect_movie_down_filter_documents(self):
        time.sleep(2)
        self.browser.find_element(*self.sortingFileSizeDown).click()
        WebDriverWait(self.browser, 20).until(EC.presence_of_element_located(self.firstFileSizeDimension))
        time.sleep(7)
        first_file_size = self.browser.find_element(*self.secondFileSizeDimension).text
        first_file = first_file_size.split(".")
        file_name = int(first_file[0])
        print(file_name)
        second_file_size = self.browser.find_element(*self.thirdFileSizeDimension).text
        second_file = second_file_size.split(".")
        file_name_two = int(second_file[0])
        print(file_name_two)
        return file_name, file_name_two

    #@allure.step('Verify user can click apply A-Z')
    def verify_file_sorting_a_to_z(self):
        self.browser.find_element(*self.sortingFileAtoZButton).click()
        time.sleep(8)
        all_movies_name = self.browser.find_elements(*self.allAssetTitleText)
        for whole_text in all_movies_name:
            movies_name = whole_text.text
            m = movies_name[0]
            assert (m == '0') or (m == '1') or (m == '2') or (m == '3') or (m == '4') or (m == '5') or (m == '6') or (
                    m == '7') or (m == '8') or (m == '9') or (m == 'A') or (m == 'a') or (m == 'T') or (m == 't') or (
                           m == 'R')

    #@allure.step('Verify user can click apply A-Z')
    def verify_file_sorting_z_to_a(self):
        self.browser.find_element(*self.sortingFileZtoAButton).click()
        time.sleep(8)
        all_movies_name = self.browser.find_elements(*self.allAssetTitleText)
        for whole_text in all_movies_name:
            movies_name = whole_text.text
            m = movies_name[0]
            assert (m == 'Z') or (m == 'Y') or (m == 'T') or (m == 'X') or (m == 'W') or (m == 'A') or (m == 'R')

    #@allure.step('Verify on click list View button page open in list view')
    def click_list_view_button(self):
        self.browser.find_element(*self.listViewButton).click()
        time.sleep(2)
        return self.browser.find_element(*self.listHeaderFileNameText).is_displayed()

    #@allure.step('Verify File-Size is present in heading in list view')
    def verify_file_size_text(self):
        return self.browser.find_element(*self.listHeaderFileSizeText).is_displayed()

    #@allure.step('Verify Add-To-Cart is Clickable and new pop should get open')
    def verify_add_to_cart_clickable(self):
        self.browser.find_element(*self.listFirstAddCartButton).click()
        WebDriverWait(self.browser, 5).until(EC.presence_of_element_located(self.addToCartPopup))
        return self.browser.find_element(*self.addToCartPopup).is_displayed()

    #@allure.step('Verify Checkbox present in list Asset Section')
    def verify_list_first_checkbox(self):
        return self.browser.find_element(*self.listFirstCheckBox).is_displayed()

    #@allure.step('Verify Asset type is present in heading in list view')
    def verify_asset_type_text(self):
        return self.browser.find_element(*self.listHeaderFileAssetTypeText).is_displayed()

    #@allure.step('Verify on click grid View button page open in list view')
    def click_grid_view_button(self):
        self.browser.find_element(*self.gridViewButton).click()
        time.sleep(2)
        try:
            filter_text = self.browser.find_element(*self.listHeaderFileNameText).is_displayed()
            if filter_text:
                return True
        except:
            return False

    #@allure.step('Verify on click select all button is selecting all Items')
    def click_all_assets_select_all_button(self):
        self.browser.find_element(*self.selectAll).click()
        time.sleep(2)
        return self.browser.find_element(*self.itemsSelectedText).is_displayed()

    #@allure.step('Verify on click select all button is selecting all Items')
    def click_video_select_all_button(self):
        self.browser.find_element(*self.selectAll).click()
        time.sleep(2)
        return self.browser.find_element(*self.itemSelectedText).is_displayed()

    #@allure.step('Verify on click select all button is selecting all Items')
    def click_documents_select_all_button(self):
        self.browser.find_element(*self.selectAll).click()
        time.sleep(2)
        return self.browser.find_element(*self.threeItemsSelectedText).is_displayed()

    #@allure.step('Verify footer popup showing for selected 2 Items')
    def verify_two_items_selected(self):
        time.sleep(2)
        return self.browser.find_element(*self.twoItemsSelectedText).is_displayed()

    #@allure.step('Verify Download button is present in footer popup')
    def verify_footer_download_button(self):
        WebDriverWait(self.browser, 7).until(EC.presence_of_element_located(self.footerDownloadButton))
        time.sleep(2)
        return self.browser.find_element(*self.footerDownloadButton).is_displayed()

    #@allure.step('Verify Download button is clickable in footer popup')
    def click_footer_download_button(self):
        WebDriverWait(self.browser, 10).until(EC.presence_of_element_located(self.footerDownloadButton))
        time.sleep(4)
        download_button = self.browser.find_element(*self.footerDownloadButton)
        self.browser.execute_script("arguments[0].click();", download_button)


    #@allure.step('Verify cancel button is present in footer popup')
    def verify_footer_cancel_button(self):
        time.sleep(2)
        return self.browser.find_element(*self.cancelButton).is_displayed()

    #@allure.step('Verify close button is present in footer popup')
    def verify_footer_close_button(self):
        time.sleep(2)
        return self.browser.find_element(*self.downloadFooterCloseButton).is_displayed()

    #@allure.step('Verify close button is clickable in footer popup')
    def click_footer_close_button(self):
        time.sleep(2)
        self.browser.find_element(*self.downloadFooterCloseButton).click()
        try:
            time.sleep(3)
            close_button = self.browser.find_element(*self.downloadFooterCloseButton).is_displayed()
            if close_button:
                return True
        except:
            return False

    #@allure.step('Verify Cancel button is clickable in footer popup')
    def click_footer_cancel_button(self):
        time.sleep(2)
        self.browser.find_element(*self.cancelButton).click()
        try:
            time.sleep(8)
            close_button = self.browser.find_element(*self.cancelButton).is_displayed()
            if close_button:
                return True
        except:
            return False

    #@allure.step('Verify Description is present in footer popup')
    def verify_footer_download_description(self):
        time.sleep(2)
        return self.browser.find_element(*self.downloadPopupDescription).is_displayed()

    #@allure.step('Verify number of count selected item in footer popup')
    def verify_footer_download_selected_count(self):
        time.sleep(2)
        whole_text_cap = self.browser.find_element(*self.downloadPopupDescription).text
        whole_text = whole_text_cap.upper()
        half_text = whole_text.split('CONTAINING')
        print(half_text[1])
        new_text = half_text[1].split(" ")
        return new_text[1]

    #@allure.step('Verify footer popup showing for selected 1 Item')
    def verify_single_item_selected(self):
        time.sleep(2)
        return self.browser.find_element(*self.singleItemSelected).is_displayed()

    #@allure.step('Verify on click reset filter button is resetting all filter')
    def click_reset_filter_button_all_assets(self):
        time.sleep(1)
        reset_button = self.browser.find_element(*self.resetFiltersButton)
        self.browser.execute_script("arguments[0].click();", reset_button)
        time.sleep(7)
        try:
            filter_text = self.browser.find_element(*self.itemsSelectedText).is_displayed()
            if filter_text:
                return True
        except:
            return False

    # @allure.step('Verify on click reset filter button is resetting all filter')
    def click_reset_filter_button_for_video(self):
        time.sleep(1)
        reset_button = self.browser.find_element(*self.resetFiltersButton)
        self.browser.execute_script("arguments[0].click();", reset_button)
        time.sleep(7)
        try:
            filter_text = self.browser.find_element(*self.selectedOne).is_displayed()
            if filter_text:
                return True
        except:
            return False



    #@allure.step('Verify on click reset filter button is resetting all filter')
    def click_reset_filter_button_video(self):
        time.sleep(1)
        reset_button = self.browser.find_element(*self.resetFiltersButton)
        self.browser.execute_script("arguments[0].click();", reset_button)
        time.sleep(7)
        try:
            filter_text = self.browser.find_element(*self.itemSelectedText).is_displayed()
            if filter_text:
                return True
        except:
            return False

    #@allure.step('Verify on click reset filter button is resetting all filter')
    def click_reset_filter_button_documents(self):
        time.sleep(1)
        reset_button = self.browser.find_element(*self.resetFiltersButton)
        self.browser.execute_script("arguments[0].click();", reset_button)
        time.sleep(7)
        try:
            filter_text = self.browser.find_element(*self.threeItemsSelectedText).is_displayed()
            if filter_text:
                return True
        except:
            return False

    #@allure.step('Verify on double click user is able to deselect  all Items')
    def click_again_all_assets_select_all_button(self):
        self.browser.find_element(*self.selectAll).click()
        time.sleep(2)
        try:
            filter_text = self.browser.find_element(*self.itemsSelectedText).is_displayed()
            if filter_text:
                return True
        except:
            return False

    #@allure.step('Verify on double click user is able to deselect  all Items')
    def click_again_video_select_all_button(self):
        self.browser.find_element(*self.selectAll).click()
        time.sleep(2)
        try:
            filter_text = self.browser.find_element(*self.itemSelectedText).is_displayed()
            if filter_text:
                return True
        except:
            return False

    #@allure.step('Verify on double click user is able to deselect  all Items')
    def click_again_documents_select_all_button(self):
        self.browser.find_element(*self.selectAll).click()
        time.sleep(2)
        try:
            filter_text = self.browser.find_element(*self.twoItemsSelectedText).is_displayed()
            if filter_text:
                return True
        except:
            return False

    #@allure.step('Verify collapse all button is collapsing all filter dropdown in Assets All page')
    def click_all_assets_collapse_all_button(self):
        WebDriverWait(self.browser, 20).until(EC.presence_of_element_located(self.collapseAll))
        time.sleep(1)
        self.browser.find_element(*self.collapseAll).click()
        time.sleep(2)
        try:
            filter_text = self.browser.find_element(*self.fileTypePdfText).is_displayed()
            if filter_text:
                return True
        except:
            return False

    #@allure.step('Verify collapse all button is collapsing all filter dropdown in Assets All page')
    def click_all_images_collapse_all_button(self):
        WebDriverWait(self.browser, 20).until(EC.presence_of_element_located(self.collapseAll))
        time.sleep(1)
        self.browser.find_element(*self.collapseAll).click()
        time.sleep(2)
        try:
            filter_text = self.browser.find_element(*self.fileTypeJpegPhoto).is_displayed()
            if filter_text:
                return True
        except:
            return False

    #@allure.step('Verify collapse all button is collapsing all filter dropdown in Assets videos page')
    def click_videos_collapse_all_button(self):
        WebDriverWait(self.browser, 20).until(EC.presence_of_element_located(self.collapseAll))
        time.sleep(1)
        self.browser.find_element(*self.collapseAll).click()
        time.sleep(2)
        try:
            filter_text = self.browser.find_element(*self.fileTypeVideo).is_displayed()
            if filter_text:
                return True
        except:
            return False

    #@allure.step('Verify Tab Title-Overview button is present in banner section')
    def verify_tab_title_overview(self):
        time.sleep(2)
        return self.browser.find_element(*self.tabTitleOverview).is_displayed()

    #@allure.step('Verify Result count is present in All-Assets Section')
    def verify_all_assets_result(self):
        time.sleep(2)
        return self.browser.find_element(*self.allAssetsResult).is_displayed()

    #@allure.step('Verify Pagination is present in All-Assets Section')
    def verify_pagination_next_button(self):
        time.sleep(2)
        return self.browser.find_element(*self.paginationVerify).is_displayed()

    #@allure.step('Verify movie cards are  present in all assets page')
    def verify_all_assets_first_card(self):
        time.sleep(2)
        return self.browser.find_element(*self.allAssetsFirstCard).is_displayed()

    #@allure.step('Verify Sorting Filter button is present in Header Section')
    def verify_sorting_filter(self):
        time.sleep(2)
        return self.browser.find_element(*self.sortingFilterButton).is_displayed()

    #@allure.step('Verify File Type filter is present in Header Section')
    def verify_file_type_text(self):
        time.sleep(2)
        return self.browser.find_element(*self.fileTypeFilterText).is_displayed()

    #@allure.step('Verify Video Properties text is present assets Section')
    def verify_video_properties_text(self):
        time.sleep(2)
        video_property = self.browser.find_element(*self.videoPropertiesText)
        self.browser.execute_script("arguments[0].scrollIntoView();", video_property)
        time.sleep(2)
        return self.browser.find_element(*self.videoPropertiesText).is_displayed()

    #@allure.step('Verify asset type text is present assets Section')
    def verify_asset_type_heading_text(self):
        time.sleep(2)
        asset_type = self.browser.find_element(*self.assetTypeText)
        self.browser.execute_script("arguments[0].scrollIntoView();", asset_type)
        time.sleep(2)
        return self.browser.find_element(*self.assetTypeText).is_displayed()

    #@allure.step('Verify Document text is present in asset type Page')
    def verify_asset_type_documents(self):
        time.sleep(2)
        return self.browser.find_element(*self.assetTypeDocuments).is_displayed()

    #@allure.step('Verify Photo-Image text is present in asset type Page')
    def verify_asset_type_photo_image(self):
        time.sleep(2)
        return self.browser.find_element(*self.assetTypePhotoImages).is_displayed()

    #@allure.step('Verify Ads filter is present in asset type Page')
    def verify_asset_type_ads(self):
        time.sleep(2)
        return self.browser.find_element(*self.assetTypeAds).is_displayed()

    #@allure.step('Verify Video filter is present in asset type Page')
    def verify_asset_type_video(self):
        time.sleep(2)
        return self.browser.find_element(*self.assetTypeVideos).is_displayed()

    #@allure.step('Verify File_Size text is present assets Section')
    def verify_file_size_heading_text(self):
        time.sleep(2)
        video_property = self.browser.find_element(*self.fileSizeHeadingText)
        self.browser.execute_script("arguments[0].scrollIntoView();", video_property)
        time.sleep(2)
        return self.browser.find_element(*self.fileSizeHeadingText).is_displayed()

    #@allure.step('Verify user can apply file-size filter')
    def verify_size_filter(self):
        move = ActionChains(self.browser)
        move_element = self.browser.find_element(*self.fileSizeLeftPoint)
        move.click_and_hold(move_element).move_by_offset(240, 0).release().perform()
        time.sleep(8)

    #@allure.step('Verify Range filter Text present in Video Tab')
    def verify_range_filter(self):
        move_element = self.browser.find_element(*self.fileSizeRangeText)
        return move_element.is_displayed()

    #@allure.step('Verify Range filter Text present in Video Tab')
    def verify_range_mb_filter(self):
        move_element = self.browser.find_element(*self.fileSizeRangeMb)
        return move_element.is_displayed()

    #@allure.step('Verify Reset-Filter Button is present in All Assets Page')
    def verify_reset_filter_button(self):
        time.sleep(1)
        return self.browser.find_element(*self.resetFiltersButton).is_displayed()

    #@allure.step('Verify grid view Button is present in All Assets Page')
    def verify_grid_view_button(self):
        time.sleep(1)
        return self.browser.find_element(*self.gridViewButton).is_displayed()

    #@allure.step('Verify list view Button is present in All Assets Page')
    def verify_list_view_button(self):
        time.sleep(1)
        return self.browser.find_element(*self.listViewButton).is_displayed()

    #@allure.step('Verify Select All Button is present in All Assets Page')
    def verify_select_all_button(self):
        time.sleep(1)
        return self.browser.find_element(*self.selectAll).is_displayed()

    #@allure.step('Verify collapse all Button is present in All Assets Page')
    def verify_collapse_all_button(self):
        time.sleep(1)
        return self.browser.find_element(*self.collapseAll).is_displayed()

    #@allure.step('Verify Tab all Assets button is present in banner section')
    def verify_tab_all_assets(self):
        time.sleep(1.5)
        return self.browser.find_element(*self.tabAllAssets).is_displayed()

    #@allure.step('Verify Tab all Assets button is present in banner section')
    def click_all_assets_button(self):
        WebDriverWait(self.browser, 40).until(EC.element_to_be_clickable(self.tabAllAssets))
        # time.sleep(1)
        all_assets = self.browser.find_element(*self.tabAllAssets)
        self.browser.execute_script("arguments[0].click();", all_assets)

        WebDriverWait(self.browser, 20).until(EC.presence_of_element_located(self.resetFiltersButton))
        reset_button = self.browser.find_element(*self.resetFiltersButton)
        self.browser.execute_script("arguments[0].scrollIntoView();", reset_button)

    # @allure.step('Verify Tab all Assets button is present in banner section')
    def click_reset_text(self):
        # WebDriverWait(self.browser, 40).until(EC.element_to_be_clickable(self.tabAllAssets))
        time.sleep(5)
        reset_filter_button = self.browser.find_element(*self.resetFiltersButton)
        self.browser.execute_script("arguments[0].click();", reset_filter_button)
        time.sleep(7.5)
        WebDriverWait(self.browser, 20).until(EC.presence_of_element_located(self.resetFiltersButton))
        reset_button = self.browser.find_element(*self.resetFiltersButton)
        self.browser.execute_script("arguments[0].scrollIntoView();", reset_button)

    #@allure.step('Verify Tab all Assets button is present in banner section')
    def click_all_images_photo_button(self):
        WebDriverWait(self.browser, 20).until(EC.presence_of_element_located(self.tabImagesPhotos))
        time.sleep(1)
        image_photo = self.browser.find_element(*self.tabImagesPhotos)
        self.browser.execute_script("arguments[0].scrollIntoView();", image_photo)
        time.sleep(1.5)
        self.browser.find_element(*self.tabImagesPhotos).click()
        WebDriverWait(self.browser, 20).until(EC.presence_of_element_located(self.resetFiltersButton))
        reset_button = self.browser.find_element(*self.resetFiltersButton)
        self.browser.execute_script("arguments[0].scrollIntoView();", reset_button)

    #@allure.step('Verify Tab video button is clickable in banner section')
    def click_video_tab_button(self):
        WebDriverWait(self.browser, 20).until(EC.presence_of_element_located(self.tabVideo))
        time.sleep(1)
        image_photo = self.browser.find_element(*self.tabVideo)
        self.browser.execute_script("arguments[0].scrollIntoView();", image_photo)
        time.sleep(1.5)
        self.browser.find_element(*self.tabVideo).click()
        WebDriverWait(self.browser, 20).until(EC.presence_of_element_located(self.resetFiltersButton))
        reset_button = self.browser.find_element(*self.resetFiltersButton)
        self.browser.execute_script("arguments[0].scrollIntoView();", reset_button)

    #@allure.step('Verify Tab Document button is clickable in banner section')
    def click_document_tab_button(self):
        WebDriverWait(self.browser, 20).until(EC.presence_of_element_located(self.tabDocuments))
        time.sleep(1)
        document_tab = self.browser.find_element(*self.tabDocuments)
        self.browser.execute_script("arguments[0].scrollIntoView();", document_tab)
        time.sleep(1.5)
        self.browser.find_element(*self.tabDocuments).click()
        WebDriverWait(self.browser, 20).until(EC.presence_of_element_located(self.resetFiltersButton))
        reset_button = self.browser.find_element(*self.resetFiltersButton)
        self.browser.execute_script("arguments[0].scrollIntoView();", reset_button)

    #@allure.step('Verify Tab Paid ad Memo button is clickable in banner section')
    def click_paid_ad_memo_tab_button(self):
        WebDriverWait(self.browser, 20).until(EC.presence_of_element_located(self.tabPaidAdMemo))
        time.sleep(1)
        document_tab = self.browser.find_element(*self.tabPaidAdMemo)
        self.browser.execute_script("arguments[0].scrollIntoView();", document_tab)
        time.sleep(1.5)
        self.browser.find_element(*self.tabPaidAdMemo).click()
        WebDriverWait(self.browser, 20).until(EC.presence_of_element_located(self.resetFiltersButton))
        reset_button = self.browser.find_element(*self.resetFiltersButton)
        self.browser.execute_script("arguments[0].scrollIntoView();", reset_button)

    #@allure.step('Verify Tab images and photos button is present in banner section')
    def verify_tab_images_photo(self):
        time.sleep(1.5)
        return self.browser.find_element(*self.tabImagesPhotos).is_displayed()

    #@allure.step('Verify Tab Documents button is present in banner section')
    def verify_tab_documents(self):
        time.sleep(1.5)
        return self.browser.find_element(*self.tabDocuments).is_displayed()

    #@allure.step('Verify Paid Ad Memo button is present in banner section')
    def verify_tab_paid_ad_memo(self):
        time.sleep(1.5)
        return self.browser.find_element(*self.tabPaidAdMemo).is_displayed()

    #@allure.step('Verify Add to List tab in footer popup')
    def verify_assets_active(self):
        time.sleep(1.5)
        class_text = self.browser.find_element(*self.assetsActive).get_attribute('class')
        return class_text

    #@allure.step('Verify movies page have Banner-Image')
    def verify_first_title_card(self):
        WebDriverWait(self.browser, 90).until(EC.presence_of_element_located(self.firstTitleCard))
        return self.browser.find_element(*self.firstTitleCard).is_displayed()

    #@allure.step('Verify banner-image is displayed in Assets page')
    def verify_banner_image(self):
        banner = self.browser.find_element(*self.bannerText)
        self.browser.execute_script("arguments[0].scrollIntoView();", banner)
        time.sleep(1.5)
        banner_image = self.browser.find_element(*self.bannerImage).is_displayed()
        return banner_image

    #@allure.step('Verify banner-text is displayed in Assets page')
    def verify_banner_text(self):
        banner_text = self.browser.find_element(*self.bannerText).is_displayed()
        return banner_text

    #@allure.step('Verify banner-Image is displayed in card detail page')
    def verify_card_banner_image(self):
        banner_image = self.browser.find_element(*self.cardBannerImage).is_displayed()
        return banner_image

    #@allure.step('Verify banner-Image is displayed in card detail page')
    def verify_card_tabs(self):
        banner_tabs = self.browser.find_element(*self.cardTabs).is_displayed()
        return banner_tabs

    #@allure.step('Verify User can click on card details back Button')
    def click_card_back_button(self):
        banner = self.browser.find_element(*self.cardBackButton)
        self.browser.execute_script("arguments[0].click();", banner)
        WebDriverWait(self.browser, 30).until(EC.presence_of_element_located(self.searchInputField))
        return self.browser.find_element(*self.searchInputField).is_displayed()

    #@allure.step('Click on How It Ends movie card')
    def click_how_it_ends_movie_card(self):
        WebDriverWait(self.browser, 30).until(EC.presence_of_element_located(self.howItEndsMovieCard))
        self.browser.find_element(*self.howItEndsMovieCard).click()
        WebDriverWait(self.browser, 30).until(EC.presence_of_element_located(self.synopsisTitle))

    #@allure.step('Click on Respect movie card')
    def click_respect_movie(self):
        WebDriverWait(self.browser, 30).until(EC.presence_of_element_located(self.respectMovie))
        self.browser.find_element(*self.respectMovie).click()
        WebDriverWait(self.browser, 30).until(EC.presence_of_element_located(self.synopsisTitle))

    #@allure.step('Verify the search result')
    def verify_assets_search_result(self):
        WebDriverWait(self.browser, 25).until(EC.presence_of_element_located(self.searchResultCount))
        total_count = self.browser.find_element(*self.searchResultCount)
        self.browser.execute_script("arguments[0].scrollIntoView();", total_count)
        time.sleep(2.5)
        return self.browser.find_element(*self.respectMovie).is_displayed()

    #@allure.step('Verify Search-input-field is displayed in film and series page')
    def verify_banner_search_field(self):
        search_input_field = self.browser.find_element(*self.searchInputField).is_displayed()
        return search_input_field

    #@allure.step('verify User can Click on Filter chips button')
    def click_filter_chips_action(self):
        WebDriverWait(self.browser, 30).until(EC.presence_of_element_located(self.actionCrossButton))
        clear_button = self.browser.find_element(*self.actionCrossButton)
        filter_chips_before_click = self.browser.find_element(*self.actionCrossButton).is_displayed()
        time.sleep(1.5)
        self.browser.execute_script("arguments[0].click();", clear_button)
        time.sleep(10)
        return filter_chips_before_click

    #@allure.step('verify User can Click on clear button in Video Properties')
    def click_clear_button_video_property(self):
        clear_button = self.browser.find_element(*self.videoPropertiesClearButton)
        time.sleep(1)
        self.browser.execute_script("arguments[0].click();", clear_button)
        time.sleep(8)

    #@allure.step('verify User can Click on clear button in asset type section')
    def click_clear_button_asset_type_property(self):
        clear_button = self.browser.find_element(*self.assetTypeClearButton)
        time.sleep(1)
        self.browser.execute_script("arguments[0].click();", clear_button)
        time.sleep(8)

    #@allure.step('verify Reset button present in File type section')
    def verify_reset_button_files_size_property(self):
        return self.browser.find_element(*self.fileSizeResetButton).is_displayed()

    #@allure.step('verify User can Click on Reset button in File type section')
    def click_reset_button_files_size_property(self):
        clear_button = self.browser.find_element(*self.fileSizeResetButton)
        time.sleep(1)
        self.browser.execute_script("arguments[0].click();", clear_button)
        time.sleep(8)

    #@allure.step('verify Filter chips should not present after click')
    def verify_filter_chips_clickable_assets(self):
        try:

            filter_chips_after_click = self.browser.find_element(*self.actionCrossButton)
            if filter_chips_after_click.is_displayed():
                return True
        except:
            return False

    #@allure.step('click on last page')
    def click_last_page_button(self):
        WebDriverWait(self.browser, 40).until(EC.presence_of_element_located(self.paginationLastPageNumber))
        last_page = self.browser.find_element(*self.paginationLastPageNumber)
        self.browser.execute_script("arguments[0].scrollIntoView();", last_page)
        time.sleep(1.5)
        self.browser.execute_script("arguments[0].click();", last_page)


