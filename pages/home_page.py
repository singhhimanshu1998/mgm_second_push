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


class homePageObj:
    right_navigation_view = (By.XPATH, "//h2[text()='Action']/ancestor::div[3]/following-sibling::div//a")
    second_right_navigation_view = (By.XPATH, "//h2[text()='Action']/ancestor::div[3]/following-sibling::div//a[2]")
    right_navigation = (
    By.XPATH, "//h2[text()='Action']/ancestor::div[3]/following-sibling::div//a/i[@class='next-icon icon']")
    recently_movie_card = (
    By.XPATH, '//h2[text()="Recently Watched"]/ancestor::div[4]//div[@class="movie-poster"]/div[@class="movie"]')
    left_navigation = (By.XPATH, "//h2[text()='Action']/ancestor::div[3]/following-sibling::div//a[1]")
    left_navigation_view = (
    By.XPATH, "//h2[text()='Action']/ancestor::div[3]/following-sibling::div//a/i[@class='previous-icon icon']")
    recently_watched = (By.XPATH, "//h2[contains(text(),'Recently Watched')]")
    recently_watch_next_navigation = (
    By.XPATH, "//h2[text()='Recently Watched']/ancestor::div[3]/following-sibling::div//a//i")
    tv_unscripted = (By.XPATH, "//h2[contains(text(),'TV Unscripted')]")
    # title_text = (By.XPATH, "//div[@class='movie-detail']/p[1]")
    title_text = (By.XPATH, "//h2[contains(text(),'Recently Watched')]/ancestor::div["
                            "3]/following-sibling::div//ul/li[1]//mgm-movie-poster[1]//div[1]//div[1]//div[3]//p[1]")
    recently_watched_first_poster = (By.XPATH, "//h2[contains(text(),'Recently Watched')]/ancestor::div[3]"
                                               "/following-sibling::div//ul/li[1]//mgm-movie-poster[1]//div[1]//div[1]/div[@class='movie']")
    tv_title_text = (By.XPATH, "//h2[contains(text(),'TV Unscripted')]/ancestor::div["
                               "3]/following-sibling::div//ul/li[1]//mgm-movie-poster[1]//div[1]//div[1]//div[3]//p[1]")
    play_nextMoviname = (By.XPATH, "//h2[contains(text(),'Action')]/parent::div/parent::div/parent::div"
                                   "/following-sibling::div//ul/li[1]//div[@class='desk-on']//div[3]/p[1]")
    # movie_cards = (By.XPATH, "//div[@class='home']/mgm-block-picker[2]/mgm-movies-block[1]/div[1]["
    #                          "@class='movies-block-container dark_background']")
    movie_cards = (By.XPATH, "//div[@class='home']/mgm-block-picker[2]/mgm-movies-block[1]//div["
                             "@class='movie-poster']//div[@class='movie-poster-alias']/img")
    recent_watchedScroll = (By.XPATH, "//div[@class='card-section']/ng-scrollbar/div[1]/div["
                                      "1]/following-sibling::scrollbar-x[1]")
    header_logo = (By.XPATH, "//a[@class='logo-img ng-star-inserted']/img[@alt='logo-img']")
    # next_arrow = (By.XPATH, "//mgm-block-picker[2]/mgm-movies-block[1]/div[1]/div[2]/mgm-navigation-arrows[1]/div["
    #                         "1]/a[1]/i[1]")
    next_arrow = (By.XPATH, "//h2[text()='Recently Watched']/ancestor::div[3]/following-sibling::div//a")
    tv_next_arrow = (By.XPATH, "//h2[text()='TV Unscripted']/ancestor::div[3]/following-sibling::div//a")
    click_next_arrow = (By.XPATH, "//h2[text()='Recently Watched']/ancestor::div[3]/following-sibling::div//a//i")
    prev_arrow = (By.XPATH, "//div[@class='navigation-arrow']/a")
    action_adventure = (By.XPATH, "//h2[contains(text(),'Action')]")
    # watch_movie = (By.XPATH, "//h2[contains(text(),'Action')]/ancestor::div[3]/following-sibling::div//ul/li[3]//button[contains(text(),'Watch movie')]")
    # watch_movie = (By.XPATH, "//h2[contains(text(),'Action')]/parent::div/parent::div/parent::div"
    #                          "/following-sibling::div//ul[@class='movies-list d-flex ng-star-inserted active']/li["
    #                          "2]//button[contains(text(),'Watch movie')]")
    watchmovie_moviecard = (
    By.XPATH, "(//h2[contains(text(),'Action')]/ancestor::div/following-sibling::div[1]//li//button[contains(text("
              "),'Watch now')])[1]")
    watchmovie_name = (By.XPATH,
                       "//h2[contains(text(),'Action')]/ancestor::div[3]/following-sibling::div//ul/li[1]//div[@class='movie-poster']//div[3]/p[1]")
    body_element = (By.XPATH, "(//body//div[@class='bmpui-container-wrapper'])[31]")
    close_button = (By.XPATH, "//div[@class='modal-content']//div/div/div/img[@class='close-btn-image']")
    play_begining = (By.XPATH, "//button[@class='watch-again-btn btn-view']")
    # poster_image = (By.XPATH, "//div//img[@class='image-loaded']")
    poster_image = (By.XPATH, "//div[@class='movies-block-container dark_background']//ul[@class='movies-list d-flex "
                              "active']//li[1]//mgm-movie-poster[1]//div[1]//div[1]//div[1]//div[1]")
    movie_generes = (By.XPATH,
                     "//ul[@class='movies-list d-flex z-test active']//li[1]//mgm-movie-poster[1]//div[1]//div[1]//div[3]//span[2]")
    cardhover_option1 = (By.XPATH,
                         "(//h2[contains(text(),'Recently Watched')]/ancestor::div[3]/following-sibling::div[1]//li//button[contains(text(),'ADD TO LIST')])[1]")
    cardhover_option2 = (By.XPATH,
                         "//h2[contains(text(),'Recently Watched')]/ancestor::div[3]/following-sibling::div[1]//li//button[contains(text(),'Watch now')][1]")
    cardhover_option3 = (By.XPATH,
                         "(//h2[contains(text(),'Recently Watched')]/ancestor::div[3]/following-sibling::div[1]//li//button[contains(text(),'Watch trailer')])[1]")
    cardhover_option4 = (By.XPATH,
                         "(//h2[contains(text(),'Recently Watched')]/ancestor::div[3]/following-sibling::div[1]//li//button[contains(text(),'View details')])[1]")
    alert = (By.XPATH, "//div[@class='createNewList']")
    watch_popup = (By.XPATH, "//div[@id='bitmovin-player']")
    mgm_img = (By.XPATH, "//a[@class='logo-img']//img")
    movie_added = (By.XPATH, "//h2[contains(text(),'Oscar-winning "
                             "Films')]/parent::div/parent::div/parent::div/following-sibling::div//ul["
                             "@class='movies-list d-flex active']/li[1]//button[contains(text(),'ADD TO LIST')]")
    # myList_seeall = (By.XPATH, "//a[contains(text(),'SEE ALL')]")
    zoom_in_zoom_out_button = (
    By.XPATH, '(//div[@class="bmpui-container-wrapper"]//div[@class="bmpui-container-wrapper"]/button)[11]')
    myList_seeall = (By.XPATH, "//a[contains(text(),'SEE LISTS')]")
    automation_mylist = (By.XPATH, "//a[contains(text(),'" + automation_listt + "')]")
    # delete_btn = (By.XPATH, "//button[contains(text(),'DELETE')]")
    delete_btn = (By.XPATH, "//span[contains(text(),'DELETE')]")
    # delete_btn_footer = (By.XPATH, "//button[contains(text(),'DELETE')]")
    delete_btn_footer = (By.XPATH, "//button/span[contains(text(),'DELETE')]")
    mylist_tab = (By.XPATH, "//ul[@class='menu-items']//a[@id='My Lists']")
    autoRand_list = (By.XPATH, "//a[contains(text(),'" + new_List_name + "')]")
    delete_permission = (By.XPATH, "//button[@class='cui-btn cui-btn-primary ng-star-inserted']")
    # footer
    privacy_policy = (By.XPATH, "//div//ul/li/a[contains(text(),'Privacy Notice')]")
    terms_use = (By.XPATH, "//a[contains(text(),'Terms of use')]")
    footer_logo = (By.XPATH, "//a[@class='footer-logo']/img[@class='d-none d-md-inline']")
    support = (By.XPATH, '//a[contains(@class,"support-link")]')
    address = (By.XPATH, "//span[contains(@class,'contact-address')]")
    legal = (By.XPATH, "//h6[contains(text(), 'Legal')]")
    contact_us = (By.XPATH, "//h6[contains(text(),'contact us')]")
    connect = (By.XPATH, "//h6[contains(text(),'connect')]")
    youtube_icon = (By.XPATH, "//div[@class='inner-container']//i[@class='YouTube icon']")
    fb_icon = (By.XPATH, "//div[@class='inner-container']//i[@class='FaceBook icon']")
    twitter_icon = (By.XPATH, "//div[@class='inner-container']//i[@class='Twitter icon']")
    insta_icon = (By.XPATH, "//div[@class='inner-container']//i[@class='Instagram icon']")
    copyright = (By.XPATH, "//div[@class='col-md-12 copy-right']//p[1]")
    title_overview = (By.XPATH, "//p[contains(text(),'TITLE OVERVIEW')]")
    synopsis_title_text = (By.XPATH, "//div[contains(@class,'synopsis-title')]")
    delete_success_msg = (By.XPATH, "//div/h3[contains(text(),'Delete Title ')]")  # div ad
    list_action_slider = (
    By.XPATH, '//h2[text()="Action"]/ancestor::div[3]/following-sibling::div//div[@class="ng-scrollbar-track"]')
    list_see_all = (By.XPATH, '//h2[text()="Action"]/ancestor::div[3]//div/a[@class="see-all-text"]')
    list_action_title = (By.XPATH, '//div[contains(@class,"list-name")]/div')
    my_list=(By.XPATH,'(//a[@id="My Lists"])[1]')
    share_mgm=(By.XPATH,'//p[text()="Shared by MGM"]')
    list_p=(By.XPATH,'//h2[text()="Lists"]')
    poster_img=(By.XPATH,'//div[@class="col-12 text-left no-title"]')
    privacy_notice =(By.XPATH,'//a[text()="Privacy Notice"]')
    him_list=(By.XPATH,'//a[text()="him"]')
    him_title=(By.XPATH,'(//div[@class="movies-list-container"])[1]')
    poster_button=(By.XPATH,"(//button[text()='View details'])[1]")
    poster_title=(By.XPATH,"//div[text()=' How It Ends ']")
    him_checkbox=(By.XPATH,"//h2[text()='Lists']/parent::div//input[@type='checkbox']")
    select_item=(By.XPATH,"//span[text()= 'DOWNLOAD .XLSX' ]")
    films_footer=(By.XPATH,'(//a[contains(text(),"Films & Series")])[1]')
    film_title=(By.XPATH,"//h2[contains(text(),'Our Titles')]")
    add_list=(By.XPATH,"//button[text()='ADD TO LIST']")
    my_lists=(By.XPATH,"//i[contains(text(),'list')]/parent::a")
    your_list=(By.XPATH,"//p[text()='Your Lists']")
    movies_list=(By.XPATH,"//a[text()='MoviesList']")
    title_movies=(By.XPATH,"//div[@id='top-title']")
    list_grid=(By.XPATH,'//div[contains(@class,"presentation")]')
    grid_button=(By.XPATH,"(//p[contains(text(),' The Addams Family (2019) ')])[1]")
    grid_view=(By.XPATH,'//div[contains(@class,"list-icon")]')
    grid_text=(By.XPATH,"//div[text()='Synopsis']")
    assets_button=(By.XPATH,'//li[contains(@class,"menu menu-label")]/a[@id="Assets"]')
    assets_popup=(By.XPATH,'//div[text()=" Welcome to ROAR "]')
    assets_checkbox1=(By.XPATH,'(//div[@class="roar-sub-header"]//input[@type="checkbox"])[1]')
    assets_checkbox2 = (By.XPATH, '(//div[@class="roar-sub-header"]//input[@type="checkbox"])[2]')
    assets_checkbox3 = (By.XPATH, '(//div[@class="roar-sub-header"]//input[@type="checkbox"])[3]')
    continue_button=(By.XPATH,'//button[text()="CONTINUE"]')
    banner_poster=(By.XPATH,"//h2[text()='Our Titles']")
    value_text=(By.XPATH,'//input[@placeholder="Search Movie or TV Titles"]')
    search_icon=(By.XPATH,'//div[@class="search-icon"]//i[@class="fa-search"]')
    movie_poster=(By.XPATH,'//div[@class="desk-on"]//p[text()=" Gladiators Australia - 2024 (series) "]')
    filter_text=(By.XPATH,"//div[text()=' type ']")
    film_filter=(By.XPATH,'(//i[text()=" radio_button_unchecked " ])[1]')
    after_filter=(By.XPATH,"//span[text()='Films']")
    my_cart=(By.XPATH,'//ul[@class="menu-items"]//a[text()="My Carts"]')
    your_cart=(By.XPATH,'//p[text()="Your Carts"]')
    him_cart=(By.XPATH,"//a[text()='himCart']")
    poster_click=(By.XPATH,"//div[@class='poster']/img[@alt='Poster image for Alive']")
    movie_name=(By.XPATH,'//div[text()=" Alive "]')
    all_assets=(By.XPATH,'//p[text()="ALL ASSETS"]')
    add_to_cart=(By.XPATH,'//div[contains(@class,"movie-poster")][2]//button[text()="Add to cart"]')
    card_verify=(By.XPATH,'//span[text()=" himCart "]')
    movies_text=(By.XPATH,'//div[text()="ALIVE Content Package Deck.pdf "]')
    my_cart_input=(By.XPATH,'//input[@placeholder="My New Cart Name"]')
    create_cart=(By.XPATH,"//i[text()='keyboard_arrow_right']")
    verify_cart=(By.XPATH,"//a[text()='pythonCart']")
    add_cart_popup=(By.XPATH,'//span[text()=" pythonCart "]')
    add_button=(By.XPATH,'//span[text()=" Add To Cart(s) "]')
    cart_text=(By.XPATH,'//a[text()="pythonCart"]/following-sibling::span[text()=" (1 Asset)"]')
    delete_button=(By.XPATH,'//a[contains(text(),"pythonCart")]//parent::div//following-sibling::div//span[text()="Delete"]')
    delete_cart=(By.XPATH,"//button[text()=' Delete Cart ']")
    delete_popup=(By.XPATH,'//h3[text()="Delete Cart "]')
    mgm_admin=(By.LINK_TEXT,"MGM+ Screeners Admin")
    mgm_text=(By.XPATH,"//span[text()='MGM+ Screeners Admin']")
    mgm_roar_img=(By.XPATH,"//button[contains(@class,'dropdown-toggle btn')]")
    delete_cart_cross_button = (By.XPATH,'//div[@class="modal-content"]//div[@class="close-x desk-close"]/img[@src="assets/images/icons/black-close.png"]')
    search_bar=(By.XPATH,'//input[@placeholder="Search Users"]')
    search_value=(By.XPATH,'(//tbody/tr[@class="table-container"]//td[@class="nameColWidth paddingLeft0Px click-info"]/div[text()=" tara "])[1]')
    search_icon_btn=(By.XPATH,'//input[@placeholder="Search Users"]/parent::div//button[@type="submit"]')
    invite_button=(By.XPATH,'//div[text()="INVITES"]')
    invite_tag_name=(By.XPATH,'//th[text()="Name/Email/Company"]')


    def __init__(self, browser):
        self.browser = browser

    #@allure.step('Verify Recently watched Heading is displayed ')
    def verify_recentlywatched(self):
        WebDriverWait(self.browser, 50).until(EC.presence_of_element_located(self.recently_watched))
        recently = self.browser.find_element(*self.recently_watched)
        self.browser.execute_script("arguments[0].scrollIntoView();", recently)
        return self.browser.find_element(*self.recently_watched).text
    def verify_poster_img(self):
        WebDriverWait(self.browser, 60).until(EC.presence_of_element_located(self.privacy_notice))
        recently = self.browser.find_element(*self.privacy_notice)
        self.browser.execute_script("arguments[0].scrollIntoView();", recently)
        time.sleep(10)
        WebDriverWait(self.browser,60).until(EC.presence_of_element_located(self.poster_img))
        return self.browser.find_element(*self.poster_img).is_displayed()

    def verify_list_checkbox(self):
        WebDriverWait(self.browser, 50).until(EC.presence_of_element_located(self.him_checkbox))
        self.browser.find_element(*self.him_checkbox).click()
        return self.browser.find_element(*self.select_item).is_displayed()

    def verify_film_series(self):
        WebDriverWait(self.browser, 50).until(EC.presence_of_element_located(self.films_footer))
        self.browser.find_element(*self.films_footer).click()
        return self.browser.find_element(*self.film_title).is_displayed()


    def verify_list_button(self):
        self.browser.find_element(*self.my_list).click()
        time.sleep(5)
        WebDriverWait(self.browser, 50).until(EC.presence_of_element_located(self.list_p))
        return self.browser.find_element(*self.list_p).is_displayed()


    def verify_him_button(self):
        self.browser.find_element(*self.him_list).click()
        time.sleep(10)
        WebDriverWait(self.browser,50).until(EC.presence_of_element_located(self.him_title))
        recently = self.browser.find_element(*self.him_title)
        self.browser.execute_script("arguments[0].scrollIntoView();", recently)
        return self.browser.find_element(*self.him_title).is_displayed()



    def verify_poster_view(self):
        self.browser.find_element(*self.poster_button).click()
        # time.sleep(10)
        WebDriverWait(self.browser, 50).until(EC.presence_of_element_located(self.poster_button))
        recently = self.browser.find_element(*self.poster_title)
        self.browser.execute_script("arguments[0].scrollIntoView();", recently)
        return self.browser.find_element(*self.poster_title).is_displayed()


    #@allure.step('Verify Title text of movie in recently watched ')
    def verify_titleText(self):
        WebDriverWait(self.browser, 30).until(EC.presence_of_element_located(self.title_text))
        first = self.browser.find_element(*self.title_text)  # Title 1
        time.sleep(1)
        ActionChains(self.browser).move_to_element(first).perform()
        time.sleep(1.5)
        return first.is_displayed

    #@allure.step('Verify Title text of movie in recently watched ')
    def verify_recently_watch_first_poster(self):
        WebDriverWait(self.browser, 20).until(EC.presence_of_element_located(self.recently_watched_first_poster))
        # time.sleep(2)
        first = self.browser.find_element(*self.recently_watched_first_poster)
        time.sleep(1)
        ActionChains(self.browser).move_to_element(first).perform()
        time.sleep(1.5)
        return first.is_displayed()

    #@allure.step('Verify Title text of tv section')
    def verify_tv_titleText(self):
        WebDriverWait(self.browser, 20).until(EC.presence_of_element_located(self.tv_title_text))
        first = self.browser.find_element(*self.tv_title_text)  # Title 1
        ##print(first.text)
        ActionChains(self.browser).move_to_element(first).perform()
        time.sleep(2)
        return first.is_displayed()

    #@allure.step('Verify movie cards in recently watched ')
    def verify_moviecards(self):
        # return self.browser.find_element(*self.movie_cards).get_attribute("hover-class")
        return self.browser.find_element(*self.poster_image).is_displayed()

    #@allure.step('Verify horizontal watched scroll in recently watched ')
    def verify_scroll(self):
        scroll = self.browser.find_elements(*self.recent_watchedScroll)
        return scroll[1].is_displayed()

    #@allure.step('Go back to homepage')
    def Refresh_ClickLogo(self):
        time.sleep(2)
        self.browser.refresh()
        time.sleep(10)
        self.browser.find_element(*self.header_logo).click()
        time.sleep(10)

    #@allure.step('Verify Right navigation arrow is displayed in recently watched')
    def verify_rightarrow(self):
        WebDriverWait(self.browser, 30).until(EC.presence_of_element_located(self.recently_watched))
        recently = self.browser.find_element(*self.recently_watched)
        self.browser.execute_script("arguments[0].scrollIntoView();", recently)
        right_nav = self.browser.find_element(*self.next_arrow)
        time.sleep(1.5)
        ActionChains(self.browser).move_to_element(right_nav).perform()
        return right_nav.is_displayed()

    #@allure.step('Verify Right navigation arrow is displayed in recently watched')
    def verify_tv_rightarrow(self):
        WebDriverWait(self.browser, 50).until(EC.presence_of_element_located(self.tv_unscripted))
        recently = self.browser.find_element(*self.tv_unscripted)
        self.browser.execute_script("arguments[0].scrollIntoView();", recently)
        right_nav = self.browser.find_element(*self.tv_next_arrow)
        time.sleep(4)
        ActionChains(self.browser).move_to_element(right_nav).perform()
        return right_nav.is_displayed()

    #@allure.step('click on Right navigation arrow in recently watched')
    def click_rightarrow(self):
        time.sleep(1)
        self.browser.find_element(*self.recently_watch_next_navigation).click()

    #@allure.step('click on Right navigation arrow in action list')
    def click_list_right_arrow(self):
        first_right_navigation = self.browser.find_element(*self.right_navigation_view)
        # time.sleep(1)
        self.browser.execute_script("arguments[0].scrollIntoView();", first_right_navigation)
        time.sleep(1)
        ActionChains(self.browser).move_to_element(first_right_navigation).perform()
        time.sleep(1.5)
        right_navigation_arrow = self.browser.find_element(*self.right_navigation).is_displayed()

        self.browser.find_element(*self.right_navigation).click()
        return right_navigation_arrow

    #@allure.step('click on Right navigation arrow in action list')
    def click_list_second_right_arrow(self):
        second_right_navigation = self.browser.find_element(*self.second_right_navigation_view)
        # time.sleep(1)
        self.browser.execute_script("arguments[0].scrollIntoView();", second_right_navigation)
        time.sleep(1.5)
        ActionChains(self.browser).move_to_element(second_right_navigation).perform()
        time.sleep(1.5)
        self.browser.find_element(*self.right_navigation).click()
        try:
            time.sleep(1.5)
            right_navigation_arrow = self.browser.find_element(*self.right_navigation)

            if right_navigation_arrow.is_displayed():
                return True
        except:
            return False

    #@allure.step('Verify Right navigation arrow in action list')
    def verify_right_navigation_arrow(self):
        first_right_navigation = self.browser.find_element(*self.right_navigation_view)
        self.browser.execute_script("arguments[0].scrollIntoView();", first_right_navigation)
        time.sleep(1.5)
        ActionChains(self.browser).move_to_element(first_right_navigation).perform()
        time.sleep(1.5)
        right_navigation_arrow = self.browser.find_element(*self.right_navigation).is_displayed()
        return right_navigation_arrow

    #@allure.step('click on Right navigation arrow in recently watched')
    def verify_list_slider(self):
        return self.browser.find_element(*self.list_action_slider).is_displayed()

    #@allure.step('click on Right navigation arrow in recently watched')
    def click_list_left_arrow(self):
        first_right_navigation = self.browser.find_element(*self.left_navigation)
        # time.sleep(1)
        self.browser.execute_script("arguments[0].scrollIntoView();", first_right_navigation)
        time.sleep(2)
        ActionChains(self.browser).move_to_element(first_right_navigation).perform()
        time.sleep(2)
        left_navigation = self.browser.find_element(*self.left_navigation_view).is_displayed()
        return left_navigation

    #@allure.step('click on Right navigation arrow in recently watched')
    def click_left_navigation_arrow(self):
        first_right_navigation = self.browser.find_element(*self.left_navigation)
        # time.sleep(1)
        self.browser.execute_script("arguments[0].scrollIntoView();", first_right_navigation)
        time.sleep(1.5)
        ActionChains(self.browser).move_to_element(first_right_navigation).perform()
        time.sleep(2)
        self.browser.find_element(*self.left_navigation_view).click()
        try:
            time.sleep(2)
            left_navigation_arrow = self.browser.find_element(*self.left_navigation_view)

            if left_navigation_arrow.is_displayed():
                return True
        except:
            return False

    #@allure.step('click on Right navigation arrow in recently watched')
    def verify_left_navigation_arrow(self):
        time.sleep(1)
        try:
            left_navigation_arrow = self.browser.find_element(*self.left_navigation_view)

            if left_navigation_arrow.is_displayed():
                return True
        except:
            return False

    #@allure.step('click on Right navigation arrow in Tv Unscripted')
    def click_tv_rightarrow(self):
        time.sleep(2)
        self.browser.find_element_by_xpath(
            "//h2[text()='TV Unscripted']/ancestor::div[3]/following-sibling::div//a//i").click()

    #@allure.step('click on Right navigation arrow in recently watched')
    def second_click_rightarrow(self):
        time.sleep(1.5)
        self.browser.find_element_by_xpath(
            "//h2[text()='Recently Watched']/ancestor::div[3]/following-sibling::div//a[2]//i").click()

    #@allure.step('Verify Left navigation arrow is displayed in recently watched')
    def verify_leftarrow(self):
        left_nav = self.browser.find_element(*self.prev_arrow)
        time.sleep(2)
        ActionChains(self.browser).move_to_element(left_nav).perform()
        time.sleep(1.5)
        return left_nav.is_displayed()

    #@allure.step('Verify Left navigation arrow is displayed in Tv Unscripted')
    def verify_tv_leftarrow(self):
        left_nav = self.browser.find_element(*self.prev_arrow)
        time.sleep(5)
        ActionChains(self.browser).move_to_element(left_nav).perform()
        time.sleep(3)
        return left_nav.is_displayed()

    #@allure.step('click on Left navigation arrow in recently watched')
    def click_prevarrow(self):
        prev = self.browser.find_element(*self.prev_arrow)
        time.sleep(1.5)
        ActionChains(self.browser).move_to_element(prev).click(prev).perform()

    #@allure.step('click on Left navigation arrow in recently watched')
    def verify_list_count(self):
        time.sleep(1.5)
        cards = self.browser.find_elements(*self.recently_movie_card)
        time.sleep(1.5)
        return len(cards)

    #@allure.step('click on Left navigation arrow in recently watched')
    def click_tv_prevarrow(self):
        prev = self.browser.find_element(*self.prev_arrow)
        self.browser.implicitly_wait(10)
        ActionChains(self.browser).move_to_element(prev).click(prev).perform()

    #@allure.step('Click on watch movie from Action /Adventure cards ')
    def click_watchmovie(self):
        WebDriverWait(self.browser, 40).until(EC.presence_of_element_located(self.action_adventure))
        adventures = self.browser.find_element(*self.action_adventure)
        self.browser.execute_script("arguments[0].scrollIntoView();", adventures)
        time.sleep(1)
        watch = self.browser.find_element(*self.watchmovie_moviecard)
        time.sleep(1)
        ActionChains(self.browser).move_to_element(watch).click().perform()

        time.sleep(12)
        try:
            condition = self.browser.find_element(*self.play_begining)
            condition1 = condition.is_displayed()
        except:
            condition1 = False
            time.sleep(20)  # 60

        if condition1 == True:
            time.sleep(1.5)
            self.browser.find_element(*self.play_begining).click()
            time.sleep(20)  # 60

    #@allure.step('get the movie name, which you are going to play.')
    def play_moviename(self):
        global movie_name
        movie_name = self.browser.find_element(*self.watchmovie_name).text
        time.sleep(1.5)
        return movie_name

    #@allure.step('CLick on close image to close movie')
    def click_action_list_see_all(self):
        self.browser.refresh()
        WebDriverWait(self.browser, 40).until(EC.presence_of_element_located(self.list_see_all)) # taking more time 25 is not sufficent
        self.browser.find_element(*self.list_see_all).click()
        WebDriverWait(self.browser, 35).until(EC.presence_of_element_located(self.list_action_title))
        return self.browser.find_element(*self.list_action_title).is_displayed()

    #@allure.step('CLick on close image to close movie')
    def click_crossimg(self):
        # self.browser.find_element(*self.close_button).click()
        close_button = self.browser.find_element(*self.close_button)
        self.browser.execute_script("arguments[0].click();", close_button)

    #@allure.step('Verify close image should be present')
    def Validate_crossimg_button(self):
        move = ActionChains(self.browser)
        body_ = self.browser.find_element(*self.body_element)
        move.move_to_element_with_offset(body_, 511, 65)
        move.click()
        move.perform()
        time.sleep(2)
        WebDriverWait(self.browser, 25).until(EC.presence_of_element_located(self.zoom_in_zoom_out_button))
        zoom_button = self.browser.find_element(*self.zoom_in_zoom_out_button).is_displayed()
        return zoom_button

    #@allure.step('Get the movie name that has been added in recently watched playlist ')
    def recent_moviename(self):
        self.browser.refresh()
        WebDriverWait(self.browser, 35).until(EC.presence_of_element_located(self.recently_watched))
        global recent_movie
        recently = self.browser.find_element(*self.recently_watched)
        self.browser.execute_script("arguments[0].scrollIntoView();", recently)
        time.sleep(2)
        first = self.browser.find_element(*self.title_text)
        time.sleep(1)
        recent_movie = first.text
        return recent_movie

    #@allure.step('Get the 2nd Movie name in recently watched section')
    def play_2movieCard_name(self):
        time.sleep(2)
        second = self.browser.find_element(*self.play_nextMoviname)  # title 2
        ##print(second.text)
        time.sleep(2)
        recent_movie = second.text
        time.sleep(1)
        return recent_movie

    def RecentlyWatchedPosterImage(self):
        image = self.browser.find_element(*self.poster_image)
        image.location_once_scrolled_into_view
        a = image.is_displayed()
        return a

    #@allure.step('Movie Title Element')
    def verifyMovieTitle(self):
        WebDriverWait(self.browser, 35).until(EC.presence_of_element_located(self.title_text))
        movie_title = self.browser.find_element(*self.title_text).is_displayed()  # title 1
        ##print(first.text)
        return movie_title

    #@allure.step('Movie Genre Element')
    def MovieGenre(self):
        return self.browser.find_element(*self.movie_generes).is_displayed()

    #@allure.step('Verify Add to List option in recently watched movie card')
    def addTolist(self):
        # time.sleep(2)
        self.browser.refresh()
        WebDriverWait(self.browser, 35).until(EC.presence_of_element_located(self.recently_watched))
        rec_watched = self.browser.find_element(*self.recently_watched)
        self.browser.execute_script("arguments[0].scrollIntoView();", rec_watched)
        time.sleep(1.5)
        card1 = self.browser.find_element(*self.cardhover_option1)
        ActionChains(self.browser).move_to_element(card1).perform()
        return self.browser.find_element(*self.cardhover_option1).text

    #@allure.step('Verify Watch movie option in recently watched movie card')
    def watchMoviesoption(self):
        time.sleep(2.5)
        card2 = self.browser.find_element(*self.cardhover_option2)
        ActionChains(self.browser).move_to_element(card2).perform()
        textt = self.browser.find_element(*self.cardhover_option2).text
        time.sleep(1)
        return self.browser.find_element(*self.cardhover_option2).text

    #@allure.step('Verify Watch Trailer option in recently watched movie card')
    def watchTraileroption(self):
        time.sleep(1.5)
        card3 = self.browser.find_element(*self.cardhover_option3)
        ActionChains(self.browser).move_to_element(card3).perform()
        return self.browser.find_element(*self.cardhover_option3).text

    #@allure.step('Verify View Details option in recently watched movie card')
    def viewDetailsoption(self):
        time.sleep(1)
        card4 = self.browser.find_element(*self.cardhover_option4)
        ActionChains(self.browser).move_to_element(card4).perform()
        return self.browser.find_element(*self.cardhover_option4).text

    #@allure.step('Click on add to List ')
    def click_addList(self):
        time.sleep(1)
        self.browser.find_element(*self.cardhover_option1).click()

    #@allure.step('Verify Alert that consist success message ')
    def verifyAlert(self):
        ignored_exceptions = (NoSuchElementException, StaleElementReferenceException,)
        WebDriverWait(self.browser, 10, ignored_exceptions).until(EC.presence_of_element_located(self.alert))
        alert = self.browser.find_element(*self.alert).text
        ##print(alert)
        return alert

    #@allure.step('Clicking button in recently watched on cards hover -> watch movie ')
    def click_recwatch_movie(self):
        # time.sleep(2)
        WebDriverWait(self.browser, 45).until(EC.presence_of_element_located(self.recently_watched))
        recently_section = self.browser.find_element(*self.recently_watched)

        time.sleep(1.5)
        self.browser.execute_script("arguments[0].scrollIntoView();", recently_section)
        time.sleep(1)
        card2 = self.browser.find_element(*self.cardhover_option2)
        ActionChains(self.browser).move_to_element(card2).perform()
        time.sleep(1)
        card2.click()
        time.sleep(2)
        try:
            condition = self.browser.find_element(*self.play_begining)
            condition1 = condition.is_displayed()
        except:
            condition1 = False
            time.sleep(2)  # 60

        if condition1 == True:
            time.sleep(2)
            self.browser.find_element(*self.play_begining).click()
            time.sleep(2)  # 60

    #@allure.step('Choose and click in Resume watching and Playt from begining')
    def choose_click(self):
        try:
            condition = self.browser.find_element(*self.play_begining)
            condition1 = condition.is_displayed()
        except:
            condition1 = False
            time.sleep(2)

        if condition1 == True:
            time.sleep(2)
            self.browser.find_element(*self.play_begining).click()
            time.sleep(2)

    #@allure.step('Verify pop up for watch trailer is opening ')
    def watch_movie_popup(self):
        time.sleep(2)
        styl = self.browser.find_element(*self.watch_popup).get_attribute('style')
        ##print(styl)
        return styl

    #@allure.step('CLick on View Details button ')
    def click_viewdetails(self):
        time.sleep(1.5)
        card4 = self.browser.find_element(*self.cardhover_option4)
        ActionChains(self.browser).move_to_element(card4).perform()
        time.sleep(1.5)
        card4.click()

    #@allure.step('Verify Page title ')
    def verify_pagetitle(self):
        # time.sleep(2)
        WebDriverWait(self.browser, 45).until(EC.presence_of_element_located(self.title_overview))
        title = self.browser.find_element(*self.synopsis_title_text).text
        return title

    #@allure.step('Click on watch trailer button in hover of cards ')
    def click_recwatch_trailer(self):
        # time.sleep(2)
        recently_section = self.browser.find_element(*self.recently_watched)
        time.sleep(1)
        self.browser.execute_script("arguments[0].scrollIntoView();", recently_section)
        time.sleep(1.5)
        card3 = self.browser.find_element(*self.cardhover_option3)
        ActionChains(self.browser).move_to_element(card3).perform()
        time.sleep(1)
        card3.click()
        time.sleep(3)
        try:
            condition = self.browser.find_element(*self.play_begining)
            condition1 = condition.is_displayed()
        except:
            condition1 = False
            time.sleep(2)  # 60

        if condition1 == True:
            time.sleep(1.5)
            self.browser.find_element(*self.play_begining).click()
            time.sleep(2)  # 60

    #@allure.step('Click on watch trailer button in hover of cards ')
    def watchrecwatch_trailer(self):
        styl = self.browser.find_element(*self.watch_movie_popup).get_attribute('style')
        ##print(styl)
        return styl

    #@allure.step('Verify on click right navigation arrow the 1st movie card is displayed ')
    def verify_1card_slide(self):
        first = self.browser.find_element(*self.title_text)  # title 1
        ##print(first.text)
        time.sleep(2)
        return first.is_displayed()

    #@allure.step('Click Second Right nav arrow ')
    def click_secnav_arrow(self):
        try:
            condition = self.browser.find_element(*self.next_arrow)  # sec_next_arrow
            time.sleep(2)
            condition1 = condition.is_displayed()
        except:
            condition1 = False

        if condition1 == True:
            time.sleep(2)
            right_nav = self.browser.find_element(*self.click_next_arrow)  # sec_next_arrow
            time.sleep(10)
            ActionChains(self.browser).move_to_element(right_nav).click(right_nav).perform()

    #@allure.step('Verify Right nav arrow got disabled when we are on last ')
    def verify_right_disbaled(self):
        try:
            isPresent = self.browser.find_element_by_xpath(
                "//h2[text()='Recently Watched']/ancestor::div[3]/following-sibling::div//a[2]//i")  # third_next_arrow
            time.sleep(2.5)
            if isPresent.is_displayed():
                return True

        except:
            return False

    #@allure.step('Verify Left nav arrow got disabled when we are on first ')
    def verify_left_disbaled(self):
        try:
            WebDriverWait(self.browser, 50).until(EC.presence_of_element_located(self.recently_watched))
            time.sleep(1)
            recently = self.browser.find_element(*self.recently_watched)
            self.browser.execute_script("arguments[0].scrollIntoView();", recently)
            time.sleep(1.5)
            isPresent = self.browser.find_element_by_xpath("//a/i[@class='previous-icon icon']")
            time.sleep(1)
            if isPresent.is_displayed():
                return True
        except:
            return False

    #@allure.step('CLick on Automaion List to veriy movie added ')
    def clickAutomationlist(self):
        time.sleep(2)
        self.browser.find_element(*self.myList_seeall).click()
        time.sleep(1)
        WebDriverWait(self.browser, 10).until(EC.presence_of_element_located(self.automation_mylist))
        self.browser.find_element(*self.automation_mylist).click()

    #@allure.step('Verify Movie is added in Automation List  ')
    def verifyMovie_list(self, movie):
        time.sleep(2)
        WebDriverWait(self.browser, 30).until(EC.presence_of_element_located((By.XPATH,
                                                                              "//div[@class='desk-on']//p[@class='movie-title light-color'][contains(text(),'" + str(
                                                                                  movie) + "')]")))
        time.sleep(3)
        movie_name = self.browser.find_element_by_xpath(
            "//div[@class='desk-on']//p[@class='movie-title light-color'][contains(text(),'" + str(movie) + "')]")
        return movie_name.text

    #@allure.step('Delete movie from list')
    def delete_movie(self, movie):
        time.sleep(2)
        self.browser.find_element_by_xpath("//div[1][div[div[p[contains(text(),'" + str(
            movie) + "')]]]]/ancestor::div[1]/preceding-sibling::div[1]//input").click()
        # self.browser.execute_script("arguments[0].click();", check)
        time.sleep(2)
        self.browser.find_element(*self.delete_btn_footer).click()
        time.sleep(2)
        self.browser.find_element(*self.delete_permission).click()
        WebDriverWait(self.browser, 65).until(EC.presence_of_element_located(self.delete_success_msg))

    #@allure.step('Click and verify newly created list ')
    def click_verify_new_list(self):
        time.sleep(4)
        self.browser.find_element(*self.mylist_tab).click()
        WebDriverWait(self.browser, 25).until(EC.presence_of_element_located(self.autoRand_list))
        self.browser.find_element(*self.autoRand_list).click()

    # Footer
    #@allure.step('Verify Privacy policy should be displayed in footer')
    def verify_Privacypolicy(self):
        WebDriverWait(self.browser, 20).until(EC.presence_of_element_located(self.privacy_policy))
        time.sleep(1)  # need for scroll - website is slow
        self.browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(1.5)
        self.browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        WebDriverWait(self.browser, 3).until(EC.presence_of_element_located(self.privacy_policy))
        return self.browser.find_element(*self.privacy_policy).is_displayed()

    #@allure.step('Verify Privacy policy should be displayed in footer')
    def privacyPolicy_click(self):
        # time.sleep(4)
        WebDriverWait(self.browser, 30).until(EC.presence_of_element_located(self.privacy_policy))
        privacy_policy_button = self.browser.find_element(*self.privacy_policy)
        time.sleep(1.5)
        self.browser.execute_script("arguments[0].scrollIntoView();", privacy_policy_button)
        time.sleep(1.5)
        home_screen = self.browser.window_handles[0]
        # self.browser.execute_script("arguments[0].click();", privacy_policy_button)
        self.browser.find_element(*self.privacy_policy).click()
        time.sleep(8)
        policy_screen = self.browser.window_handles[1]
        self.browser.switch_to.window(policy_screen)
        privacy_url = self.browser.current_url
        self.browser.close()
        self.browser.switch_to.window(home_screen)
        return privacy_url

    #@allure.step('Verify Privacy policy should be displayed in footer')
    def termsOfUse_Click(self):
        WebDriverWait(self.browser, 85).until(EC.presence_of_element_located(self.privacy_policy))
        time.sleep(1.5)
        self.browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(1.5)
        self.browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        WebDriverWait(self.browser, 5).until(EC.presence_of_element_located(self.terms_use))
        home_screen = self.browser.window_handles[0]
        self.browser.find_element(*self.terms_use).click()
        time.sleep(6)
        terms_screen = self.browser.window_handles[1]
        self.browser.switch_to.window(terms_screen)
        terms_of_use = self.browser.current_url
        self.browser.close()
        self.browser.switch_to.window(home_screen)
        return terms_of_use

    #@allure.step('Verify terms of use should be present in footer')
    def verify_termsUse(self):
        WebDriverWait(self.browser, 4).until(EC.presence_of_element_located(self.terms_use))
        return self.browser.find_element(*self.terms_use).is_displayed()

    #@allure.step('Verify mgm logo in footer')
    def verify_footerLogo(self):
        WebDriverWait(self.browser, 4).until(EC.presence_of_element_located(self.footer_logo))
        return self.browser.find_element(*self.footer_logo).is_displayed()

    #@allure.step('Verify support link should be displayed in footer')
    def verify_supportLink(self):
        WebDriverWait(self.browser, 15).until(EC.presence_of_element_located(self.support))
        return self.browser.find_element(*self.support).is_displayed()

    #@allure.step('Verify Address should be displayed in footer')
    def verify_address(self):
        WebDriverWait(self.browser, 5).until(EC.presence_of_element_located(self.address))
        return self.browser.find_element(*self.address).is_displayed()

    #@allure.step('Verify legal Text should be displayed in footer')
    def verify_legal(self):
        WebDriverWait(self.browser, 5).until(EC.presence_of_element_located(self.legal))
        return self.browser.find_element(*self.legal).is_displayed()

    #@allure.step('Verify legal Text should be displayed in footer')
    def verify_contact_us(self):
        WebDriverWait(self.browser, 5).until(EC.presence_of_element_located(self.contact_us))
        return self.browser.find_element(*self.contact_us).is_displayed()

    #@allure.step('Verify Youtube icon should be displayed in footer')
    def verify_youtubeIcon(self):
        WebDriverWait(self.browser, 5).until(EC.presence_of_element_located(self.youtube_icon))
        return self.browser.find_element(*self.youtube_icon).is_displayed()

    #@allure.step('Verify Youtube icon is clickable')
    def click_youtubeIcon(self):
        # time.sleep(2)
        WebDriverWait(self.browser, 40).until(EC.presence_of_element_located(self.youtube_icon))
        self.browser.find_element(*self.youtube_icon).click()
        time.sleep(8)
        self.browser.switch_to.window(self.browser.window_handles[1])
        youtube_title = self.browser.title
        time.sleep(2)
        mgm_txt = self.browser.find_element_by_xpath('//div[@id="text-container"]').text
        assert 'MGM - YouTube' in youtube_title
        self.browser.close()
        time.sleep(3)
        self.browser.switch_to.window(self.browser.window_handles[0])
        time.sleep(6)
        roar_title = self.browser.title
        assert 'ROAR' in roar_title
        return mgm_txt

    #@allure.step('Verify Facebook icon is clickable')
    def click_facebookIcon(self):
        # time.sleep(2)
        self.browser.find_element(*self.fb_icon).click()
        time.sleep(5)
        self.browser.switch_to.window(self.browser.window_handles[1])
        fb_title = self.browser.title
        assert ('MGM Studios' in fb_title) or ('Facebook' in fb_title)
        time.sleep(1.5)
        self.browser.close()
        time.sleep(1.5)
        self.browser.switch_to.window(self.browser.window_handles[0])
        time.sleep(1.5)
        roar_title = self.browser.title
        return roar_title

    #@allure.step('Verify Twitter icon is clickable')
    def click_twitterIcon(self):
        # time.sleep(2)
        self.browser.find_element(*self.twitter_icon).click()
        time.sleep(5)
        self.browser.switch_to.window(self.browser.window_handles[1])
        twitter_title = self.browser.title
        assert 'MGM Studios (@mgm_studios) / Twitter' in twitter_title
        twitter_txt = self.browser.find_element_by_xpath('//span[contains(text(),"MGM Studios")]').text
        self.browser.close()
        time.sleep(1.5)
        self.browser.switch_to.window(self.browser.window_handles[0])
        time.sleep(1.5)
        roar_title = self.browser.title
        assert 'ROAR' in roar_title
        return twitter_txt

    #@allure.step('Verify Insta icon is clickable')
    def click_instagramIcon(self):
        # time.sleep(3)
        insta_icon = self.browser.find_element(*self.insta_icon)
        time.sleep(1)
        self.browser.execute_script("arguments[0].click();", insta_icon)
        time.sleep(5)
        self.browser.switch_to.window(self.browser.window_handles[1])
        insta_title = self.browser.title
        assert 'Instagram' in insta_title
        time.sleep(1.5)
        self.browser.close()
        time.sleep(1.5)
        self.browser.switch_to.window(self.browser.window_handles[0])
        time.sleep(1.5)
        roar_title = self.browser.title
        return roar_title


    #@allure.step('Verify Facebook icon should be displayed in footer')
    def verify_fbIcon(self):
        WebDriverWait(self.browser, 5).until(EC.presence_of_element_located(self.fb_icon))
        return self.browser.find_element(*self.fb_icon).is_displayed()

    #@allure.step('Verify Twitter should be displayed in footer')
    def verify_twitterIcon(self):
        WebDriverWait(self.browser, 5).until(EC.presence_of_element_located(self.twitter_icon))
        return self.browser.find_element(*self.twitter_icon).is_displayed()

    #@allure.step('Verify Insta icon should be displayed in footer')
    def verify_instaIcon(self):
        WebDriverWait(self.browser, 5).until(EC.presence_of_element_located(self.insta_icon))
        return self.browser.find_element(*self.insta_icon).is_displayed()

    #@allure.step('Verify Copyright should be displayed in footer')
    def verify_copyright(self):
        WebDriverWait(self.browser, 5).until(EC.presence_of_element_located(self.copyright))
        return self.browser.find_element(*self.copyright).is_displayed()

    #@allure.step('Verify Connect should be displayed in footer')
    def verify_connect(self):
        WebDriverWait(self.browser, 5).until(EC.presence_of_element_located(self.connect))
        return self.browser.find_element(*self.connect).is_displayed()

    # def verify_add_list(self):
    #     list1=WebDriverWait(self.browser,5).until(EC.presence_of_element_located(self.add_list))
    #     list1.click()
    #     time.sleep(5)
    #     return self.browser.find_element(*self.list_text).is_displayed()

    def add_to_list(self):
        self.browser.find_element(*self.my_lists).click()
        WebDriverWait(self.browser, 20).until(EC.presence_of_element_located(self.your_list))
        return self.browser.find_element(*self.your_list).is_displayed()

    def verify_add_list(self):
        self.browser.find_element(*self.your_list).click()
        self.browser.find_element(*self.movies_list).click()
        WebDriverWait(self.browser, 20).until(EC.presence_of_element_located(self.title_movies))
        return self.browser.find_element(*self.title_movies).is_displayed()

    def verify_grid_button(self):
        WebDriverWait(self.browser, 20).until(EC.presence_of_element_located(self.list_grid))
        time.sleep(30)
        self.browser.find_element(*self.list_grid).click()
        WebDriverWait(self.browser, 20).until(EC.presence_of_element_located(self.grid_button))
        return self.browser.find_element(*self.grid_button).is_displayed()

    def verify_grid_view(self):
        WebDriverWait(self.browser, 20).until(EC.presence_of_element_located(self.grid_view))
        time.sleep(30)
        self.browser.find_element(*self.grid_view).click()
        WebDriverWait(self.browser, 20).until(EC.presence_of_element_located(self.grid_text))
        return self.browser.find_element(*self.grid_text).is_displayed()

    def verify_assets_button(self):
        self.browser.find_element(*self.assets_button).click()
        time.sleep(4)
        WebDriverWait(self.browser, 20).until(EC.presence_of_element_located(self.assets_popup))
        return self.browser.find_element(*self.assets_popup).is_displayed()
    def verify_checkbox_button(self):
        WebDriverWait(self.browser, 20).until(EC.presence_of_element_located(self.assets_popup))
        time.sleep(30)
        self.browser.find_element(*self.assets_checkbox1).click()
        time.sleep(5)
        self.browser.find_element(*self.assets_checkbox2).click()
        time.sleep(4)
        self.browser.find_element(*self.assets_checkbox3).click()
        time.sleep(4)
        self.browser.find_element(*self.continue_button).click()
        time.sleep(3)
        WebDriverWait(self.browser, 20).until(EC.presence_of_element_located(self.banner_poster))
        return self.browser.find_element(*self.banner_poster).is_displayed()

    def verify_send_value(self,value):
        WebDriverWait(self.browser, 20).until(EC.presence_of_element_located(self.value_text))
        self.browser.find_element(*self.value_text).click()
        self.browser.find_element(*self.value_text).send_keys(value)
        time.sleep(20)
        self.browser.find_element(*self.search_icon).click()
        time.sleep(20)
        return self.browser.find_element(*self.movie_poster).is_displayed()

    def verify_filter_text(self):
        self.browser.find_element(*self.filter_text).click()
        time.sleep(4)
        self.browser.find_element(*self.film_filter).click()
        time.sleep(5)
        return self.browser.find_element(*self.after_filter).is_displayed()

    def verify_my_cart(self):
        self.browser.find_element(*self.my_cart).click()
        time.sleep(6)
        WebDriverWait(self.browser, 20).until(EC.presence_of_element_located(self.your_cart))
        return self.browser.find_element(*self.your_cart).is_displayed()

    def verify_your_cart(self):
        self.browser.find_element(*self.your_cart).click()
        time.sleep(4)
        WebDriverWait(self.browser, 20).until(EC.presence_of_element_located(self.him_cart))
        return self.browser.find_element(*self.him_cart).is_displayed()

    def verify_assets_click(self):
        self.browser.find_element(*self.assets_button).click()
        time.sleep(5)
        poster_button = self.browser.find_element(*self.poster_click)
        time.sleep(1.5)
        self.browser.execute_script("arguments[0].scrollIntoView();", poster_button)
        time.sleep(4)
        WebDriverWait(self.browser, 50).until(EC.presence_of_element_located(self.poster_click))
        time.sleep(10)
        self.browser.find_element(*self.poster_click).click()
        time.sleep(5)
        WebDriverWait(self. browser, 50).until(EC.presence_of_element_located(self.movie_name))
        return self.browser.find_element(*self.movie_name).is_displayed()

    def verify_all_assets(self):
        self.browser.find_element(*self.all_assets).click()
        time.sleep(10)
        view_details = self.browser.find_element(*self.movies_text)
        ActionChains(self.browser).move_to_element(view_details).perform()
        card_overview = self.browser.find_element(*self.add_to_cart)
        time.sleep(10)
        card_overview.click()
        time.sleep(5)
        WebDriverWait(self.browser, 10).until(EC.presence_of_element_located(self.card_verify))
        return self.browser.find_element(*self.card_verify).is_displayed()


    def input_cart_text(self,text_value):
        WebDriverWait(self.browser, 20).until(EC.presence_of_element_located(self.my_cart_input))
        self.browser.find_element(*self.my_cart_input).send_keys(text_value) 
        create_button12 = self.browser.find_element(*self.create_cart)
        time.sleep(1.5)
        self.browser.execute_script("arguments[0].scrollIntoView();", create_button12)
        time.sleep(3)
        self.browser.find_element(*self.create_cart).click()
        time.sleep(5)
        self.browser.find_element(*self.add_button).click()
        time.sleep(10)
        self.browser.find_element(*self.my_cart).click()
        time.sleep(5)
        self.browser.find_element(*self.your_cart).click()
        time.sleep(5)
        WebDriverWait(self.browser, 20).until(EC.presence_of_element_located(self.cart_text))
        return self.browser.find_element(*self.cart_text).is_displayed()

    def verify_delete_button(self):
        self.browser.find_element(*self.delete_button).click()
        time.sleep(5)
        self.browser.find_element(*self.delete_cart).click()
        WebDriverWait(self.browser, 20).until(EC.presence_of_element_located(self.delete_popup))
        return self.browser.find_element(*self.delete_popup).is_displayed()


    def verify_mgm_admin(self):
        cross_button = self.browser.find_element(*self.delete_cart_cross_button)
        self.browser.execute_script("arguments[0].click();", cross_button)
        WebDriverWait(self.browser, 20).until(EC.presence_of_element_located(self.mgm_roar_img))
        time.sleep(4)
        self.browser.find_element(*self.mgm_roar_img).click()
        time.sleep(2)
        self.browser.find_element(*self.mgm_admin).click()
        time.sleep(6)
        WebDriverWait(self.browser, 20).until(EC.presence_of_element_located(self.mgm_text))
        return self.browser.find_element(*self.mgm_text).is_displayed()

    def verify_search_field(self,value):
        WebDriverWait(self.browser, 20).until(EC.presence_of_element_located(self.search_bar))
        time.sleep(1)
        self.browser.find_element(*self.search_bar).clear()
        time.sleep(.5)
        self.browser.find_element(*self.search_bar).send_keys(value)
        time.sleep(2)
        self.browser.find_element(*self.search_bar).send_keys(Keys.ENTER)
        #self.browser.find_element(*self.search_icon_btn).click()
        time.sleep(2)
        WebDriverWait(self.browser, 20).until(EC.presence_of_element_located(self.search_value))
        time.sleep(2)
        return self.browser.find_element(*self.search_value).is_displayed()

    def verify_invite_button(self):
        self.browser.find_element(*self.invite_button).click()
        time.sleep(4)
        WebDriverWait(self.browser, 20).until(EC.presence_of_element_located(self.invite_tag_name))
        time.sleep(2)
        return self.browser.find_element(*self.invite_tag_name).is_displayed()
















































































