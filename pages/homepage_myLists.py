import allure, time
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from resources.variables import *


class homePagemylistsObj:
    total_lists = (By.XPATH, "//h2[contains(text(),'My Lists')]/ancestor::div[3]/following-sibling::div[1]//ul[1]//li")
    # auto_list = (By.XPATH, "//p[contains(text(),'" + automation_listt + "')]")
    delete_direct_mylist = (By.XPATH, '//div/button[contains(text()," Delete List ")]')
    delete_direct_cart = (By.XPATH, '//div/button[contains(text()," Delete Cart ")]')
    auto_list = (By.XPATH, "//div[p[contains(text(),'" + automation_listt + "')]]")
    # lists_cards = (By.XPATH, "//div[p[contains(text(),'" + automation_listt + "')]]")
    lists_cards = (By.XPATH, '//div[@class="description"]/p[contains(text(),"Action")]')
    card_titles = (By.XPATH, "//p[contains(text(),'" + automation_listt + "')]/parent::div[1]/p[2]/span[1]")
    # user_created = (By.XPATH, "//a[contains(text(),'" + automation_listt + "')]")
    user_created = (By.XPATH, "//a[contains(text(),'Demo')]")
    header_mylist = (By.XPATH, "//li[contains(@class,'menu menu-label')]//a[@id='My Lists']")
    lists = (By.XPATH, "//p[contains(text(),'Your Lists')]")
    testCuratedList = (By.XPATH, '//div/span[contains(text(),"Shared by Automation Account")]'
                                 '/ancestor::div[3]//div/a[contains(text(),"test")]')
    list_heading = (By.XPATH, '//div[@id="top-title"]')
    first_card_movie_name = (By.XPATH, '(//div[@class="desk-on"]//div[@class="movie-detail"]/p)[1]')
    recentlyList = (By.XPATH, "//a[text()='recentlyList']")
    tvShowList = (By.XPATH, '//a[contains(text(),"TvShow")]')
    fiascoSeries = (By.XPATH, '//div[@class = "desk-on"]//p[contains(text(),"(series)")]')
    series_name = (By.XPATH, '//div[@class = "desk-on"]//p[contains(text(),"(series)")]')
    fiascoSeriesListPage = (By.XPATH, '//div[@class = "desk-on"]//p[contains(text(),"(series)")]'
                                      '/ancestor::div[2]//ul/li/button[contains(text(),"Watch now")]')
    single_list = (By.XPATH, "//div/a[contains(text(),'" + automation_listt + "')]/parent::div/parent::div//div/input[@type='checkbox']")
    share_button = (By.XPATH, "//a[contains(text(),'Demo')]/ancestor::div[4]//button//span[contains(text(),'Email Spreadsheet')]")
    title_count = (By.XPATH, "//a[contains(text(),'Demo')]/ancestor::div[1]//span")
    delete_button = (By.XPATH, "//a[contains(text(),'Demo')]/ancestor::div[4]//button//span[contains(text(),'Delete')]")
    delete_button_test2 = (By.XPATH, "//a[contains(text(),'test2')]/ancestor::div[4]//button//span[contains(text(),'Delete')]")
    raw_demo = (By.XPATH, "//a[contains(text(),'Demo')]/ancestor::div[4]//button//span[contains(text(),'Delete')]")
    your_list_first_delete_button = (By.XPATH,"(//span[text()='Delete'])[1]")
    first_carousel_title = (By.XPATH, '//ul[contains(@class,"carousel-menu-list")]/li[1]/a')
    delete_list_confirmation_text = (By.XPATH, '//div/h3[contains(text(),"Delete List")]')
    delete_cart_confirmation_text = (By.XPATH, '//div/h3[contains(text(),"Delete Cart")]')
    raw_test2 = (By.XPATH, "//a[contains(text(),'test2')]/ancestor::div[4]//button//span[contains(text(),'Delete')]")
    raw_test1 = (By.XPATH, "//a[contains(text(),'test1')]/ancestor::div[4]//button//span[contains(text(),'Delete')]")
    raw_test = (By.XPATH, "//a[contains(text(),'test')]/ancestor::div[4]//button//span[contains(text(),'Delete')]")
    testingCart2 = (By.XPATH, '//a[contains(text(),"testingCart2")]/ancestor::div[2]//button//span[contains(text(),"Delete")]')
    testingCart = (
    By.XPATH, '//a[contains(text(),"testingCart")]/ancestor::div[2]//button//span[contains(text(),"Delete")]')
    raw_recentlyList2 = (By.XPATH, "//a[contains(text(),'recentlyList2')]/ancestor::div[4]//button//span[contains(text(),'Delete')]")
    raw_recentlyList = (By.XPATH, "//a[contains(text(),'recentlyList')]/ancestor::div[4]//button//span[contains(text(),'Delete')]")
    raw_filmSeriesList = (By.XPATH, "//a[contains(text(),'filmSeriesList')]/ancestor::div[4]//button//span[contains(text(),'Delete')]")
    raw_moviesList = (
    By.XPATH, "//a[contains(text(),'MoviesList')]/ancestor::div[4]//button//span[contains(text(),'Delete')]")
    raw_tvSowList = (
    By.XPATH, "//a[contains(text(),'TvShow')]/ancestor::div[4]//button//span[contains(text(),'Delete')]")
    raw_listDataList = (By.XPATH, "//a[contains(text(),'listData')]/ancestor::div[4]//button"
                                  "//span[contains(text(),'Delete')]")
    raw_filmSeriesSecondList = (
    By.XPATH, "//a[contains(text(),'filmSeriesSecondList')]/ancestor::div[4]//button//span[contains(text(),'Delete')]")


    # share_button = (By.XPATH,   "//div[div[a[contains(text(),'Automation List5983')]]]/following-sibling::div[2]//span["
    #                             "@class='share']")
    # delete_button = (By.XPATH, "//div[div[a[contains(text(),'" + automation_listt + "')]]]/following-sibling::div[2]//span["
    #                                                                "@class='delete-txt']")

    first_movie_card = (By.XPATH, '//ul[contains(@class,"movie-card")]/li[1]')
    view_details_movie_card = (By.XPATH, '//ul[contains(@class,"movie-card")]/li[1]//ul/li/button[contains(text(),"View details")]')
    watch_trailer_movie_card = (
    By.XPATH, '//ul[contains(@class,"movie-card")]/li[1]//ul/li/button[contains(text(),"Watch trailer")]')
    watch_now_movie_card = (
        By.XPATH, '//ul[contains(@class,"movie-card")]/li[1]//ul/li/button[contains(text(),"Watch now")]')
    add_to_list_movie_card = (
        By.XPATH, '//ul[contains(@class,"movie-card")]/li[1]//ul/li/button[contains(text(),"ADD TO LIST")]')
    myList = (By.XPATH, "//div[h2[contains(text(),'My Lists')]]")
    myListSlider = (By.XPATH, '//h2[text()="My Lists"]/ancestor::div[4]//div[@class="card-section"]//scrollbar-x/div/div')
    all_test_list = (By.XPATH, "//div/a[contains(text(),'test')]/parent::div/parent::div//div/input[@type='checkbox']")
    # myList = (By.XPATH, "//div[h2[contains(text(),'Your Lists')]]")
    # myList_rightNav = (By.XPATH, "(//div//a[@role='button']/i[@class='next-icon icon'])[1]")
    myList_rightNav = (By.XPATH, "//h2[text()='My Lists']/ancestor::div[3]/following-sibling::div//a[@role='button']")
    click_mylist_rightNav = (By.XPATH, "//h2[text()='My Lists']/ancestor::div[3]/following-sibling::div//a[@role='button']/i")
    # myList_rightNav = (By.XPATH, "//h2[text()='My Lists']/ancestor::div[3]/following-sibling::div//i["
    #                              "@class='next-icon icon']")
    myList_prevNav = (By.XPATH, "//h2[text()='My Lists']/ancestor::div[3]/following-sibling::div//a[@role='button'][1]")
    myList_second_navigation_view = (By.XPATH, "//h2[text()='My Lists']/ancestor::div[3]/following-sibling::div//a[@role='button'][2]")
    myList_second_navigation = (By.XPATH, "//h2[text()='My Lists']/ancestor::div[3]/following-sibling::div//a[@role='button'][2]/i")
    click_myList_prevNav = (By.XPATH, "//h2[text()='My Lists']/ancestor::div[3]/following-sibling::div//a[@role='button'][1]/i")
    mylist_previous_arrow = (By.XPATH, 'a/i[@class="previous-icon icon"]')
    myList_seeall = (By.XPATH, "//a[contains(text(),'SEE LISTS')]")
    your_list_title = (By.XPATH, "//div/p[contains(text(),'Your Lists')]")
    mylist_cards = (By.XPATH, "//h2[text()='My Lists']/ancestor::div[3]/following-sibling::div//div[@class='description']/p[1]")
    list_title_heading = (By.XPATH, "//div[@id='top-title']")
    mylistDemo = (By.XPATH, '//div[@class="description"]/p[contains(text(), "Demo")]')
    mylistRecentlyList = (By.XPATH, '//div[@class="description"]/p[contains(text(), "recentlyList")]')
    title_text = (By.XPATH, "//h2[contains(text(),'My Lists')]")
    recently_list = (By.XPATH, "//p[contains(text(),'recentlyList')]")
    recentlyListTitleCount = (By.XPATH, '//p[contains(text(),"recentlyList")]/parent::div/p[@class="count"]')
    myListCards = (By.XPATH, '//h2[contains(text(),"My Lists")]/parent::div/parent::'
                             'div/parent::div/parent::div//div[@class="description"]')
    myListName = (By.XPATH, '//h2[contains(text(),"My Lists")]/parent::div/parent::div/parent::'
                            'div/parent::div//ul/li[1]//div[@class="description"]/p[1]')
    myListTitle = (By.XPATH, '//h2[contains(text(),"My Lists")]/parent::div/parent::div/parent::'
                             'div/parent::div//ul/li[1]//div[@class="description"]/p[2]')
    # lists_cards = (By.XPATH, "//div[p[contains(text(),'" + automation_listt + "')]]")
    list_page_tile = (By.XPATH, "//p[@class='yourList ng-tns-c168-0']")
    # detail_title = (By.XPATH, "//span[@class='view-title']")
    detail_title = (By.XPATH, "//div[@id='top-title']")
    select_all_list_page = (By.XPATH, '//div/input[@id="select-all"]')
    grid_view = (By.XPATH, '(//div[contains(@class,"container")]//div[contains(@class,"row")]//div[contains(@class,"row")]/div[contains(@class,"grid-icon")]/div)[2]')
    list_director = (By.XPATH, '//div[contains(text(),"Directed By")]')
    list_main_cast = (By.XPATH, '//div[contains(text(),"Main Cast")]')
    list_synopsis = (By.XPATH, '//div[contains(text(),"Synopsis")]')
    list_card_checkbox = (By.XPATH, '//ul[contains(@class,"movie-card")]//div[@class="checkbox-shell-dark"]/span')
    list_first_checkbox = (By.XPATH, '//ul[contains(@class,"movie-card")]'
                                     '/li[1]//div[@class="checkbox-shell-dark"]/input[@type="checkbox"]')
    list_view = (By.XPATH, '//div[contains(@class,"list-icon")]')
    email_spreadsheet = (By.XPATH, '//span[contains(text(),"Email Spreadsheet")]')
    email_spreadsheet_text = (By.XPATH, '//div/button/span[contains(text(),"Email Spreadsheet")]')
    delete_list_page_header = (By.XPATH, '//span[contains(text(),"Delete")]')
    sortFilter = (By.XPATH, '//div[contains(@class,"sort-filter")]/div')
    sorting_filter = (By.XPATH, '//div[contains(@class,"dropdown-filter")]')
    release_date_filter_new = (By.XPATH, '//div[contains(@class,"dropdown-default")]/span[contains(text(),"RELEASE DATE")][1]')
    release_date_filter_old = (
    By.XPATH, '//div[contains(@class,"dropdown-default")]/span[contains(text(),"RELEASE DATE")][1]')
    sort_az = (By.XPATH, '//div[contains(@class,"dropdown-default")]/span[contains(text(),"SORT A-Z ")]')
    sort_za = (By.XPATH, '//div[contains(@class,"dropdown-default")]/span[contains(text(),"SORT Z-A ")]')
    first_card_checkbox = (By.XPATH, '//ul[contains(@class,"movie-card")]/li[1]//div[contains(@class,"checkbox-shell-dark")]')
    # card_titles = (By.XPATH, "//p[contains(text(),'" + automation_listt + "')]/parent::div[1]/p[2]/span[1]")
    # curated_title = (By.XPATH, "//p[@class='title'][contains(text(),'Blockbusters')]")
    curated_title = (By.XPATH, "//ul[@class='movies-list d-flex active']/li[1]//div[@class='description']/p[1]")
    # curated_made = (By.XPATH, "//p[@class='title'][contains(text(),'Blockbusters')]/ancestor::a[1]/p[1]")
    curated_made = (By.XPATH, "//ul[@class='movies-list d-flex active']/li[1]//p[contains(text(),'LIST MADE FOR YOU')]")
    # curated_numTitle = (By.XPATH, "//p[@class='title'][contains(text(),'Blockbusters')]/parent::div[1]/p[2]/span[1]")
    curated_numTitle = (By.XPATH, "//ul[@class='movies-list d-flex active']/li[1]//div[@class='description']/p["
                                  "2]/span[1]")
    title = (By.XPATH, "//div/p[contains(text(),'Your Lists')]")
    # user_created = (By.XPATH, "//a[contains(text(),'" + automation_listt + "')]")
    heading_detailed = (By.XPATH, "//input[@id='top-title']")
    # share_button = (By.XPATH, "//div[div[a[contains(text(),'" + automation_listt + "')]]]/following-sibling::div[2]//span["
    #                           "@class='share']")
    # delete_button = (By.XPATH, "//div[div[a[contains(text(),'" + automation_listt + "')]]]/following-sibling::div[2]//span["
    #                            "@class='delete-txt']")
    list_check = (By.XPATH, "//div[p[text()='Your Lists']]/following-sibling::div[1]/div[2]//mgm-checkbox-single["
                            "1]/div[1]/input[1]")
    verifylist_check = (By.XPATH, "//a[contains(text(),'Demo')]/ancestor::div[3]//div/input")
    second_check_box = (By.XPATH, "//a[contains(text(),'test1')]/ancestor::div[3]//div/input")
    test_checkbox = (By.XPATH, "//a[contains(text(),'test')]/ancestor::div[3]//div/input")
    demo_check = (By.XPATH, "//div[p[text()='Your Lists']]/following-sibling::div[1]/div[3]//mgm-checkbox-single["
                            "1]/div[1]/input[1]")
    list_selected = (By.XPATH, "//div/span[contains(text(), 'Item Selected' )]")
    list_selected_items = (By.XPATH, "//div/span[contains(text(), 'Items Selected' )]")
    spreadsheetDeleteButton = (By.XPATH, '//button/span[contains(text(),"DELETE")]')
    download = (By.XPATH, "//span[contains(text(),'DOWNLOAD.CSV')]")
    download_footer = (By.XPATH, "//button/span[contains(text(),'DOWNLOAD .XLSX')]")
    add_to_list_footer = (By.XPATH, "//button/span[contains(text(),'DOWNLOAD .XLSX')]")
    share_popup_footer = (By.XPATH, "//button/span[contains(text(),'EMAIL SPREADSHEET')]")
    share_popup = (By.XPATH, "//span[contains(text(),'SHARE LIST')]")
    share_title = (By.XPATH, "//span[contains(text(),'SHARE TITLE')]")
    delete_popup_footer = (By.XPATH, "//button/span[contains(text(),'DELETE')]")
    add_to_list_popup_footer = (By.XPATH, "//button/span[contains(text(),'ADD TO LIST')]")
    delete_popup = (By.XPATH, "//span[contains(text(),'DELETE')]")
    auto_delete_btn = (By.XPATH, "//a[contains(text(),'" + automation_listt + "')]/ancestor::div[3]//following-sibling::button[1]")
    delete_success = (By.XPATH, "//h3[contains(text(),'Delete List ')]")

    def __init__(self, browser):
        self.browser = browser

    #@allure.step('Verify number of lists in My Lists section')
    def verify_Mylists(self):
        count = self.browser.find_elements(*self.total_lists)
        ##print(len(count))
        return len(count)

    #@allure.step('Verify in My list Automation List is displayed')
    def verify_autoList(self):
        WebDriverWait(self.browser, 38).until(EC.presence_of_element_located(self.myList))
        lst = self.browser.find_element(*self.myList)
        self.browser.execute_script("arguments[0].scrollIntoView();", lst)
        time.sleep(30)
        print('autolisllllt-------->>>>>>>', self.browser.find_element(*self.auto_list).text)
        return self.browser.find_element(*self.auto_list).is_displayed()

    #@allure.step('Verify user can select multiple checkbox')
    def click_multiple_checkbox(self):
        all_created_list =[]
        all_created_list = self.browser.find_elements(*self.all_test_list)
        for list_data in all_created_list:
            time.sleep(2)
            self.browser.execute_script("arguments[0].scrollIntoView();", list_data)
            time.sleep(2)
            list_data.click()
            time.sleep(2)

    #@allure.step('Verify user can select multiple checkbox')
    def click_single_checkbox(self):
        single_checkbox = self.browser.find_element(*self.single_list)
        self.browser.execute_script("arguments[0].scrollIntoView();", single_checkbox)
        single_checkbox.click()
        time.sleep(2)


    #@allure.step('Click on List card ')
    def click_listCard(self):
        time.sleep(3)
        self.browser.find_element(*self.auto_list)
        time.sleep(4)
        self.browser.find_element(*self.auto_list).click()

    #@allure.step('Verify Detail Page for list is opened ')
    def verify_detailedPage(self):
        WebDriverWait(self.browser, 40).until(EC.presence_of_element_located(self.detail_title))
        return self.browser.find_element(*self.detail_title).is_displayed()

    #@allure.step('Verify select all present in list page')
    def verify_select_all_checkbox(self):
        WebDriverWait(self.browser, 48).until(EC.presence_of_element_located(self.select_all_list_page))
        return self.browser.find_element(*self.select_all_list_page).is_displayed()

    #@allure.step('Click select all present in list page')
    def click_select_all_checkbox(self):
        WebDriverWait(self.browser, 58).until(EC.presence_of_element_located(self.select_all_list_page))
        list = self.browser.find_element(*self.select_all_list_page)
        self.browser.execute_script("arguments[0].click();", list)


    #@allure.step('Verify grid button present in list page')
    def verify_grid_view_button(self):
        WebDriverWait(self.browser, 50).until(EC.presence_of_element_located(self.grid_view))
        return self.browser.find_element(*self.grid_view).is_displayed()

    # @allure.step('Verify grid button present in list page')
    def click_grid_view_button(self):
        WebDriverWait(self.browser, 130).until(EC.presence_of_element_located(self.list_heading))
        time.sleep(25)  # it taking too much time
        WebDriverWait(self.browser, 130).until(EC.element_to_be_clickable(self.grid_view))
        grid_view_button = self.browser.find_element(*self.grid_view)
        self.browser.execute_script("arguments[0].click();", grid_view_button)

    # @allure.step('Verify grid button present in list page')
    def click_list_grid_view_button(self):
        print("start")
        WebDriverWait(self.browser, 130).until(EC.presence_of_element_located(self.list_heading))
        print("head")
        time.sleep(5)  # it taking too much time
        WebDriverWait(self.browser, 130).until(EC.element_to_be_clickable(self.grid_view))
        print("grid element")
        grid_view_button = self.browser.find_element(*self.grid_view)
        print("after click")
        self.browser.execute_script("arguments[0].click();", grid_view_button)

    #@allure.step('Verify list button clickable')
    def click_list_view_button(self):
        WebDriverWait(self.browser, 30).until(EC.presence_of_element_located(self.list_view))
        list = self.browser.find_element(*self.list_view)
        self.browser.execute_script("arguments[0].scrollIntoView();", list)
        time.sleep(2)
        self.browser.find_element(*self.list_view).click()
        WebDriverWait(self.browser, 40).until(EC.presence_of_element_located(self.list_director))
        return self.browser.find_element(*self.list_director).is_displayed()

    #@allure.step('Verify list card checkbox')
    def verify_list_checkbox_button(self):
        WebDriverWait(self.browser, 40).until(EC.presence_of_element_located(self.list_card_checkbox))
        return self.browser.find_element(*self.list_card_checkbox).is_displayed()

    #@allure.step('click on list card checkbox')
    def click_list_checkbox_button(self):
        WebDriverWait(self.browser, 60).until(EC.presence_of_element_located(self.list_first_checkbox))
        time.sleep(2.5) #due to checkbox not visible
        list_checkbox = self.browser.find_element(*self.list_first_checkbox)
        self.browser.execute_script("arguments[0].click();", list_checkbox)

    # @allure.step('click on list card checkbox')
    def list_first_card_movie_name(self):
        WebDriverWait(self.browser, 60).until(EC.presence_of_element_located(self.first_card_movie_name))
        time.sleep(2.5)  # due to checkbox not visible
        return self.browser.find_element(*self.first_card_movie_name).text

    #@allure.step('Verify list main cast text')
    def verify_list_main_cast(self):
        return self.browser.find_element(*self.list_main_cast).is_displayed()

    #@allure.step('Verify list synopsis text')
    def verify_list_synopsis(self):
        return self.browser.find_element(*self.list_synopsis).is_displayed()

    #@allure.step('Verify list button clickable')
    def click_grid_view_button(self):
        WebDriverWait(self.browser, 40).until(EC.presence_of_element_located(self.grid_view))
        self.browser.find_element(*self.grid_view).click()
        try:
            time.sleep(3)
            list_director = self.browser.find_element(*self.list_director).is_displayed()
            if list_director == True:
                return True
        except:
            return False

    #@allure.step('Verify list button present in list page')
    def verify_list_view_button(self):
        WebDriverWait(self.browser, 45).until(EC.presence_of_element_located(self.list_view))
        return self.browser.find_element(*self.list_view).is_displayed()

    #@allure.step('Verify email spreadsheet present in list page')
    def verify_email_spreadsheet(self):
        WebDriverWait(self.browser, 45).until(EC.presence_of_element_located(self.email_spreadsheet))
        return self.browser.find_element(*self.email_spreadsheet).is_displayed()

    #@allure.step('Verify email spreadsheet present in list page')
    def click_list_header_email_spreadsheet(self):
        WebDriverWait(self.browser, 55).until(EC.presence_of_element_located(self.email_spreadsheet))
        time.sleep(5) #45
        list = self.browser.find_element(*self.email_spreadsheet_text)
        time.sleep(1)
        self.browser.execute_script("arguments[0].click();", list)
        time.sleep(1)


    #@allure.step('Verify delete button present in list page')
    def verify_header_delete(self):
        WebDriverWait(self.browser, 55).until(EC.presence_of_element_located(self.delete_list_page_header))
        return self.browser.find_element(*self.delete_list_page_header).is_displayed()

    #@allure.step('click delete button present in list page')
    def click_header_delete_list(self):
        WebDriverWait(self.browser, 95).until(EC.element_to_be_clickable(self.delete_list_page_header))
        time.sleep(10)
        list = self.browser.find_element(*self.delete_list_page_header)
        self.browser.execute_script("arguments[0].click();", list)

    #@allure.step('Verify sorting option present in list page')
    def verify_sorting_filter(self):
        WebDriverWait(self.browser, 45).until(EC.presence_of_element_located(self.sorting_filter))
        return self.browser.find_element(*self.sorting_filter).is_displayed()

    #@allure.step('click on sorting filter button')
    def click_sorting_filter(self):
        WebDriverWait(self.browser, 55).until(EC.presence_of_element_located(self.sortFilter))
        time.sleep(4)
        list = self.browser.find_element(*self.sortFilter)
        self.browser.execute_script("arguments[0].click();", list)


    #@allure.step('Verify release button new to old present in list page')
    def verify_release_date_new_to_old_filter(self):
        WebDriverWait(self.browser, 50).until(EC.presence_of_element_located(self.release_date_filter_new))
        return self.browser.find_element(*self.release_date_filter_new).is_displayed()

    #@allure.step('Verify release button old to new present in list page')
    def verify_release_date_old_to_new_filter(self):
        WebDriverWait(self.browser, 50).until(EC.presence_of_element_located(self.release_date_filter_old))
        return self.browser.find_element(*self.release_date_filter_old).is_displayed()

    #@allure.step('Verify sorting A-Z button present in list page')
    def verify_sorting_az(self):
        WebDriverWait(self.browser, 50).until(EC.presence_of_element_located(self.sort_az))
        return self.browser.find_element(*self.sort_az).is_displayed()

    #@allure.step('Verify sorting Z-A button present in list page')
    def verify_sorting_za(self):
        WebDriverWait(self.browser, 50).until(EC.presence_of_element_located(self.sort_za))
        return self.browser.find_element(*self.sort_za).is_displayed()

    #@allure.step('Verify delete button present in list page')
    def verify_first_card_checkbox(self):
        WebDriverWait(self.browser, 60).until(EC.presence_of_element_located(self.first_card_checkbox))
        return self.browser.find_element(*self.first_card_checkbox).is_displayed()

    #@allure.step('Verify number of titles on list cards ')
    def verify_Numbtitles(self):
        return self.browser.find_element(*self.card_titles).is_displayed()

    #@allure.step('Click on see all Button ')
    def click_seeALL(self):
        time.sleep(2)
        lst = self.browser.find_element(*self.myList)
        self.browser.execute_script("arguments[0].scrollIntoView();", lst)
        time.sleep(2)
        self.browser.find_element(*self.myList_seeall).click()

    #@allure.step('Verify My lists Right navigation arrow')
    def verify_rightNav(self):
        time.sleep(1)
        ryt = self.browser.find_element(*self.myList_rightNav)
        time.sleep(1)
        ActionChains(self.browser).move_to_element(ryt).perform()
        time.sleep(1.5)
        return ryt.is_displayed()

    #@allure.step('Verify My lists Right navigation arrow')
    def verify_second_rightNav(self):
        ryt = self.browser.find_element(*self.myList_second_navigation_view)
        time.sleep(1)
        ActionChains(self.browser).move_to_element(ryt).perform()
        time.sleep(1)
        self.browser.find_element(*self.myList_second_navigation).click()
        time.sleep(1)
        try:
            movie = self.browser.find_element(*self.myList_second_navigation).is_displayed()

            if movie == True:
                return True
        except:
            return False




    #@allure.step('Verify My Lists Left Navigation arrow')
    def verify_LeftNav(self):
        # time.sleep(1)
        ledt_nav = self.browser.find_element(*self.myList_prevNav)
        time.sleep(1)
        ActionChains(self.browser).move_to_element(ledt_nav).perform()
        time.sleep(1.5)
        return ledt_nav.is_displayed()

    #@allure.step('Verify My Lists Left Navigation arrow')
    def verify_left_navigation(self):
        time.sleep(2)
        try:
            ledt_nav = self.browser.find_element(*self.mylist_previous_arrow)

            if ledt_nav.is_displayed():
                return True
        except:
            return False


    #@allure.step('Click on Right navigation arrow in My Lists Section ')
    def click_rightNav(self):
        time.sleep(1)
        self.browser.find_element(*self.click_mylist_rightNav).click()

    #@allure.step('Click on Left Navigation arrow in My lists section ')
    def click_leftNav(self):
        time.sleep(1.5)
        self.browser.find_element(*self.click_myList_prevNav).click()

    #@allure.step('Verify Title text in My lists section ')
    def verify_Mylists_title(self):
        WebDriverWait(self.browser, 30).until(EC.presence_of_element_located(self.title_text))
        my_list = self.browser.find_element(*self.title_text)
        time.sleep(1)
        self.browser.execute_script("arguments[0].scrollIntoView();", my_list)
        time.sleep(1.5)
        return self.browser.find_element(*self.title_text).is_displayed()

    #@allure.step('Verify See all button in my Lists section')
    def verify_seeAll(self):
        time.sleep(1)
        return self.browser.find_element(*self.myList_seeall).is_displayed()

    #@allure.step('Verify Recently list present in my Lists section ')
    def verify_recently_list(self):
        time.sleep(2)
        return self.browser.find_element(*self.recently_list).is_displayed()

    #@allure.step('Verify Recently list present in my Lists section ')
    def verify_recently_list_title_count(self):
        time.sleep(2)
        return self.browser.find_element(*self.recentlyListTitleCount).is_displayed()

    #@allure.step('Verify my list total cards ')
    def verify_my_list_total_cards(self):
        time.sleep(2)
        my_list_card = self.browser.find_elements(*self.myListCards)
        return len(my_list_card)

    #@allure.step('Verify Recently added card is present in My-list section')
    def verify_my_recently_added_card(self):
        try:
            time.sleep(2)
            my_list_demo_card = self.browser.find_element(*self.mylistDemo).is_displayed()
            time.sleep(1)
            if my_list_demo_card:
                return True
        except:
            time.sleep(2)
            return self.browser.find_element(*self.mylistRecentlyList).is_displayed()

    #@allure.step('Verify list name is present in My_list Section')
    def verify_mylist_list_name(self):
        WebDriverWait(self.browser, 38).until(EC.presence_of_element_located(self.myListName))
        time.sleep(0.5)
        my_list_title_name = self.browser.find_element(*self.myListName).is_displayed()
        return my_list_title_name

    #@allure.step('Verify list Title is present in My_list Section')
    def verify_mylist_title(self):
        time.sleep(1)
        my_list_title = self.browser.find_element(*self.myListTitle).is_displayed()
        return my_list_title

    #@allure.step('Verify See all button in my Lists section ')
    def click_myList_see_all(self):
        # time.sleep(2)
        WebDriverWait(self.browser, 4).until(EC.presence_of_element_located(self.myList_seeall))
        self.browser.find_element(*self.myList_seeall).click()
        WebDriverWait(self.browser, 16).until(EC.presence_of_element_located(self.your_list_title))
        return self.browser.find_element(*self.your_list_title).is_displayed()

    #@allure.step('Verify See all button in my Lists section ')
    def click_myList_card(self):
        time.sleep(1)
        cards = self.browser.find_elements(*self.mylist_cards)
        time.sleep(1)
        cards[1].click()
        WebDriverWait(self.browser, 40).until(EC.presence_of_element_located(self.list_title_heading))
        current_url = self.browser.current_url
        time.sleep(1)
        return current_url

    #@allure.step('Verify List cards in myList section ')
    def verify_listCards(self):
        time.sleep(2)
        return self.browser.find_element(*self.lists_cards).is_displayed()

    #@allure.step('Verify slider in myList section ')
    def verify_my_list_slider(self):
        time.sleep(1)
        return self.browser.find_element(*self.myListSlider).is_displayed()

    #@allure.step('Verify List page heading i.e opening after click on see all button')
    def verify_list_Heading(self):
        WebDriverWait(self.browser, 90).until(EC.presence_of_element_located(self.list_page_tile))
        title_text = self.browser.find_element(*self.list_page_tile).text
        print('title----->', title_text)
        return title_text

    #@allure.step('Verify Text List made for you on curated list cards ')
    def verify_curatedText(self):
        time.sleep(2)
        return self.browser.find_element(*self.curated_made).text

    #@allure.step('Verify List title on curated list cards')
    def verify_curateList_title(self):
        return self.browser.find_element(*self.curated_title).is_displayed()

    #@allure.step('Verify number of titles on curated list ')
    def verify_curatedNumtitles(self):
        return self.browser.find_element(*self.curated_numTitle).is_displayed()

    #@allure.step('Verify Title of lists ')
    def verify_listsTitle(self):
        WebDriverWait(self.browser, 40).until(EC.presence_of_element_located(self.title))
        return self.browser.find_element(*self.title).text

    #@allure.step('Verify User created List in table ')
    def verify_userCreated_list(self):
        WebDriverWait(self.browser, 35).until(EC.presence_of_element_located(self.user_created))
        return self.browser.find_element(*self.user_created).text

    #@allure.step('Verify on list detailed page heading is showing ')
    def heading_detailedPage(self):
        time.sleep(2)
        return self.browser.find_element(*self.heading_detailed).is_displayed()

    #@allure.step('Verify share button is displayed in list page')
    def verify_shareButton(self):
        time.sleep(1)
        return self.browser.find_element(*self.share_button).is_displayed()

    #@allure.step('Verify share button is displayed in list page')
    def verify_yourlist_title(self):
        time.sleep(0.5)
        return self.browser.find_element(*self.title_count).is_displayed()

    #@allure.step('Verify Delete button is displayed in list page ')
    def verify_deleteButton(self):
        WebDriverWait(self.browser, 5).until(EC.presence_of_element_located(self.delete_button))
        return self.browser.find_element(*self.delete_button).is_displayed()

    #@allure.step('Verify Check box is displayed in list  page ')
    def verify_checkBox(self):
        WebDriverWait(self.browser, 5).until(EC.presence_of_element_located(self.verifylist_check))
        chk = self.browser.find_element(*self.verifylist_check)
        return chk.is_displayed()

    #@allure.step('Verify Check box gets selected after clicking on check box')
    def verify_checkselected(self):
        time.sleep(2.5)
        return self.browser.find_element(*self.verifylist_check).is_selected()

    #@allure.step('Clicking on check box in list page')
    def click_list_checkBox(self):
        time.sleep(0.5)
        self.browser.find_element(*self.verifylist_check).click()

    #@allure.step('Verify Check box gets selected after clicking on check box foe multiple')
    def verify_second_checkbox_selected(self):
        time.sleep(2)
        return self.browser.find_element(*self.test_checkbox).is_selected()

    #@allure.step('Clicking on check box in list page for multiple')
    def click_Demo_checkBox(self):
        # time.sleep(2)
        demo_checkbox = self.browser.find_element(*self.verifylist_check)
        self.browser.execute_script("arguments[0].click();", demo_checkbox)

    def Refresh(self):
        self.browser.refresh()
        WebDriverWait(self.browser, 300).until(EC.presence_of_element_located(self.user_created))
        # time.sleep(2)

    def RefreshMyList(self):
        # self.browser.refresh()
        WebDriverWait(self.browser, 95).until(EC.presence_of_element_located(self.header_mylist))
        time.sleep(16)
        self.browser.find_element(*self.header_mylist).click()
        time.sleep(10)
        self.browser.refresh()
        time.sleep(10)
        WebDriverWait(self.browser, 60).until(EC.presence_of_element_located(self.testCuratedList))
        time.sleep(2)
        return self.browser.find_element(*self.testCuratedList).is_displayed()

    def Refresh_List_page(self):
        self.browser.refresh()
        WebDriverWait(self.browser, 300).until(EC.presence_of_element_located(self.list_heading))
        time.sleep(45) # taking too much time

    def Refresh_List(self):
        self.browser.refresh()
        time.sleep(60)

    #@allure.step('Clicking on check box in list page for multiple')
    def click_test_checkBox(self):
        # WebDriverWait(self.browser, 35).until(EC.presence_of_element_located(self.second_check_box))
        time.sleep(1.5)
        second = self.browser.find_element(*self.second_check_box)
        self.browser.execute_script("arguments[0].scrollIntoView();", second)
        time.sleep(1)
        self.browser.find_element(*self.second_check_box).click()
        time.sleep(1)

    #@allure.step('Clicking on check box in list page for multiple')
    def click_first_test_checkBox(self):
        time.sleep(.5)
        second = self.browser.find_element(*self.test_checkbox)
        self.browser.execute_script("arguments[0].scrollIntoView();", second)
        time.sleep(2)
        self.browser.find_element(*self.test_checkbox).click()
        time.sleep(2)

    #@allure.step('Verify List selected Text in opened footer popup')
    def verify_Listtext(self):
        time.sleep(0.5)
        return self.browser.find_element(*self.list_selected).text

    #@allure.step('Verify List selected Text in opened footer popup')
    def verify_List_text_multi(self):
        time.sleep(0.5)
        return self.browser.find_element(*self.list_selected_items).text

    #@allure.step('Verify Download.csv file  in footer popup')
    def verify_downloadCsv(self):
        time.sleep(0.5)
        return self.browser.find_element(*self.download_footer).is_displayed()

    #@allure.step('Verify Download.csv is clickable  in footer popup')
    def verify_downloading_started(self):
        time.sleep(10)
        try:
            downloading_start = self.browser.find_element(*self.list_selected_items).is_displayed()
            if downloading_start:
                return False
        except:
            return True

    #@allure.step('Verify Delete button is not present in Curated list')
    def verify_delete_button_curated(self):
        time.sleep(2)
        try:
            delete_button = self.browser.find_element(*self.spreadsheetDeleteButton).is_displayed()
            if delete_button:
                return False
        except:
            return True

    #@allure.step('Verify Download.csv button is clickable in curated footer popup')
    def click_download_csv_curated_popup(self):
        time.sleep(2)
        self.browser.find_element(*self.download_footer).click()

    #@allure.step('Verify Download.csv file  in footer popup')
    def verify_add_to_list_footer(self):
        time.sleep(2)
        return self.browser.find_element(*self.download_footer).is_displayed()

    #@allure.step('Verify csv file is downloaded')
    def verify_csv_file_downloaded(self):
        time.sleep(18)
        try:
            download_csv = self.browser.find_element(*self.list_selected).is_displayed()
            if download_csv:
                return True
        except:
            return False

    #@allure.step('click on add to list in footer popup')
    def click_add_to_list_footer(self):
        time.sleep(1.5)
        return self.browser.find_element(*self.add_to_list_popup_footer).click()

    #@allure.step('Verify Download.csv file  in footer popup')
    def click_download_csv(self):
        time.sleep(1.5)
        self.browser.find_element(*self.download_footer).click()
        time.sleep(3)



    #@allure.step('Verify Download.csv file  in footer popup')
    def click_list_multi_download_csv(self):
        time.sleep(1)
        second = self.browser.find_element(*self.download_footer)
        self.browser.execute_script("arguments[0].click();", second)

    #@allure.step('Verify share list  in footer popup')
    def verify_shareList(self):
        time.sleep(.5)
        return self.browser.find_element(*self.share_popup_footer).is_displayed()

    #@allure.step('Verify share list  in footer popup')
    def click_footer_shareList(self):
        time.sleep(5)
        footer_email= self.browser.find_element(*self.share_popup_footer)
        self.browser.execute_script("arguments[0].click();", footer_email)

    #@allure.step('Verify share title from footer on movie ')
    def verify_shareTitle(self):
        time.sleep(2)
        return self.browser.find_element(*self.share_title).is_displayed()

    #@allure.step('Verify Delete tab in footer popup ')
    def verify_DeleteFooterpopup(self):
        time.sleep(.5)
        return self.browser.find_element(*self.delete_popup_footer).is_displayed()

    #@allure.step('Verify Add to list tab in footer popup ')
    def verify_AddToListFooterpopup(self):
        time.sleep(1)
        return self.browser.find_element(*self.add_to_list_popup_footer).is_displayed()

    #@allure.step('Verify click on add to list footer popup ')
    def verify_click_AddToListFooterpopup(self):
        WebDriverWait(self.browser, 60).until(EC.presence_of_element_located(self.add_to_list_popup_footer))
        time.sleep(.5)
        list = self.browser.find_element(*self.add_to_list_popup_footer)
        self.browser.execute_script("arguments[0].click();", list)

    #@allure.step('Verify Delete tab in footer popup ')
    def click_DeleteFooterpopup(self):
        time.sleep(.5)
        self.browser.find_element(*self.delete_popup_footer).click()

    #@allure.step('Verify Delete tab in footer popup ')
    def click_DeleteFooterpopup(self):
        time.sleep(2)
        return self.browser.find_element(*self.delete_popup_footer).click()

    #@allure.step('Click on list name to redirect on list detailed page')
    def click_Createdlist(self):
        WebDriverWait(self.browser, 15).until(EC.presence_of_element_located(self.user_created))
        self.browser.find_element(*self.user_created).click()

    #@allure.step('Click on list name to redirect on list detailed page')
    def click_recentlyList(self):
        WebDriverWait(self.browser, 60).until(EC.presence_of_element_located(self.recentlyList))
        self.browser.find_element(*self.recentlyList).click()

    #@allure.step('Click on list name to redirect on list detailed page')
    def click_tvShowList(self):
        WebDriverWait(self.browser, 70).until(EC.presence_of_element_located(self.tvShowList))
        self.browser.find_element(*self.tvShowList).click()

    #@allure.step('Click on list name to redirect on list detailed page')
    def verify_tv_show_my_list(self):
        WebDriverWait(self.browser, 30).until(EC.presence_of_element_located(self.series_name))
        time.sleep(2.5)
        return self.browser.find_element(*self.series_name).is_displayed()

    #@allure.step('Movie cards view details button in list details page')
    def viewDetails_first_movie_card(self):
        WebDriverWait(self.browser, 40).until(EC.presence_of_element_located(self.first_movie_card))
        list = self.browser.find_element(*self.first_movie_card)
        self.browser.execute_script("arguments[0].scrollIntoView();", list)
        time.sleep(1)
        view_details = self.browser.find_element(*self.view_details_movie_card)
        ActionChains(self.browser).move_to_element(view_details).perform()
        time.sleep(1)
        return view_details.is_displayed()

    #@allure.step('click on Movie cards view details button in list details page')
    def click_viewDetails_first_movie_card_list(self):
        WebDriverWait(self.browser, 28).until(EC.presence_of_element_located(self.first_movie_card))
        time.sleep(1.5)
        list = self.browser.find_element(*self.first_movie_card)
        self.browser.execute_script("arguments[0].scrollIntoView();", list)
        time.sleep(1.5)
        view_details = self.browser.find_element(*self.view_details_movie_card)
        ActionChains(self.browser).move_to_element(view_details).perform()
        time.sleep(1.5)
        view_details.click()


    #@allure.step('Movie cards view details button in best pictures winners section')
    def watch_trailer_first_movie_card(self):
        WebDriverWait(self.browser, 28).until(EC.presence_of_element_located(self.first_movie_card))
        list = self.browser.find_element(*self.first_movie_card)
        self.browser.execute_script("arguments[0].scrollIntoView();", list)
        time.sleep(2)
        watch_trailer = self.browser.find_element(*self.watch_trailer_movie_card)
        ActionChains(self.browser).move_to_element(watch_trailer).perform()
        time.sleep(2)
        return watch_trailer.is_displayed()

    #@allure.step('Movie cards watch-now button')
    def watch_now_first_movie_card(self):
        WebDriverWait(self.browser, 28).until(EC.presence_of_element_located(self.first_movie_card))
        list = self.browser.find_element(*self.first_movie_card)
        self.browser.execute_script("arguments[0].scrollIntoView();", list)
        time.sleep(2)
        watch_trailer = self.browser.find_element(*self.watch_now_movie_card)
        ActionChains(self.browser).move_to_element(watch_trailer).perform()
        time.sleep(2)
        return watch_trailer.is_displayed()

    #@allure.step('Click onMovie cards watch now button ')
    def click_watch_now_first_movie_card(self):

        WebDriverWait(self.browser, 28).until(EC.presence_of_element_located(self.first_movie_card))
        time.sleep(3)
        list = self.browser.find_element(*self.first_movie_card)
        self.browser.execute_script("arguments[0].scrollIntoView();", list)
        time.sleep(1.5)
        watch_trailer = self.browser.find_element(*self.watch_now_movie_card)
        ActionChains(self.browser).move_to_element(watch_trailer).perform()
        time.sleep(1.5)
        watch_trailer.click()

    #@allure.step('Verify Movie cards add-to-list button ')
    def add_to_list_first_movie_card(self):
        WebDriverWait(self.browser, 28).until(EC.presence_of_element_located(self.first_movie_card))
        list = self.browser.find_element(*self.first_movie_card)
        self.browser.execute_script("arguments[0].scrollIntoView();", list)
        time.sleep(2)
        watch_trailer = self.browser.find_element(*self.add_to_list_movie_card)
        ActionChains(self.browser).move_to_element(watch_trailer).perform()
        time.sleep(2)
        return watch_trailer.is_displayed()

    #@allure.step('Click on Movie cards add to list button ')
    def click_add_to_list_first_movie_card(self):
        WebDriverWait(self.browser, 28).until(EC.presence_of_element_located(self.first_movie_card))
        list = self.browser.find_element(*self.first_movie_card)
        self.browser.execute_script("arguments[0].scrollIntoView();", list)
        time.sleep(2)
        add_to_list = self.browser.find_element(*self.add_to_list_movie_card)
        ActionChains(self.browser).move_to_element(add_to_list).perform()
        time.sleep(2)
        add_to_list.click()

    #@allure.step('Click on list name to redirect on list detailed page')
    def click_delete_my_list(self):
        WebDriverWait(self.browser, 16).until(EC.presence_of_element_located(self.delete_button))
        self.browser.find_element(*self.delete_button).click()

    #@allure.step('Click on list name to redirect on list detailed page')
    def click_delete_test2_my_list(self):
        WebDriverWait(self.browser, 5).until(EC.presence_of_element_located(self.delete_button_test2))
        self.browser.find_element(*self.delete_button_test2).click()

    def click_automationList_toDel(self):
        self.browser.find_element(*self.auto_delete_btn).click()
        time.sleep(2)

    #@allure.step('delete demo list ')
    def delete_Demo_list(self,URL):
        try:
            try:
                WebDriverWait(self.browser, 180).until(
                    EC.presence_of_element_located(self.your_list_first_delete_button))
                first_list_delete_button = self.browser.find_element(*self.your_list_first_delete_button)
                if first_list_delete_button.is_displayed():
                    print("list element is present")
            except:
                self.browser.get(URL)
                WebDriverWait(self.browser, 30).until(EC.presence_of_element_located(self.first_carousel_title))
                self.browser.find_element(*self.header_mylist).click()
                WebDriverWait(self.browser, 40).until(EC.presence_of_element_located(self.lists))
                time.sleep(1)
                self.browser.find_element(*self.lists).click()
                WebDriverWait(self.browser, 35).until(
                    EC.presence_of_element_located(self.your_list_first_delete_button))

            demo_list = self.browser.find_element(*self.raw_demo)
            if demo_list.is_displayed():
                list_name = self.browser.find_element(*self.raw_demo)
                self.browser.execute_script("arguments[0].scrollIntoView();", list_name)
                time.sleep(2)
                self.browser.execute_script("arguments[0].click();", list_name)
                time.sleep(2)
                self.browser.find_element(*self.delete_direct_mylist).click()
                WebDriverWait(self.browser, 20).until(EC.presence_of_element_located(self.delete_list_confirmation_text))
                self.browser.find_element(*self.delete_list_confirmation_text).is_displayed()
        except:
            print("Demo list is not present")

    #@allure.step('delete demo list ')
    def delete_Demo1_list(self):
        try:
            WebDriverWait(self.browser, 5).until(EC.presence_of_element_located(self.your_list_first_delete_button))
            demo_list = self.browser.find_element(*self.raw_demo)
            if demo_list.is_displayed():
                list_name = self.browser.find_element(*self.raw_demo)
                self.browser.execute_script("arguments[0].scrollIntoView();", list_name)
                time.sleep(2)
                self.browser.execute_script("arguments[0].click();", list_name)
                time.sleep(2)
                self.browser.find_element(*self.delete_direct_mylist).click()
                WebDriverWait(self.browser, 20).until(
                    EC.presence_of_element_located(self.delete_list_confirmation_text))
                self.browser.find_element(*self.delete_list_confirmation_text).is_displayed()
        except:
            print("Demo list is not present")

    #@allure.step('delete test2 list ')
    def delete_test2_list(self):
        try:
            WebDriverWait(self.browser, 5).until(EC.presence_of_element_located(self.your_list_first_delete_button))
            demo_list = self.browser.find_element(*self.raw_test2)
            if demo_list.is_displayed():
                list_name = self.browser.find_element(*self.raw_test2)
                self.browser.execute_script("arguments[0].scrollIntoView();", list_name)
                time.sleep(2)
                self.browser.execute_script("arguments[0].click();", list_name)
                time.sleep(2)
                self.browser.find_element(*self.delete_direct_mylist).click()
                WebDriverWait(self.browser, 20).until(EC.presence_of_element_located(self.delete_list_confirmation_text))
                self.browser.find_element(*self.delete_list_confirmation_text).is_displayed()
        except:
            print("test-2 list is not present")

    #@allure.step('delete test1 list ')
    def delete_raw_test1_list(self):
        try:
            WebDriverWait(self.browser, 5).until(EC.presence_of_element_located(self.your_list_first_delete_button))
            demo_list = self.browser.find_element(*self.raw_test1)
            if demo_list.is_displayed():
                list_name = self.browser.find_element(*self.raw_test1)
                self.browser.execute_script("arguments[0].scrollIntoView();", list_name)
                time.sleep(2)
                self.browser.execute_script("arguments[0].click();", list_name)
                time.sleep(2)
                self.browser.find_element(*self.delete_direct_mylist).click()
                WebDriverWait(self.browser, 20).until(EC.presence_of_element_located(self.delete_list_confirmation_text))
                self.browser.find_element(*self.delete_list_confirmation_text).is_displayed()
        except:
            print("test-1 list is not present")

    #@allure.step('delete test  list ')
    def delete_raw_test_list(self):
        try:
            WebDriverWait(self.browser, 5).until(EC.presence_of_element_located(self.your_list_first_delete_button))
            demo_list = self.browser.find_element(*self.raw_test)
            if demo_list.is_displayed():
                list_name = self.browser.find_element(*self.raw_test)
                self.browser.execute_script("arguments[0].scrollIntoView();", list_name)
                time.sleep(2)
                self.browser.execute_script("arguments[0].click();", list_name)
                time.sleep(2)
                self.browser.find_element(*self.delete_direct_mylist).click()
                WebDriverWait(self.browser, 20).until(
                    EC.presence_of_element_located(self.delete_list_confirmation_text))
                self.browser.find_element(*self.delete_list_confirmation_text).is_displayed()
        except:
            print("test list is not present")

    #@allure.step('delete recentlyList2  list ')
    def delete_raw_recentlyList2(self):
        try:
            WebDriverWait(self.browser, 5).until(EC.presence_of_element_located(self.your_list_first_delete_button))
            demo_list = self.browser.find_element(*self.raw_recentlyList2)
            if demo_list.is_displayed():
                list_name = self.browser.find_element(*self.raw_recentlyList2)
                self.browser.execute_script("arguments[0].scrollIntoView();", list_name)
                time.sleep(2)
                self.browser.execute_script("arguments[0].click();", list_name)
                time.sleep(2)
                self.browser.find_element(*self.delete_direct_mylist).click()
                WebDriverWait(self.browser, 20).until(
                    EC.presence_of_element_located(self.delete_list_confirmation_text))
                self.browser.find_element(*self.delete_list_confirmation_text).is_displayed()
        except:
            print("recentlyList-2 list is not present")

    #@allure.step('delete recentlyList  list ')
    def delete_raw_recentlyList(self):
        try:
            WebDriverWait(self.browser, 5).until(EC.presence_of_element_located(self.your_list_first_delete_button))
            demo_list = self.browser.find_element(*self.raw_recentlyList)
            if demo_list.is_displayed():
                list_name = self.browser.find_element(*self.raw_recentlyList)
                self.browser.execute_script("arguments[0].scrollIntoView();", list_name)
                time.sleep(2)
                self.browser.execute_script("arguments[0].click();", list_name)
                time.sleep(2)
                self.browser.find_element(*self.delete_direct_mylist).click()
                WebDriverWait(self.browser, 20).until(
                    EC.presence_of_element_located(self.delete_list_confirmation_text))
                self.browser.find_element(*self.delete_list_confirmation_text).is_displayed()
        except:
            print("recentlyList list is not present")

    #@allure.step('delete Film Series list ')
    def delete_raw_film_series_list(self):
        try:
            WebDriverWait(self.browser, 5).until(EC.presence_of_element_located(self.your_list_first_delete_button))
            demo_list = self.browser.find_element(*self.raw_filmSeriesList)
            if demo_list.is_displayed():
                list_name = self.browser.find_element(*self.raw_filmSeriesList)
                self.browser.execute_script("arguments[0].scrollIntoView();", list_name)
                time.sleep(2)
                self.browser.execute_script("arguments[0].click();", list_name)
                time.sleep(2)
                self.browser.find_element(*self.delete_direct_mylist).click()
                WebDriverWait(self.browser, 20).until(EC.presence_of_element_located(self.delete_list_confirmation_text))
                self.browser.find_element(*self.delete_list_confirmation_text).is_displayed()
        except:
            print("test-2 list is not present")

    #@allure.step('delete Film Series Movies List')
    def delete_raw_film_series_movies_list(self):
        try:
            WebDriverWait(self.browser, 5).until(EC.presence_of_element_located(self.your_list_first_delete_button))
            demo_list = self.browser.find_element(*self.raw_moviesList)
            if demo_list.is_displayed():
                list_name = self.browser.find_element(*self.raw_moviesList)
                self.browser.execute_script("arguments[0].scrollIntoView();", list_name)
                time.sleep(2)
                self.browser.execute_script("arguments[0].click();", list_name)
                time.sleep(2)
                self.browser.find_element(*self.delete_direct_mylist).click()
                WebDriverWait(self.browser, 20).until(EC.presence_of_element_located(self.delete_list_confirmation_text))
                self.browser.find_element(*self.delete_list_confirmation_text).is_displayed()
        except:
            print("test-2 list is not present")

    #@allure.step('delete Film Series list ')
    def delete_raw_tv_show_list(self):
        try:
            WebDriverWait(self.browser, 15).until(EC.presence_of_element_located(self.your_list_first_delete_button))
            time.sleep(5)
            demo_list = self.browser.find_element(*self.raw_tvSowList)
            if demo_list.is_displayed():
                list_name = self.browser.find_element(*self.raw_tvSowList)
                self.browser.execute_script("arguments[0].scrollIntoView();", list_name)
                time.sleep(2.5)
                self.browser.execute_script("arguments[0].click();", list_name)
                time.sleep(2.5)
                self.browser.find_element(*self.delete_direct_mylist).click()
                WebDriverWait(self.browser, 20).until(
                    EC.presence_of_element_located(self.delete_list_confirmation_text))
                self.browser.find_element(*self.delete_list_confirmation_text).is_displayed()
        except:
            print("Film Series List is not present")

    #@allure.step('delete Film Series list ')
    def delete_raw_list_data_list(self):
        try:
            WebDriverWait(self.browser, 25).until(EC.presence_of_element_located(self.your_list_first_delete_button))
            time.sleep(10)
            demo_list = self.browser.find_element(*self.raw_listDataList)
            if demo_list.is_displayed():
                list_name = self.browser.find_element(*self.raw_listDataList)
                self.browser.execute_script("arguments[0].scrollIntoView();", list_name)
                time.sleep(2)
                self.browser.execute_script("arguments[0].click();", list_name)
                time.sleep(2)
                self.browser.find_element(*self.delete_direct_mylist).click()
                WebDriverWait(self.browser, 20).until(
                    EC.presence_of_element_located(self.delete_list_confirmation_text))
                self.browser.find_element(*self.delete_list_confirmation_text).is_displayed()
        except:
            print("Film Series List is not present")

    #@allure.step('delete Film Series Second list ')
    def delete_raw_film_series_second_list(self, URL):
        try:
            try:
                WebDriverWait(self.browser, 185).until(
                    EC.presence_of_element_located(self.your_list_first_delete_button))
                first_list_delete_button = self.browser.find_element(*self.your_list_first_delete_button)
                if first_list_delete_button.is_displayed():
                    print("list element is present")
            except:
                self.browser.get(URL)
                WebDriverWait(self.browser, 60).until(EC.presence_of_element_located(self.first_carousel_title))
                self.browser.find_element(*self.header_mylist).click()
                WebDriverWait(self.browser, 50).until(EC.presence_of_element_located(self.lists))
                time.sleep(1)
                self.browser.find_element(*self.lists).click()
                WebDriverWait(self.browser, 35).until(
                    EC.presence_of_element_located(self.your_list_first_delete_button))

            demo_list = self.browser.find_element(*self.raw_filmSeriesSecondList)
            if demo_list.is_displayed():
                list_name = self.browser.find_element(*self.raw_filmSeriesSecondList)
                self.browser.execute_script("arguments[0].scrollIntoView();", list_name)
                time.sleep(2)
                self.browser.execute_script("arguments[0].click();", list_name)
                time.sleep(2)
                self.browser.find_element(*self.delete_direct_mylist).click()
                WebDriverWait(self.browser, 20).until(EC.presence_of_element_located(self.delete_list_confirmation_text))
                self.browser.find_element(*self.delete_list_confirmation_text).is_displayed()
        except:
            print("Film Series Second List is not present")

    #@allure.step('delete testing cart2 ')
    def delete_Testing_cart2_carts(self):
        try:
            time.sleep(10)
            demo_list = self.browser.find_element(*self.testingCart2)
            if demo_list.is_displayed():
                list_name = self.browser.find_element(*self.testingCart2)
                self.browser.execute_script("arguments[0].scrollIntoView();", list_name)
                time.sleep(2)
                self.browser.execute_script("arguments[0].click();", list_name)
                time.sleep(2)
                self.browser.find_element(*self.delete_direct_cart).click()
                WebDriverWait(self.browser, 20).until(
                    EC.presence_of_element_located(self.delete_cart_confirmation_text))
                self.browser.find_element(*self.delete_cart_confirmation_text).is_displayed()
        except:
            print("testing cart 2 is not present")

    #@allure.step('delete testing cart ')
    def delete_Testing_cart_carts(self):
        try:
            time.sleep(5)
            demo_list = self.browser.find_element(*self.testingCart)
            if demo_list.is_displayed():
                list_name = self.browser.find_element(*self.testingCart)
                self.browser.execute_script("arguments[0].scrollIntoView();", list_name)
                time.sleep(2)
                self.browser.execute_script("arguments[0].click();", list_name)
                time.sleep(2)
                self.browser.find_element(*self.delete_direct_cart).click()
                WebDriverWait(self.browser, 20).until(
                    EC.presence_of_element_located(self.delete_cart_confirmation_text))
                self.browser.find_element(*self.delete_cart_confirmation_text).is_displayed()
                time.sleep(3)
        except:
            print("testing cart is not present")