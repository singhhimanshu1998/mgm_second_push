import allure, time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import StaleElementReferenceException
from resources.variables import *


class ViewDetailsSeriesPage:
    bannerImage = (By.XPATH, '//div[contains(@class,"header")]/div[@class="header-img"]')
    titleText = (By.XPATH, '//div/p[text() = "TITLE OVERVIEW"]')
    addToListButton = (By.XPATH, '//li[@class="addList"]//button')
    titleOverViewButton = (By.XPATH, '//div[contains(@class,"sub-menu-synopsis")]/p[contains(text(),"TITLE OVERVIEW")]')
    episodeButton = (By.XPATH, '//div[contains(@class,"episode")]/p')
    titleOverImage = (By.XPATH, '//div[@class="card-list"]/img')
    movieCast = (By.XPATH, '//p[contains(@class,"cast-title")]')
    seasonDropDownArrow = (By.XPATH, '//div[contains(@class,"dropdown-list-btn")]/span/i')
    seasonButton = (By.XPATH, '//div[contains(@class,"dropdown-list-btn")]/div')
    selectSeasonText = (By.XPATH, '//div[contains(@class,"dropdown-list-container")]'
                                  '/div[contains(text(),"SELECT SEASON")]')
    SeasonOneText = (By.XPATH, '//div[contains(@class,"dropdown-list-container")]'
                               '/div[contains(text(),"SEASON 1")]')
    episodeCards = (By.XPATH, '//div[contains(@class,"episode-card")]//div[@class="card"]')
    firstEpisodeCard = (By.XPATH, '//div[contains(@class,"episode-card")]/div[1]/div[@class="card"]')
    firstCardImage = (By.XPATH, '//div[contains(@class,"episode-card")]/div[1]/div[@class="card"]//img')
    firstCardEpisodeText = (By.XPATH, '//div[contains(@class,"episode-card")]/div[1]/div[@class="card"]'
                                      '//div[contains(text() ,"EPISODE 1")]')
    firstCardEpisodeName = (By.XPATH, '//div[contains(@class,"episode-card")]/div[1]/div[@class="card"]'
                                      '//div[contains(text() ,"First Impressions Are Everything")]')
    firstCardSynopsis = (By.XPATH, '//div[contains(@class,"episode-card")]/div[1]/div[@class="card"]'
                                   '//div[contains(@class,"synopsis")]')
    backToEpisodeButton = (By.XPATH, '//span[contains(text(),"BACK TO EPISODES")]')
    episodeSynopsis = (By.XPATH, '//p[contains(@class,"synopsis-desc")]')
    episodeImage = (By.XPATH, '//div[contains(@class,"card-list")]/img')
    episodePlayButton = (By.XPATH, '//div[contains(@class,"card-list")]/i')






    def __init__(self, browser):
        self.browser = browser

    #@allure.step('Verify Banner image in Series page')
    def verify_banner_image(self):
        time.sleep(18)
        WebDriverWait(self.browser, 160).until(EC.presence_of_element_located(self.bannerImage)) # 90 sec is not working
        return self.browser.find_element(*self.bannerImage).is_displayed()

    #@allure.step('Verify Title Text in Series page')
    def verify_title_text(self):
        return self.browser.find_element(*self.titleText).is_displayed()

    #@allure.step('Verify user can click on Title Text in Series page')
    def click_title_text(self):
        self.browser.find_element(*self.titleText).click()
        WebDriverWait(self.browser, 26).until(EC.presence_of_element_located(self.movieCast))
        time.sleep(1.5)
        return self.browser.find_element(*self.movieCast).is_displayed()

    #@allure.step('Verify season dropdown arrow present in Series page')
    def verify_season_dropdown(self):
        return self.browser.find_element(*self.seasonDropDownArrow).is_displayed()

    #@allure.step('Verify season dropdown arrow present in Series page')
    def verify_season_episode_button(self):
        return self.browser.find_element(*self.episodeButton).is_displayed()

    #@allure.step('Verify user can click on season button in Series page')
    def click_title_season_button(self):
        # time.sleep(2)
        WebDriverWait(self.browser, 26).until(EC.element_to_be_clickable(self.seasonButton))
        season_button = self.browser.find_element(*self.seasonButton)
        self.browser.execute_script("arguments[0].click();", season_button)

    #@allure.step('Verify season dropdown arrow present in Series page')
    def verify_select_season_text(self):
        time.sleep(2)
        return self.browser.find_element(*self.selectSeasonText).is_displayed()

    #@allure.step('Verify season dropdown arrow present in Series page')
    def click_select_season_text(self):
        time.sleep(2)
        self.browser.find_element(*self.selectSeasonText).click()

    #@allure.step('Verify season dropdown arrow present in Series page')
    def verify_season_season_one(self):
        return self.browser.find_element(*self.SeasonOneText).is_displayed()

    #@allure.step('Verify synopsis in Series page')
    def verify_all_synopsis_level(self):
        WebDriverWait(self.browser, 26).until(EC.presence_of_element_located(self.episodeSynopsis))
        time.sleep(2)
        series_level = self.browser.find_element(*self.episodeSynopsis).text


    #@allure.step('Verify user can click on any season in Series page')
    def click_on_season_one(self):
        # self.browser.find_element(*self.SeasonOneText).click()
        season_one_text = self.browser.find_element(*self.SeasonOneText)
        self.browser.execute_script("arguments[0].click();", season_one_text)
        time.sleep(2.5)
        WebDriverWait(self.browser, 26).until(EC.presence_of_element_located(self.episodeButton))
        return self.browser.find_element(*self.episodeButton).is_displayed()

    #@allure.step('Verify Episode tab is present in Series page')
    def verify_episode_tab(self):
        try:
            WebDriverWait(self.browser, 16).until(EC.presence_of_element_located(self.episodeCards))
            return self.browser.find_element(*self.episodeCards).is_displayed()
        except:
            episode_button = self.browser.find_element(*self.episodeButton)
            self.browser.execute_script("arguments[0].click();", episode_button)
            WebDriverWait(self.browser, 36).until(EC.presence_of_element_located(self.episodeCards))
            return self.browser.find_element(*self.episodeCards).is_displayed()


    #@allure.step('Verify Image present in Series card')
    def verify_first_card_image_tab(self):
        time.sleep(1)
        return self.browser.find_element(*self.firstCardImage).is_displayed()

    #@allure.step('Verify Episode Number present in Series card')
    def verify_first_card_episode_number(self):
        time.sleep(1)
        return self.browser.find_element(*self.firstCardEpisodeText).is_displayed()

    #@allure.step('Verify Episode Name present in Series card')
    def verify_first_card_episode_name(self):
        time.sleep(1)
        return self.browser.find_element(*self.firstCardEpisodeName).is_displayed()

    #@allure.step('Verify Episode Name present in Series card')
    def verify_first_card_description(self):
        time.sleep(1)
        return self.browser.find_element(*self.firstCardSynopsis).is_displayed()

    #@allure.step('Verify Episode cards are clickable in Series page')
    def click_first_episode_card(self):
        self.browser.find_element(*self.firstEpisodeCard).click()
        WebDriverWait(self.browser, 26).until(EC.presence_of_element_located(self.backToEpisodeButton))
        time.sleep(2)
        return self.browser.find_element(*self.backToEpisodeButton).is_displayed()

    #@allure.step('Verify back_to_episode button ')
    def verify_back_to_episode_button(self):
        return self.browser.find_element(*self.backToEpisodeButton).is_displayed()

    #@allure.step('click on back_to_episode button ')
    def click_back_to_episode_button(self):
        time.sleep(4)
        self.browser.find_element(*self.backToEpisodeButton).click()
        WebDriverWait(self.browser, 26).until(EC.presence_of_element_located(self.episodeCards))
        time.sleep(2)
        return self.browser.find_element(*self.episodeCards).is_displayed()

    #@allure.step('Verify Synopsis Description present in Episode page ')
    def verify_episode_page_synopsis(self):
        return self.browser.find_element(*self.episodeSynopsis).is_displayed()

    #@allure.step('Verify Episode image present in Episode page ')
    def verify_episode_page_image(self):
        return self.browser.find_element(*self.episodeImage).is_displayed()

    #@allure.step('Verify play button present in Episode page ')
    def verify_episode_play_button(self):
        return self.browser.find_element(*self.episodePlayButton).is_displayed()

    #@allure.step('Click play button present in Episode page ')
    def click_episode_play_button(self):
        self.browser.find_element(*self.episodePlayButton).click()