import allure, time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import StaleElementReferenceException
from resources.variables import *


class ViewDetailsMoviePage:
    bannerImage = (By.XPATH, '//div[contains(@class,"header")]/div[@class="header-img"]'
                             '/img[contains(@class,"page-banner")]')
    logoImage = (By.XPATH, '//div[contains(@class,"television-logo")]/img')

    watchNowButton = (By.XPATH, '//li/button[contains(text(),"Watch now")]')
    watchTrailerButton = (By.XPATH, '//li/button[contains(text(),"Watch trailer")]')
    addToListButton = (By.XPATH, '//li//button[contains(text(),"ADD TO LIST")]')
    sellSheetButton = (By.XPATH, '//li/button[contains(text(),"Sell Sheet")]')
    titleOverViewText = (By.XPATH, '//div/p[contains(text(),"TITLE OVERVIEW")]')
    titleOverViewImage = (By.XPATH, '//div[contains(@class,"card-list")]/img')
    movieDescription = (By.XPATH, '//p[contains(@class,"synopsis-desc")]')
    movieRated = (By.XPATH, '//div[contains(@class,"main-title")]/p[text()="Rated"]')
    movieRatedName = (By.XPATH, '//div[contains(@class,"main-title")]/p[text()="Rated"]/parent::div/p[2]')
    movieGenre = (By.XPATH, '//div[contains(@class,"main-title")]/p[text()="Genre"]')
    movieGenreName = (By.XPATH, '//div[contains(@class,"main-title")]/p[text()="Genre"]/parent::div/p[2]')
    movieReleasedDate = (By.XPATH, '//div[contains(@class,"main-title")]/p[text()="Us Release Date"]')
    movieReleasedDateName = (By.XPATH, '//div[contains(@class,"main-title")]'
                                       '/p[text()="Us Release Date"]/parent::div/p[2]')
    movieDirector = (By.XPATH, '//p[contains(@class,"director-title")]')
    movieDirectorName = (By.XPATH, '//p[contains(@class,"director-title")]/parent::div/p[2]')
    movieCast = (By.XPATH, '//p[contains(@class,"cast-title")]')
    movieCastName = (By.XPATH, '//p[contains(@class,"cast-title")]/parent::div/p[2]')
    movieCopyRight = (By.XPATH, '//p[contains(@class,"copyright-desc")]')
    titleOverViewSynopsisTitle = (By.XPATH, '//div[contains(@class,"synopsis-title")]')  ###text_extract
    sellSheetCloseButton = (By.XPATH, '//div[@class="close tele-close"]/img[@class="close-btn-image"]')
    sellSheetDownloadButton = (By.XPATH, '//div[@class="movie-details"]/a/button')
    sellSheetTitleSynopsis = (By.XPATH, '//div/div[@class="preview-container"]')
    photoTitle = (By.XPATH, '//div//div/div[@class="title"]')  ####text
    sliderImage = (By.XPATH, '//div[contains(@class,"active-img")]/img')
    activeImageRightCrossButton = (By.XPATH, '//div[contains(@class,"active-img")]/parent::div//i[contains(@class,"next")]')
    sliderNextButton = (By.XPATH, '//div[contains(@class,"active-img")]/img//div[contains(@class,"active-img")]/img')
    sliderPreviousButton = (By.XPATH, '//div[contains(@class,"photos-container")]//i[contains(@class,"previous")]')
    videoPlayerCloseButton = (By.XPATH, '//div[@class="close tele-close"]/img')
    addToListPopUpAddToListButton = (By.XPATH, '//div/button/span[contains(text()," Add To List(s) ")]')
    castCrewProductionTitle = (By.XPATH, '//h1[contains(text(),"Cast, Production and Crew")]')
    viewPortFirstImage = (By.XPATH, '//ul/li[contains(@class,"photo-card")][1]')
    viewPortThirdPosition = (By.XPATH, '//ul/li[contains(@class,"photo-card")][3]')
    viewPortThirdImage = (By.XPATH, '//ul/li[contains(@class,"photo-card")][3]/img')
    rightArrowPosition = (By.XPATH, '//div[@class="navigation-arrow"]/a[contains(@class,"carousel-control-next")]')
    rightArrow = (By.XPATH, '//a[contains(@class,"carousel-control-next")]/i')
    # viewdetails=(By.XPATH,'(//h2[contains(text(),"Bond")]/ancestor::div[4]/div[@class="movies-list-container"]//button[contains(text(),"View details")])[2]')
    viewdetails = (By.XPATH,
                   '//div[@class="wel-txt"]')

    def __init__(self, browser):
        self.browser = browser

    #@allure.step('Verify movies page have Logo-Image')
    def verify_logo_image(self):
        WebDriverWait(self.browser, 46).until(EC.presence_of_element_located(self.logoImage))
        time.sleep(1.5)
        logo_image = self.browser.find_element(*self.logoImage)
        time.sleep(1)
        self.browser.execute_script("arguments[0].scrollIntoView();", logo_image)
        time.sleep(1.5)
        return self.browser.find_element(*self.logoImage).is_displayed()

    #@allure.step('Verify right cross arrow present in view port')
    def verify_view_port_right_cross_arrow(self):
        right_arrow = self.browser.find_element(*self.rightArrowPosition)
        time.sleep(.5)
        self.browser.execute_script("arguments[0].scrollIntoView();", right_arrow)
        time.sleep(1.5)
        ActionChains(self.browser).move_to_element(self.browser.find_element(*self.rightArrowPosition)).perform()
        time.sleep(1)
        return self.browser.find_element(*self.rightArrow).is_displayed()

    #@allure.step('Verify movies page have Banner-Image')
    def verify_banner_image(self):
        WebDriverWait(self.browser, 30).until(EC.presence_of_element_located(self.bannerImage))
        return self.browser.find_element(*self.bannerImage).is_displayed()

    #@allure.step('Verify Cast, Crew and Production Title should be present')
    def verify_cast_crew_production_title(self):
        return self.browser.find_element(*self.castCrewProductionTitle).is_displayed()

    #@allure.step('click on watch trailer button')
    def click_on_watch_trailer(self):
        time.sleep(2)
        self.browser.find_element(*self.watchTrailerButton).click()
        time.sleep(3)


    #@allure.step('click on close video player button')
    def click_on_close_video_player_button(self):
        self.browser.find_element(*self.videoPlayerCloseButton).click()

    #@allure.step('click on watch-now button')
    def click_on_watch_now(self):
        WebDriverWait(self.browser, 30).until(EC.presence_of_element_located(self.watchNowButton))
        self.browser.find_element(*self.watchNowButton).click()
        time.sleep(3)

    #@allure.step('click on add to list')
    def click_on_add_to_list(self):
        time.sleep(3)
        WebDriverWait(self.browser, 30).until(EC.presence_of_element_located(self.addToListButton))
        self.browser.find_element(*self.addToListButton).click()
        WebDriverWait(self.browser, 30).until(EC.presence_of_element_located(self.addToListButton))
        time.sleep(1)
        add_to_list_button = self.browser.find_element(*self.addToListPopUpAddToListButton).is_displayed()
        return add_to_list_button

    #@allure.step('Verify Watch trailer button present in movie details page')
    def verify_watch_trailer_button(self):
        return self.browser.find_element(*self.watchTrailerButton).is_displayed()

    #@allure.step('Verify Watch-Now button present in movie details page')
    def verify_watch_now_button(self):
        return self.browser.find_element(*self.watchNowButton).is_displayed()



    #@allure.step('Verify Add-To_list button present in movie details page')
    def verify_add_to_list_button(self):
        return self.browser.find_element(*self.addToListButton).is_displayed()

    #@allure.step('Verify sell-sheet button present in movie details page')
    def verify_sell_sheet_button(self):
        return self.browser.find_element(*self.sellSheetButton).is_displayed()

    #@allure.step('click on sell-sheet')
    def click_on_sell_sheet(self):
        time.sleep(3.5)
        WebDriverWait(self.browser, 30).until(EC.presence_of_element_located(self.sellSheetButton))
        self.browser.find_element(*self.sellSheetButton).click()
        WebDriverWait(self.browser, 30).until(EC.presence_of_element_located(self.sellSheetDownloadButton))
        sell_sheet = self.browser.find_element(*self.sellSheetDownloadButton).is_displayed()
        return sell_sheet

    #@allure.step('Verify sell sheet page title')
    def verify_sell_sheet_title_synopsis(self):
        return self.browser.find_element(*self.sellSheetTitleSynopsis).is_displayed()

    #@allure.step('verify download button present in sell-sheet page')
    def verify_sell_sheet_download_button(self):
        return self.browser.find_element(*self.sellSheetDownloadButton).is_displayed()

    #@allure.step('Verify close button present in sell-sheet page')
    def verify_sell_sheet_close_button(self):
        close_button = self.browser.find_element(*self.sellSheetCloseButton).is_displayed()
        time.sleep(2)
        self.browser.find_element(*self.sellSheetCloseButton).click()
        time.sleep(2)
        return close_button

    def refresh_movie(self):
        time.sleep(1)
        self.browser.refresh()
        WebDriverWait(self.browser, 180).until(EC.presence_of_element_located(self.watchNowButton))
        time.sleep(10)

    #@allure.step('verify title overview text present in movie detail page')
    def verify_title_overview_text(self):
        time.sleep(2)
        return self.browser.find_element(*self.titleOverViewText).is_displayed()

    #@allure.step('verify title overview image present in movie detail page')
    def verify_title_overview_image(self):
        time.sleep(1)
        return self.browser.find_element(*self.titleOverViewImage).is_displayed()

    #@allure.step('verify description present in movie detail page')
    def verify_movie_description(self):
        WebDriverWait(self.browser, 36).until(EC.presence_of_element_located(self.movieDescription))
        time.sleep(5)
        return self.browser.find_element(*self.movieDescription).is_displayed()

    #@allure.step('Verify movie Rated present in movie details page')
    def verify_movie_rated(self):
        return self.browser.find_element(*self.movieRated).is_displayed()

    #@allure.step('Verify movie Rated present in movie details page')
    def verify_movie_rated_name(self):
        return self.browser.find_element(*self.movieRatedName).is_displayed()

    #@allure.step('Verify movie Cast present in movie details page')
    def verify_movie_cast(self):
        return self.browser.find_element(*self.movieCast).is_displayed()

    #@allure.step('Verify movie Cast present in movie details page')
    def verify_movie_cast_name(self):
        return self.browser.find_element(*self.movieCastName).is_displayed()

    #@allure.step('Verify movie Genre present in movie details page')
    def verify_movie_genre(self):
        return self.browser.find_element(*self.movieGenre).is_displayed()

    #@allure.step('Verify movie Genre present in movie details page')
    def verify_movie_genre_name(self):
        return self.browser.find_element(*self.movieGenreName).is_displayed()

    #@allure.step('Verify movie Director present in movie details page')
    def verify_movie_director(self):
        return self.browser.find_element(*self.movieDirector).is_displayed()

    #@allure.step('Verify movie Director present in movie details page')
    def verify_movie_director_name(self):
        return self.browser.find_element(*self.movieDirectorName).is_displayed()

    #@allure.step('Verify movie Release Date present in movie details page')
    def verify_movie_release_date(self):
        return self.browser.find_element(*self.movieReleasedDate).is_displayed()

    #@allure.step('Verify movie Release Date present in movie details page')
    def verify_movie_release_date_name(self):
        return self.browser.find_element(*self.movieReleasedDateName).is_displayed()

    #@allure.step('Verify movie Copyright present in movie details page')
    def verify_movie_copyright(self):
        return self.browser.find_element(*self.movieCopyRight).is_displayed()

    #@allure.step('verify synopsis title present in movie detail page')  ####text
    def verify_synopsis_title(self):
        synopsis_title = self.browser.find_element(*self.titleOverViewSynopsisTitle).text
        time.sleep(2)
        return synopsis_title

    #@allure.step('verify photo title present in movie detail page')
    def verify_photo_title(self):
        WebDriverWait(self.browser, 26).until(EC.presence_of_element_located(self.photoTitle))
        time.sleep(1.5)
        photo_title = self.browser.find_element(*self.photoTitle).is_displayed()
        time.sleep(.5)
        return photo_title

    #@allure.step('verify View-Port present in movie detail page')
    def verify_view_port_first_image(self):
        right_arrow = self.browser.find_element(*self.viewPortFirstImage)
        time.sleep(1)
        self.browser.execute_script("arguments[0].scrollIntoView();", right_arrow)
        time.sleep(1.5)
        photo_title = self.browser.find_element(*self.viewPortFirstImage).is_displayed()
        time.sleep(.5)
        return photo_title

    #@allure.step('verify slider image present in view details page')
    def verify_slider_image(self):
        image = self.browser.find_element(*self.sliderImage)
        time.sleep(.5)
        self.browser.execute_script("arguments[0].scrollIntoView();", image)
        time.sleep(1.5)
        return self.browser.find_element(*self.sliderImage).is_displayed()

    #@allure.step('verify left arrow navigation ')
    def verify_slider_left_arrow(self):
        return self.browser.find_element(*self.sliderPreviousButton).is_displayed()

    #@allure.step('verify right arrow navigation ')
    def verify_slider_right_arrow(self):
        return self.browser.find_element(*self.sliderNextButton).is_displayed()

    #@allure.step('click right arrow navigation ')
    def click_slider_right_arrow(self):
        self.browser.find_element(*self.sliderNextButton).click()

    #@allure.step('Verify Add to List tab in footer popup')
    def verify_active_image_right_cross_button(self):
        time.sleep(1)
        first_image_text = self.browser.find_element(*self.sliderImage).get_attribute('src')
        time.sleep(.5)
        self.browser.find_element(*self.activeImageRightCrossButton).click()
        time.sleep(4)
        second_image_text = self.browser.find_element(*self.sliderImage).get_attribute('src')
        time.sleep(1)
        try:
            if first_image_text != second_image_text:
                return True
        except:
            return False

    #@allure.step('Verify Add to List tab in footer popup')
    def verify_view_port_clickable(self):
        time.sleep(1)
        view_port_image = self.browser.find_element(*self.viewPortThirdImage).get_attribute('src')
        time.sleep(1)
        new_text = view_port_image.split('/')
        position_text = new_text[9]
        self.browser.find_element(*self.viewPortThirdPosition).click()
        time.sleep(4)
        second_image_text = self.browser.find_element(*self.sliderImage).get_attribute('s rc')
        time.sleep(1)
        new_active_text = second_image_text.split('/')
        active_text = new_active_text[9]
        try:
            if position_text == active_text:
                return True
        except:
            return False


    def verify_view_details_button(self):
        WebDriverWait(self.browser, 36).until(EC.presence_of_element_located(self.viewdetails))
        time.sleep(5)
        return self.browser.find_element(*self.viewdetails).is_displayed()








