import allure, time
import json
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import StaleElementReferenceException
from resources.variables import *


class filmSeriesPage:
    movieNameAboutFate = 'p[contains(text()," About Fate ")]'
    movieNameCyrano = 'p[contains(text()," Cyrano ")]'
    seriesNameBigShot = 'p[contains(text()," The Big Shot With Bethenny (series) ")]'
    firstCardPoster = (By.XPATH, '//ul[contains(@class,"search-list")]/li[1]/div[2]//div[@class="poster"]')
    firstCardTitle = (
    By.XPATH, '//ul[contains(@class,"search-list")]/li[1]//div[@class="desk-on"]//div[@class="movie-detail"]/p')
    firstCardGenre = (
    By.XPATH, '//ul[contains(@class,"search-list")]/li[1]//div[@class="desk-on"]//div[@class="movie-detail"]/span[1]')
    bannerImage = (By.XPATH, '//div[@class="header"]/div/img')
    bannerText = (By.XPATH, '//div[@class="banner-text"]/h2[contains(text(),"Our Titles")]')
    searchInputField = (By.XPATH, '//div[@class="search-content"]/input[@placeholder="Search Movie or TV Titles"]')
    searchButton = (By.XPATH, '//div[@class="search-content"]/button[@class="search-btn"]/div[@class="search-icon"]')
    searchFirstMovieCard = (By.XPATH,
                            '//div[contains(@class,"search-list-section")]/ul/li[1]/div[2]/mgm-list-poster/div[1]//div[@class="movie-detail"]/p')
    searchResultCount = (By.XPATH, '//div[contains(@class,"count-section")]/div[contains(@class,"search-counts")]/h2/span[1]')
    firstCardMovieName = (By.XPATH, '(//div[@class="desk-on"]//div[@class="movie-detail"]/p)[1]')
    searchResultSText = (By.XPATH, '//div[contains(@class,"count-section")]/div[contains(@class,"search-counts")]/h2/span[2]')
    loadingText = (By.XPATH, '//div[contains(@class,"search-list-container")]//h2[contains(@class,"count-text")]/span[text()="Loading"]')
    searchClearButton = (By.XPATH, '//button[@class="search-btn"]/div[@class="clear"]')
    allMovieCardCheckbox = (By.XPATH, '//div[@class="checkbox-shell-dark"]/input[@type="checkbox"]')
    all_poster = (By.XPATH, '//div[@class="poster"]')
    filterType = (By.XPATH, '//div[contains(@class,"dropdown-filter-section")]/div/div/div[contains(text(),"type")]')
    filterGenre = (By.XPATH, '//div[contains(@class,"dropdown-filter-section")]/div/div/div[contains(text(),"Genre")]')
    filterRating = (
    By.XPATH, '//div[contains(@class,"dropdown-filter-section")]/div/div/div[contains(text(),"rating")]')
    actionGenreFilterApplied = (By.XPATH, '//ul/li/span[contains(text(),"Action")]')
    nc_17RatingFilterApplied = (By.XPATH, '//ul/li/span[contains(text(),"NC-17")]')
    filterYear = (By.XPATH, '//div[contains(@class,"dropdown-filter-section")]/div/div[last()]/div')
    allSimpleFilter = (By.XPATH, '//div[contains(@class,"dropdown-filter-section")]/div/div/div[contains(@class,"dropdown-filter")]')
    advanceFilter = (By.XPATH, '//div/a[contains(text(),"Show Advanced Filters")]')
    hideAdvanceFilter = (By.XPATH, '//div/span[contains(text(),"Hide Advanced Filters")]')
    allAdvanceFilter = (By.XPATH, '//div[contains(@class,"advance-filter-context")]/div')
    advancePlotTheme = (By.XPATH, '//div[contains(@class,"advance-filter-context")]//span[contains(text(),"Plot Theme")]')
    advanceSettingRegion = (By.XPATH, '//div[contains(@class,"advance-filter-context")]//span[contains(text(),"Setting Region")]')
    advanceTimePeriod = (By.XPATH, '//div[contains(@class,"advance-filter-context")]//span[contains(text(),"Time Period")]')
    advanceHoliday = (By.XPATH, '//div[contains(@class,"advance-filter-context")]//span[contains(text(),"Holiday")]')
    advanceCommunity = (By.XPATH, '//div[contains(@class,"advance-filter-context")]//span[contains(text(),"Community")]')
    advanceBasedOn = (By.XPATH, '//div[contains(@class,"advance-filter-context")]//span[contains(text(),"Based On")]')

    sortFilter = (By.XPATH, '//div[contains(@class,"sort-filter")]/div')
    allSortFilter = (By.XPATH, '//div[contains(@class,"dropdown-default")]/span')
    gridListMenu = (By.XPATH, '//div[contains(@class,"viewModebtn")]/div')
    nextPaginationButton = (By.XPATH, '//li[contains(@class,"pagination-next")]/a')
    nextPaginationSingleButton = (By.XPATH, '//li[contains(@class,"pagination-next")]')
    paginationSecondLast = (By.XPATH, '//nav[@aria-label="Pagination"]/ul/li[last()-1]/a/span[2]')
    pagination_44 = (By.XPATH, '//li/a/span[contains(text(),"44")]')
    pagination_3 = (By.XPATH, '//li/a/span[contains(text(),"3")]')
    pagination_5 = (By.XPATH, '//li/a/span[contains(text(),"5")]')
    left_cursor_disabled = (By.XPATH, '//nav[@aria-label="Pagination"]/ul/li[1]')
    right_cursor_disabled = (By.XPATH, '//nav[@aria-label="Pagination"]/ul/li[last()]')
    paginationNextButtonClick = (By.XPATH, '//nav[@aria-label="Pagination"]/ul/li[last()]/a')
    right_asset_cursor_disabled = (By.XPATH, '//ul[@aria-label="Pagination"]/li[8]')
    hobbit_card = (By.XPATH, ' //div/p[contains(text(),"The Hobbit: The Battle Of The Five Armies")] ')
    disablePages = (By.XPATH, '//nav/ul/li[@class="ng-star-inserted"]')
    activePage = (By.XPATH, '//li[contains(@class,"current")]')
    leftCursor = (By.XPATH, '//nav[@aria-label="Pagination"]/ul/li[1]/a')
    clearAllFilter = (By.XPATH, '//li[contains(@class,"clear-filter")]/span')
    filterTypeFilms = (By.XPATH, '//div[contains(@class,dropdown-filter-section)]/span[contains(text(),"Films")]')
    filterTypeSeries = (By.XPATH, '//div[contains(@class,dropdown-filter-section)]/span[contains(text(),"Series")]')
    filterGenreAction = (
    By.XPATH, '//span[contains(@class,"ng-star-inserted")]/span[contains(text(),"Action")]/parent::span/i')
    filterGenreAdventure = (
    By.XPATH, '//span[contains(@class,"ng-star-inserted")]/span[contains(text(),"Adventure")]/parent::span/i')
    applyFilterButton = (By.XPATH, '//div[contains(@class,"apply-filter-state")]/span')
    verifyApplyFilterButton = (By.XPATH, '//div[contains(@class,"filter-btns")]/span')
    applyFilterYearButton = (By.XPATH, '//div[contains(@class,"filter-btns")]/span')
    agentSpiesText = (By.XPATH, '//li/span[contains(text(),"Agents & Spies")]')
    aliensText = (By.XPATH, '//li/span[contains(text(),"Aliens")]')
    plotThemeAgentSpies = (By.XPATH, '(//span[contains(text(),"Agents & Spies")])[1]')
    plotThemeAliens = (By.XPATH, '//span[contains(text(),"Aliens")]')
    settingRegionAfricaMiddleEast = (By.XPATH, '//span[contains(text(),"Africa & Middle East")]')
    holidayChristmas = (By.XPATH, '//span[contains(text(),"Christmas")]')
    holidayChristmasText = (By.XPATH, '//li/span[contains(text(),"Christmas")]')
    holidayEaster = (By.XPATH, '//span[contains(text(),"Easter")]')
    holidayEasterText = (By.XPATH, '//li/span[contains(text(),"Easter")]')
    communityBlackAfricanAmerican = (By.XPATH, '//span[contains(text(),"Black / African-American")]')
    communityBlackAfricanAmericanText = (By.XPATH, '//li/span[contains(text(),"Black / African-American")]')
    basedOnNovelStory = (By.XPATH, '//span[contains(text(),"Novel or Short Story")]')
    basedOnNovelStoryText = (By.XPATH, '//li/span[contains(text(),"Novel or Short Story")]')
    basedOnRealPeople = (By.XPATH, '//span[contains(text(),"Real People or Actual Events")]')
    basedOnRealPeopleText = (By.XPATH, '//li/span[contains(text(),"Real People or Actual Events")]')
    communityLatinx = (By.XPATH, '//span[contains(text(),"Latinx")]')
    communityLatinxText = (By.XPATH, '//li/span[contains(text(),"Latinx")]')
    timePeriodMedieval = (By.XPATH, '//span[contains(text(),"Set in Medieval Times & The Renaissance")]')
    timePeriodMedievalText = (By.XPATH, '//li/span[contains(text(),"Set in Medieval Times & The Renaissance")]')
    timePeriodPrehistory = (By.XPATH, '//span[contains(text(),"Set in Ancient Times & Prehistory")]')
    timePeriodPrehistoryText = (By.XPATH, '//li/span[contains(text(),"Set in Ancient Times & Prehistory")]')
    settingRegionArcticAntarctic = (By.XPATH, '//span[contains(text(),"Arctic & Antarctic")]')
    settingRegionArcticAntarcticText = (By.XPATH, '//li/span[contains(text(),"Arctic & Antarctic")]')
    settingRegionAfricaMiddleEastText = (By.XPATH, '//li/span[contains(text(),"Africa & Middle East")]')
    settingRegionAfricaCrossBtn = (By.XPATH, '//li/span[contains(text(),"Africa & Middle East")]'
                                             '/parent::li/span[2]')
    movieCardActionTag = (By.XPATH, '//div[contains(@class,"search-list-section")]/ul/li/div[2]/mgm-list-poster/div[1]'
                                    '//div[@class="movie-detail"]/span[contains(text(),"Action")]')
    filterRatingNc_17 = (
    By.XPATH, '//span[contains(@class,"ng-star-inserted")]/span[contains(text(),"NC-17")]/parent::span/i')

    filterRatingTvMa = (
    By.XPATH, '//span[contains(@class,"ng-star-inserted")]/span[contains(text(),"TV-MA")]/parent::span/i')
    filterYearLeftSliderButton = (By.XPATH, '//div[contains(@class,"slider")]/ngx-slider/span[5]')
    gridButton = (By.XPATH, '//div[contains(@class,"viewModebtn")]/div[contains(@class,"grid-icon")]')
    listButton = (By.XPATH, '//div[contains(@class,"viewModebtn")]/div[contains(@class,"list-icon")]')
    listTableHead = (By.XPATH, '//ul[contains(@class,"search-list")]/div')
    listTitle = (By.XPATH, '//ul[contains(@class,"search-list")]/div/div[contains(text(),"Title")]')
    listDirectedBy = (By.XPATH, '//ul[contains(@class,"search-list")]/div/div[contains(text(),"Directed By")]')
    listMainCast = (By.XPATH, '//ul[contains(@class,"search-list")]/div/div[contains(text(),"Main Cast")]')
    listSynopsis = (By.XPATH, '//ul[contains(@class,"search-list")]/div/div[contains(text(),"Synopsis")]')
    sortDown = (By.XPATH, '//div[contains(@class,"sort-filter")]/div/span[contains(@class,"dropdown-text")]'
                          '/div[contains(@class,"custom-down-arrow ")]/img')
    sortUp = (By.XPATH, '//div[contains(@class,"sort-filter")]/div/span[contains(@class,"dropdown-text")]'
                        '/div[contains(@class,"custom-up-arrow")]/img')
    sortAtoZ = (By.XPATH, '//div[contains(@class,"sort-filter")]/div/span[contains(text()," SORT A-Z ")]')
    sortZtoA = (By.XPATH, '//div[contains(@class,"sort-filter")]/div/span[contains(text()," SORT Z-A ")]')
    selectAllCheckBox = (By.XPATH, '//div[@class="checkbox-shell-dark"]/input[@id="select-all"]')
    allSelectedCheckBox = (By.XPATH, '//div[contains(@class,"item-actions")]/span')
    sharePopupTitleName = (By.XPATH, '//div[@class="sub-title"]/div')
    sharePopupStaticText = (By.XPATH, '//div[contains(@class,"share-header")]')
    sharePopupEmailInputField = (By.XPATH, '//div[@class="listing"]//div/input[@type="text"]')
    sharePopupButton = (By.XPATH, '//button[contains(text(), "share")]')
    sharePopupCloseButton = (By.XPATH, '//div[@class="share-input"]//div[contains(@class,"close-btn")]/img')
    footerDownloadButton = (By.XPATH, '//div[@class="item-action download-list ng-tns-c148-1 ng-star-inserted"]/button')
    footerEmailSpreadsheet = (
    By.XPATH, '//div[@class="item-action share share-list ng-tns-c148-1 ng-star-inserted"]/button')
    footerAddToList = (By.XPATH, '//div[@class="item-action add-list ng-tns-c148-1 ng-star-inserted"]/button')
    releaseDateList = (By.XPATH, '//div[contains(@class,"title-card-list")]/div/div[@class="releasedDate"]')
    movieNameList = (By.XPATH, '//div[contains(@class,"title-card-list")]/div/div/p[@class="movieName"]')
    movieNameWithAllOptions = (By.XPATH, '//div[1]/div/div[@class="movie-detail"]/p[contains(text()," Being James Bond ")]/parent::div/parent::div//div[contains(@class,"button-hover")]')
    hobbitFirstCard = (By.XPATH, '(//div[1]/div/div[@class="movie-detail"]/parent::div/parent::div//div[contains(@class,"button-hover")])[1]')
    hobbitSecondCard = (By.XPATH,
                       '(//div[1]/div/div[@class="movie-detail"]/parent::div/parent::div//div[contains(@class,"button-hover")])[1]')
    addToListFirstButton = (By.XPATH, '(//div[contains(@class,"button-hover")]//button[contains(text(),"ADD TO LIST")])[1]')
    addToListSecondButton = (
    By.XPATH, '(//div[contains(@class,"button-hover")]//button[contains(text(),"ADD TO LIST")])[2]')
    first_carousel_title = (By.XPATH, '//ul[contains(@class,"carousel-menu-list")]/li[1]/a')
    addToListButton = (By.XPATH, '//div[1]/div/div[@class="movie-detail"]/p[contains(text()," Being James Bond ")]'
                                 '/parent::div/parent::div//div[contains(@class,"button-hover")]//button[contains(text(),"ADD TO LIST")]')
    addToListHobbit = (By.XPATH, '//div[1]/div/div[@class="movie-detail"]/p[contains(text()," The Hobbit:'
                                 ' The Battle Of The Five Armies ")]/parent::div/parent::div//div[contains(@class,'
                                 '"button-hover")]//button[contains(text(),"ADD TO LIST")]')

    watchNow = (By.XPATH, '//div[1]/div/div[@class="movie-detail"]/p[contains(text()," Being James Bond ")]/parent::div/parent::div//div[contains(@class,"button-hover")]//button[contains(text(),"Watch now")]')
    firstMovieNameWithWatchNowOption = (By.XPATH, '(//div[contains(@class,"button-hover")]//'
                                                  'button[contains(text(),"Watch now")])[1]/ancestor::div'
                                                  '[contains(@class,"movie-poster")]//div[@class="movie-detail"]/p')
    watchTrailer = (By.XPATH, '//div[1]/div/div[@class="movie-detail"]/p[contains(text()," Being James Bond ")]/parent::div/parent::div//div[contains(@class,"button-hover")]//button[contains(text(),"Watch trailer")]')
    viewDetails = (By.XPATH, '//div[1]/div/div[@class="movie-detail"]/p[contains(text()," Being James Bond ")]'
                             '/parent::div/parent::div//div[contains(@class,"button-hover")]//button[contains(text(),"View details")]')

    movieAboutFate = (By.XPATH, '//div[1]/div/div[@class="movie-detail"]/'+movieNameAboutFate+'/parent::div/parent::div//div[contains(@class,"button-hover")]')
    viewDetailsAboutFate = (By.XPATH, '//div[1]/div/div[@class="movie-detail"]/'+movieNameAboutFate+'/parent::div/parent::div//div[contains(@class,"button-hover")]//button'
                                     '[contains(text(),"View details")]')
    addToListAboutFate = (By.XPATH, '//div[1]/div/div[@class="movie-detail"]/'+movieNameAboutFate+
                                   '/parent::div/parent::div//div[contains(@class,"button-hover")]//button[contains(text(),"ADD TO LIST")]')
    synopsisTitle = (By.XPATH, '//div[contains(@class,"synopsis-title")]')
    titleOverviewButton = (By.XPATH, '//div[contains(@class,"sub-menu-synopsis")]/p[contains(text(),"TITLE OVERVIEW")]')
    videoPlayerCloseButton = (By.XPATH, '//div[@class="close tele-close"]/img')
    filmAndSeriesActive = (By.XPATH, '//li[@class="menu menu-label"]/a[@id="Films & Series"]')
    createNewListPopupText = (By.XPATH, '//span[contains(text(),"CREATE A NEW LIST")]')
    grid_title = (By.XPATH,
                  '//ul[contains(@class,"search-list")]/li[1]//div[contains(@class,"title-card-list")]//p[@class="movieName"]')
    firstCardCheckBox = (By.XPATH, '//ul[contains(@class,"search-list")]/li[1]//div/input[@type="checkbox"]')
    viewDetailsAddamsFamily2 = (
    By.XPATH, '//div[1]/div/div[@class="movie-detail"]/p[contains(text()," The Addams Family 2 ")]'
              '/parent::div/parent::div//div[contains(@class,"button-hover")]//button[contains(text(),"View details")]')
    movieAddamsFamily2 = (
    By.XPATH, '//div[1]/div/div[@class="movie-detail"]/p[contains(text()," The Addams Family 2 ")]'
              '/parent::div/parent::div//div[contains(@class,"button-hover")]')
    viewDetailsCyrano = (By.XPATH,
                            '//div[1]/div/div[@class="movie-detail"]/' + movieNameCyrano + '/parent::div/parent::div//div[contains(@class,"button-hover")]//button'
                                                                                              '[contains(text(),"View details")]')
    movieCyrano = (By.XPATH, '//div[1]/div/div[@class="movie-detail"]/'+ movieNameCyrano +'/parent::div/parent::div//div[contains(@class,"button-hover")]')
    viewDetailsBigShot = (
        By.XPATH, '//div[1]/div/div[@class="movie-detail"]/'+seriesNameBigShot+'/parent::div/parent::div//div[contains(@class,"button-hover")]//button[contains(text(),"View details")]')
    seriesBigShot = (
        By.XPATH, '//div[1]/div/div[@class="movie-detail"]/'+seriesNameBigShot+'/parent::div/parent::div//div[contains(@class,"button-hover")]')

    def __init__(self, browser):
        self.browser = browser

    #@allure.step('Verify banner-image is displayed in film and series page')
    def verify_banner_image(self):
        WebDriverWait(self.browser, 55).until(EC.presence_of_element_located(self.bannerImage))
        banner = self.browser.find_element(*self.bannerText)
        self.browser.execute_script("arguments[0].scrollIntoView();", banner)
        time.sleep(1.5)
        banner_image = self.browser.find_element(*self.bannerImage).is_displayed()
        return banner_image

    #@allure.step('Verify banner-text is displayed in film and series page')
    def verify_banner_text(self):
        banner_text = self.browser.find_element(*self.bannerText).is_displayed()
        return banner_text

    #@allure.step('Verify Add to list popup should be open after clicking on add-to-list button')
    def verify_add_to_list_popup(self):
        time.sleep(2)
        create_list_text = self.browser.find_element(*self.createNewListPopupText).is_displayed()
        return create_list_text

    #@allure.step('Verify title name is present on spreadsheet popup')
    def verify_spreadsheet_title(self):
        WebDriverWait(self.browser, 12).until(EC.presence_of_element_located(self.sharePopupTitleName))
        time.sleep(2)
        title_name = self.browser.find_element(*self.sharePopupTitleName).is_displayed()
        return title_name

    #@allure.step('Verify static text is present on spreadsheet popup')
    def verify_spreadsheet_static_text(self):
        static_text = self.browser.find_element(*self.sharePopupStaticText).is_displayed()
        return static_text

    #@allure.step('Verify email input field is present on spreadsheet popup')
    def verify_spreadsheet_email_input_field(self):
        email_field = self.browser.find_element(*self.sharePopupEmailInputField).is_displayed()
        return email_field

    #@allure.step('Verify share button is present on spreadsheet popup')
    def verify_spreadsheet_share_button(self):
        share_button = self.browser.find_element(*self.sharePopupButton).is_displayed()
        return share_button

    #@allure.step('Verify close button is present on spreadsheet popup')
    def verify_spreadsheet_close_button(self):
        close_button = self.browser.find_element(*self.sharePopupCloseButton).is_displayed()
        return close_button

    #@allure.step('Verify Search-input-field is displayed in film and series page')
    def verify_banner_search_field(self):
        search_input_field = self.browser.find_element(*self.searchInputField).is_displayed()
        return search_input_field

    #@allure.step('Verify Search-input-field is displayed in film and series page')
    def verify_banner_search_button(self):
        search_button = self.browser.find_element(*self.searchButton).is_displayed()
        return search_button

    #@allure.step('Verify User can type any Movie and Tv-show name')
    def type_search_field(self):
        WebDriverWait(self.browser, 95).until(EC.presence_of_element_located(self.searchInputField))
        self.browser.find_element(*self.searchInputField).clear()
        global movie_name
        data = json.load(open('resources/dataFile.json', 'r'))
        for key, value in data.items():
            movie_name = value
        self.browser.find_element(*self.searchInputField).send_keys(movie_name)
        return movie_name

    # @allure.step('Verify User can type any Movie and Tv-show name')
    def type_series_name_in_search_field(self):
        WebDriverWait(self.browser, 90).until(EC.presence_of_element_located(self.searchInputField))
        self.browser.find_element(*self.searchInputField).clear()
        global seires_name
        data = json.load(open('resources/seriesName.json', 'r'))
        for key, value in data.items():
            seires_name = value
        self.browser.find_element(*self.searchInputField).send_keys(seires_name)
        return seires_name

    # @allure.step('Verify User can type any Movie and Tv-show name')
    def type_search_assets_field(self):
        WebDriverWait(self.browser, 45).until(EC.presence_of_element_located(self.searchInputField))
        self.browser.find_element(*self.searchInputField).clear()
        global movie_name
        data = json.load(open('resources/assetsCardName.json', 'r'))
        for key, value in data.items():
            movie_name = value
        self.browser.find_element(*self.searchInputField).send_keys(movie_name)
        return movie_name

    #@allure.step('Verify User can Search any Movie and Tv-show')
    def click_search_button(self):
        WebDriverWait(self.browser, 65).until(EC.element_to_be_clickable(self.searchButton))
        time.sleep(1)
        self.browser.find_element(*self.searchButton).click()
        time.sleep(2.5)

    #@allure.step('Verify the search result')
    def verify_search_result(self):
        # WebDriverWait(self.browser, 35).until(EC.presence_of_element_located(self.loadingText))
        time.sleep(12.5)
        WebDriverWait(self.browser, 55).until(EC.presence_of_element_located(self.searchResultCount))
        WebDriverWait(self.browser, 55).until(EC.presence_of_element_located(self.firstCardMovieName))
        WebDriverWait(self.browser, 55).until(EC.presence_of_element_located(self.searchResultSText))
        # time.sleep(30)
        time.sleep(1.5)
        total_count = self.browser.find_element(*self.searchResultCount)
        self.browser.execute_script("arguments[0].scrollIntoView();", total_count)
        return self.browser.find_element(*self.firstCardMovieName).text
        # time.sleep(2)

    #@allure.step('Verify the search result')
    def verify_click_search_cross_button(self):
        try:
            time.sleep(10)
            WebDriverWait(self.browser, 55).until(EC.presence_of_element_located(self.searchResultCount))
            WebDriverWait(self.browser, 55).until(EC.presence_of_element_located(self.firstCardMovieName))
            WebDriverWait(self.browser, 55).until(EC.presence_of_element_located(self.searchResultSText))
            return int(self.browser.find_element(*self.searchResultCount).text)

        except:
            return 0

    #@allure.step('verify number of movie-card present on search result')
    def verify_total_movie_card_search_result_button(self):
        time.sleep(1)
        total_poster = self.browser.find_elements(*self.all_poster)
        time.sleep(1)
        return len(total_poster)

    #@allure.step('Verify Film and Series page is highlighted')
    def verify_film_and_series_Active(self):
        time.sleep(2)
        class_text = self.browser.find_element(*self.filmAndSeriesActive).get_attribute('class')
        return class_text

    def page_refresh(self):
        time.sleep(1)
        self.browser.refresh()
        WebDriverWait(self.browser, 300).until(EC.presence_of_element_located(self.firstCardMovieName))
        # time.sleep(10)

    #@allure.step('Verify User Search input field')
    def verify_search_clear_button(self):
        return self.browser.find_element(*self.searchClearButton).is_displayed()

    #@allure.step('Verify User can clear Search input field')
    def click_search_clear(self):
        self.browser.find_element(*self.searchClearButton).click()

    #@allure.step('Verify filters are displayed ')
    def verify_filter_button(self):
        time.sleep(1)
        simple_filter = self.browser.find_elements(*self.allSimpleFilter)
        time.sleep(1)
        filter = len(simple_filter)
        return filter

    #@allure.step('Verify Advance filters are displayed ')
    def verify_advance_filter_button(self):
        self.browser.find_element(*self.advanceFilter).click()
        time.sleep(2)
        filters = self.browser.find_elements(*self.allAdvanceFilter)
        filter = len(filters)
        return filter

    #@allure.step('Verify user can click on hide Advance-Filter button')
    def verify_hide_advance_filter_button(self):
        self.browser.find_element(*self.hideAdvanceFilter).click()
        time.sleep(2)
        return self.browser.find_element(*self.advanceFilter).is_displayed()

    #@allure.step('Verify Plot Theme filters are displayed ')
    def verify_advance_plot_theme_button(self):
        time.sleep(1)
        return self.browser.find_element(*self.advancePlotTheme).is_displayed()

    #@allure.step('User can click on Advance filter Plot-Theme Button')
    def click_advance_plot_theme_button(self):
        time.sleep(1)
        self.browser.find_element(*self.advancePlotTheme).click()

    #@allure.step('Verify apply filter button is present')
    def verify_apply_filter_button(self):
        time.sleep(1)
        apply_filter = self.browser.find_element(*self.verifyApplyFilterButton)
        time.sleep(2)
        self.browser.execute_script("arguments[0].scrollIntoView();", apply_filter)
        time.sleep(2)
        return self.browser.find_element(*self.verifyApplyFilterButton).is_displayed()

    #@allure.step('Click apply filter button is present')
    def click_apply_filter_button(self):
        time.sleep(1.5)
        apply_filter = self.browser.find_element(*self.applyFilterButton)
        time.sleep(1.5)
        self.browser.execute_script("arguments[0].scrollIntoView();", apply_filter)
        time.sleep(2)
        self.browser.find_element(*self.applyFilterButton).click()
        time.sleep(5)

    #@allure.step('Click apply filter button is present')
    def click_apply_filter_button_setting_region(self):
        time.sleep(1)
        self.browser.find_element(*self.applyFilterButton).click()

    #@allure.step('Verify check box text is present')
    def verify_plot_theme_agent(self):
        time.sleep(1)
        return self.browser.find_element(*self.plotThemeAgentSpies).is_displayed()

    #@allure.step('User can Click on Agent and Spies checkbox')
    def click_plot_theme_agent(self):
        time.sleep(1.5)
        return self.browser.find_element(*self.plotThemeAgentSpies).click()

    #@allure.step('User can Click on Aliens checkbox')
    def click_plot_theme_aliens(self):
        time.sleep(1)
        self.browser.find_element(*self.plotThemeAliens).click()

    #@allure.step('User can Click on Aliens checkbox')
    def click_setting_region_africa_middel_east(self):
        time.sleep(1)
        self.browser.find_element(*self.settingRegionAfricaMiddleEast).click()

    #@allure.step('User can Click on Arctic and Antarctic')
    def click_setting_region_arctic_antarctic(self):
        time.sleep(1)
        self.browser.find_element(*self.settingRegionArcticAntarctic).click()

    #@allure.step('User can Click on Time Period Medieval')
    def click_time_period_medieval(self):
        time.sleep(1)
        self.browser.find_element(*self.timePeriodMedieval).click()

    #@allure.step('User can Click on holiday christmas')
    def click_holiday_christmas(self):
        time.sleep(1)
        self.browser.find_element(*self.holidayChristmas).click()

    #@allure.step('User can Click on Community black african')
    def click_community_black_african(self):
        time.sleep(1)
        self.browser.find_element(*self.communityBlackAfricanAmerican).click()

    #@allure.step('User can Click on Based on novel and story')
    def click_based_on_novel_story(self):
        time.sleep(1)
        self.browser.find_element(*self.basedOnNovelStory).click()

    #@allure.step('User can Click on Based on Real People')
    def click_based_on_real_people(self):
        time.sleep(1)
        self.browser.find_element(*self.basedOnRealPeople).click()

    #@allure.step('User can Click on Community latinx checkbox')
    def click_community_latinx(self):
        time.sleep(1)
        self.browser.find_element(*self.communityLatinx).click()

    #@allure.step('User can Click on holiday easter checkbox')
    def click_holiday_easter(self):
        time.sleep(1)
        self.browser.find_element(*self.holidayEaster).click()

    #@allure.step('User can Click on Time Period Prehistory')
    def click_time_period_prehistory(self):
        time.sleep(1)
        self.browser.find_element(*self.timePeriodPrehistory).click()

    #@allure.step('Verify Community filters are displayed ')
    def verify_advance_community_button(self):
        time.sleep(1)
        return self.browser.find_element(*self.advanceCommunity).is_displayed()

    #@allure.step('Click on advance Community button')
    def click_advance_community_button(self):
        time.sleep(1)
        self.browser.find_element(*self.advanceCommunity).click()

    #@allure.step('Verify Holiday filters are displayed ')
    def verify_advance_holiday_button(self):
        time.sleep(1)
        return self.browser.find_element(*self.advanceHoliday).is_displayed()

    #@allure.step('User can Click on Holiday filters button')
    def click_advance_holiday_button(self):
        time.sleep(1)
        self.browser.find_element(*self.advanceHoliday).click()

    #@allure.step('Verify Based On filters are displayed ')
    def verify_advance_based_on_button(self):
        time.sleep(1)
        return self.browser.find_element(*self.advanceBasedOn).is_displayed()

    #@allure.step('user can click Based On filter ')
    def click_advance_based_on_button(self):
        time.sleep(1)
        self.browser.find_element(*self.advanceBasedOn).click()

    #@allure.step('Verify Setting Region filters are displayed ')
    def verify_advance_setting_region_button(self):
        time.sleep(1)
        return self.browser.find_element(*self.advanceSettingRegion).is_displayed()

    #@allure.step('Verify Setting Region button is clickable')
    def click_advance_setting_region_button(self):
        WebDriverWait(self.browser, 25).until(EC.presence_of_element_located(self.advanceSettingRegion))
        next_button = self.browser.find_element(*self.advanceSettingRegion)
        time.sleep(2)
        self.browser.execute_script("arguments[0].scrollIntoView();", next_button)
        self.browser.find_element(*self.advanceSettingRegion).click()

    #@allure.step('Verify Time Period filters are displayed ')
    def verify_advance_time_period_button(self):
        time.sleep(1)
        return self.browser.find_element(*self.advanceTimePeriod).is_displayed()

    #@allure.step('User can click on Time Period filters ')
    def click_advance_time_period_button(self):
        time.sleep(1)
        self.browser.find_element(*self.advanceTimePeriod).click()

    #@allure.step('Verify sorting Filters are displayed')
    def verify_sort_filter_button(self):
        self.browser.find_element(*self.sortFilter).click()
        time.sleep(2)
        filters = self.browser.find_elements(*self.allSortFilter)
        filter = len(filters)
        return filter

    #@allure.step('Verify Grid and List Filters are displayed')
    def verify_menu_filter_button(self):
        time.sleep(2)
        filters = self.browser.find_elements(*self.gridListMenu)
        filter = len(filters)
        return filter

    #@allure.step('Verify Right-Cursor is displayed')
    def verify_right_cursor_button(self):
        WebDriverWait(self.browser, 30).until(EC.presence_of_element_located(self.nextPaginationButton))
        next_button = self.browser.find_element(*self.nextPaginationButton)
        time.sleep(1.5)
        self.browser.execute_script("arguments[0].scrollIntoView();", next_button)
        time.sleep(1.5)
        right_cursor = self.browser.find_element(*self.nextPaginationButton).is_displayed()
        return right_cursor

    #@allure.step('Verify left cursor disabled')
    def verify_left_disabled_cursor(self):
        time.sleep(1)
        WebDriverWait(self.browser, 30).until(EC.presence_of_element_located(self.left_cursor_disabled))
        element = self.browser.find_element(*self.left_cursor_disabled)
        time.sleep(1)
        disable_text = element.get_attribute('class')
        return disable_text

    #@allure.step('Verify right cursor disabled')
    def verify_right_disabled_cursor(self):
        time.sleep(.5)
        WebDriverWait(self.browser, 30).until(EC.presence_of_element_located(self.right_cursor_disabled))
        element = self.browser.find_element(*self.right_cursor_disabled)
        time.sleep(1.5)
        disable_text = element.get_attribute('class')
        return disable_text

    #@allure.step('Verify right cursor disabled')
    def verify_right_disabled_cursor_asset(self):
        time.sleep(1)
        WebDriverWait(self.browser, 90).until(EC.presence_of_element_located(self.right_cursor_disabled))
        element = self.browser.find_element(*self.right_cursor_disabled)
        time.sleep(1.5)
        disable_text = element.get_attribute('class')
        return disable_text

    #@allure.step('Verify expect one all pages are disabled')
    def verify_expect_one_disabled_pages_button(self):
        time.sleep(1)
        disable_pages = self.browser.find_elements(*self.disablePages)
        time.sleep(1)
        number_of_disable_pages = len(disable_pages)
        time.sleep(.5)
        return number_of_disable_pages

    #@allure.step('Verify one  pages is active')
    def verify_one_active_page(self):
        time.sleep(1)
        active_page = self.browser.find_element(*self.activePage).is_displayed()
        return active_page

    #@allure.step('Verify Right-Cursor is displayed')
    def click_right_cursor_button(self):
        time.sleep(1)
        right_pagination = self.browser.find_element(*self.nextPaginationButton)
        self.browser.execute_script("arguments[0].click();", right_pagination)
        time.sleep(1.5)
        WebDriverWait(self.browser, 30).until(EC.presence_of_element_located(self.leftCursor))
        prev_button = self.browser.find_element(*self.leftCursor)
        time.sleep(1.5)
        self.browser.execute_script("arguments[0].scrollIntoView();", prev_button)
        time.sleep(1.5)
        previous_button = self.browser.find_element(*self.leftCursor).is_displayed()
        return previous_button

    #@allure.step('Verify Right-Cursor is disabled')
    def verify_right_cursor_button_disabled(self):
        WebDriverWait(self.browser, 30).until(EC.presence_of_element_located(self.nextPaginationSingleButton))
        time.sleep(2)
        next_button = self.browser.find_element(*self.nextPaginationSingleButton)
        time.sleep(2)
        self.browser.execute_script("arguments[0].scrollIntoView();", next_button)
        time.sleep(3)
        disable_text = next_button.get_attribute('class')
        return disable_text

    #@allure.step('click on last page')
    def click_last_page_button(self):
        WebDriverWait(self.browser, 20).until(EC.presence_of_element_located(self.paginationSecondLast))
        last_page = self.browser.find_element(*self.paginationSecondLast)
        self.browser.execute_script("arguments[0].scrollIntoView();", last_page)
        time.sleep(1.5)
        self.browser.find_element(*self.paginationSecondLast).click()

    #@allure.step('click on last page')
    def click_last_page_button_asset(self):
        WebDriverWait(self.browser, 20).until(EC.presence_of_element_located(self.pagination_3))
        last_page = self.browser.find_element(*self.pagination_3)
        self.browser.execute_script("arguments[0].scrollIntoView();", last_page)
        time.sleep(3)
        self.browser.find_element(*self.pagination_3).click()
        time.sleep(5)

    # @allure.step('click on last page')
    def click_last_respect_last_page_button_asset(self):
        WebDriverWait(self.browser, 55).until(EC.element_to_be_clickable(self.paginationSecondLast))
        last_page = self.browser.find_element(*self.paginationSecondLast)
        self.browser.execute_script("arguments[0].scrollIntoView();", last_page)
        time.sleep(4.5)
        self.browser.find_element(*self.paginationSecondLast).click()
        time.sleep(5)


    #@allure.step('verify result text Agent and Spies is present')
    def verify_agent_spies_search(self):
        WebDriverWait(self.browser, 15).until(EC.presence_of_element_located(self.agentSpiesText))
        search_text = self.browser.find_element(*self.agentSpiesText)
        self.browser.execute_script("arguments[0].scrollIntoView();", search_text)
        time.sleep(3)
        return self.browser.find_element(*self.agentSpiesText).is_displayed()

    #@allure.step('verify result Africa-Middle-East is present')
    def verify_setting_region_africa_middle_east_search_result(self):
        WebDriverWait(self.browser, 15).until(EC.presence_of_element_located(self.settingRegionAfricaMiddleEastText))
        search_text = self.browser.find_element(*self.settingRegionAfricaMiddleEastText)
        self.browser.execute_script("arguments[0].scrollIntoView();", search_text)
        time.sleep(3)
        return self.browser.find_element(*self.settingRegionAfricaMiddleEastText).is_displayed()

    #@allure.step('verify result Medieval time is present')
    def verify_time_period_medieval_search_result(self):
        WebDriverWait(self.browser, 15).until(EC.presence_of_element_located(self.timePeriodMedievalText))
        search_text = self.browser.find_element(*self.timePeriodMedievalText)
        self.browser.execute_script("arguments[0].scrollIntoView();", search_text)
        time.sleep(3)
        return self.browser.find_element(*self.timePeriodMedievalText).is_displayed()

    #@allure.step('verify result Christmas text is present in search result')
    def verify_holiday_christmas_search_result(self):
        WebDriverWait(self.browser, 15).until(EC.presence_of_element_located(self.holidayChristmasText))
        search_text = self.browser.find_element(*self.holidayChristmasText)
        self.browser.execute_script("arguments[0].scrollIntoView();", search_text)
        time.sleep(3)
        return self.browser.find_element(*self.holidayChristmasText).is_displayed()

    #@allure.step('verify result community black african american Text is present in search result')
    def verify_community_black_search_result(self):
        WebDriverWait(self.browser, 15).until(EC.presence_of_element_located(self.communityBlackAfricanAmericanText))
        search_text = self.browser.find_element(*self.communityBlackAfricanAmericanText)
        self.browser.execute_script("arguments[0].scrollIntoView();", search_text)
        time.sleep(3)
        return self.browser.find_element(*self.communityBlackAfricanAmericanText).is_displayed()

    #@allure.step('verify result Based_On Novel Story Text is present in search result')
    def verify_based_novel_story_search_result(self):
        WebDriverWait(self.browser, 15).until(EC.presence_of_element_located(self.basedOnNovelStoryText))
        search_text = self.browser.find_element(*self.basedOnNovelStoryText)
        self.browser.execute_script("arguments[0].scrollIntoView();", search_text)
        time.sleep(3)
        return self.browser.find_element(*self.basedOnNovelStoryText).is_displayed()

    #@allure.step('verify result Based_On Novel Story Text is present in search result')
    def verify_based_real_people_search_result(self):
        WebDriverWait(self.browser, 15).until(EC.presence_of_element_located(self.basedOnRealPeopleText))
        return self.browser.find_element(*self.basedOnRealPeopleText).is_displayed()

    #@allure.step('verify result community latinx Text is present in search result')
    def verify_community_latinx_search_result(self):
        WebDriverWait(self.browser, 15).until(EC.presence_of_element_located(self.communityLatinxText))
        return self.browser.find_element(*self.communityLatinxText).is_displayed()

    #@allure.step('verify result Easter text is present in search result')
    def verify_holiday_easter_search_result(self):
        WebDriverWait(self.browser, 15).until(EC.presence_of_element_located(self.holidayEasterText))
        return self.browser.find_element(*self.holidayEasterText).is_displayed()

    #@allure.step('verify result Prehistory is present')
    def verify_time_period_prehistory_search_result(self):
        WebDriverWait(self.browser, 15).until(EC.presence_of_element_located(self.timePeriodPrehistoryText))
        return self.browser.find_element(*self.timePeriodPrehistoryText).is_displayed()

    #@allure.step('verify result Africa-Middle-East is present')
    def verify_setting_region_antarctic_search_result(self):
        WebDriverWait(self.browser, 15).until(EC.presence_of_element_located(self.settingRegionArcticAntarcticText))
        return self.browser.find_element(*self.settingRegionArcticAntarcticText).is_displayed()

    #@allure.step('verify result text Aliens is present')
    def verify_aliens_search(self):
        WebDriverWait(self.browser, 15).until(EC.presence_of_element_located(self.aliensText))
        return self.browser.find_element(*self.agentSpiesText).is_displayed()

    #@allure.step('Verify left cursior is clikable')
    def click_left_cursor_button(self):
        time.sleep(1)
        self.browser.find_element(*self.leftCursor).click()

    #@allure.step('Verify total number of movie and series')
    def verify_total_movies_series(self):
        time.sleep(2.5)
        WebDriverWait(self.browser, 55).until(EC.presence_of_element_located(self.searchResultCount))
        WebDriverWait(self.browser, 55).until(EC.presence_of_element_located(self.firstCardMovieName))
        WebDriverWait(self.browser, 55).until(EC.presence_of_element_located(self.searchResultSText))
        total_film_series = int(self.browser.find_element(*self.searchResultCount).text)
        time.sleep(2)
        return total_film_series

    #@allure.step('Verify user can apply Type-Filter and check the total numbers of movies')
    def verify_type_films_filter(self):
        self.browser.find_element(*self.filterType).click()
        time.sleep(1)
        self.browser.find_element(*self.filterTypeFilms).click()
        WebDriverWait(self.browser, 55).until(EC.presence_of_element_located(self.searchFirstMovieCard))
        # time.sleep(10)
        time.sleep(2.5)
        WebDriverWait(self.browser, 55).until(EC.presence_of_element_located(self.searchResultCount))
        WebDriverWait(self.browser, 55).until(EC.presence_of_element_located(self.firstCardMovieName))
        WebDriverWait(self.browser, 55).until(EC.presence_of_element_located(self.searchResultSText))
        try:
            only_films = int(self.browser.find_element(*self.searchResultCount).text)
            return only_films
        except:
            time.sleep(15)
            only_films = int(self.browser.find_element(*self.searchResultCount).text)
            return only_films

    #@allure.step('Verify clear-All is working in filter-section')
    def click_clear_all_filter(self):
        WebDriverWait(self.browser, 50).until(EC.presence_of_element_located(self.clearAllFilter))
        time.sleep(2.5)
        clear_button = self.browser.find_element(*self.clearAllFilter)
        time.sleep(1)
        self.browser.execute_script("arguments[0].scrollIntoView();", clear_button)
        time.sleep(2.5)
        self.browser.find_element(*self.clearAllFilter).click()
        # WebDriverWait(self.browser, 30).until(EC.presence_of_element_located(self.searchResultCount))
        # time.sleep(10)
        time.sleep(12.5)
        WebDriverWait(self.browser, 55).until(EC.presence_of_element_located(self.searchResultCount))
        WebDriverWait(self.browser, 55).until(EC.presence_of_element_located(self.firstCardMovieName))
        WebDriverWait(self.browser, 55).until(EC.presence_of_element_located(self.searchResultSText))
        clear_all_total_count = int(self.browser.find_element(*self.searchResultCount).text)
        time.sleep(1.5)
        return clear_all_total_count

    #@allure.step('Verify clear-All is clickable')
    def click_clear_cross_setting_region_africa(self):
        WebDriverWait(self.browser, 30).until(EC.presence_of_element_located(self.settingRegionAfricaCrossBtn))
        clear_button = self.browser.find_element(*self.settingRegionAfricaCrossBtn)
        time.sleep(2)
        self.browser.execute_script("arguments[0].click();", clear_button)
        time.sleep(1)

    #@allure.step('verify User can Click on Filter chips button')
    def click_filter_chips_setting_region_africa(self):
        WebDriverWait(self.browser, 30).until(EC.presence_of_element_located(self.settingRegionAfricaCrossBtn))
        clear_button = self.browser.find_element(*self.settingRegionAfricaCrossBtn)
        filter_chips_before_click = self.browser.find_element(*self.settingRegionAfricaCrossBtn).is_displayed()
        time.sleep(2)
        self.browser.execute_script("arguments[0].click();", clear_button)
        time.sleep(10)
        return filter_chips_before_click

    #@allure.step('verify Filter chips should not present after click')
    def verify_filter_chips_clickable(self):
        try:

            filter_chips_after_click = self.browser.find_element(*self.settingRegionAfricaCrossBtn)
            if filter_chips_after_click.is_displayed():
                return True
        except:
            return False

    #@allure.step('Verify user can apply Type-Filter and check the total numbers of Series')
    def verify_type_series_filter(self):
        self.browser.find_element(*self.filterType).click()
        time.sleep(1.5)
        self.browser.find_element(*self.filterTypeSeries).click()
        # WebDriverWait(self.browser, 30).until(EC.presence_of_element_located(self.searchFirstMovieCard))
        # time.sleep(10)
        time.sleep(12.5)
        WebDriverWait(self.browser, 55).until(EC.presence_of_element_located(self.searchResultCount))
        WebDriverWait(self.browser, 55).until(EC.presence_of_element_located(self.firstCardMovieName))
        WebDriverWait(self.browser, 55).until(EC.presence_of_element_located(self.searchResultSText))
        only_series = int(self.browser.find_element(*self.searchResultCount).text)
        return only_series

    #@allure.step('Verify user can apply Genre-Filter and check the total numbers of movies')
    def verify_genre_Action_filter(self):
        self.browser.find_element(*self.filterGenre).click()
        time.sleep(2)
        self.browser.find_element(*self.filterGenreAction).click()
        WebDriverWait(self.browser, 80).until(EC.presence_of_element_located(self.searchFirstMovieCard))
        self.browser.find_element(*self.applyFilterButton).click()

        # time.sleep(10)
        time.sleep(12.5)
        WebDriverWait(self.browser, 55).until(EC.presence_of_element_located(self.searchResultCount))
        WebDriverWait(self.browser, 55).until(EC.presence_of_element_located(self.firstCardMovieName))
        WebDriverWait(self.browser, 55).until(EC.presence_of_element_located(self.searchResultSText))
        action_movie_list = self.browser.find_elements(*self.movieCardActionTag)
        time.sleep(2)
        action_movies = len(action_movie_list)
        return action_movies

    #@allure.step('Verify user can apply Genre-Filter ')
    def verify_genre_Action_filter_applied(self):
        return self.browser.find_element(*self.actionGenreFilterApplied).is_displayed()

    #@allure.step('Verify user can apply Rating-Filter ')
    def verify_genre_nc_17_filter_applied(self):
        return self.browser.find_element(*self.nc_17RatingFilterApplied).is_displayed()

    #@allure.step('Verify User can Apply multiple Genre-Filter')
    def verify_genre_action_adventure_filter(self):
        self.browser.find_element(*self.filterGenre).click()
        time.sleep(2)
        self.browser.find_element(*self.filterGenreAction).click()
        self.browser.find_element(*self.filterGenreAdventure).click()
        WebDriverWait(self.browser, 80).until(EC.presence_of_element_located(self.searchFirstMovieCard))
        self.browser.find_element(*self.applyFilterButton).click()
        time.sleep(10)
        action_movies = int(self.browser.find_element(*self.searchResultCount).text)
        return action_movies

    #@allure.step('Verify user can apply Rating-Filter and check the total numbers of movies')
    def verify_rating_NC17_filter(self):
        self.browser.find_element(*self.filterRating).click()
        time.sleep(2)
        self.browser.find_element(*self.filterRatingNc_17).click()
        WebDriverWait(self.browser, 10).until(EC.presence_of_element_located(self.searchFirstMovieCard))
        self.browser.find_element(*self.applyFilterButton).click()
        time.sleep(10)
        nc_17_movies = int(self.browser.find_element(*self.searchResultCount).text)
        return nc_17_movies

    #@allure.step('Verify user can apply Rating-Filter and check the total numbers of movies')
    def verify_rating_TvMa_single_filter(self):
        self.browser.find_element(*self.filterRating).click()
        time.sleep(2)
        self.browser.find_element(*self.filterRatingTvMa).click()
        WebDriverWait(self.browser, 10).until(EC.presence_of_element_located(self.searchFirstMovieCard))
        self.browser.find_element(*self.applyFilterButton).click()
        time.sleep(10)

    #@allure.step('Verify user can apply multiple rating filter')
    def verify_rating_NC17_TvMa_multiple_filter(self):
        self.browser.find_element(*self.filterRating).click()
        time.sleep(2)
        self.browser.find_element(*self.filterRatingNc_17).click()
        time.sleep(1)
        self.browser.find_element(*self.filterRatingTvMa).click()
        WebDriverWait(self.browser, 10).until(EC.presence_of_element_located(self.searchFirstMovieCard))
        self.browser.find_element(*self.applyFilterButton).click()
        time.sleep(10)
        rating_filter_count = int(self.browser.find_element(*self.searchResultCount).text)
        return rating_filter_count

    #@allure.step('Verify user can apply Year-Filter and check the total numbers of movies')
    def verify_year_filter(self):
        self.browser.find_element(*self.filterYear).click()
        time.sleep(2)
        move = ActionChains(self.browser)
        move_element = self.browser.find_element(*self.filterYearLeftSliderButton)
        move.click_and_hold(move_element).move_by_offset(240, 0).release().perform()
        time.sleep(2.5)
        self.browser.find_element(*self.applyFilterYearButton).click()
        time.sleep(10)
        WebDriverWait(self.browser, 55).until(EC.presence_of_element_located(self.searchResultCount))
        WebDriverWait(self.browser, 55).until(EC.presence_of_element_located(self.firstCardMovieName))
        WebDriverWait(self.browser, 55).until(EC.presence_of_element_located(self.searchResultSText))
        year_filter_movies = int(self.browser.find_element(*self.searchResultCount).text)
        return year_filter_movies

    #@allure.step('Verify user can click list-button')
    def verify_list_button(self):
        # time.sleep(10)
        time.sleep(3)
        WebDriverWait(self.browser, 55).until(EC.presence_of_element_located(self.listButton))
        self.browser.find_element(*self.listButton).click()
        time.sleep(1.5)
        WebDriverWait(self.browser, 55).until(EC.presence_of_element_located(self.listTableHead))
        list_table_head = self.browser.find_element(*self.listTableHead)
        self.browser.execute_script("arguments[0].scrollIntoView();", list_table_head)
        time.sleep(1.5)
        table_head = self.browser.find_element(*self.listTableHead).is_displayed()
        return table_head

    #@allure.step('Verify list title heading is present')
    def verify_list_title(self):
        table_title = self.browser.find_element(*self.listTitle).is_displayed()
        return table_title

    #@allure.step('Verify list Directed By heading is present')
    def verify_list_directed_by(self):
        directed_by = self.browser.find_element(*self.listDirectedBy).is_displayed()
        return directed_by

    #@allure.step('Verify list Main Cast heading is present')
    def verify_list_main_cast(self):
        main_cast = self.browser.find_element(*self.listMainCast).is_displayed()
        return main_cast

    #@allure.step('Verify list Synopsis heading is present')
    def verify_list_synopsis(self):
        synopsis = self.browser.find_element(*self.listSynopsis).is_displayed()
        return synopsis

    #@allure.step('Verify user can click on Select-All')
    def verify_select_all(self):
        self.browser.find_element(*self.selectAllCheckBox).click()
        time.sleep(4)
        total_selected_footer_text = self.browser.find_element(*self.allSelectedCheckBox).text
        return total_selected_footer_text

    #@allure.step('Verify user can click on single checkbox')
    def click_first_checkbox(self):
        time.sleep(18)
        first_checkbox = self.browser.find_element(*self.firstCardCheckBox)
        self.browser.execute_script("arguments[0].click();", first_checkbox)
        time.sleep(1.5)
        total_selected_footer_text = self.browser.find_element(*self.allSelectedCheckBox).is_displayed()
        return total_selected_footer_text

    #@allure.step('Verify user can click on single checkbox')
    def click_first_checkbox_again(self):
        first_checkbox = self.browser.find_element(*self.firstCardCheckBox)
        time.sleep(1)
        self.browser.execute_script("arguments[0].scrollIntoView();", first_checkbox)
        time.sleep(2.5)
        self.browser.find_element(*self.firstCardCheckBox).click()
        time.sleep(4)
        try:
            total_selected_footer_text = self.browser.find_element(*self.allSelectedCheckBox).is_displayed()
            if total_selected_footer_text == True:
                return total_selected_footer_text
        except:
            return False

    #@allure.step('Verify footer popup should be visible visible')
    def verify_footer_popup_for_single_checkbox(self):
        total_selected_footer_text = self.browser.find_element(*self.allSelectedCheckBox).is_displayed()
        return total_selected_footer_text

    #@allure.step('Verify Footer for movies')
    def verify_Movies_and_Series_footer(self):
        download_button = self.browser.find_element(*self.footerDownloadButton).is_displayed()
        email_spread_button = self.browser.find_element(*self.footerEmailSpreadsheet).is_displayed()
        add_to_list_button = self.browser.find_element(*self.footerAddToList).is_displayed()
        return download_button, email_spread_button, add_to_list_button

    #@allure.step('Verify user can click apply Down-Sort-Filter')
    def verify_sorting_button(self):
        sort_filter = self.browser.find_element(*self.sortFilter)
        time.sleep(1)
        self.browser.execute_script("arguments[0].scrollIntoView();", sort_filter)
        time.sleep(4)
        self.browser.find_element(*self.sortFilter).click()
        time.sleep(2)

    #@allure.step('Verify user can unselect the select-All checkbox')
    def verify_deselect_all(self):
        select_all_checkbox = self.browser.find_element(*self.selectAllCheckBox)
        time.sleep(2)
        self.browser.execute_script("arguments[0].scrollIntoView();", select_all_checkbox)
        time.sleep(3)
        select_all_checkbox.click()
        time.sleep(2)
        checkbox = select_all_checkbox.is_selected()
        return checkbox

    #@allure.step('Verify user can apply Down-Sort')
    def verify_sorting_down_apply(self):
        self.browser.find_element(*self.sortDown).click()
        time.sleep(10)
        all_release_date = self.browser.find_elements(*self.releaseDateList)
        for whole_text in all_release_date:
            new_text = whole_text.text.split(" ")
            dates = new_text[1].split("-")
            year = dates[0]
            assert int(year) < 1965, 'down year sorting is  not applied'
        time.sleep(3)
        after_sort = int(self.browser.find_element(*self.searchResultCount).text)
        return after_sort

    #@allure.step('Verify Result count is present on film and series page')
    def verify_total_count_text(self):
        result_count = int(self.browser.find_element(*self.searchResultCount).text)
        return result_count

    #@allure.step('Verify poster is present in film and series page')
    def verify_first_card_poster(self):
        WebDriverWait(self.browser, 30).until(EC.presence_of_element_located(self.firstCardPoster))
        time.sleep(10)
        return self.browser.find_element(*self.firstCardPoster).is_displayed()

    #@allure.step('Verify poster title is present in  movie card')
    def verify_first_card_title(self):
        return self.browser.find_element(*self.firstCardTitle).is_displayed()

    #@allure.step('Verify Genre title is present in  movie card')
    def verify_first_card_genre(self):
        return self.browser.find_element(*self.firstCardGenre).is_displayed()

    #@allure.step('Verify user can click apply Up-Sort')
    def verify_sorting_up(self):
        self.browser.find_element(*self.sortUp).click()
        time.sleep(10)
        all_release_date = self.browser.find_elements(*self.releaseDateList)
        for whole_text in all_release_date:
            new_text = whole_text.text.split(" ")
            dates = new_text[1].split("-")
            year = dates[0]
            assert int(year) > 2018, 'Up year sorting is  not applied'
        time.sleep(3)
        after_sort = int(self.browser.find_element(*self.searchResultCount).text)
        return after_sort

    #@allure.step('Verify user can click apply A-Z')
    def verify_sorting_a_to_z(self):
        self.browser.find_element(*self.sortAtoZ).click()
        time.sleep(10)
        all_movies_name = self.browser.find_elements(*self.movieNameList)
        for whole_text in all_movies_name:
            movies_name = whole_text.text
            m = movies_name[0]
            assert (m == '0') or (m == '1') or (m == '2') or (m == '3') or (m == '4') or (m == '5') or (m == '6') or (
                    m == '7') or (m == '8') or (m == '9') or (m == 'A') or (m == 'a') or (m == 'T') or (m == 't')
        time.sleep(1.5)
        after_sort = int(self.browser.find_element(*self.searchResultCount).text)
        return after_sort

    #@allure.step('Verify user can click apply A-Z')
    def verify_sorting_z_to_a(self):
        self.browser.find_element(*self.sortZtoA).click()
        time.sleep(10)
        all_movies_name = self.browser.find_elements(*self.movieNameList)
        for whole_text in all_movies_name:
            movies_name = whole_text.text
            m = movies_name[0]
            assert (m == 'Z') or (m == 'Y') or (m == 'T') or (m == 'X') or (m == 'W') or (m == 'A')
        time.sleep(3)
        after_sort = int(self.browser.find_element(*self.searchResultCount).text)
        return after_sort


    #@allure.step('Mouse-Hover on movie card')
    def mouse_hover_on_movie(self):
        # WebDriverWait(self.browser, 80).until(EC.presence_of_element_located(self.movieNameWithAllOptions))
        time.sleep(10)
        movie_card = self.browser.find_element(*self.movieNameWithAllOptions)
        time.sleep(2)
        # print("movie Card---", movie_card)
        # print("movie Card---text", movie_card.text)
        self.browser.execute_script("arguments[0].scrollIntoView();", movie_card)
        time.sleep(2)
        view_details = self.browser.find_element(*self.movieNameWithAllOptions)
        ActionChains(self.browser).move_to_element(view_details).perform()
        time.sleep(2)

    # # @allure.step('Verify we can type in search input field')
    # def get_the_movie_name_with_all_four_options(self):
    #     global movie_card_name_with_all_four_options
    #     data = json.load(open('resources/dataFile.json', 'r'))
    #     for key, value in data.items():
    #         movie_card_name_with_all_four_options = value

    #@allure.step('Mouse-Hover on movie card')
    def mouse_hover_on_search_movie_card(self):
        # WebDriverWait(self.browser, 80).until(EC.presence_of_element_located(self.hobbitFromSearchField))
        try:
            movie_card = self.browser.find_element(*self.hobbitFirstCard)
            time.sleep(1)
            self.browser.execute_script("arguments[0].scrollIntoView();", movie_card)
            time.sleep(1)
            add_to_list = self.browser.find_element(*self.addToListFirstButton)
            ActionChains(self.browser).move_to_element(add_to_list).perform()
            time.sleep(1)
            add_to_list.click()
        except:
            movie_card = self.browser.find_element(*self.hobbitSecondCard)
            time.sleep(1)
            self.browser.execute_script("arguments[0].scrollIntoView();", movie_card)
            time.sleep(1)
            add_to_list = self.browser.find_element(*self.addToListSecondButton)
            ActionChains(self.browser).move_to_element(add_to_list).perform()
            time.sleep(1)
            add_to_list.click()


    #@allure.step('Mouse-Hover on movie card')
    def mouse_hover_on_about_fate_movie(self):
        WebDriverWait(self.browser, 60).until(EC.presence_of_element_located(self.movieAboutFate))
        candy_man = self.browser.find_element(*self.movieAboutFate)
        time.sleep(1)
        self.browser.execute_script("arguments[0].scrollIntoView();", candy_man)
        time.sleep(1.5)
        view_details = self.browser.find_element(*self.viewDetailsAboutFate)
        ActionChains(self.browser).move_to_element(view_details).perform()
        time.sleep(1)

    #@allure.step('Mouse-Hover on movie card')
    def mouse_hover_on_addams_family2(self):
        WebDriverWait(self.browser, 60).until(EC.presence_of_element_located(self.movieAddamsFamily2))
        addams_family = self.browser.find_element(*self.movieAddamsFamily2)
        time.sleep(2)
        self.browser.execute_script("arguments[0].scrollIntoView();", addams_family)
        time.sleep(2)
        view_details = self.browser.find_element(*self.viewDetailsAddamsFamily2)
        ActionChains(self.browser).move_to_element(view_details).perform()
        time.sleep(2)
        view_details.click()
        time.sleep(3)

    #@allure.step('Mouse-Hover on movie card')
    def mouse_hover_cyrano(self):
        WebDriverWait(self.browser, 60).until(EC.presence_of_element_located(self.movieCyrano))
        a_day_to_die = self.browser.find_element(*self.movieCyrano)
        time.sleep(1)
        self.browser.execute_script("arguments[0].scrollIntoView();", a_day_to_die)
        time.sleep(1.5)
        view_details = self.browser.find_element(*self.viewDetailsCyrano)
        ActionChains(self.browser).move_to_element(view_details).perform()
        time.sleep(1.5)
        view_details.click()
        time.sleep(2)

    #@allure.step('Mouse-Hover on movie card')
    def mouse_hover_on_big_shot(self):
        WebDriverWait(self.browser, 110).until(EC.presence_of_element_located(self.seriesBigShot))
        big_shot = self.browser.find_element(*self.seriesBigShot)
        time.sleep(1)
        self.browser.execute_script("arguments[0].scrollIntoView();", big_shot)
        time.sleep(1.5)
        view_details = self.browser.find_element(*self.viewDetailsBigShot)
        ActionChains(self.browser).move_to_element(view_details).perform()
        time.sleep(1)
        view_details.click()
        time.sleep(1.5)


    #@allure.step('Mouse-Hover on Add-to-List')
    def mouse_hover_on_add_to_list(self):
        time.sleep(2)
        add_to_list = self.browser.find_element(*self.addToListButton)
        ActionChains(self.browser).move_to_element(add_to_list).perform()
        time.sleep(2)
        return add_to_list.is_displayed()

    #@allure.step('Mouse-Hover on watch-now')
    def mouse_hover_on_Watch_now(self):
        time.sleep(2)
        watch_now = self.browser.find_element(*self.watchNow)
        ActionChains(self.browser).move_to_element(watch_now).perform()
        time.sleep(2)
        return watch_now.is_displayed()

    #@allure.step('Go to homepage')
    def visit_home_url(self, URL):
        time.sleep(2)
        self.browser.get(URL)
        WebDriverWait(self.browser, 300).until(EC.presence_of_element_located(self.first_carousel_title))

    #@allure.step('Mouse-Hover on watch-now')
    def click_on_watch_now_button(self):
        time.sleep(2)
        watch_now = self.browser.find_element(*self.watchNow)
        ActionChains(self.browser).move_to_element(watch_now).perform()
        time.sleep(3)
        watch_now.click()

    #@allure.step('Mouse-Hover on watch-now')
    def mouse_hover_on_watch_trailer(self):
        time.sleep(2)
        watch_trailer = self.browser.find_element(*self.watchTrailer)
        ActionChains(self.browser).move_to_element(watch_trailer).perform()
        time.sleep(2)
        return watch_trailer.is_displayed()

    #@allure.step('Mouse-Hover on view_details')
    def mouse_hover_on_view_details(self):
        time.sleep(2)
        view_details = self.browser.find_element(*self.viewDetails)
        ActionChains(self.browser).move_to_element(view_details).perform()
        time.sleep(2)
        return view_details.is_displayed()

    #@allure.step(' click on view detail on movie card')
    def click_on_view_details(self):
        time.sleep(1.5)
        WebDriverWait(self.browser, 35).until(EC.presence_of_element_located(self.viewDetails))
        view_details = self.browser.find_element(*self.viewDetails)
        time.sleep(2)
        view_details.click()
        WebDriverWait(self.browser, 75).until(EC.presence_of_element_located(self.synopsisTitle))
        movies_name = self.browser.find_element(*self.synopsisTitle).is_displayed()
        return movies_name

    #@allure.step(' click on view detail on candy-man')
    def click_on_about_fate_view_details(self):
        WebDriverWait(self.browser, 35).until(EC.presence_of_element_located(self.viewDetailsAboutFate))
        view_details = self.browser.find_element(*self.viewDetailsAboutFate)
        time.sleep(2)
        view_details.click()
        WebDriverWait(self.browser, 35).until(EC.presence_of_element_located(self.synopsisTitle))
        movies_name = self.browser.find_element(*self.synopsisTitle).is_displayed()
        return movies_name

    #@allure.step('click on watch-now button')
    def click_on_watch_trailer(self):
        time.sleep(1.5)
        WebDriverWait(self.browser, 12).until(EC.presence_of_element_located(self.watchTrailer))
        watch_trailer = self.browser.find_element(*self.watchTrailer)
        ActionChains(self.browser).move_to_element(watch_trailer).perform()
        time.sleep(2)
        watch_trailer.click()
        time.sleep(3)

    #@allure.step('click on Title button')
    def click_grid_title(self):
        WebDriverWait(self.browser, 65).until(EC.presence_of_element_located(self.grid_title))
        self.browser.find_element(*self.grid_title).click()
        try:
            time.sleep(10)
            movies_name = self.browser.find_element(*self.synopsisTitle).is_displayed()
            if movies_name:
                return True
        except:
            return self.browser.find_element(*self.titleOverviewButton).is_displayed()

    #@allure.step('click on watch-now button')
    def click_on_watch_now(self):
        time.sleep(3)
        self.browser.find_element(*self.videoPlayerCloseButton).click()
        time.sleep(2)
        watch_now = self.browser.find_element(*self.watchNow)
        ActionChains(self.browser).move_to_element(watch_now).perform()
        time.sleep(2)
        watch_now.click()
        time.sleep(5)
        movie_close_button = self.browser.find_element(*self.videoPlayerCloseButton).is_displayed()
        return movie_close_button

    #@allure.step('Mouse-Hover on Add-to-List')
    def click_on_add_to_list(self):
        time.sleep(3)
        add_to_list = self.browser.find_element(*self.addToListButton)
        ActionChains(self.browser).move_to_element(add_to_list).perform()
        time.sleep(2)
        add_to_list.click()
        time.sleep(7.5)

    #@allure.step('Mouse-Hover on Add-to-List')
    def click_on_add_to_list_about_fate_movie(self):
        time.sleep(2)
        add_to_list = self.browser.find_element(*self.addToListAboutFate)
        ActionChains(self.browser).move_to_element(add_to_list).perform()
        time.sleep(1.5)
        add_to_list.click()
        time.sleep(1)
