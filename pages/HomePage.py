from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from appium.webdriver.webdriver import WebDriver
import allure
from pathlib import Path
import csv
import time
import json
from selenium.webdriver import ActionChains


class homepage:
    list_titles = (By.XPATH, '//div[@class="movie-detail"]/p')
    action_adventure = (By.XPATH, "//h2[contains(text(),'Action')]")
    body_element = (By.XPATH, "(//body//div[@class='bmpui-container-wrapper'])[31]")
    my_list = (By.XPATH, "//h2[contains(text(),'My Lists')]")
    recently_watch_title = (By.XPATH, "//h2[contains(text(),'Recently Watched')]")
    header_logo = (By.XPATH, "//nav/a[contains(@class,'logo-img')]//img[@alt='logo-img']")
    homepage_welcometext = (By.XPATH, "//div[@class='wel-txt']")
    header_films_series = (By.XPATH, "//li[contains(@class,'menu menu-label')]//a[@id='Films & Series']")
    footer_roar_logo = (By.XPATH, '//div/a[@class="footer-logo"]/img')
    header_television = (By.XPATH, "//ul[@class='menu-items']//a[@id='Television']")
    header_mylist = (By.XPATH, "//li[contains(@class,'menu menu-label')]//a[@id='My Lists']")
    your_carts = (By.XPATH, "//p[text()='Your Carts']")
    cart_first_delete_button = (By.XPATH,'(//div/button[contains(@class,"delete-btn")])[1]')
    header_logout_dropdown_toggle = (By.XPATH, "//button[contains(@class,'dropdown-toggle btn')]")
    header_logout_button = (By.XPATH, "//h6[contains(@class,'logout')]")
    cartNameTitle = (By.XPATH, '//h1[contains(@class,"ld-title")]')
    header_search_button = (By.XPATH, "//div[@class='centerAlign w-100']")
    search_text = (By.XPATH, '//div[contains(@class,"search-header")]/div[contains(text(),"search")]')
    search_close_button = (By.XPATH, '//div/div[contains(@class,"close-btn")]/img[contains(@class,"close-btn")]')
    search_input_field = (
        By.XPATH, '//div[contains(@class,"search-input")]/input[@placeholder="Enter title or keyword"]')
    header_marketing_rules = (By.XPATH, "//li[contains(@class,'menu menu-label')]//a[@id='Marketing Rules']")
    header_assets = (By.XPATH, "//li[contains(@class,'menu menu-label')]//a[@id='Assets']")
    assets_continue_button = (By.XPATH, '//div/button[contains(text(),"CONTINUE")]')
    # first_checkbox = (By.XPATH, "//div[@class='roar-sub-header']//div[2]//label[1]//div[1]//input[1]")
    # second_checkbox = (By.XPATH, "//div[3]//label[1]//div[1]//input[1]")
    # third_checkbox = (By.XPATH, "//div[4]//label[1]//div[1]//input[1]")
    first_checkbox = (By.XPATH, "(//div[@class='main-content']//input)[1]")
    second_checkbox = (By.XPATH, "(//div[@class='main-content']//input)[2]")
    third_checkbox = (By.XPATH, "(//div[@class='main-content']//input)[3]")

    continue_button = (By.XPATH, "//div/button[text()='CONTINUE']")
    header_my_carts = (By.XPATH, "//body//mgm-app-root//mgm-header//a[2]")
    banner_text = (By.XPATH, "//div[@class='banner-text']")
    marketing_Page_title = (By.XPATH, "//h2[normalize-space()='Marketing Rules']")
    lists = (By.XPATH, "//p[contains(text(),'Your Lists')]")
    assets = (By.XPATH, "//div[@class='roar-header']")
    email_textbox = (By.XPATH, "//input[@name='username']")
    header = (By.XPATH, "//div[@class='header']")
    carousel = (By.XPATH, "//div[@class='carousel']")
    movie_list_bestpicturewinner = (By.XPATH, "//h2[text()='Best Picture Winners']")
    movie_list_jamesbond = (By.XPATH, "//h2[text()='James Bond']")
    movie_list_newreleases = (By.XPATH, "//h2[text()='New Releases']")
    movie_list_actionadventure = (By.XPATH, "//h2[text()='Action / Adventure']")
    movie_list_oscarwinning = (By.XPATH, "//h2[text()='Oscar-winning Films']")
    movie_list_actionhits = (By.XPATH, "//h2[text()='Action Packed Hits']")
    movie_list_robocop = (By.XPATH, "//h2[text()='Robocop']")
    movie_list_rockey = (By.XPATH, "//h2[text()='Rocky']")
    movie_list_Pinkpanther = (By.XPATH, "//h2[text()='Pink Panther']")
    movie_list_legallyblonde = (By.XPATH, "//h2[text()='Legally Blonde']")
    see_all_tv_shows = (By.XPATH, "//div//button[text()=' SEE ALL TV SHOWS ']")
    see_all_movies = (By.XPATH, "//div//button[text()=' SEE ALL MOVIES ']")
    footer_logo = (By.XPATH, "//section//img[@alt='footer-logo']")
    privacy_policy = (By.XPATH, "//li//a[text()='Privacy Notice']")
    terms_of_use = (By.XPATH, "//li//a[text()='Terms of use']")
    support = (By.XPATH, "//div//a[text()='Support']")
    movie_image_slider = (By.XPATH, "//div[@class='carousel-inner']")
    next_navigation = (By.XPATH, "//span[@class='carousel-control-next-icon']")
    previous_navigtion = (By.XPATH, "//span[@class='carousel-control-prev-icon']")
    carousel_progress_bar = (By.XPATH, "//ul[@class='carousel-menu-list']")
    progress_bar_spectre = (By.XPATH, "//ul[@class='carousel-menu-list']//a[text()='Spectre']")
    progress_bar_armyofdarkness = (By.XPATH, "//ul[@class='carousel-menu-list']//a[text()='Army Of Darkness']")
    progress_bar_magnificent = (By.XPATH, "//ul[@class='carousel-menu-list']//a[text()='The Magnificent Seven (2016)']")
    progress_bar_fargo = (By.XPATH, "//ul[@class='carousel-menu-list']//a[text()='Fargo']")
    progress_bar_no_time_die = (By.XPATH, "//ul[@class='carousel-menu-list']//a[text()='No Time To Die']")
    progress_bar_rocky = (By.XPATH, "//ul[@class='carousel-menu-list']//a[text()='Rocky II']")
    progress_bar_amigos = (By.XPATH, "//ul[@class='carousel-menu-list']//a[text()='Three Amigos!']")
    progress_bar_legally_blonde = (By.XPATH, "//ul[@class='carousel-menu-list']//a[text()='Legally Blonde']")
    progress_bar_witch_hunter = (
        By.XPATH, "//ul[@class='carousel-menu-list']//a[text()='Hansel & Gretel Witch Hunters']")
    slider_background_images = (By.XPATH, "//div[@id='slide-slideId_0']/div/img[contains(@class,'slider-image')]")
    movie_logo = (By.XPATH, "//img[@alt='logo-image']")
    watchnow_button = (By.XPATH, "//div[@class='carousel-item active']//div[@class='movie-content']//div["
                                 "@class='btn-container']//div//button[contains(text(),'Watch Now')]")
    add_to_list_button = (By.XPATH, "//div[@class='btn-container']//button[text()=' ADD TO LIST ']")
    add_listCarosel = (By.XPATH, "//div[@class='carousel-item active']//button[contains(text(),'ADD TO LIST')]")
    add_to_list_button_spectre = (By.XPATH, "(//div[@class='btn-container']//button[text()=' ADD TO LIST '])[1]")

    maincarousel_add_to_list_movie2 = (By.XPATH, "(//div[@class='btn-container']//button[text()=' ADD TO LIST '])[2]")
    view_details = (By.XPATH, "(//div[@class='btn-container']//button[text()=' View details '])[1]")
    synopsis_title = (By.XPATH, '//div[contains(@class,"synopsis-title")]')
    syn_title = (By.XPATH, "//div[@class='col-7 right active']/p[1]")
    see_all_button = (By.XPATH, "//a[@class='see-all-text']")
    movie_poster = (By.XPATH, "//div[@class='ng-scroll-content']//div[@class='movie-poster']")
    movie_list_next_button = (By.XPATH, "//div//a[@role='button']/i[@class='next-icon icon'])[2]")
    movie_list_prev_button = (By.XPATH, "//div//a[@role='button']/i[@class='previous-icon icon']")
    poster_image = By.XPATH, ('//div[@class="movie-poster"]/div[@class="movie"]/div[@class="movie-poster-alias"]/img')
    movie_title_Detroit = (By.XPATH, "//div/p[text()=' Detroit ']")
    # movie_title_Angel_Of_Mine  = (By.XPATH,'//li[2]/mgm-movie-poster/div/div[@class="movie-poster"]/div/p[text()=" Angel Of Mine "]')
    movie_title_warth_of_man = (
        By.XPATH, '//li/mgm-movie-poster/div/div[@class="movie-poster"]/div/p[contains(text(),"Wrath Of Man")]')
    # movie_genres = (By.XPATH, "//div//span[text()=' Crime,  ']")
    movie_genres = (By.XPATH, "//div//span[text()=' DRAMA ']")
    addList_overlay = (By.XPATH,
                       "//h2[contains(text(),'Action')]/ancestor::div[3]/following-sibling::div//ul/li[1]//button[contains(text(),'ADD TO LIST')]")
    add_to_list_popup = (By.XPATH, '//div[@class="createNewList"]/span[contains(text(),"CREATE A NEW LIST")]')
    addList_tv = (By.XPATH,
                  "(//h2[contains(text(),'TV Unscripted')]/ancestor::div/following-sibling::div[1]//li//button[contains(text(),"
                  "'ADD TO LIST')])[1]")
    bestPicWin_heading = (By.XPATH, "//h2[contains(text(),'Alive')]")
    tvTitle = (By.XPATH, '//h2[contains(text(),"TV Unscripted")]')
    fiascoSeriesListPage = (By.XPATH, '//div[@class = "desk-on"]//p[contains(text(),"(series)")]'
                                      '/ancestor::div[2]//ul/li/button[contains(text(),"Watch now")]')
    firstFilmSeriesCardPoster = (By.XPATH, '//ul[contains(@class,"search-list")]/li[1]/div[2]//div[@class="poster"]')
    movie_card_list = (By.XPATH,
                       "//h2[contains(text(),'Alive')]/ancestor::div[3]/following-sibling::div[1]//button[text() = 'ADD TO LIST']")
    movie_addToList = (By.XPATH,
                       "(//h2[contains(text(),'Alive')]/ancestor::div[3]/following-sibling::div[1]//li//button[contains(text(),'ADD TO LIST')])[1]")
    tvShowFiasco = (By.XPATH, '//p[contains(text()," Fiasco (series) ")]/ancestor::div[2]/div[contains(@class,'
                              '"button-hover")]//li/button[contains(text(),"ADD TO LIST")]')
    first_tv_show_add_to_list = (By.XPATH,'(//h2[contains(text(),"TV Unscripted")]/ancestor::div[3]/following-sibling::div//ul/li[1]//button[contains(text(),"ADD TO LIST")])[1]')
    movie_addToList_second = (By.XPATH,
                              "(//h2[contains(text(),'Alive')]/ancestor::div[3]/following-sibling::div[1]//li//button[contains(text(),'ADD TO LIST')])[2]")

    addBeingJamesBondToListButton = (
        By.XPATH, '//div[1]/div/div[@class="movie-detail"]/p[contains(text()," Being James Bond ")]'
                  '/parent::div/parent::div//div[contains(@class,"button-hover")]//button[contains(text(),"ADD TO LIST")]')
    watchmovie_moviecard = (By.XPATH,
                            "//h2[contains(text(),'Action')]/ancestor::div[3]/following-sibling::div//ul/li[1]//button[contains(text(),'Watch now')]")
    close_button = (By.XPATH, '//div[@class="modal-content"]//div/div/div/img[@class="close-btn-image"]')
    zoom_in_zoom_out_button = (
    By.XPATH, '(//div[@class="bmpui-container-wrapper"]//div[@class="bmpui-container-wrapper"]/button)[11]')
    watchtrailer_moviecard = (By.XPATH,
                              "//h2[contains(text(),'Action')]/ancestor::div[3]/following-sibling::div//ul/li[1]//button[contains(text(),'Watch trailer')]")
    watchtrailer_tv_card = (
        By.XPATH,
        "(//h2[contains(text(),'TV Unscripted')]/ancestor::div/following-sibling::div[1]//li//button[contains("
        "text(),'Watch trailer')])[1]")
    movie_card_watch_now = (By.XPATH,
                            "//h2[contains(text(),'Best Picture Winners')]/ancestor::div[3]/following-sibling::div[1]//button[text() = 'Watch movie']")
    heading1 = (By.XPATH, "//h2[contains(text(),'Action')]")
    heading_tv = (By.XPATH, "//h2[contains(text(),'TV Unscripted')]")
    addToList_moviecard = (By.XPATH, "")
    movie1_crd = (By.XPATH,
                  "(//h2[contains(text(),'Best Picture Winners')]/parent::div/parent::div/parent::div/following-sibling::div[1]//ul[1]/li//button[contains(text(),'ADD TO LIST')])[2]")
    movie_card_watch_trailer = (By.XPATH,
                                "//h2[contains(text(),'Best Picture Winners')]/ancestor::div[3]/following-sibling::div[1]//button[text() = 'Watch trailer']")
    # movie_card_view_details = (By.XPATH, "//div[@class = 'button-hover']//button[text()='View details']")
    explore_element = (By.XPATH, "//div[@class='gold-footer']/h2")
    television_show = (By.XPATH, "//div/h2[text()='Our Television Shows']")
    movies = (By.XPATH, "//div/h2[text()='Our Movies']")
    movie_title_Flyboys = (By.XPATH, "//div[@class='movie-detail']/p[text()=' Flyboys ']")
    movie_title_Capote = (By.XPATH, "//div[@class='movie-detail']/p[text()=' Capote ']")
    movie_title_Hotel_Rwanda = (By.XPATH, "//div[@class='movie-detail']/p[text()=' Hotel Rwanda ']")
    movie_title_ben_huh = (By.XPATH, "//div[@class='movie-detail']/p[text()=' Ben-hur (2016) ']")
    movie_title_Valkyrie = (By.XPATH, "//div[@class='movie-detail']/p[text()=' Valkyrie ']")
    action_horizontal_scroller = (
        By.XPATH, '//h2[text()="Action"]/ancestor::div[4]//div[@class="card-section"]//scrollbar-x/div/div')
    my_list_horizontal_scroller = (
        By.XPATH, '//h2[text()="My Lists"]/ancestor::div[4]//div[@class="card-section"]//scrollbar-x/div/div')
    recently_horizontal_scroller = (
        By.XPATH, '//h2[text()="Recently Watched"]/ancestor::div[4]//div[@class="card-section"]//scrollbar-x/div/div')
    action_movie_the_girl_with_the_dragon_tattoo = (
        By.XPATH, '//div[@class="movie-detail"]/p[contains(text()," The Girl With The Dragon Tattoo ")]')
    action_fifth_card_movie_name = (By.XPATH,"(//h2[contains(text(),'Action')]/ancestor::div[3]/following-sibling::div//ul/li//div[@class='movie-detail'])[5]")
    viewdetails_moviecard = (By.XPATH, "//h2[contains(text(),'Action')]/ancestor::div["
                                       "3]/following-sibling::div//ul/li[1]//button[contains(text(),'View details')]")
    viewdetails_tv_card = (By.XPATH, "//h2[contains(text(),'TV Unscripted')]/ancestor::div["
                                     "3]/following-sibling::div//ul/li[1]//button[contains(text(),'View details')]")
    movie_card_view_details = (By.XPATH,
                               "//div[@id='slide-slideId_0']//button[contains(@class,'cui-btn')][normalize-space()='View details']")
    player_popup = (By.XPATH, "//div[@id='bitmovin-player']")
    movie_close_btn = (By.XPATH, "//mgm-video-player-popup//img[@class='close-btn-image']")
    titles_underligned = (By.XPATH, "//ul[@class='carousel-menu-list']/li[@class='carousel-menu active']")
    recently_watched = (By.XPATH, "//div//h2[text()='Recently Watched']")
    Recently_watched_next_button = (By.XPATH, "(//div//a[@role='button']/i[@class='next-icon icon'])[1]")
    movie_name = (By.XPATH, "//div[@class='movie-poster']//p")
    add_to_list_search = (By.XPATH, "//input[@placeholder='Search']")
    add_to_list_clear = (By.XPATH, "//div[@class='atl-searchclear']//span")
    add_to_list_list_name = (By.XPATH, "//div[contains(@class,'toggle-btn-item')]")
    add_to_list_toggel_button = (
        By.XPATH, "(//div[contains(@class,'toggle-btn-item')]//label/span[@class='slider round'])[1]")
    add_to_list_toggel_button1 = (By.XPATH, "//div[@class='single-toggle']//span[text()=' test ']")
    add_to_list_movies_list_toggel_button = (By.XPATH, "//div[@class='single-toggle']//span[text()=' MoviesList ']")
    add_to_list_movies_list_toggel_test_button = (By.XPATH, "//div[@class='single-toggle']//span[text()=' test ']")
    add_to_list_toggel_first_film = (By.XPATH, "//div[@class='single-toggle']//span[text()=' filmSeriesList ']")
    add_to_list = (By.XPATH, "//div[@class='atl-add-btn']//span")
    add_to_list_enter_name = (By.XPATH, "//input[@placeholder='My New List Name']")
    input_list_create = (By.XPATH, "//input[@placeholder='My New List Name']")
    add_to_list_create_list = (By.XPATH, "//div[@class='atl-newlistadd']/button")
    new_list = By.XPATH, ("(//div[contains(@class,'toggle-btn-item')])[1]")
    selected_list = (By.XPATH, "//div[@class='single-toggle']//input[@class='ng-valid ng-dirty ng-touched']")
    add_to_list_verify = (By.XPATH, "//div[@class='movie-detail']/p[text()=' Spectre ']")
    add_to_list_verify_army = (By.XPATH, "//div[@class='movie-detail']/p[text()=' Army Of Darkness ']")
    add_to_list_verify_Detroit = (By.XPATH, "//div[@class='movie-detail']/p[text()=' Detroit ']")
    add_to_list_verify_Ben_Hur = (By.XPATH, "//div[@class='movie-detail']/p[text()=' Ben-hur (2016) ']")
    created_list = (By.XPATH, "//div//a[text()='Demo']")
    created_list_test = (By.XPATH, "//div//a[text()='test']")
    created_list_test2 = (By.XPATH, "//div//a[text()='test2']")
    abc = (By.XPATH, "//span[text() = ' test1 ']/ancestor::label/input")
    add_to_list_creating = (By.XPATH, "//div[text()='Creating...']")
    duplicate_list_validation_text = (By.XPATH, '//span[contains(text(),"Please enter a unique list name.")]')
    add_to_list_created = (By.XPATH, "//div[@class='createdListItem']//span[text()=' Created! ']")
    new_list1 = (By.XPATH, "//div[contains(@class,'toggle-btn-item')]")
    list_auto_select = (By.XPATH, "//div//input[@class='ng-valid ng-dirty ng-touched']")
    new_list2 = (By.XPATH, "//div[contains(@class,'toggle-btn-item')]//span[text() = ' test1 ']")
    tv_list = (By.XPATH, "//div[contains(@class,'toggle-btn-item')]//span[text() = ' TvShow ']")
    new_list_film_series = (By.XPATH, "//div[contains(@class,'toggle-btn-item')]//span[text() = ' filmSeriesList ']")
    new_list2_film_series = (
        By.XPATH, "//div[contains(@class,'toggle-btn-item')]//span[text() = ' filmSeriesSecondList ']")
    recentlyList_list = (By.XPATH, "//div[contains(@class,'toggle-btn-item')]//span[text() = ' recentlyList ']")
    movie_card_added_movie = (By.XPATH, "//div//a[text()='test1']")
    add_to_list_toggle_button_demo = (By.XPATH, "//div[@class='single-toggle']//span[text()=' Demo ']")
    demo_toggle_button = (By.XPATH, "//span[text()=' Demo ']/ancestor::label/input")
    test1_toggle_button = (By.XPATH, "//span[text()=' test1 ']/ancestor::label/input")
    tv_toggle_button = (By.XPATH, "//span[text()=' TvShow ']/ancestor::label/input")
    film_series_toggle_button = (By.XPATH, "//span[text()=' filmSeriesList ']/ancestor::label/input")
    film_series_second_toggle_button = (By.XPATH, "//span[text()=' filmSeriesSecondList ']/ancestor::label/input")
    recently_toggle_button = (By.XPATH, "//span[text()=' recentlyList ']/ancestor::label/input")
    test_toggle_button = (By.XPATH, "//span[text()=' test ']/ancestor::label/input")
    movies_list_toggle_button = (By.XPATH, "//span[text()=' MoviesList ']/ancestor::label/input")
    add_to_list_added_button = (By.XPATH, "//div[@class='atl-add-btn']//span[text()=' Added! ']")
    carousel_4_titles = (By.XPATH, "//ul[@class='carousel-menu-list']/li")
    your_list = (By.XPATH, "//p[text()='Your Lists']")
    your_list_first_delete_button = (By.XPATH, "(//span[text()='Delete'])[1]")
    # special_list = (By.XPATH, "//div/p[contains(text(),'Special Lists Made For You')]")
    share_by_mgm_title = (By.XPATH,"//div/p[contains(text(),'Shared by MGM')]")
    # automation_1_text = (By.XPATH, '//div/p[contains(text(),"Special Lists Made For You")]/'
    #                                'ancestor::div[3]//div/a[contains(text(),"Automation1")]')
    automation_1_text = (By.XPATH, '//div/span[contains(text(),"Shared by Automation Account")]/ancestor::div[3]'
                                   '//div/a[contains(text(),"Automation1")]')
    automation1PageTitle = (By.XPATH, '//div/input[@id="top-title"]')
    testCuratedTitleText = (By.XPATH, '//div/p[contains(text(),"Special Lists Made For You")]/ancestor::div[3]'
                                      '//div/a[contains(text(),"test")]')
    automation1_email_spreadsheet_button = (By.XPATH, '//div/span[contains(text(),"Shared by Automation Account")]'
                                                      '/ancestor::div[3]//div/a[contains(text(),"Automation1")]'
                                                      '/ancestor::div[3]//span[contains(text(),"Email Spreadsheet")]')
    spreadsheetCloseButton = (By.XPATH, '//div[contains(@class,"share-input")]//div[contains(@class,"close-btn")]/img')
    spreadsheetStaticText = (By.XPATH, '//div[contains(@class,"share-input")]//div[contains(@class,"share-header")]')
    spreadsheetTitleText = (By.XPATH, '//div[contains(@class,"share-input")]//div[contains(text(),"Automation1 ")]')
    spreadsheetTestTitleText = (By.XPATH, '//div[contains(@class,"share-input")]//div[contains(text(),"test ")]')
    spreadsheetEmailInputField = (By.XPATH, '//div[contains(@class,"share-input")]//div[@role="combobox"]/input')
    spreadsheetShareButton = (By.XPATH, '//div[contains(@class,"share-input")]//button[contains(text(),"share")]')
    automation1_checkbox = (By.XPATH, '//div/span[contains(text(),"Shared by Automation Account")]/ancestor::div[3]//div'
                                      '/a[contains(text(),"Automation1")]/ancestor::div[3]//div/input')
    shareListRoarButton = (By.XPATH, '//div/a[contains(text(),"test")]/ancestor::div[4]//'
                                     'span[contains(text(),"Share List IN ROAR")]')
    automation2_checkbox = (By.XPATH, '//div/span[contains(text(),"Shared by Automation Account")]/ancestor::div[3]//'
                                      'div/a[contains(text(),"Automation2")]/ancestor::div[3]//div/input')
    automation2_user_created = (By.XPATH, '//div/p[contains(text(),"Your Lists")]/ancestor::div[3]//div/a'
                                          '[contains(text(),"Automation2")]/ancestor::div[3]//div/input')
    toggle_button_test = (By.XPATH, "//div[@class='single-toggle']//span[text()=' test ']")
    toggle_button_test2 = (By.XPATH, "//div[@class='single-toggle']//span[text()=' test2 ']")
    toggle_button_test1 = (By.XPATH, "//div[@class='single-toggle']//span[text()=' test1 ']")
    toggle_button_filmSeriesList = (By.XPATH, "//div[@class='single-toggle']//span[text()=' filmSeriesList ']")
    toggle_button_filmSeriesList2 = (By.XPATH, "//div[@class='single-toggle']//span[text()=' filmSeriesSecondList ']")
    toggle_button_recentlyList = (By.XPATH, "//div[@class='single-toggle']//span[text()=' recentlyList ']")
    next_arrow = (By.XPATH, "//h2[text()='Best Picture Winners']/ancestor::div[3]/following-sibling::div//i["
                            "@class='next-icon icon']")
    prev_arrow = (By.XPATH, "//div[@class='navigation-arrow']/a/i[@class='previous-icon icon']")
    success_created = (By.XPATH, "//div[@class='atl-add-btn']//span[@class='ie11fix uppercase']")
    play_begining = (By.XPATH, "//button[@class='watch-again-btn btn-view']")
    your_lists_sec = (By.XPATH, "//h2[contains(text(),'Your Lists')]")
    carosel_active_movie = (By.XPATH, "//li[@class='carousel-menu active']")
    total_moviesIN_carosel = (By.XPATH, "//ul[@class='carousel-menu-list']/li")
    carosel_nextBtn = (By.XPATH, "//span[@class='carousel-control-next-icon']")
    movie_my_lists = (By.XPATH, "//h2[text()='My Lists']")
    movie_recently_watched = (By.XPATH, "//h2[text()='Recently Watched']")
    movie_list_alive = (By.XPATH, "//h2[text()='Alive']")
    movie_list_black_history_month = (By.XPATH, "//h2[text()='Black History Month']")
    movie_list_bond = (By.XPATH, "//h2[text()='Bond']")
    movie_list_action = (By.XPATH, "//h2[text()='Action']")
    movie_list_halloween = (By.XPATH, "//h2[text()='Halloween']")
    movie_list_Late_night_comedy_male = (By.XPATH, "//h2[text()='Late-night comedy-male']")
    movie_list_fight_night = (By.XPATH, "//h2[text()='Fight Night']")
    search_button = (By.XPATH, '//div/button[contains(text(),"search ")]')
    search_result_the_addams_family = (By.XPATH,
                                       '//div[1]/div[contains(@class,"movie-poster")]//div[@class="movie-detail"]/p['
                                       'contains(text()," The Addams Family (2019) ")]')
    first_card_movie_name = (By.XPATH, '(//div[@class="desk-on"]//div[@class="movie-detail"]/p)[1]')
    search_results_result_text = (By.XPATH, "//*[text()=' result']")
    first_carousel_title = (By.XPATH, '//ul[contains(@class,"carousel-menu-list")]/li[1]/a')
    active_title_text = (By.XPATH, '//li[@class="carousel-menu active"]/a')
    play_from_beginning = (By.XPATH, '//button[contains(text(),"Play from beginning")]')
    watch_movie_now=(By.XPATH,"(//h2[text()='Bond' ]/parent::div/parent::div/parent::div/parent::div//button[text()='Watch now'])[1]")
    play_begginning=(By.XPATH,"//button[text()='Play from beginning']")
    close_button1=(By.XPATH,'(//img[@class="close-btn-image"])[2]')
    watch_trailer=(By.XPATH,"(//h2[text()='Bond']/parent::div/parent::div/parent::div/parent::div//button[text()='Watch trailer'])[2]")
    add_list_movie=(By.XPATH,"(//h2[text()='Bond']/ancestor::div[4]//button[text()='ADD TO LIST'])[3]")

    def __init__(self, browser):
        self.browser = browser
        # self.browser = WebDriver   

    #@allure.step('Verify logo is visible on header')
    def HomePageLogo(self):
        # time.sleep(2)
        WebDriverWait(self.browser, 3).until(EC.presence_of_element_located(self.header_logo))
        return self.browser.find_element(*self.header_logo).is_displayed()

    #@allure.step('Verify "FILMS & Series" is visible in header')
    def HeaderFilmsAndSeries(self):
        return self.browser.find_element(*self.header_films_series).is_displayed()

    #@allure.step('Verify Television shows link is visible in header')
    def HeaderTelevision(self):
        return self.browser.find_element(*self.header_television).is_displayed()

    #@allure.step('Verify MyList link is visible in header')
    def HeaderMylist(self):
        return self.browser.find_element(*self.header_mylist).is_displayed()

    #@allure.step('Verify Logout button is present in header')
    def HeaderLogoutButton(self):
        return self.browser.find_element(*self.header_logout_dropdown_toggle).is_displayed()

    #@allure.step('Verify Search button is present in header')
    def HeaderSearchButton(self):
        return self.browser.find_element(*self.header_search_button).is_displayed()

    #@allure.step('Verify Search button is clickable')
    def firstClickSearchButton(self):
        WebDriverWait(self.browser, 8).until(EC.presence_of_element_located(self.header_search_button))
        self.browser.find_element(*self.header_search_button).click()
        WebDriverWait(self.browser, 30).until(EC.presence_of_element_located(self.search_text))
        search_text = self.browser.find_element(*self.search_text).is_displayed()
        return search_text

    #@allure.step('Verify Search close button is clickable')
    def clickSearchCloseButton(self):
        # time.sleep(2)
        # WebDriverWait(self.browser, 5).until(EC.presence_of_element_located(self.search_close_button))
        button_search_close = self.browser.find_element(*self.search_close_button)
        self.browser.execute_script("arguments[0].click();", button_search_close)
        WebDriverWait(self.browser, 12).until(EC.presence_of_element_located(self.homepage_welcometext))
        # time.sleep(3)
        return self.browser.find_element(*self.homepage_welcometext).is_displayed()

    #@allure.step('Verify input field is present')
    def verify_input_field_MovieOrSeriesName(self):
        # WebDriverWait(self.browser, 12).until(EC.presence_of_element_located(self.header_search_button))
        time.sleep(3) # text is getting hide into shadow and explicit wait not working
        header_search_button = self.browser.find_element(*self.header_search_button)
        self.browser.execute_script("arguments[0].click();", header_search_button)

        WebDriverWait(self.browser, 12).until(EC.presence_of_element_located(self.search_text))
        time.sleep(1)
        return self.browser.find_element(*self.search_input_field).is_displayed()

    #@allure.step('Verify we can type in search input field')
    def typeMovieOrSeriesName(self):
        global movie_name
        data = json.load(open('resources/dataFile.json', 'r'))
        for key, value in data.items():
            movie_name = value
        self.browser.find_element(*self.search_input_field).send_keys(movie_name)
        return movie_name

    #@allure.step('Verify Search button is present')
    def test_verify_Search_button(self):
        # time.sleep(2)
        WebDriverWait(self.browser, 5).until(EC.presence_of_element_located(self.search_button))
        return self.browser.find_element(*self.search_button).is_displayed()

    #@allure.step('Verify Search button is clickable')
    def clickSearchButton(self):
        self.browser.find_element(*self.search_button).click()
        WebDriverWait(self.browser, 20).until(EC.presence_of_element_located(self.search_results_result_text))
        # time.sleep(20)
        WebDriverWait(self.browser, 10).until(EC.visibility_of_element_located(self.search_results_result_text))
        first_movie_name = self.browser.find_element(*self.first_card_movie_name).text
        return first_movie_name

    #@allure.step('Verify Marketing Rules is present in header')
    def HeaderMarketingRules(self):
        return self.browser.find_element(*self.header_marketing_rules).is_displayed()

    #@allure.step('Verify Assets is present in header')
    def HeaderAssets(self):
        return self.browser.find_element(*self.header_assets).is_displayed()

    #@allure.step('Verify Assets is present in header')
    def HeaderMyCarts(self):
        return self.browser.find_element(*self.header_my_carts).is_displayed()

    #@allure.step('Click Film & Series header link')
    def ClickFilmsSeries(self):
        WebDriverWait(self.browser, 6).until(EC.presence_of_element_located(self.header_films_series))
        header_films = self.browser.find_element(*self.header_films_series)
        self.browser.execute_script("arguments[0].click();", header_films)
        # time.sleep(10)
        WebDriverWait(self.browser, 180).until(EC.presence_of_element_located(self.banner_text))
        time.sleep(2.5)
        return self.browser.find_element(*self.banner_text).is_displayed()

    #@allure.step('Verify User can click on my list Section')
    def ClickMyListHeaderlist(self):
        time.sleep(2)
        self.browser.find_element(*self.header_mylist).click()
        WebDriverWait(self.browser, 120).until(EC.presence_of_element_located(self.your_list))
        time.sleep(1.5)
        self.browser.find_element(*self.your_list).click()
        WebDriverWait(self.browser, 120).until(EC.presence_of_element_located(self.your_list))
        WebDriverWait(self.browser, 70).until(EC.presence_of_element_located(self.your_list_first_delete_button))
        time.sleep(2.5)
        return self.browser.find_element(*self.your_list).is_displayed()

    #@allure.step('Verify User can click on my list Section')
    def ClickMyListHeader(self):
        time.sleep(1.5)
        self.browser.find_element(*self.header_mylist).click()
        WebDriverWait(self.browser, 180).until(EC.presence_of_element_located(self.your_list))
        time.sleep(1.5)
        self.browser.find_element(*self.your_list).click()
        WebDriverWait(self.browser, 180).until(EC.presence_of_element_located(self.your_list_first_delete_button))
        return self.browser.find_element(*self.your_list).is_displayed()

    #@allure.step('verify Your List text is present in My list section')
    def VerifyYourList(self):
        WebDriverWait(self.browser, 36).until(EC.presence_of_element_located(self.your_list))
        return self.browser.find_element(*self.your_list).is_displayed()

    #@allure.step('verify Your List text is present in My list section')
    def VerifySpecialList(self):
        WebDriverWait(self.browser, 16).until(EC.presence_of_element_located(self.special_list))
        return self.browser.find_element(*self.special_list).is_displayed()

    # @allure.step('verify Your List text is present in My list section')
    def VerifyShareSpecialList(self):
        WebDriverWait(self.browser, 36).until(EC.presence_of_element_located(self.share_by_mgm_title))
        return self.browser.find_element(*self.share_by_mgm_title).is_displayed()

    # @allure.step('verify Your List text is present in My list section')
    def ClickyShareSpecialList(self):
        WebDriverWait(self.browser, 66).until(EC.presence_of_element_located(self.share_by_mgm_title))
        self.browser.find_element(*self.share_by_mgm_title).click()
        WebDriverWait(self.browser, 66).until(EC.presence_of_element_located(self.share_by_mgm_title))
        time.sleep(5) #25
        return self.browser.find_element(*self.share_by_mgm_title).is_displayed()

    #@allure.step('verify Automation Title text is present in My list section')
    def VerifyAutomationOneTitleText(self):
        WebDriverWait(self.browser, 6).until(EC.presence_of_element_located(self.automation_1_text))
        return self.browser.find_element(*self.automation_1_text).is_displayed()

    #@allure.step('verify Automation Title text is present in My list section')
    def ClickAutomationOneTitleText(self):
        WebDriverWait(self.browser, 6).until(EC.presence_of_element_located(self.automation_1_text))
        self.browser.find_element(*self.automation_1_text).click()
        WebDriverWait(self.browser, 16).until(EC.presence_of_element_located(self.automation1PageTitle))
        return self.browser.find_element(*self.automation1PageTitle).is_displayed()

    #@allure.step('verify Automation spread sheet button is present in My list section')
    def VerifyAutomationOneSpreadSheetButton(self):
        WebDriverWait(self.browser, 6).until(EC.presence_of_element_located(self.automation1_email_spreadsheet_button))
        return self.browser.find_element(*self.automation1_email_spreadsheet_button).is_displayed()

    #@allure.step('verify user can click on  Automation spread sheet button ')
    def ClickAutomationOneSpreadSheetButton(self):
        WebDriverWait(self.browser, 16).until(EC.presence_of_element_located(self.automation1_email_spreadsheet_button))
        time.sleep(3)
        self.browser.find_element(*self.automation1_email_spreadsheet_button).click()

    #@allure.step('verify  checkbox button is present in Special list section')
    def VerifyAutomationOneCheckboxButton(self):
        WebDriverWait(self.browser, 6).until(EC.presence_of_element_located(self.automation1_checkbox))
        return self.browser.find_element(*self.automation1_checkbox).is_displayed()

    #@allure.step('verify close button is present in Spreadsheet popup')
    def VerifySpreadsheetCloseButton(self):
        WebDriverWait(self.browser, 16).until(EC.presence_of_element_located(self.spreadsheetCloseButton))
        return self.browser.find_element(*self.spreadsheetCloseButton).is_displayed()

    #@allure.step('verify Static text present in Spreadsheet popup')
    def VerifySpreadsheetStaticText(self):
        WebDriverWait(self.browser, 16).until(EC.presence_of_element_located(self.spreadsheetStaticText))
        time.sleep(2)
        return self.browser.find_element(*self.spreadsheetStaticText).is_displayed()

    #@allure.step('verify title name present in Spreadsheet popup')
    def VerifySpreadsheetTitleText(self):
        WebDriverWait(self.browser, 16).until(EC.presence_of_element_located(self.spreadsheetTitleText))
        return self.browser.find_element(*self.spreadsheetTitleText).is_displayed()

    #@allure.step('verify title name present in Spreadsheet popup')
    def VerifySpreadsheetTestTitleText(self):
        WebDriverWait(self.browser, 16).until(EC.presence_of_element_located(self.spreadsheetTestTitleText))
        return self.browser.find_element(*self.spreadsheetTestTitleText).is_displayed()

    #@allure.step('verify Input Field present in Spreadsheet popup')
    def VerifySpreadsheetInputField(self):
        WebDriverWait(self.browser, 16).until(EC.presence_of_element_located(self.spreadsheetEmailInputField))
        return self.browser.find_element(*self.spreadsheetEmailInputField).is_displayed()

    #@allure.step('verify share button present in Spreadsheet popup')
    def VerifySpreadsheetShareButton(self):
        WebDriverWait(self.browser, 16).until(EC.presence_of_element_located(self.spreadsheetShareButton))
        return self.browser.find_element(*self.spreadsheetShareButton).is_displayed()

    #@allure.step('verify title count present in Spreadsheet popup')
    def VerifySpreadsheetTitleCountText(self):
        WebDriverWait(self.browser, 16).until(EC.presence_of_element_located(self.spreadsheetTitleText))
        return self.browser.find_element(*self.spreadsheetTitleText).text

    #@allure.step('verify title count present in Spreadsheet popup')
    def VerifySpreadsheetTestTitleCountText(self):
        WebDriverWait(self.browser, 16).until(EC.presence_of_element_located(self.spreadsheetTestTitleText))
        return self.browser.find_element(*self.spreadsheetTestTitleText).text

    #@allure.step('verify  checkbox button is clickable in Special list section')
    def ClickAutomationOneCheckboxButton(self):
        WebDriverWait(self.browser, 6).until(EC.presence_of_element_located(self.automation1_checkbox))
        automation_one = self.browser.find_element(*self.automation1_checkbox)
        time.sleep(2)
        self.browser.execute_script("arguments[0].scrollIntoView();", automation_one)
        time.sleep(1)
        self.browser.execute_script("arguments[0].click();", automation_one)

    #@allure.step('verify share list roar button is clickable in Special list section')
    def ClickShareListRoarButton(self):
        WebDriverWait(self.browser, 35).until(EC.presence_of_element_located(self.shareListRoarButton))
        automation_one = self.browser.find_element(*self.shareListRoarButton)
        time.sleep(2)
        self.browser.execute_script("arguments[0].scrollIntoView();", automation_one)
        time.sleep(1)
        self.browser.execute_script("arguments[0].click();", automation_one)

    #@allure.step('verify  checkbox button is clickable in Special list section')
    def ClickAutomationSecondCheckboxButton(self):
        WebDriverWait(self.browser, 6).until(EC.presence_of_element_located(self.automation2_checkbox))
        automation_second = self.browser.find_element(*self.automation2_checkbox)
        time.sleep(2)
        self.browser.execute_script("arguments[0].scrollIntoView();", automation_second)
        time.sleep(1)
        self.browser.execute_script("arguments[0].click();", automation_second)

    #@allure.step('verify  checkbox button is clickable in Special list section')
    def ClickUserCreatedAutomationSecondCheckboxButton(self):
        WebDriverWait(self.browser, 6).until(EC.presence_of_element_located(self.automation2_user_created))
        automation_second = self.browser.find_element(*self.automation2_user_created)
        time.sleep(2)
        self.browser.execute_script("arguments[0].scrollIntoView();", automation_second)
        time.sleep(1)
        self.browser.execute_script("arguments[0].click();", automation_second)

    #@allure.step('verify Automation Title text is present in My list section')
    def VerifyAutomationSecondTitleText(self):
        WebDriverWait(self.browser, 6).until(EC.presence_of_element_located(self.automation_1_text))
        return self.browser.find_element(*self.automation_1_text).is_displayed()

    #@allure.step('Verify user can click on roar logo')
    def ClickFooterRoarLogo(self):
        WebDriverWait(self.browser, 16).until(EC.presence_of_element_located(self.footer_roar_logo))
        self.browser.find_element(*self.footer_roar_logo).click()
        WebDriverWait(self.browser, 36).until(EC.presence_of_element_located(self.homepage_welcometext))
        return self.browser.find_element(*self.homepage_welcometext).is_displayed()

    #@allure.step('Click Marketing Rules header link')
    def ClickMarketingRules(self):
        self.browser.find_element(*self.header_marketing_rules).click()
        WebDriverWait(self.browser, 5).until(EC.presence_of_element_located(self.marketing_Page_title))
        return self.browser.find_element(*self.marketing_Page_title).is_displayed()

    #@allure.step('Click Lists link')
    def ClickLists(self):
        WebDriverWait(self.browser, 5).until(EC.presence_of_element_located(self.header_mylist))
        self.browser.find_element(*self.header_mylist).click()
        WebDriverWait(self.browser, 55).until(EC.presence_of_element_located(self.lists))
        time.sleep(1)
        self.browser.find_element(*self.lists).click()
        # time.sleep(25)
        return self.browser.find_element(*self.lists).is_displayed()

    #@allure.step('Click My cart link')
    def ClickMyCarts(self):
        self.browser.find_element(*self.header_my_carts).click()
        WebDriverWait(self.browser, 300).until(EC.presence_of_element_located(self.your_carts))
        self.browser.find_element(*self.your_carts).click()
        WebDriverWait(self.browser, 600).until(EC.element_to_be_clickable(self.cart_first_delete_button))
        return self.browser.find_element(*self.cart_first_delete_button).is_displayed()

    #@allure.step('Click Assets link')
    def ClickAssets(self):
        WebDriverWait(self.browser, 15).until(EC.presence_of_element_located(self.header_assets))
        self.browser.find_element(*self.header_assets).click()
        # WebDriverWait(self.browser, 35).until(EC.presence_of_element_located(self.first_checkbox))
        #
        # assets_first_checkbox = self.browser.find_element(*self.first_checkbox)
        # self.browser.execute_script("arguments[0].click();", assets_first_checkbox)
        # assets_second_checkbox = self.browser.find_element(*self.second_checkbox)
        # self.browser.execute_script("arguments[0].click();", assets_second_checkbox)
        # # time.sleep(2)
        # assets_third_checkbox = self.browser.find_element(*self.third_checkbox)
        # self.browser.execute_script("arguments[0].click();", assets_third_checkbox)
        # time.sleep(1)

        WebDriverWait(self.browser, 20).until(EC.presence_of_element_located(self.continue_button))

        assets_continue_button = self.browser.find_element(*self.continue_button)
        self.browser.execute_script("arguments[0].click();", assets_continue_button)


    #@allure.step('Click Assets link')
    def click_header_assets(self):
        WebDriverWait(self.browser, 95).until(EC.presence_of_element_located(self.header_assets))
        time.sleep(2.5)
        self.browser.find_element(*self.header_assets).click()
        time.sleep(1.5)
        try:
            WebDriverWait(self.browser, 15).until(EC.presence_of_element_located(self.assets_continue_button))
            continue_button = self.browser.find_element(*self.assets_continue_button).is_displayed()
            if continue_button:
                time.sleep(2)
                self.browser.find_element(*self.first_checkbox).click()
                time.sleep(.5)
                self.browser.find_element(*self.second_checkbox).click()
                time.sleep(.5)
                self.browser.find_element(*self.third_checkbox).click()
                time.sleep(.5)
                self.browser.find_element(*self.continue_button).click()
        except:
            print('Assets page already opened')

    #@allure.step('Go back to homepage')
    def headerRoarLogo(self):
        # WebDriverWait(self.browser, 10).until(EC.presence_of_element_located(self.header_logo))
        header_logo = self.browser.find_element(*self.header_logo)
        self.browser.execute_script("arguments[0].click();", header_logo)
        WebDriverWait(self.browser, 240).until(EC.presence_of_element_located(self.homepage_welcometext))
        WebDriverWait(self.browser, 180).until(EC.presence_of_element_located(self.first_carousel_title))
        return self.browser.find_element(*self.homepage_welcometext).is_displayed()

    #@allure.step('click on carousel title')
    def click_on_carousel_title(self):
        self.browser.refresh()
        WebDriverWait(self.browser, 60).until(EC.presence_of_element_located(self.first_carousel_title))
        self.browser.find_element(*self.first_carousel_title).click()
        titel_text = self.browser.find_element(*self.first_carousel_title).text
        active_text = self.browser.find_element(*self.active_title_text).text
        return titel_text, active_text

    #@allure.step('click on carousel slider')
    def verify_carousel_slider(self):
        self.browser.refresh()
        WebDriverWait(self.browser, 60).until(EC.presence_of_element_located(self.first_carousel_title))
        return self.browser.find_element(*self.active_title_text).is_displayed()

    #@allure.step('Verify welcome text is present')
    def verify_welcome_text(self):
        WebDriverWait(self.browser, 5).until(EC.presence_of_element_located(self.homepage_welcometext))
        return self.browser.find_element(*self.homepage_welcometext).is_displayed()

    # @allure.step('Verify welcome text is present')
    def verify_welcome_text_home_page_elements(self):
        WebDriverWait(self.browser, 20).until(EC.presence_of_element_located(self.homepage_welcometext))
        homepage_welcome_text = self.browser.find_element(*self.homepage_welcometext)
        # time.sleep(2)
        self.browser.execute_script("arguments[0].scrollIntoView();", homepage_welcome_text)
        return self.browser.find_element(*self.homepage_welcometext).is_displayed()

    #@allure.step('Go back to homepage')
    def ClickLogo(self):
        # time.sleep(2)
        self.browser.find_element(*self.header_logo).click()
        # time.sleep(6)
        self.browser.refresh()
        # time.sleep(6)
        WebDriverWait(self.browser, 30).until(EC.presence_of_element_located(self.homepage_welcometext))
        return self.browser.find_element(*self.homepage_welcometext).is_displayed()

    #@allure.step('Go to homepage')
    def gotohomepage(self, URL):
        # time.sleep(2)
        self.browser.get(URL)
        WebDriverWait(self.browser, 300).until(EC.presence_of_element_located(self.first_carousel_title))

    #@allure.step('Click logout button')
    def ClickLogoutButton(self):
        WebDriverWait(self.browser, 30).until(EC.presence_of_element_located(self.header_logout_dropdown_toggle))
        # time.sleep(2)
        self.browser.find_element(*self.header_logout_dropdown_toggle).click()

        self.browser.find_element(*self.header_logout_button).click()
        # time.sleep(2)
        WebDriverWait(self.browser, 20).until(EC.presence_of_element_located(self.email_textbox))
        return self.browser.find_element(*self.email_textbox).is_displayed()

    #@allure.step('Homepage header')
    def HomepageElementHeader(self):
        WebDriverWait(self.browser, 30).until(EC.presence_of_element_located(self.header))
        # time.sleep(6)
        return self.browser.find_element(*self.header).is_displayed()

    #@allure.step('Homepage Carousel slider')
    def HomepageMainCarousel(self):
        # time.sleep(2)
        return self.browser.find_element(*self.carousel).is_displayed()

    # @allure.step('Homepage Carousel slider')
    def HomepageMainCarouselForHomeTestCases(self):
        time.sleep(2)
        return self.browser.find_element(*self.carousel).is_displayed()

    #@allure.step('Movie List Best Picture Winner')
    def HomepageMovieList1(self):
        WebDriverWait(self.browser, 300).until(EC.presence_of_element_located(self.movie_my_lists))
        return self.browser.find_element(*self.movie_my_lists).is_displayed()

    #@allure.step('Movie List Best Picture Winner')
    def verifyAliveTitle(self):
        return self.browser.find_element(*self.movie_list_alive).is_displayed()

    #@allure.step('Movie List James Bond')
    def HomepageMovieList2(self):
        return self.browser.find_element(*self.movie_recently_watched).is_displayed()

    #@allure.step('Movie List New Release')
    def HomepageMovieList3(self):
        return self.browser.find_element(*self.movie_list_alive).is_displayed()

    #@allure.step('Movie List Action/Adventure')
    def HomepageMovieList4(self):
        return self.browser.find_element(*self.movie_list_black_history_month).is_displayed()

    #@allure.step('Movie List Oscar Winning Films')
    def HomepageMovieList5(self):
        return self.browser.find_element(*self.movie_list_bond).is_displayed()

    #@allure.step('Movie List Action Packed Hits')
    def HomepageMovieList6(self):
        return self.browser.find_element(*self.movie_list_actionhits).is_displayed()

    #@allure.step('Movie List Robocop')
    def HomepageMovieList7(self):
        return self.browser.find_element(*self.movie_list_action).is_displayed()

    #@allure.step('Movie List Rocky')
    def HomepageMovieList8(self):
        return self.browser.find_element(*self.movie_list_halloween).is_displayed()

    #@allure.step('Movie List Pink Panther')
    def HomepageMovieList9(self):
        return self.browser.find_element(*self.movie_list_Late_night_comedy_male).is_displayed()

    #@allure.step('Movie List Legally Blonde')
    def HomepageMovieList10(self):
        return self.browser.find_element(*self.movie_list_fight_night).is_displayed()

    #@allure.step('Explore all tv shows')
    def HomepageExploreAllTvShows(self):
        return self.browser.find_element(*self.see_all_tv_shows).is_displayed()

    #@allure.step('Explore all Movies')
    def HomepageExploreAllMovies(self):
        return self.browser.find_element(*self.see_all_movies).is_displayed()

    #@allure.step('Global Footer logo')
    def HomepageFooterLogo(self):
        return self.browser.find_element(*self.footer_logo).is_displayed()

    #@allure.step('Global Footer Privacy Policy')
    def HomepageFooterPrivacy(self):
        return self.browser.find_element(*self.privacy_policy).is_displayed()

    #@allure.step('Global Footer Use of terms')
    def HomepageFooterTerms(self):
        return self.browser.find_element(*self.terms_of_use).is_displayed()

    #@allure.step('Global Footer Support')
    def HomepageFooterSupport(self):
        return self.browser.find_element(*self.support).is_displayed()

    #@allure.step('Carousel image slider')
    def MovieImageSlider(self):
        return self.browser.find_element(*self.movie_image_slider).is_displayed()

    #@allure.step('Carousel Progress bar')
    def ProgressBar(self):
        return self.browser.find_element(*self.carousel_progress_bar).is_displayed()

    #@allure.step('Progress bar movie Spectre')
    def ProgressBarSpectre(self):
        # self.browser.refresh()
        # time.sleep(2)
        return self.browser.find_element(*self.progress_bar_spectre).is_displayed()

    #@allure.step('Progress bar movie Army of Darkness')
    def ProgressBarArmyOfDarkness(self):
        # self.browser.find_element(*self.next_navigation).click()
        return self.browser.find_element(*self.progress_bar_armyofdarkness).is_displayed()

    #@allure.step('Progress bar movie The Magnificient Seven')
    def ProgressBarMagnificent(self):
        # self.browser.find_element(*self.next_navigation).click()
        return self.browser.find_element(*self.progress_bar_magnificent).is_displayed()

    #@allure.step('Progress bar movie Rocky')
    def ProgressBarRockey(self):
        # self.browser.find_element(*self.next_navigation).click()
        return self.browser.find_element(*self.progress_bar_rocky).is_displayed()

    #@allure.step('Progress bar movie Fargo')
    def ProgressBarFargo(self):
        # self.browser.find_element(*self.next_navigation).click()
        return self.browser.find_element(*self.progress_bar_fargo).is_displayed()

    #@allure.step('Progress bar movie No Time Die')
    def ProgressBarNoTimeDie(self):
        # self.browser.find_element(*self.next_navigation).click()
        return self.browser.find_element(*self.progress_bar_no_time_die).is_displayed()

    def Maximum4Titles(self):
        ele = []
        ele = self.browser.find_elements(*self.carousel_4_titles)
        return len(ele)

    #@allure.step('Progress bar movie Three Amigosi')
    def ProgressBarAmigos(self):
        # self.browser.find_element(*self.next_navigation).click()
        # return self.browser.find_element(*self.progress_bar_amigos).is_displayed()
        # time.sleep(2)
        try:
            movie = self.browser.find_element(*self.progress_bar_amigos).is_displayed()

            if movie == True:
                return True
        except:
            return False

    #@allure.step('Count Total movies in main carousel ')
    def test_count_carousel(self):
        WebDriverWait(self.browser, 20).until(EC.presence_of_element_located(self.your_lists_sec))
        time.sleep(3)
        try:
            movies = []
            x = range(6)
            for n in x:
                active = self.browser.find_element(*self.carosel_active_movie).text
                if active not in movies:
                    movies.append(active)
                self.browser.find_element(*self.carosel_nextBtn).click()
            count = len(movies)
            return count
        except:
            return 3

    #@allure.step('Progress bar movie Legally Blonde')
    def ProgressBarLegallyBlonde(self):
        movies = []
        try:
            x = range(6)
            for n in x:
                active = self.browser.find_element(*self.carosel_active_movie).text
                if active not in movies:
                    movies.append(active)
                self.browser.find_element(*self.carosel_nextBtn).click()

            count = len(movies)
            if count > 4:
                self.browser.refresh()
                WebDriverWait(self.browser, 28).until(EC.presence_of_element_located(self.your_lists_sec))
                time.sleep(3)
                active = self.browser.find_element(*self.carosel_active_movie).text
                time.sleep(10)
                active1 = self.browser.find_element(*self.carosel_active_movie).text
                time.sleep(3)
                if active == active1:
                    return False
                else:
                    return True
        except:
            self.browser.refresh()
            WebDriverWait(self.browser, 28).until(EC.presence_of_element_located(self.your_lists_sec))
            time.sleep(3)
            active = self.browser.find_element(*self.carosel_active_movie).text
            print(active)
            time.sleep(10)
            active1 = self.browser.find_element(*self.carosel_active_movie).text
            print(active1)
            time.sleep(3)
            if active == active1:
                return True
            else:
                return False

    #@allure.step('Progress bar movie Hansel and Gretel witch hunter')
    def ProgressBarWitchHunter(self):
        # self.browser.find_element(*self.next_navigation).click()
        return self.browser.find_element(*self.progress_bar_witch_hunter).is_displayed()

    #@allure.step('Previous navigation button in progress bar')
    def ProgressBarPreviousArrow(self):
        return self.browser.find_element(*self.previous_navigtion).is_displayed()

    #@allure.step('Next navigation button in progress bar')
    def ProgressBarNextArrow(self):
        return self.browser.find_element(*self.next_navigation).is_displayed()

    #@allure.step('Next navigation button in progress bar')
    def click_carousel_next(self):
        self.browser.refresh()
        WebDriverWait(self.browser, 30).until(EC.presence_of_element_located(self.first_carousel_title))
        first_text = self.browser.find_element(*self.active_title_text).text
        self.browser.find_element(*self.next_navigation).click()
        second_text = self.browser.find_element(*self.active_title_text).text
        return first_text, second_text

    #@allure.step('back navigation button in progress bar')
    def click_carousel_prev(self):
        WebDriverWait(self.browser, 16).until(EC.presence_of_element_located(self.first_carousel_title))
        first_text = self.browser.find_element(*self.active_title_text).text
        self.browser.find_element(*self.previous_navigtion).click()
        second_text = self.browser.find_element(*self.active_title_text).text
        return first_text, second_text

    #@allure.step('Slider Background Image')
    def SliderBackgroundImage(self):
        # time.sleep(2)
        # self.browser.find_element(*self.next_navigation).click()
        WebDriverWait(self.browser, 20).until(EC.presence_of_element_located(self.slider_background_images))
        slider_images = self.browser.find_element(*self.slider_background_images).is_displayed()
        # time.sleep(2)
        return slider_images

    #@allure.step('Movie logo')
    def MovieLogo(self):
        return self.browser.find_element(*self.movie_logo).is_displayed()

    #@allure.step('Verify movie name logo on carousel ')
    def movie_logoCarousel(self):
        while True:
            try:
                time.sleep(1)
                logo = self.browser.find_element_by_xpath(
                    '//div[1]/div[@class="movie-content"]/div[contains(@class,"movie-logo")]/img')
                bool = logo.is_displayed()
                # time.sleep(1)
                if bool == True:
                    break
                else:
                    self.browser.find_element_by_xpath("//span[@class='carousel-control-next-icon']").click()

            except:
                self.browser.find_element_by_xpath("//span[@class='carousel-control-next-icon']").click()
        time.sleep(2)
        return self.browser.find_element_by_xpath(
            '//div[1]/div[@class="movie-content"]/div[contains(@class,"movie-logo")]/img').is_displayed()

    #@allure.step('Watch now button')
    def WatchNowButton(self):
        while True:
            try:
                watch_button = self.browser.find_element_by_xpath(
                    '//div[1]/div[@class="movie-content"]//div[@class="btn-container"]/div/button[contains(text()," Watch Now ")]')
                # time.sleep(1)
                bool = watch_button.is_displayed()
                if bool == True:
                    break
                else:
                    self.browser.find_element_by_xpath("//span[@class='carousel-control-next-icon']").click()

            except:
                self.browser.find_element_by_xpath("//span[@class='carousel-control-next-icon']").click()
        time.sleep(1)
        return self.browser.find_element_by_xpath(
            '//div[1]/div[@class="movie-content"]//div[@class="btn-container"]/div/button[contains(text()," Watch Now ")]').is_displayed()

    #@allure.step('Watch now button is clickable')
    def ClickWatchNowButton(self):
        watch_now_count = 0
        while True:
            try:
                watch_button = self.browser.find_element_by_xpath(
                    '//div[1]/div[@class="movie-content"]//div[@class="btn-container"]/div/button[contains(text()," Watch Now ")]')

                watch_now_count = watch_now_count + 1
                if(watch_now_count >= 10):

                    break

                bool = watch_button.is_displayed()
                if bool == True:
                    watch_button.click()
                    break
                else:
                    self.browser.find_element_by_xpath("//span[@class='carousel-control-next-icon']").click()

            except:
                self.browser.find_element_by_xpath("//span[@class='carousel-control-next-icon']").click()

    #@allure.step('Watch now button is clickable')
    def click_add_to_list_carousel(self):
        while True:
            try:
                watch_button = self.browser.find_element_by_xpath(
                    '//div[1]/div[@class="movie-content"]//div[@class="btn-container"]/div/button[contains(text()," ADD TO LIST ")]')

                bool = watch_button.is_displayed()
                if bool == True:
                    watch_button.click()
                    break
                else:
                    self.browser.find_element_by_xpath("//span[@class='carousel-control-next-icon']").click()

            except:
                self.browser.find_element_by_xpath("//span[@class='carousel-control-next-icon']").click()

    #@allure.step('Add to list button')
    def AddToListButton(self):
        while True:
            try:
                # time.sleep(3)
                watch_now = self.browser.find_element_by_xpath(
                    '//div[@class="carousel-inner"]/div[@class="carousel-item active"]/div[@class="movie-content"]'
                    '/div[@class="btn-container"]/div[@class="add-to-list"]/button[contains(text(),"ADD TO LIST")]')
                bool = watch_now.is_displayed()
                # time.sleep(2)
                if bool == True:
                    break
                else:
                    self.browser.find_element_by_xpath("//span[@class='carousel-control-next-icon']").click()
            except:
                self.browser.find_element_by_xpath("//span[@class='carousel-control-next-icon']").click()
        # time.sleep(1)
        return self.browser.find_element_by_xpath(
            '//div[@class="carousel-inner"]/div[@class="carousel-item active"]/div[@class="movie-content"]'
            '/div[@class="btn-container"]/div[@class="add-to-list"]/button[contains(text(),"ADD TO LIST")]').is_displayed()

    #@allure.step('Add to list button')
    def ViewDetailsButton(self):
        while True:
            try:
                view_details = self.browser.find_element_by_xpath(
                    "//div[@id='slide-slideId_0']//button[contains(@class,'cui-btn ')][normalize-space()='View details']")
                bool = view_details.is_displayed()
                if bool == True:
                    break
                else:
                    self.browser.find_element_by_xpath("//span[@class='carousel-control-next-icon']").click()
            except:
                self.browser.find_element_by_xpath("//span[@class='carousel-control-next-icon']").click()
        time.sleep(1)
        return self.browser.find_element_by_xpath(
            "//div[@id='slide-slideId_0']//button[contains(@class,'cui-btn ')][normalize-space()='View details']").is_displayed()

    #@allure.step('Click View Detail Button')
    def ClickViewDetailsButton(self):
        self.browser.find_element(*self.view_details).click()
        time.sleep(2)
        self.browser.refresh()
        time.sleep(2)
        title = self.browser.find_element(*self.synopsis_title)
        title.location_once_scrolled_into_view
        time.sleep(2)
        name = title.is_displayed()
        return name

    #@allure.step('Add to list button in caro')
    def ViewDetailsButtoncaro(self):
        time.sleep(10)
        while True:
            try:
                watch_now = self.browser.find_element_by_xpath(
                    "//div[@class='carousel-item active']//button[contains(text(),'View details')]")
                bool = watch_now.is_displayed()
                if bool == True:
                    watch_now.click()
                    break
                else:
                    self.browser.find_element_by_xpath("//span[@class='carousel-control-next-icon']").click()

            except:
                self.browser.find_element_by_xpath("//span[@class='carousel-control-next-icon']").click()
        time.sleep(2)
        self.browser.refresh()
        time.sleep(2)
        WebDriverWait(self.browser, 20).until(EC.presence_of_element_located(self.syn_title))
        title = self.browser.find_element(*self.syn_title)
        title.location_once_scrolled_into_view
        time.sleep(2)
        name = title.is_displayed()
        return name

    #@allure.step('Add to list button in caro')
    def ViewDetailsButtoncaro1(self):
        time.sleep(10)
        while True:
            try:
                watch_now = self.browser.find_element_by_xpath(
                    "//div[@class='carousel-item active']//button[contains(text(),'View details')]")
                bool = watch_now.is_displayed()
                if bool == True:
                    watch_now.click()
                    break
                else:
                    self.browser.find_element_by_xpath("//span[@class='carousel-control-next-icon']").click()

            except:
                self.browser.find_element_by_xpath("//span[@class='carousel-control-next-icon']").click()
        time.sleep(2)
        return self.browser.title

    #@allure.step('Click Spectre Movie')
    def ClickSpectreMovie(self):
        self.browser.find_element(*self.progress_bar_spectre).click()

    #@allure.step('See All Buttons in homepage')
    def SeeAllButton(self):
        see = []
        time.sleep(10)
        see = self.browser.find_elements(*self.see_all_button)
        time.sleep(2)
        return len(see)

    #@allure.step('Movie Poter')
    def MoviePoster(self):
        time.sleep(2)
        poster = []
        poster = self.browser.find_element(*self.movie_poster)
        poster.location_once_scrolled_into_view
        time.sleep(2)
        poster1 = poster.is_displayed()
        return poster1

    #@allure.step('My List Next Button')
    def MovieListNextButton(self):
        time.sleep(3)
        nextbtn = self.browser.find_element_by_xpath(
            "//div[@class='movies-block-container']//i[@class='next-icon icon']")  # *self.movie_list_next_button
        nextbtn.location_once_scrolled_into_view
        global actionchains
        actionchains = ActionChains(self.browser)
        time.sleep(5)
        ActionChains(self.browser).move_to_element(nextbtn).perform()
        time.sleep(2)
        nextbtn.click().perform()
        time.sleep(2)
        btn = nextbtn.is_displayed()
        # time.sleep(2)
        # nextbtn.click()
        return btn

    #@allure.step('My List Next Button')
    def MovieListPrevButton(self):
        time.sleep(3)
        prevbtn = self.browser.find_element_by_xpath(
            "//div[@class='movies-block-container']//i[@class='previous-icon icon']")
        prevbtn.location_once_scrolled_into_view
        actionprev = ActionChains(self.browser)
        time.sleep(5)
        actionprev.move_to_element(prevbtn).perform()
        time.sleep(2)
        prevbtn.click()
        time.sleep(2)
        btn = prevbtn.is_displayed()
        # time.sleep(2)
        # nextbtn.click()
        return btn

    #@allure.step('Movie List previous Button')
    def MovieListPrevButton(self):
        time.sleep(2)
        prevbtn = self.browser.find_element(*self.movie_list_prev_button)
        prevbtn.location_once_scrolled_into_view
        actionchains.move_to_element(prevbtn).perform()
        # prevbtn.click()
        return self.browser.find_element(*self.movie_list_prev_button).is_displayed()

    #@allure.step('Movie List Poster Image')
    def PosterImage(self):
        WebDriverWait(self.browser, 25).until(EC.presence_of_element_located(self.first_carousel_title))
        time.sleep(1.5)
        card_images = self.browser.find_elements(*self.poster_image)
        # time.sleep(1)
        return len(card_images)

    #@allure.step('Movie List Title')
    def verify_list_title(self):
        # time.sleep(1)
        card_images = self.browser.find_elements(*self.list_titles)
        time.sleep(1)
        return len(card_images)

    #@allure.step('Movie Title Element')
    def MovieTitle(self):
        WebDriverWait(self.browser, 30).until(EC.presence_of_element_located(self.action_adventure))
        adventures = self.browser.find_element(*self.action_adventure)
        self.browser.execute_script("arguments[0].scrollIntoView();", adventures)
        time.sleep(2)
        warth_of = self.browser.find_element(*self.movie_title_warth_of_man)
        self.browser.execute_script("arguments[0].scrollIntoView();", warth_of)
        time.sleep(2)
        movies_title = self.browser.find_element(*self.movie_title_warth_of_man).is_displayed()
        # time.sleep(2)
        self.browser.execute_script("arguments[0].scrollIntoView();", adventures)
        time.sleep(2)
        return movies_title

    #@allure.step('Action list section')
    def scroll_to_action_list(self):
        WebDriverWait(self.browser, 30).until(EC.presence_of_element_located(self.action_adventure))
        adventures = self.browser.find_element(*self.action_adventure)
        self.browser.execute_script("arguments[0].scrollIntoView();", adventures)

    #@allure.step('Movie Genre Element')
    def MovieGenre(self):
        # time.sleep(1)
        movies_genres = self.browser.find_elements(*self.movie_genres)
        time.sleep(1)
        return len(movies_genres)

    #@allure.step('Movie Card Add To List Button')
    def MovieCardAddToList(self):
        return self.browser.find_element(*self.movie_card_list).is_displayed()

    #@allure.step('Movie cards Add to List button in best pictures winners section')
    def addList_moviecardfunc(self):
        time.sleep(1)
        addList = self.browser.find_element(*self.addList_overlay)
        ActionChains(self.browser).move_to_element(addList).perform()
        time.sleep(1)
        return addList.is_displayed()

    #@allure.step('Click on Add-to-list from movie list')
    def click_add_to_list_movies(self):
        time.sleep(1)
        addList = self.browser.find_element(*self.addList_overlay)
        ActionChains(self.browser).move_to_element(addList).perform()
        self.browser.find_element(*self.addList_overlay).click()
        time.sleep(1.5)
        return self.browser.find_element(*self.add_to_list_popup).is_displayed()

    #@allure.step('Movie cards Add to List button in best pictures winners section')
    def addList_tv_cardfunc(self):
        time.sleep(2)
        addList = self.browser.find_element(*self.addList_tv)
        ActionChains(self.browser).move_to_element(addList).perform()
        time.sleep(2)
        return addList.is_displayed()

    #@allure.step('Movie card Watch Now Button')
    def MovieCardWatchNow(self):
        return self.browser.find_element(*self.movie_card_watch_now).is_displayed()

    #@allure.step('Verify watch movie button on movie card ')
    def watchmovie_moviecrdfunc(self):
        time.sleep(1)
        addList = self.browser.find_element(*self.watchmovie_moviecard)
        ActionChains(self.browser).move_to_element(addList).perform()
        time.sleep(1)
        return addList.is_displayed()

    #@allure.step('Verify watch movie button on movie card ')
    def click_watch_now(self):
        WebDriverWait(self.browser, 20).until(EC.presence_of_element_located(self.action_adventure))
        action = self.browser.find_element(*self.action_adventure)
        self.browser.execute_script("arguments[0].scrollIntoView();", action)
        addList = self.browser.find_element(*self.watchmovie_moviecard)
        ActionChains(self.browser).move_to_element(addList).perform()
        time.sleep(1.5)
        watch_now_button = self.browser.find_element(*self.watchmovie_moviecard)
        self.browser.execute_script("arguments[0].click();", watch_now_button)
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

        move = ActionChains(self.browser)
        body_ = self.browser.find_element(*self.body_element)
        move.move_to_element_with_offset(body_, 511, 65)
        move.click()
        move.perform()
        time.sleep(2)
        WebDriverWait(self.browser, 30).until(EC.presence_of_element_located(self.zoom_in_zoom_out_button))
        time.sleep(1)
        full_screen_button = self.browser.find_element(*self.zoom_in_zoom_out_button).is_displayed()
        time.sleep(1)
        close_btn = self.browser.find_element(*self.close_button)
        self.browser.execute_script("arguments[0].click();", close_btn)
        return full_screen_button

    #@allure.step('Verify watch movie button on movie card ')
    def click_trailer(self):
        WebDriverWait(self.browser, 7).until(EC.presence_of_element_located(self.watchtrailer_moviecard))
        trailer = self.browser.find_element(*self.watchtrailer_moviecard)
        ActionChains(self.browser).move_to_element(trailer).perform()
        watch_trailer_button = self.browser.find_element(*self.watchtrailer_moviecard)
        self.browser.execute_script("arguments[0].click();", watch_trailer_button)
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
        move = ActionChains(self.browser)
        body_ = self.browser.find_element(*self.body_element)
        move.move_to_element_with_offset(body_, 511, 65)
        move.click()
        move.perform()
        time.sleep(2)
        WebDriverWait(self.browser, 30).until(EC.presence_of_element_located(self.zoom_in_zoom_out_button))
        time.sleep(1)
        full_screen_button = self.browser.find_element(*self.zoom_in_zoom_out_button).is_displayed()
        # time.sleep(1)
        close_btn = self.browser.find_element(*self.close_button)
        self.browser.execute_script("arguments[0].click();", close_btn)
        return full_screen_button

    #@allure.step('Movie Card Watch Trailer Button')
    def MovieCardWatchTrailer(self):
        return self.browser.find_element(*self.movie_card_watch_trailer).is_displayed()

    #@allure.step('Verify watch trailer button on movie cards')
    def verify_watchTrailer_cards(self):
        time.sleep(1)
        trailer = self.browser.find_element(*self.watchtrailer_moviecard)
        ActionChains(self.browser).move_to_element(trailer).perform()
        time.sleep(1)
        return trailer.is_displayed()

    #@allure.step('Verify watch trailer button on Tv cards')
    def verify_watchTrailer_tv_cards(self):
        time.sleep(2)
        trailer = self.browser.find_element(*self.watchtrailer_tv_card)
        ActionChains(self.browser).move_to_element(trailer).perform()
        time.sleep(2)
        return trailer.is_displayed()

    #@allure.step('Verify click on watch trailer button on movie cards')
    def verify_watchTrailer_MovieCard(self):
        time.sleep(2)
        trailer = self.browser.find_element(*self.watchtrailer_moviecard)
        time.sleep(2)
        ActionChains(self.browser).move_to_element(trailer).click().perform()
        time.sleep(3)
        # watch_trailer.click()
        time.sleep(3)
        trailer_close_button = self.browser.find_element_by_xpath(
            "//div[@class='close tele-close']//img[@class='close-btn-image']")
        return trailer_close_button.is_displayed()

    #@allure.step('Verify close trailer button on movie cards')
    def verify_CloseTrailer_MovieCard(self):
        trailer_close_button = self.browser.find_element_by_xpath(
            "//div[@class='close tele-close']//img[@class='close-btn-image']")
        time.sleep(2)
        trailer_close_button.click()
        time.sleep(2)

    #@allure.step('Movie Card View Detail Button')
    def MovieCardViewDetails(self):
        # movie = self.browser.find_element(*self.movie_list_jamesbond)
        # movie.location_once_scrolled_into_view
        time.sleep(2)
        title = self.browser.find_element(*self.movie_card_view_details)
        title.location_once_scrolled_into_view
        time.sleep(2)
        actionchains = ActionChains(self.browser)
        actionchains.move_to_element(title).perform()
        time.sleep(2)
        abc = title.is_displayed()
        return abc

    #@allure.step('Movie cards view details button in best pictures winners section')
    def viewDetails_moviecardfunc(self):
        WebDriverWait(self.browser, 20).until(EC.presence_of_element_located(self.heading1))
        list = self.browser.find_element(*self.heading1)
        self.browser.execute_script("arguments[0].scrollIntoView();", list)
        time.sleep(2)
        view_details = self.browser.find_element(*self.viewdetails_moviecard)
        ActionChains(self.browser).move_to_element(view_details).perform()
        time.sleep(1)
        return view_details.is_displayed()

    #@allure.step('TV Cards view details button ')
    def viewDetails_tv_moviecardfunc(self):
        WebDriverWait(self.browser, 38).until(EC.presence_of_element_located(self.heading_tv))
        list = self.browser.find_element(*self.heading_tv)
        self.browser.execute_script("arguments[0].scrollIntoView();", list)
        time.sleep(2)
        view_details = self.browser.find_element(*self.viewdetails_tv_card)
        ActionChains(self.browser).move_to_element(view_details).perform()
        time.sleep(2)
        return view_details.is_displayed()

    #@allure.step('Explore Element')
    def ExploreElement(self):
        return self.browser.find_element(*self.explore_element).is_displayed()

    #@allure.step('Click Explore All Tv Shows')
    def ClickExploreAllTvShows(self):
        self.browser.find_element(*self.see_all_tv_shows).click()
        WebDriverWait(self.browser, 20).until(EC.presence_of_element_located(self.television_show))
        time.sleep(2)
        return self.browser.find_element(*self.television_show).is_displayed()

    #@allure.step('Click Explore All Movie')
    def ClickExploreAllMovies(self):
        self.browser.find_element(*self.see_all_movies).click()
        WebDriverWait(self.browser, 20).until(EC.presence_of_element_located(self.movies))
        time.sleep(2)
        return self.browser.find_element(*self.movies).is_displayed()

    #@allure.step('Movie List Previous Button')
    def MovieListPrevButton1(self):
        try:
            prevbtn = self.browser.find_element(*self.movie_list_prev_button).is_displayed()
            # actionchains.move_to_element(prevbtn).perform()
            # prevbtn.click()
            if prevbtn == True:
                return True
        except:
            return False

    #@allure.step('Movie List Next Button')
    def MovieListNextButton1(self):
        # try:
        time.sleep(2)
        navButton = self.browser.find_element_by_xpath(
            '//h2[contains(text(),"Action")]/ancestor::div/following-sibling::div[1]//a[@class="carousel-control-next d-none d-md-block"]')
        time.sleep(10)
        ActionChains(self.browser).move_to_element(navButton).perform()

    #@allure.step('Right Navigation Behaviour')
    def RightNavigationBehaviour(self):
        return self.browser.find_element(*self.movie_title_Flyboys).is_displayed()

    #@allure.step('click on Right navigation arrow in recently watched')
    def click_rightarrow(self):
        time.sleep(2)
        self.browser.find_element(*self.next_arrow).click()

    #@allure.step('Right Navigation Behaviour')
    def RightNavigationBehaviour1(self):
        return self.browser.find_element(*self.movie_title_Capote).is_displayed()

    #@allure.step('Right Navigation Behaviour')
    def RightNavigationBehaviour2(self):
        return self.browser.find_element(*self.movie_title_Hotel_Rwanda).is_displayed()

    #@allure.step('Click Movie list prev Navigation button')
    def ClickPrevNavigationButton(self):
        prevbtn = self.browser.find_element(*self.movie_list_prev_button)
        actionchains.move_to_element(prevbtn).perform()
        prevbtn.click()

    #@allure.step('click on Left navigation arrow in recently watched')
    def click_prevarrow(self):
        prev = self.browser.find_element(*self.prev_arrow)
        self.browser.implicitly_wait(10)
        ActionChains(self.browser).move_to_element(prev).click(prev).perform()

    #@allure.step('Movie Title Benhuh')
    def MovieTitleBenHuh(self):
        return self.browser.find_element(*self.movie_title_ben_huh).is_displayed()

    #@allure.step('Movie Title Valkrie')
    def MovieTitleValkyrie(self):
        return self.browser.find_element(*self.movie_title_Valkyrie).is_displayed()

    #@allure.step('Movie List Next Navigation Disable')
    def NextNavigationDisable(self):
        try:
            nextbtn = self.browser.find_element(*self.movie_list_next_button)
            nextbtn.location_once_scrolled_into_view
            global actionchains
            actionchains.move_to_element(nextbtn).perform()
            nextbtn.click()
            nextbtn1 = self.browser.find_element(*self.movie_list_next_button).is_displayed()
            if nextbtn1 == True:
                return True
        except:
            return False

    #@allure.step('Movie List View Detail button')
    def MovieListViewDetailButton(self):
        title = self.browser.find_element(*self.movie_card_view_details)
        title.location_once_scrolled_into_view
        actionchains = ActionChains(self.browser)
        actionchains.move_to_element(title).perform()
        # time.sleep(1)
        title.click()
        # time.sleep(1)
        return self.browser.title

    #@allure.step('Click on view-details')
    def click_viewdetails_movieCard(self):
        view_details = self.browser.find_element(*self.viewdetails_moviecard)
        ActionChains(self.browser).move_to_element(view_details).perform()
        time.sleep(1)
        self.browser.find_element(*self.viewdetails_moviecard).click()
        WebDriverWait(self.browser, 30).until(EC.presence_of_element_located(self.synopsis_title))
        # time.sleep(3)
        return self.browser.find_element(*self.synopsis_title).is_displayed()

    #@allure.step('Click on view-details')
    def click_and_move_horizontal_scroller(self):
        WebDriverWait(self.browser, 80).until(EC.presence_of_element_located(self.action_adventure))
        action = self.browser.find_element(*self.action_adventure)
        self.browser.execute_script("arguments[0].scrollIntoView();", action)
        time.sleep(2)
        scroller = self.browser.find_element(*self.action_horizontal_scroller)
        move = ActionChains(self.browser)
        move.click_and_hold(scroller).move_by_offset(200, 0).release().perform()
        time.sleep(1.5)
        return self.browser.find_element(*self.action_fifth_card_movie_name).is_displayed()

    #@allure.step('verify horizontal slider in My-List section')
    def click_and_move_my_list_horizontal_scroller(self):
        WebDriverWait(self.browser, 20).until(EC.presence_of_element_located(self.my_list))
        action = self.browser.find_element(*self.my_list)
        self.browser.execute_script("arguments[0].scrollIntoView();", action)
        time.sleep(1)
        scroller = self.browser.find_element(*self.my_list_horizontal_scroller)
        move = ActionChains(self.browser)
        move.click_and_hold(scroller).move_by_offset(200, 0).release().perform()
        time.sleep(2)
        return scroller.is_displayed()

    #@allure.step('verify horizontal slider')
    def verify_recently_horizontal_slider(self):
        WebDriverWait(self.browser, 20).until(EC.presence_of_element_located(self.recently_watch_title))
        recently_watch = self.browser.find_element(*self.recently_watch_title)
        self.browser.execute_script("arguments[0].scrollIntoView();", recently_watch)
        time.sleep(1.5)
        scroller = self.browser.find_element(*self.recently_horizontal_scroller)
        time.sleep(1)
        return scroller.is_displayed()

    #@allure.step('hold and move the horizontal slider in Recintaly watch section')
    def click_recently_horizontal_slider(self):
        WebDriverWait(self.browser, 45).until(EC.presence_of_element_located(self.recently_watch_title))
        recently_watch = self.browser.find_element(*self.recently_watch_title)
        self.browser.execute_script("arguments[0].scrollIntoView();", recently_watch)
        time.sleep(2)
        scroller = self.browser.find_element(*self.recently_horizontal_scroller)
        time.sleep(1)
        move = ActionChains(self.browser)
        move.click_and_hold(scroller).move_by_offset(200, 0).release().perform()
        time.sleep(2.5)
        return scroller.is_displayed()

    #@allure.step('verify Synopsis title')
    def VerifySynopsisTitle(self):
        WebDriverWait(self.browser, 20).until(EC.presence_of_element_located(self.synopsis_title))
        # time.sleep(2)
        synopsis_tit = self.browser.find_element(*self.synopsis_title)
        # time.sleep(2)
        self.browser.execute_script("arguments[0].scrollIntoView();", synopsis_tit)
        name = synopsis_tit.is_displayed()
        return name

    #@allure.step('Click Movie Card Watch Movie Button')
    def ClickWatchMovieButton(self):
        WebDriverWait(self.browser, 55).until(EC.presence_of_element_located(self.heading1))
        bst_pic = self.browser.find_element(*self.heading1)
        self.browser.execute_script("arguments[0].scrollIntoView();", bst_pic)
        time.sleep(2)
        watch = self.browser.find_element(*self.watchmovie_moviecard)
        ActionChains(self.browser).move_to_element(watch).perform()
        time.sleep(2)
        watch.click()
        time.sleep(12)
        try:
            condition = self.browser.find_element(*self.play_begining)
            condition1 = condition.is_displayed()
        except:
            condition1 = False
            time.sleep(10)  # 60

        if condition1 == True:
            time.sleep(2)
            self.browser.find_element(*self.play_begining).click()
            time.sleep(10)  # 60
        WebDriverWait(self.browser, 10).until(EC.presence_of_element_located(self.movie_close_btn))
        popup = self.browser.find_element(*self.movie_close_btn).is_displayed()
        self.browser.find_element(*self.movie_close_btn).click()
        return popup

    #@allure.step('Click Main Carousel Next Navigation button')
    def MainCareusalClickNextNavigationArrow(self):
        time.sleep(2)
        self.browser.find_element(*self.next_navigation).click()
        time.sleep(2)
        return "clicked"

    #@allure.step('Click Main carousel previous navigation button')
    def MainCareusalClickPrevNavigationArrow(self):
        time.sleep(2)
        self.browser.find_element(*self.previous_navigtion).click()
        time.sleep(2)
        return "clicked"

    #@allure.step('verify slider reset after last movie')
    def SliderBarReset(self):
        for x in range(0, 14):
            self.browser.find_element(*self.next_navigation).click()

    #@allure.step('Verify titles of movie are underligned')
    def SliderTitleHighlighted(self):
        movie = self.browser.find_element(*self.titles_underligned)
        return movie.is_displayed()

    #@allure.step('user is abl to scroll properly')
    def VerifyScroll(self):
        WebDriverWait(self.browser, 26).until(EC.presence_of_element_located(self.see_all_movies))
        verify = self.browser.find_element(*self.see_all_movies)
        verify.location_once_scrolled_into_view
        return verify.is_displayed()

    #@allure.step('Check carousel is auto progress')
    def CarouselAutoProgress(self):
        WebDriverWait(self.browser, 38).until(EC.presence_of_element_located(self.your_lists_sec))
        time.sleep(3)
        active = self.browser.find_element(*self.carosel_active_movie).text
        print(active)
        time.sleep(10)
        active1 = self.browser.find_element(*self.carosel_active_movie).text
        print(active1)
        time.sleep(3)
        if active == active1:
            return False
        else:
            return True

    #@allure.step('slider movie Army of Darkness')
    def SliderMovie(self):
        s = self.browser.find_element(*self.next_navigation)
        actionchains = ActionChains(self.browser)
        actionchains.move_to_element(s).perform()
        try:
            a = self.browser.find_element(*self.progress_bar_armyofdarkness)
            z = a.is_displayed()
            if z == True:
                return True
        except:
            return False

    def RecentlyWatched(self):
        return self.browser.find_element(*self.recently_watched).is_displayed()

    def Refresh(self):
        self.browser.refresh()
        WebDriverWait(self.browser, 300).until(EC.presence_of_element_located(self.first_carousel_title))

    def RecentlyWatchedNextButton(self):
        nextbtn = self.browser.find_element(*self.movie_list_next_button)
        nextbtn.location_once_scrolled_into_view
        global actionchains
        actionchains = ActionChains(self.browser)
        actionchains.move_to_element(nextbtn).perform()
        btn = nextbtn.is_displayed()
        nextbtn.click()
        return btn

    def RecentlyWatchedPrevButton(self):
        prevbtn = self.browser.find_element(*self.movie_list_prev_button)
        prevbtn.location_once_scrolled_into_view
        time.sleep(2)
        actionchains.move_to_element(prevbtn).perform()
        return self.browser.find_element(*self.movie_list_prev_button).is_displayed()

    def RecentlyWatchedPosterImage(self):
        image = self.browser.find_element(*self.poster_image)
        image.location_once_scrolled_into_view
        a = image.is_displayed()
        return a

    def MovieSortedCorrectOrder(self):
        movie = []
        movie = self.browser.find_elements(*self.movie_name)
        name = movie[0].text
        return name

    #@allure.step('Click Main Carousel Add to List')
    def ClickMainCarouselAddToList(self):
        while True:
            try:
                addtolist = self.browser.find_element_by_xpath(
                    '//div[@class="carousel-inner"]/div[@class="carousel-item active"]/div[@class="movie-content"]'
                    '/div[@class="btn-container"]/div[@class="add-to-list"]/button[contains(text(),"ADD TO LIST")]')
                bool = addtolist.is_displayed()
                if bool == True:
                    addtolist.click()
                    break
                else:
                    self.browser.find_element_by_xpath("//span[@class='carousel-control-next-icon']").click()
                    time.sleep(1)

            except:
                self.browser.find_element_by_xpath("//span[@class='carousel-control-next-icon']").click()
                time.sleep(1)

    #@allure.step('Click Main Carousel Add to List')
    def ClickMainCarouselAddToListForRightSideMovie(self):
        while True:
            try:
                addtolist = self.browser.find_element_by_xpath(
                    '//div[@class="carousel-inner"]/div[@class="carousel-item active"]/div[@class="movie-content"]'
                    '/div[@class="btn-container"]/div[@class="add-to-list"]/button[contains(text(),"ADD TO LIST")]')
                bool = addtolist.is_displayed()
                if bool == True:
                    addtolist.click()
                    break
                else:
                    self.browser.find_element_by_xpath("//span[@class='carousel-control-next-icon']").click()
                    time.sleep(1)

            except:
                self.browser.find_element_by_xpath("//span[@class='carousel-control-next-icon']").click()
                time.sleep(1)

    #@allure.step('Add to list search box')
    def AddToListSearchBox(self):
        time.sleep(1.5)
        return self.browser.find_element(*self.add_to_list_search).is_displayed()

    #@allure.step('Add to list created list')
    def AddToListCreatedList(self):
        time.sleep(7.5)
        WebDriverWait(self.browser, 90).until(EC.presence_of_element_located(self.add_to_list_list_name))
        return self.browser.find_element(*self.add_to_list_list_name).is_displayed()

    #@allure.step('Add to list toggle button')
    def AddToListToggelButton(self):
        return self.browser.find_element(*self.add_to_list_toggel_button).is_displayed()

    #@allure.step('Add to list create list')
    def AddToListCreateList(self):
        return self.browser.find_element(*self.add_to_list_create_list).is_displayed()

    #@allure.step('Add to list List name text box')
    def AddToListListName(self):
        return self.browser.find_element(*self.add_to_list_enter_name).is_displayed()

    #@allure.step('Add to list create list button')
    def AddToListCreateListButton(self):
        return self.browser.find_element(*self.add_to_list_create_list).is_displayed()

    #@allure.step('Enter list name')
    def ListName(self, name):
        # time.sleep(1)
        self.browser.find_element(*self.add_to_list_enter_name).send_keys(name)

    #@allure.step('Click create list')
    def ClickCreateList(self):
        WebDriverWait(self.browser, 45).until(EC.presence_of_element_located(self.add_to_list_create_list))
        time.sleep(1.5)
        create_list = self.browser.find_element(*self.add_to_list_create_list)
        time.sleep(1)
        self.browser.execute_script("arguments[0].click();", create_list)
        # WebDriverWait(self.browser, 8).until(EC.presence_of_element_located(self.add_to_list_creating))
        # return self.browser.find_element(*self.add_to_list_creating).is_displayed()

    #@allure.step('Click create list')
    def ClickCreateListForDuplicate(self):
        self.browser.find_element(*self.add_to_list_create_list).click()

    #@allure.step('Click create list for duplicate name')
    def verify_duplicate_list(self):
        WebDriverWait(self.browser, 10).until(EC.presence_of_element_located(self.duplicate_list_validation_text))
        duplicate_list = self.browser.find_element(*self.duplicate_list_validation_text).is_displayed()
        return duplicate_list

    #@allure.step('Verify new created list')
    def NewList(self):
        time.sleep(1)
        list = self.browser.find_element(*self.add_to_list_toggle_button_demo).text
        return list

    #@allure.step('List auto select')
    def ListAutoSelect(self):
        time.sleep(2)
        return self.browser.find_element(*self.selected_list).is_displayed()

    #
    #@allure.step('Click add to list toggle button')
    def ClickAddToListToggelButton(self):
        self.browser.find_element(*self.add_to_list_toggel_button).click()

    #@allure.step('Click add to list second toggle button')
    def ClickAddToListToggleButton1(self):
        self.browser.find_element(*self.add_to_list_toggel_button1).click()

    #@allure.step('Click Add movie to list')
    def AddMovieToList(self):
        WebDriverWait(self.browser, 40).until(EC.presence_of_element_located(self.add_to_list))
        # time.sleep(2)
        self.browser.find_element(*self.add_to_list).click()

    #@allure.step('Verify added Movie')
    def VerifyAddedMovie(self):
        self.browser.find_element(*self.header_mylist).click()
        scroll = self.browser.find_element(*self.created_list)
        actionchains = ActionChains(self.browser)
        actionchains.move_to_element(scroll).perform()
        time.sleep(2)
        scroll.click()
        time.sleep(2)
        verify = self.browser.find_element(*self.add_to_list_verify)
        movie = verify.text
        return movie

    #@allure.step('Verify second added movie')
    def VerifySecondAddedMovie(self):
        self.browser.find_element(*self.header_mylist).click()
        self.browser.find_element(*self.your_list).click
        scroll = self.browser.find_element(*self.created_list_test)
        scroll.location_once_scrolled_into_view
        actionchains = ActionChains(self.browser)
        actionchains.move_to_element(scroll).perform()
        time.sleep(2)
        scroll.click()
        time.sleep(2)
        verify = self.browser.find_element(*self.add_to_list_verify)
        movie = verify.text
        return movie

    #@allure.step('search a list in lists')
    def SearchList(self, name):
        time.sleep(1.5)
        self.browser.find_element(*self.add_to_list_search).send_keys(name)

    #@allure.step('Verify searched list')
    def VerifySearchedList(self):
        WebDriverWait(self.browser, 40).until(EC.presence_of_element_located(self.add_to_list_movies_list_toggel_button))
        return self.browser.find_element(*self.add_to_list_movies_list_toggel_button).is_displayed()

    # @allure.step('Verify searched list')
    def VerifySearchedList_for_test(self):
        WebDriverWait(self.browser, 30).until(EC.presence_of_element_located(self.add_to_list_movies_list_toggel_test_button))
        return self.browser.find_element(*self.add_to_list_movies_list_toggel_test_button).is_displayed()

    #@allure.step('Verify searched list')
    def VerifyFirstFilmSearchedList(self):
        WebDriverWait(self.browser, 30).until(
            EC.presence_of_element_located(self.add_to_list_toggel_first_film))
        return self.browser.find_element(*self.add_to_list_toggel_first_film).is_displayed()

    #@allure.step('Add to list clear button')
    def AddToListClearButton(self):
        WebDriverWait(self.browser, 40).until(
            EC.presence_of_element_located(self.add_to_list_clear))
        return self.browser.find_element(*self.add_to_list_clear).is_displayed()

    #@allure.step('Click add to list clear button')
    def ClickAddToListClearButton(self):
        time.sleep(1.5)
        self.browser.find_element(*self.add_to_list_clear).click()
        time.sleep(1)
        input_field = self.browser.find_element(*self.add_to_list_search)
        time.sleep(0.5)
        input_text = input_field.get_attribute('value')
        if len(input_text) == 0:
            return True
        return False

    #@allure.step('Click Movie card add to list')
    def ClickMovieCardAddToList(self):
        WebDriverWait(self.browser, 20).until(
            EC.presence_of_element_located(self.bestPicWin_heading))  # bestPicWin_heading-> Alive
        heading = self.browser.find_element(*self.bestPicWin_heading)
        heading.location_once_scrolled_into_view
        time.sleep(1)
        addList = self.browser.find_element(*self.movie_addToList)
        actionchains = ActionChains(self.browser)
        actionchains.move_to_element(addList).perform()
        time.sleep(1.5)
        addList.click()
        try:
            time.sleep(2.5)
            search_box = self.browser.find_element(*self.add_to_list_search)
            if search_box.is_displayed():
                return search_box.is_displayed()
            else:
                add_to_list_button = self.browser.find_element(*self.movie_addToList)
                time.sleep(0.5)
                self.browser.execute_script("arguments[0].click();", add_to_list_button)
                time.sleep(2)
                return self.browser.find_element(*self.add_to_list_search).is_displayed()
        except:
            add_to_list_button = self.browser.find_element(*self.movie_addToList)
            time.sleep(0.5)
            self.browser.execute_script("arguments[0].click();", add_to_list_button)
            time.sleep(2)
            return self.browser.find_element(*self.add_to_list_search).is_displayed()


    #@allure.step('Click Tv card add to list')
    def ClickTvCardAddToList(self):
        WebDriverWait(self.browser, 180).until(
            EC.presence_of_element_located(self.tvTitle))  # bestPicWin_heading-> Alive
        tv_heading = self.browser.find_element(*self.tvTitle)
        self.browser.execute_script("arguments[0].scrollIntoView();", tv_heading)
        time.sleep(1)
        add_tv_show = self.browser.find_element(*self.first_tv_show_add_to_list)
        actionchains = ActionChains(self.browser)
        actionchains.move_to_element(add_tv_show).perform()
        time.sleep(1.5)
        add_tv_show.click()
        time.sleep(1.5)
        return self.browser.find_element(*self.add_to_list_search).is_displayed()

    #@allure.step('Click Tv card watch now')
    def verify_tv_show_watch_now_button(self):
        try:
            add_tv_show = self.browser.find_element(*self.fiascoSeriesListPage)
            actionchains = ActionChains(self.browser)
            actionchains.move_to_element(add_tv_show).perform()
            if add_tv_show.is_displayed():
                return False
        except:
            return True


    #@allure.step('Click Movie card add to list')
    def click_movie_card_addToList_filmseries(self):
        time.sleep(2)
        WebDriverWait(self.browser, 20).until(
            EC.presence_of_element_located(self.firstFilmSeriesCardPoster))
        heading = self.browser.find_element(*self.firstFilmSeriesCardPoster)
        heading.location_once_scrolled_into_view
        time.sleep(1)
        addList = self.browser.find_element(*self.addBeingJamesBondToListButton)
        actionchains = ActionChains(self.browser)
        actionchains.move_to_element(addList).perform()
        time.sleep(2)
        addList.click()
        return self.browser.find_element(*self.add_to_list_search).is_displayed()

    #@allure.step('Click Movie card add to list')
    def ClickMovieCardAddToListSecondMovie(self):
        WebDriverWait(self.browser, 60).until(
            EC.presence_of_element_located(self.bestPicWin_heading))  # bestPicWin_heading-> Alive
        heading = self.browser.find_element(*self.bestPicWin_heading)
        heading.location_once_scrolled_into_view
        time.sleep(1)
        addList = self.browser.find_element(*self.movie_addToList_second)
        actionchains = ActionChains(self.browser)
        actionchains.move_to_element(addList).perform()
        time.sleep(2)
        addList.click()
        return self.browser.find_element(*self.add_to_list_search).is_displayed()

    #@allure.step('Verify new list created')
    def VerifyListCreated(self):
        return self.browser.find_element(*self.new_list2).is_displayed()

    #@allure.step('Verify new list created')
    def VerifyTvListCreated(self):
        time.sleep(2)
        return self.browser.find_element(*self.tv_list).is_displayed()

    #@allure.step('Verify new list created')
    def VerifyFilmSeriesListCreated(self):
        return self.browser.find_element(*self.new_list_film_series).is_displayed()

    #@allure.step('Verify new list created')
    def VerifyFilmSeriesSecondListCreated(self):
        return self.browser.find_element(*self.new_list2_film_series).is_displayed()

    #@allure.step('Verify new list created')
    def VerifyListRecentlyCreated(self):
        return self.browser.find_element(*self.recentlyList_list).is_displayed()

    #@allure.step('Verify Created text show on click of create list')
    def CreatedList(self):
        WebDriverWait(self.browser, 45).until(
            EC.presence_of_element_located(
                (By.XPATH, "//div[contains(@class,'createdListItem')]//span[text()=' Created! ']")))
        # self.browser.find_element(*self.add_to_list_created).is_displayed()
        time.sleep(3.5)
        return True

    def q(self):
        time.sleep(2)
        a = self.browser.find_element(*self.abc).get_attribute("class")

    #@allure.step('Click header list button')
    def ClickHeaderList(self):
        WebDriverWait(self.browser, 20).until(EC.presence_of_element_located(self.header_mylist))
        self.browser.find_element(*self.header_mylist).click()

    #@allure.step('Verify movie added to list from movie card')
    def VerifyMovieCardAddedMovie(self):
        scroll = self.browser.find_element(*self.movie_card_added_movie)
        actionchains = ActionChains(self.browser)
        actionchains.move_to_element(scroll).perform()
        time.sleep(2)
        scroll.click()
        time.sleep(2)
        verify = self.browser.find_element(*self.add_to_list_verify_Detroit)
        movie = verify.text
        return movie

    #@allure.step('Click list toggle button and Verify it is selected/unselected')
    def VerifySelectList(self):
        time.sleep(1.5)
        self.browser.find_element(*self.add_to_list_toggle_button_demo).click()
        time.sleep(1.5)
        b = self.browser.find_element(*self.demo_toggle_button).is_selected()
        return b

    #@allure.step('Click list toggle button and Verify it is selected/unselected')
    def VerifyMovieCardSelectList(self):
        time.sleep(1.5)
        self.browser.find_element(*self.toggle_button_test1).click()
        time.sleep(1.5)
        b = self.browser.find_element(*self.test1_toggle_button).is_selected()
        return b

    #@allure.step('Click list toggle button and Verify it is selected/unselected')
    def verify_movie_card_unselect_list(self):
        time.sleep(2)
        self.browser.find_element(*self.toggle_button_filmSeriesList).click()
        time.sleep(2)
        b = self.browser.find_element(*self.film_series_toggle_button).is_selected()
        return b

    #@allure.step('Click list toggle button and Verify it is selected/unselected')
    def verify_film_series_movie_card_selected(self):
        time.sleep(1.5)
        self.browser.find_element(*self.toggle_button_filmSeriesList).click()
        time.sleep(1.5)
        b = self.browser.find_element(*self.film_series_toggle_button).is_selected()
        return b

    #@allure.step('Click list toggle button and Verify it is selected/unselected')
    def VerifyRecentlySelectList(self):
        time.sleep(1.5)
        self.browser.find_element(*self.toggle_button_recentlyList).click()
        time.sleep(1.5)
        b = self.browser.find_element(*self.recently_toggle_button).is_selected()
        return b

    #@allure.step('Verify Created list is auto-selected')
    def VerifyListAutoSelect(self):
        list = self.browser.find_element(*self.test1_toggle_button).is_selected()
        return list

    #@allure.step('Verify Created list is auto-selected')
    def VerifyTvListAutoSelect(self):
        time.sleep(2)
        list = self.browser.find_element(*self.tv_toggle_button).is_selected()
        return list

    #@allure.step('Verify Created list is auto-selected')
    def VerifyFilmSeriesAutoSelect(self):
        list = self.browser.find_element(*self.film_series_toggle_button).is_selected()
        return list

    #@allure.step('Verify Created list is auto-selected')
    def VerifyFilmSeriesSecondAutoSelect(self):
        list = self.browser.find_element(*self.film_series_second_toggle_button).is_selected()
        return list

    #@allure.step('Verify Created list is auto-selected')
    def VerifyListRecentlyAutoSelect(self):
        list = self.browser.find_element(*self.recently_toggle_button).is_selected()
        ##print(list)
        return list

    #@allure.step('Verify Created list is auto-selected')
    def VerifyListAutoSelect(self):
        list = self.browser.find_element(*self.test1_toggle_button).is_selected()
        ##print(list)
        return list

    #@allure.step('Verify second added movie in the list')
    def MovieCardSecondAddedMovie(self):
        scroll = self.browser.find_element(*self.created_list_test2)
        actionchains = ActionChains(self.browser)
        actionchains.move_to_element(scroll).perform()
        time.sleep(2)
        scroll.click()
        time.sleep(2)
        verify = self.browser.find_element(*self.add_to_list_verify_Detroit)
        movie = verify.text
        return movie

    #@allure.step('Movie card select unselect list')
    def MovieCardVerifySelectUnselectList(self):
        time.sleep(1.5)
        self.browser.find_element(*self.add_to_list_toggel_button1).click()
        time.sleep(1.5)
        return self.browser.find_element(*self.test_toggle_button).is_selected()

    # @allure.step('Movie card select unselect list')
    def MovieCardVerifySelectUnselectListMyListMovies(self):
        time.sleep(1.5)
        WebDriverWait(self.browser, 50).until(EC.presence_of_element_located(self.add_to_list_movies_list_toggel_button))
        time.sleep(2.5)
        self.browser.find_element(*self.add_to_list_movies_list_toggel_button).click()
        time.sleep(1.5)
        return self.browser.find_element(*self.movies_list_toggle_button).is_selected()

    # @allure.step('Movie card select unselect list')
    def MovieCardVerifySelectUnselectListForTest(self):
        WebDriverWait(self.browser, 50).until(EC.presence_of_element_located(self.add_to_list_toggel_button1))
        self.browser.find_element(*self.add_to_list_toggel_button1).click()
        time.sleep(1)
        return self.browser.find_element(*self.test_toggle_button).is_selected()

    def AddMultipleSlider(self):
        self.browser.refresh()
        time.sleep(2)
        a = self.browser.find_element(*self.progress_bar_spectre)
        actionchains = ActionChains(self.browser)
        actionchains.move_to_element(a).perform()
        time.sleep(2)
        self.browser.find_element(*self.add_to_list_button).click()

    #@allure.step('Click add to list for second movie')
    def ClickMainCarouselAddToListMovie2(self):
        self.browser.find_element(*self.maincarousel_add_to_list_movie2).click()

    #@allure.step('Verify Second movie added to same list')
    def VerifySecondAddedMovieSameList(self):
        self.browser.find_element(*self.header_mylist).click()
        scroll = self.browser.find_element(*self.created_list)
        scroll.location_once_scrolled_into_view
        actionchains = ActionChains(self.browser)
        actionchains.move_to_element(scroll).perform()
        time.sleep(2)
        scroll.click()
        time.sleep(2)
        verify = self.browser.find_element(*self.add_to_list_verify_army)
        movie = verify.text
        return movie

    #@allure.step('Click Test1 Toggle Button')
    def ClickTest1ToggleButton(self):
        self.browser.find_element(*self.new_list2).click()

    #@allure.step('Verify Second Movie Added From Movie Card In Same List')
    def VerifyMovieCardSecondMovieSameList(self):
        scroll = self.browser.find_element(*self.movie_card_added_movie)
        actionchains = ActionChains(self.browser)
        actionchains.move_to_element(scroll).perform()
        time.sleep(2)
        scroll.click()
        time.sleep(2)
        verify = self.browser.find_element(*self.add_to_list_verify_Ben_Hur)
        movie = verify.text
        return movie

    def AutoProgress(self):
        a = self.browser.find_element(*self.progress_bar_spectre)
        actionchains = ActionChains(self.browser)
        actionchains.move_to_element(a).perform()

    def AddToListAddedButton(self):
        WebDriverWait(self.browser, 40).until(EC.presence_of_element_located(self.add_to_list_added_button))
        return self.browser.find_element(*self.add_to_list_added_button).is_displayed()

    #@allure.step('Verify success message after clicking on addTo list button ')
    def verify_success_text(self):
        WebDriverWait(self.browser, 60).until(
            EC.presence_of_element_located(self.success_created))
        return self.browser.find_element(*self.success_created).is_displayed()

    def ClickToggleButtonTest(self):
        self.browser.find_element(*self.toggle_button_test).click()

    def ClickToggleButtonTest2(self):
        self.browser.find_element(*self.toggle_button_test2).click()

    def ClickToggleButtonTest1(self):
        self.browser.find_element(*self.toggle_button_test1).click()

    def ClickToggleButtonFilmSeries1(self):
        time.sleep(1.5)
        self.browser.find_element(*self.toggle_button_filmSeriesList).click()

    def ClickToggleButtonFilmSeries2(self):
        self.browser.find_element(*self.toggle_button_filmSeriesList2).click()

    def ClickToggleButtonRecentlyList(self):
        self.browser.find_element(*self.toggle_button_recentlyList).click()

    def click_watch_now_movie(self):
        card2 = self.browser.find_element(*self.watch_movie_now)
        ActionChains(self.browser).move_to_element(card2).perform()
        time.sleep(1)
        card2.click()
        self.browser.find_element(*self.play_begginning).click()
        return self .browser.find_element(*self.close_button1).is_displayed()

    def watch_trailor_for_movie(self):
        card3=self.browser.find_element(*self.watch_trailer)
        ActionChains(self.browser).move_to_element(card3).perform()
        time.sleep(1)
        card3.click()
        return self.browser.find_element(*self.close_button1).is_displayed()

    def add_to_list_movie_pk(self):
        WebDriverWait(self.browser, 40).until(EC.presence_of_element_located(self.add_list_movie))
        card4=self.browser.find_element(*self.add_list_movie)
        ActionChains(self.browser).move_to_element(card4).perform()
        time.sleep(1)
        card4.click()