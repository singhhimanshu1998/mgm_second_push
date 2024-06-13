from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from appium.webdriver.webdriver import WebDriver
import allure
from pathlib import Path
import csv
import time

from selenium.webdriver import ActionChains

class videoplayer:


    PlayPause_button = (By.XPATH, "(//div//span[text()='Play/Pause'])[1]")
    VolumeMute_button = (By.XPATH, "//div//span[text()='Volume/Mute']")
    setting_button = (By.XPATH, "//div//span[text()='Settings']")
    fullscreen_button = (By.XPATH, "//div//span[text()='Fullscreen']")
    playout_popup = (By.XPATH, "//div[@class='modal-body']")
    watchnow_button = (By.XPATH, "//div[@class='btn-container']/button[text()=' Watch Now ']")
    body_element = (By.XPATH,"(//body//div[@class='bmpui-container-wrapper'])[31]")
    video_player_popup = (By.XPATH, '//div[@class="modal-content"]/mgm-video-player-popup')
    close_button = (By.XPATH, '//div[@class="modal-content"]//div/div/div/img[@class="close-btn-image"]')
    zoom_in_zoom_out_button = (By.XPATH, '(//div[@class="bmpui-container-wrapper"]//div[@class="bmpui-container-wrapper"]/button)[11]')
    resume_watching = (By.XPATH, '//div[@class="playoutButton"]/button[contains(text(),"Resume watching")]')
    play_from_beginning = (By.XPATH, '//button[contains(text(),"Play from beginning")]')
    play_pause_down = (By.XPATH, '//div[contains(@class,"bmpui-container-wrapper")]/button/span'
                                 '[contains(text(),"Volume/Mute")]/parent::button/parent::div/button/span[contains(text(),"Play/Pause")]')
    volume_mute = (By.XPATH, '//div[contains(@class,"bmpui-container-wrapper")]/button/span'
                                 '[contains(text(),"Volume/Mute")]')


    def __init__(self, browser):
        self.browser = browser
        #self.browser = WebDriver

    def ClickWatchNowButton(self):
        time.sleep(2)
        self.browser.find_element(*self.watchnow_button).click()
        time.sleep(2)

    def PlayerPopup(self):
        time.sleep(2)
        return self.browser.find_element(*self.playout_popup).is_displayed()

    def PlayPauseButton(self):
        play = self.browser.find_element(*self.PlayPause_button)
        play.location_once_scrolled_into_view
        time.sleep(2)
        global actionchains
        actionchains = ActionChains(self.browser)
        actionchains.move_to_element(play).perform()
        btn = play.is_displayed()
        return btn


    def VolumeMuteButton(self):
        play = self.browser.find_element(*self.VolumeMute_button)
        play.location_once_scrolled_into_view
        time.sleep(2)
        global actionchains
        actionchains = ActionChains(self.browser)
        actionchains.move_to_element(play).perform()
        btn = play.is_displayed()
        return btn

    def SettingButton(self):
        return self.browser.find_element(*self.setting_button).is_displayed()

    def FullscreenButton(self):
        return self.browser.find_element(*self.fullscreen_button).is_displayed()

    def zoomINButton(self):
        try:
            WebDriverWait(self.browser, 18).until(EC.presence_of_element_located(self.close_button))
            return self.browser.find_element(*self.close_button).is_displayed()
        except:
            print("close button is not working")
        # time.sleep(2)
        move = ActionChains(self.browser)
        body_ = self.browser.find_element(*self.body_element)
        move.move_to_element_with_offset(body_, 511, 65)
        move.click()
        move.perform()
        time.sleep(1.5)
        return self.browser.find_element(*self.zoom_in_zoom_out_button).is_displayed()


    def ClickCloseButton(self):
        move = ActionChains(self.browser)
        # body_ = self.browser.find_element(*self.body_element)
        # move.move_to_element_with_offset(body_, 511, 65)
        # move.click()
        # move.perform()
        close_button = self.browser.find_element(*self.close_button)
        self.browser.execute_script("arguments[0].click();", close_button)

        # self.browser.find_element(*self.close_button).click()

    def MovieAlreadyPlayed(self):
        try:
            # time.sleep(2)
            WebDriverWait(self.browser, 3).until(EC.presence_of_element_located(self.play_from_beginning))
            from_beginning = self.browser.find_element(*self.play_from_beginning)

            if from_beginning.is_displayed():
                time.sleep(1)
                from_beginning.click()
                time.sleep(7)
                print("movie alredy played")
        except:
            print("movie Starting from beginning")

    def PlayPauseDownButton(self):
        return self.browser.find_element(*self.PlayPause_button).is_displayed()

    def MuteButton(self):
        return self.browser.find_element(*self.volume_mute).is_displayed()



