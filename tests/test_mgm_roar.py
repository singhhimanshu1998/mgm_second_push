import pytest
import json
from pages.LoginPage import loginpage
from pages.HomePage import homepage
from pages.MarketingRules import MarketingRulesPage
from pages.FilmSeries import filmSeriesPage
from pages.assetsPage import AssetsPage
from pages.MyCarts import MyCartsPage
from pages.viewDetailsSeriesPage import ViewDetailsSeriesPage
from pages.VideoPlayer import videoplayer
from pages.home_page import homePageObj
from pages.viewDetailsMoviePage import ViewDetailsMoviePage
from pages.recently_addList import recaddListObj
from pages.MyListPage import MyList
from pages.ListDetails import ListDetails
from resources.variables import *
from pages.myList import myListObj
from pages.mailinator import mailinatorPageObj
from pages.homepage_myLists import homePagemylistsObj
from pages.TelevisionPage import Telvision
from pages.moviedetails import moviedetails
from pages.movies_listing import movieListingObj
from pages.televisions_page import tvpageObj
from pages.tvdetails import tvdetails
from pages.homepg import homepg
from pages import gmailApi
from pages import deleteApi
import allure
import time

# test_case_ids = [113, 114, 115, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 127, 128, 129, 130, 131, 132,
#                  133, 134, 135, 136, 137, 138, 139, 140, 141, 142, 143, 144, 145, 146, 147, 148, 149, 150, 151, 152,
#                  153, 154, 155, 156, 157, 158, 159, 160, 161, 162, 163, 164, 165, 166, 167, 168, 169, 170, 171, 172,
#                  173, 174, 175, 176, 177, 178, 179, 180, 181, 182, 183, 184, 185, 186, 187, 188, 189, 190, 191, 192,
#                  193, 194, 195, 196, 197, 198, 199, 200, 201, 202, 203, 204, 205, 206, 207, 208, 209, 210, 211, 212,
#                  213, 214, 215, 216, 217, 218, 219, 220, 221, 222, 223, 224, 225, 226, 227, 228, 229, 230, 231, 232,
#                  233, 234, 235, 236, 237, 238, 239, 240, 241, 242, 243, 945, 946, 947, 948, 949, 950, 951, 952, 953,
#                  954, 955, 956, 957, 958, 959, 960, 961, 962, 963, 964, 965, 966, 967, 968, 969, 970, 971, 972, 973,
#                  974, 975, 976, 977, 978, 979, 980, 981, 982, 983, 984, 985, 986, 987, 988, 989, 990, 991, 992, 993,
#                  994, 995, 996, 997, 998, 999, 1000, 1311, 1312, 1313, 1314, 1001, 1002, 1003, 1004, 1005, 1006, 1007,
#                  1008, 1009, 1010, 1011, 1012, 1013, 1014, 1015, 1016, 1017, 1018, 1019, 1020, 1021, 1022, 1023, 1024,
#                  1025, 1026, 1027, 1028, 1029, 1030, 1031, 1032, 1033, 1034, 1035, 1036, 1037, 1038, 1039, 1040, 1041,
#                  1042, 1043, 1044, 1045, 1046, 1047, 1048, 1049, 1050, 1051, 1052, 1053, 1054, 1055, 1056, 1057, 1058,
#                  1059, 1060, 1061, 1062, 1063, 1064, 1065, 1066, 1067, 1068, 1069, 1070, 1071, 1072, 1073, 1074, 1075,
#                  1076, 1077, 1078, 1079, 1080, 1081, 1082, 1083, 1084, 1085, 1086, 1087, 1088, 1089, 1090, 1091, 1092,
#                  1093, 1094, 1095, 1096, 1097, 1098, 1099, 1100, 1101, 1102, 1103, 1104, 1105, 1106, 1107, 1108, 1109,
#                  1110, 1111, 1112, 1113, 1114, 1115, 1116, 1117, 1118, 1119, 1120, 1121, 1122, 1123, 1124, 1125, 1126,
#                  1127, 1128, 1129, 1130, 1131, 1132, 1133, 1134, 1135, 1136, 1137, 1138, 1139, 1140, 1141, 1142, 1143,
#                  1144, 1145, 1146, 1147, 1148, 1149, 1150, 1151, 1152, 1153, 1154, 1155, 1156, 1157, 1158, 1159, 1160,
#                  1161, 1162, 1163, 1164, 1165, 1166, 1167, 1168, 1169, 1170, 1171, 1172, 1173, 1174, 1175, 1176, 1177,
#                  1178, 1179, 1180, 1181, 1182, 1183, 1184, 1185, 1186, 1187, 1188, 1189, 1190, 1191, 1192, 1193, 1194,
#                  1195, 1196, 1197, 1198, 1199, 1200, 1201, 1202, 1203, 1204, 1205, 1206, 1208, 1209, 1210, 1211,
#                  1212, 1213, 1214, 1215, 1216, 1217, 1218, 1219, 1220, 1221, 1222, 1223, 1224, 1225, 1226, 1227, 1228,
#                  1229, 1230, 1231, 1232, 1233, 1234, 1235, 1236, 1237, 1238, 1239, 1240, 1241, 1242, 1243, 1244, 1245,
#                  1246, 1247, 1248, 1249, 1250, 1251, 1252, 1254, 1255, 1256, 1257, 1258, 1259, 1260, 1261, 1262,
#                  1263, 1264, 1265, 1266, 1267, 1268, 1269, 1270, 1271, 1272, 1273, 1274, 1276, 1277, 1278, 1279,
#                  1280, 1281, 1282, 1283, 1284, 1285, 1286, 1287, 1288, 1289, 1290, 1291, 1293, 1294, 1295, 1296,
#                  1297, 1298, 1299, 1300, 1301, 1303, 1304, 1305, 1306, 1307, 1308, 1309, 1310]


test_case_ids = [132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142, 143, 144, 145, 146, 147, 148, 149, 150, 151,
                 152, 153, 154, 155, 156, 157, 158, 159, 160, 161, 162, 163, 164, 165, 166, 167, 168, 169, 170, 171,
                 172, 173, 174, 175, 176, 177, 178, 179, 180, 181, 182, 183, 184, 185, 186, 187, 188, 189, 190, 191,
                 192, 193, 194, 195, 196, 197, 198, 199, 200, 201, 202, 203, 204, 205, 206, 207, 208, 209, 210, 211,
                 212, 213, 214, 215, 216, 217, 218, 219, 220, 221, 222, 223, 224, 225, 226, 227, 228, 229,
                 230, 231, 232, 233, 234, 235, 236, 237, 238, 239, 240, 241, 242, 243, 244, 245, 246, 247, 248, 249,
                 250, 251, 252, 253, 254, 255, 256, 257, 258, 259, 260, 261, 262, 263, 264, 265, 266, 267, 268, 269,
                 270, 271, 272, 273, 274, 275, 276, 277, 278, 279, 280, 281, 282, 283, 284, 285, 286, 287, 288, 289,
                 290, 291, 292, 293, 294, 295, 296, 297, 298, 299, 300, 301, 302, 303, 304, 305, 306, 307, 308, 309,
                 310, 311, 312, 313, 314, 315, 316, 317, 318, 627, 628, 629,
                 630,319, 320, 321, 322, 323, 324, 325, 326, 327, 328, 329,
                 330, 331, 332, 333, 334, 335, 336, 337, 338, 339, 340, 341, 342, 343, 344, 345, 346, 347, 348, 349,
                 350, 351, 352, 353, 354, 355, 356, 357, 358, 359, 360, 361, 362, 363, 364, 365, 366, 367, 368, 369,
                 370, 371, 372, 373, 374, 375, 376, 377, 378, 379, 380, 381, 382, 283, 384, 385, 386, 387, 388, 389,
                 390, 391, 392, 393, 394, 395, 396, 397, 398, 399, 400, 401, 402, 403, 404, 405, 406, 407, 408, 409,
                 410, 411, 412, 413, 414, 415, 416, 417, 418, 419, 420, 421, 422, 423, 424, 425, 426, 427, 428, 429,
                 430, 431, 432, 433, 434, 435, 436, 437, 438, 439, 440, 441, 442, 443, 444, 445, 446, 447, 448, 449,
                 450, 451, 452, 453, 454, 455, 456, 457, 458, 459, 460, 461, 462, 463, 464, 465, 466, 467, 468, 469,
                 470, 471, 472, 473, 474, 475, 476, 477, 478, 479, 480, 481, 482, 483, 484, 485, 486, 487, 488, 489,
                 490, 491, 492, 493, 494, 495, 496, 497, 498, 499, 500, 501, 502, 503, 504, 505, 506, 507, 508, 509,
                 510, 511, 512, 513, 514, 515, 516, 517, 518, 519, 520, 521, 522, 523, 525, 526, 527, 528, 529,
                 530, 531, 532, 533, 534, 535, 536, 537, 538, 539, 540, 541, 542, 543, 544, 545, 546, 547, 548, 549,
                 550, 551, 552, 553, 554, 555, 556, 557, 558, 559, 560, 561, 562, 563, 564, 565, 566, 567, 568, 569,
                 571, 572, 573, 574, 575, 576, 577, 578, 579, 580, 581, 582, 583, 584, 585, 586, 587, 588, 589,
                 590, 591, 592, 594, 595, 596, 597, 598, 599, 600, 601, 602, 603, 604, 605, 606, 607, 608, 609,
                 610, 611, 612, 613, 614, 615, 616, 617, 618, 619, 620, 621, 622, 623, 624, 625, 626]


global execution_time
execution_time = []

global update_testrail
update_testrail = False

"""test case 222466"""

test = ""
my_comment = ''


@pytest.fixture(scope="session")
def set_url(pytestconfig):
    return pytestconfig.getoption("set_url")


def test_print_name(set_url):
    print("url---------------------->",set_url)
    global _url_
    _url_ = set_url


#@allure.title('this is the test title ')
def test_url_32810(browser):
    home_user = loginpage(browser)
    home_user.get_url(_url_)


#@allure.title('this is the test title ')
def test_Start_32810(browser):
    global home_user
    home_user = loginpage(browser)
    if update_testrail == True:
        # print("got it")
        home_user.createTestRun(test_case_ids)

def case_fields():
    home_user.case_fields(test)

def fail_update():
    home_user.updateTestCase(test, my_comment, "fail")


def pass_update():
    home_user.updateTestCase(test, my_comment, "pass")


def teardwn():
    if update_testrail == True:
        # print("teardown")
        user.closeTestRun()


# @allure.title('TC_001: Verify user lands on login page')
@pytest.mark.usefixtures()
def test_login_page(browser):
    global user, my_comment
    user = loginpage(browser)
    global test
    test = test_case_ids[0]
    my_comment = "Log in to MGM ROAR", "Unable to load login page"
    verify = home_user.load_url(_url_)
    assert verify == 'Log in to ROAR', "Log in to MGM ROAR Unable to load login page"
    my_comment = 'User should see Login page on hitting Roar URL'


# @allure.title('TC_003: Verify carousel image set by admin is visible ')
def test_verify_carousal_image_visible(browser):
    user = loginpage(browser)
    global test, my_comment
    test = test_case_ids[2]
    my_comment = "carousel image is not present / carousel image is not set by Admin"
    verify = user.CarouselImage()
    assert verify == True, 'carousel image is not present / carousel image is not set by Admin'
    my_comment = 'Carousel Image should be visible on Login page'


# # @allure.title('TC_004: On each visit user see different carousel image')
def test_verify_different_carousel_image(browser):
    user = loginpage(browser)
    global test, my_comment
    test = test_case_ids[3]
    my_comment = "carousel image is not present / carousel image is not set by Admin"
    image_change = user.DifferentCarouselImage()
    assert image_change == True, "Carousel image is not changing on reload"
    my_comment = "carousel image should change on each visit"


# #@allure.title('TC_005: verify elements present in login model')
def test_verify_elements_of_login_model(browser):
    user = loginpage(browser)
    global test, my_comment
    test = test_case_ids[4]
    my_comment = "Email textbox not found"
    email = user.VerifyEmail()
    my_comment = "Email textbox not found"
    assert email == True, "Email textbox not found"
    next_button = user.VerifyNextButton()
    my_comment = "Next button not found"
    assert next_button == True, "Next button not found"
    request_account = user.VerifyRequestAnAccount()
    my_comment = "Request an account button not found"
    assert request_account == True, "Request an account button not found"
    my_comment = "Remember-me checkbox not found"
    remember_me = user.VerifyRememberMe()
    assert remember_me == True, "Remember-me checkbox not found"
    my_comment = '''Login Modal should have following elements:
                    1. Email Address [Textbox]
                    2. Remember me [Checkbox]
                    3. Next [Button]
                    4. Create An Account [Button]'''


# #@allure.title('TC_008: On click next button Verify validation if email field is empty')
def test_verify_empty_email_validation_on_next_button(browser):
    user = loginpage(browser)
    global test, my_comment
    test = test_case_ids[7]
    my_comment = 'Email Validation Message is not Present while email field is empty '
    email_validation = user.ClickNextValidation()
    assert 'Please enter a username' in email_validation
    my_comment = 'user Should gets an error message "Please enter a username"'


# #@allure.title('TC_006: Verify user is able to enter Email in email field')
def test_type_email_id(browser):
    user = loginpage(browser)
    global test, my_comment
    test = test_case_ids[5]
    my_comment = 'Email input field is not present '
    user.LoginPage(_url_)
    user.EnterEmail(email)
    my_comment = "User should be able to enter it's email in the Email field"


# #@allure.title('TC_007: Verify user can select the remember me checkbox')
def test_remember_me_checkbox(browser):
    user = loginpage(browser)
    global test, my_comment
    test = test_case_ids[6]
    my_comment = 'Remember Me Checkbox is not present / Remember me checkbox is not clickable'
    check_box_str=user.ClickOnRememberMe()    # ------------------------------------------------------------changed by me
    assert "checked" in check_box_str,'remember me check box is not select'
    my_comment = 'User should be able to select the remember me checkbox'



# #@allure.title('TC_009: Verify user with valid email id can proceed to next step')
def test_click_next_valid_mail(browser):
    global test, my_comment
    user = loginpage(browser)
    test = test_case_ids[8]
    my_comment = 'Click next button is not present / click next button is not clickable'
    verify = user.ClickNext()
    assert verify == True, "user not pr oceed to next step with valid email id"
    my_comment = 'On click of NEXT button with valid email entered, user should be able see Password field '


# #@allure.title('TC_014: Verify button is clickable or not ')
def test_verify_login_button_confirmation_page_elements(browser):
    global test, my_comment
    user = loginpage(browser)
    test = test_case_ids[13]
    user.EnterPassword(password)
    my_comment = 'verify button is not present / verify button is not clickable   '
    user.verifyButton()
    # time.sleep(2)
    user.confrimation_page_without_elements()
    user.confrimation_page_elements()
    verify = user.VerifyLogin()
    my_comment = 'Homepage is not open / Home page elements are not present(logout button)'
    # current_url = user.ValidateUrlForNextPage()
    # assert not 'login' in current_url
    my_comment = 'User should be able to see Home page after clicking on verify button'


# #@allure.title('TC_015: verify after click on verify button page will redirected to home page')
def test_verify_login_redirected_to_home_page(browser):
    user = loginpage(browser)
    global test, my_comment
    test = test_case_ids[14]
    my_comment = 'Due to Old session Confirmation page get open Without UI Elements '
    # user.confrimation_page_without_elements()
    # user.confrimation_page_elements()
    verify = user.VerifyLogin()
    assert verify == True, "User is not able to login with valid credentials"
    my_comment = 'User should be able to see Home page after clicking on verify button'


# def test_watch_now_movie(browser):
#     global test,my_comment
#     home=homepage(browser)
#     home.Refresh()
#     my_comment="watch now  movie button is not clickable "
#     verify_movie = home.click_watch_now_movie()
#     assert verify_movie == True,'watch movie is not clickable'
#
# def test_watch_trailer(browser):
#     global test,my_comment
#     home=homepage(browser)
#     home.Refresh()
#     my_comment="watch trailler button is not clickable"
#     verify_trailer = home.watch_trailor_for_movie()
#     assert verify_trailer==True

def test_view_details(browser):
    home = homepage(browser)
    view_det = ViewDetailsMoviePage(browser)
    global test, my_comment
    # test = test_case_ids[77]  # 190
    home_page = homePageObj(browser)
    my_comment = '"After clicking on view details button Movie de tails page is not getting open.'
    view_t =view_det.verify_view_details_button()
    # time.sleep(6)
    assert view_t == True

def test_poster_img(browser):
    home=homepage(browser)
    poster=homePageObj(browser)
    poster_img2=poster.verify_poster_img()
    assert poster_img2==True

def test_film_series_button(browser):
    home = homepage(browser)
    filmspagetitle = homePageObj(browser)
    time.sleep(50)
    film_series = filmspagetitle.verify_film_series()
    assert film_series == True


def test_list_button(browser):
    home=homepage(browser)
    list= homePageObj(browser)
    my_list2=list.verify_list_button()
    assert my_list2==True

def test_him_check_boxes(browser):
        home = homepage(browser)
        pagetitle = homePageObj(browser)
        page_title_checkox = pagetitle.verify_list_checkbox()
        assert page_title_checkox == True


def test_him_button(browser):
    home=homepage(browser)
    hometitle=homePageObj(browser)
    hometitle_button=hometitle.verify_him_button()
    assert hometitle_button==True



def test_poster_title1(browser):
    home=homepage(browser)
    hometitle2=homePageObj(browser)
    home_title3=hometitle2.verify_poster_view()
    assert home_title3==True

def test_click_my_list(browser):
    home=homepage(browser)
    hometitle4=homePageObj(browser)
    home_title5=hometitle4.add_to_list()
    assert home_title5==True

def test_click_movies(browser):
    home=homepage(browser)
    movies_title=homePageObj(browser)
    title_movie=movies_title.verify_add_list()
    assert title_movie==True

def test_grid_button(browser):
    home = homepage(browser)
    grid_title = homePageObj(browser)
    title_grid = grid_title.verify_grid_button()
    assert title_grid == True

def test_grid_click_button(browser):
    home = homepage(browser)
    grid_txt = homePageObj(browser)
    text_grid = grid_txt.verify_grid_button()
    assert text_grid == True

def test_assets_click_button(browser):
    home = homepage(browser)
    assets_button = homePageObj(browser)
    text_assets = assets_button.verify_assets_button()
    assert text_assets == True

def test_assets_checkbox_button(browser):
    home = homepage(browser)
    assets_checkboxes_button = homePageObj(browser)
    checkbox_assets = assets_checkboxes_button.verify_checkbox_button()
    assert checkbox_assets == True

def test_search_textbox(browser):
    home=homepage(browser)
    search_button=homePageObj (browser)
    search_txt=search_button.verify_send_value("gladiators")
    assert search_txt==True

def test_filter_textbox(browser):
    home=homepage(browser)
    filter_button=homePageObj(browser)
    filter_txt=filter_button.verify_filter_text()
    assert filter_txt==True

def test_mycart_button(browser):
    home=homepage(browser)
    text_cart_button=homePageObj(browser)
    your_cart=text_cart_button.verify_my_cart()
    assert your_cart==True

def test_yourcart_button(browser):
    home=homepage(browser)
    your_cart_button=homePageObj(browser)
    your_cart_button=your_cart_button.verify_my_cart()
    assert your_cart_button==True

def test_assets_clickbutton(browser):
    home=homepage(browser)
    assets_cart_button=homePageObj(browser)
    your_assets_button=assets_cart_button.verify_assets_click()
    assert your_assets_button==True


def test_assets_cart(browser):
    home=homepage(browser)
    assets_cart1=homePageObj(browser)
    my_assets_button=assets_cart1.verify_all_assets()
    assert my_assets_button==True


def test_create_cart_button(browser):
    home=homepage(browser) 
    cart_button=homePageObj(browser)
    my_cart_button=cart_button.input_cart_text("pythonCart")
    assert my_cart_button==True

def test_delete_cart(browser):
    home=homepage(browser)
    delete_cart=homePageObj(browser)
    my_delete_button=delete_cart.verify_delete_button()
    assert my_delete_button==True

def test_mgm_admin(browser):
    home=homepage(browser)
    mgm_cart=homePageObj(browser)
    my_mgm_button=mgm_cart.verify_mgm_admin()
    assert my_mgm_button==True

def test_search_field(browser):
    home=homepage(browser)
    search_box=homePageObj (browser)
    search_icon=search_box.verify_search_field("tara")
    assert search_icon==True

def test_invite_button(browser):
        home = homepage(browser)
        invite_box = homePageObj(browser)
        invite_icon = invite_box.verify_invite_button()
        assert invite_icon == True

# def test_create_list(browser):
#     global test,my_comment
#     home=homepage(browser)
#     my_comment="create a list is not creating"
#     verify_list=home.add_to_list_movie_pk()
#     assert verify_list==True


# #
# # # #@allure.title('TC_Raw: Delete the list form my list page ')
### def test_for_Row_data(browser):
# ##    home = homepage(browser)
#  ##   my_list = homePagemylistsObj(browser)
#  ### ##   list1 = home.ClickLists()
#  assert list1 == True, "Not redirecting to correct page"
#  ##   list1 = home.ClickLists()
#     my_list.delete_Demo_list(_url_)
#     my_list.delete_test2_list()
#     my_list.delete_raw_test1_list()
#     my_list.delete_raw_test_list()
#     my_list.delete_raw_recentlyList2()
#     my_list.delete_raw_recentlyList()
#     my_list.delete_raw_tv_show_list()
#     my_list.delete_raw_list_data_list()
#     my_list.delete_Demo1_list()
#     home.gotohomepage(_url_)
# # # #
# # # # #@allure.title('TC_Raw: Delete the list form my list page ')
# # # # def test_for_Row_data2(browser):
# # # #     home = homepage(browser)
# # # #     my_list = homePagemylistsObj(browser)  
# # # #     list1 = home.ClickLists()
# # # #     assert list1 == True, "Not redirecting to correct page"
# # # #     my_list.delete_Demo_list(_url_)
# # # #     my_list.delete_test2_list()
# # # #     my_list.delete_raw_test1_list()
# # # #     my_list.delete_raw_test_list()
# # # #     my_list.delete_raw_recentlyList2()
# # # #     my_list.delete_raw_recentlyList()
# # # #     my_list.delete_raw_tv_show_list()
# # # #     my_list.delete_raw_list_data_list()
# # # #     my_list.delete_Demo1_list()
# # # #     home.gotohomepage(_url_)
# # # #
# # # #
# # # #@allure.title('TC_016: Verify elements present in global header')
# def test_verify_home_page_global_header_elements(browser):
#     global test, my_comment
#     test = test_case_ids[15]
#     home = homepage(browser)
#     my_comment = 'Header logo not present in global header'
#     roar_logo = home.HomePageLogo()
#     assert roar_logo == True, "Header logo not present in global header"
#     films_series = home.HeaderFilmsAndSeries()
#     my_comment = 'Header Films & Series button is not present in global header'
#     assert films_series == True, "Header Films & Series button is not present in global header "
#     my_list = home.HeaderMylist()
#     my_comment = 'My list button is not present in global header'
#     assert my_list == True, "My list button is not present in global header"
#     logout = home.HeaderLogoutButton()
#     my_comment = 'Logout button is not present in global header'
#     assert logout == True, "Logout button is not present in global header"
#     search = home.HeaderSearchButton()
#     my_comment = 'Search button is not present in global header'
#     assert search == True, "Search button is not present in global header"
#     market_rule = home.HeaderMarketingRules()
#     my_comment = 'Search button is not present in global header'
#     assert market_rule == True, "Search button is not present in global header"
#     assets = home.HeaderAssets()
#     my_comment = 'Assets Button is not present in global header'
#     assert assets == True, "Assets Button is not present in global header"
#     my_cart = home.HeaderMyCarts()
#     my_comment = 'Assets Button is not present in global header'
#     assert my_cart == True, "My Carts button is not found in global header "
#     my_comment = '''Global Header should consist of following elements:
#                     1. Roar Logo
#                     2. Menu Links [FILMS & SERIES , MY LISTS , ASSETS , MY CARTS , MARKETING RULES]
#                     3.Search bar
#                     4. Logout [Button]'''
#
#
# # # #@allure.title('TC_017: Verify Menu links are clickable and redirects to correct page')
# def test_verify_menu_links_Clickable(browser):
#     home = homepage(browser)
#     global test, my_comment
#     test = test_case_ids[16]
#     my_comment = "Not redirecting to Film and series page / Film & Series button is not clickable "
#     movies = home.ClickFilmsSeries()
#     assert movies == True, "Not redirecting to Film and series page / Film & Series button is not clickable "
#     my_comment = "Not redirecting to Marketing Rules page / Marketing Rules button is not clickable"
#     marketing_rules = home.ClickMarketingRules()
#     assert marketing_rules == True, "Not redirecting to Marketing Rules page / Marketing Rules button is not clickable"
#     my_comment = "Not redirecting to My List page / my list button is not clickable "
#     list1 = home.ClickLists()
#     assert list1 == True, "Not redirecting to My List page / my list button is not clickable "
#     home.ClickAssets()
#     my_comment = 'Not redirecting to My cart page / My cart is not clickable'
#     my_cart = home.ClickMyCarts()
#     assert my_cart == True, "Not redirecting to My cart page / My cart is not clickable"
#     my_comment = '''Menu links should be clickable and should redirect to correct pages as below.
#                     FILMS & SERIES -- Movies and series listing
#                     MY LISTS --  All Lists
#                     ASSETS -- All title assets
#                     My CARTS  -- Carts lists
#                     MARKETING RULES -- Marketing rules page'''
#
#
# # # #@allure.title('TC_018: Verify on click of Roar logo in header user is redirected to Homepage')
# # #@allure.title('TC_019: Verify on single click search button a popup will open')
# def test_first_click_on_search(browser):
#     home = homepage(browser)
#     global test, my_comment
#     test = test_case_ids[18]
#     my_comment = 'Search button is not clickable / Search pop is not present'
#     search_text = home.firstClickSearchButton()
#     assert search_text == True, 'Search button is not clickable / Search pop is not present'
#     my_comment = 'On click search button popup should be open for search any title'
#
#
# # # #@allure.title('TC_020: Verify on click search close button a popup will hide')
# def test_click_on_search_close_button(browser):
#     home = homepage(browser)
#     global test, my_comment
#     test = test_case_ids[19]
#     my_comment = 'close button is not clickable / Search pop is not getting hide'
#     close_button = home.clickSearchCloseButton()
#     assert close_button == True, 'close button is not clickable / Search pop is not getting hide '
#     my_comment = 'On click search close button popup should be hide'
#
#
# # # #@allure.title('TC_021: Verify search field is present ')
# def test_verify_search_input_field(browser):
#     global test, my_comment
#     test = test_case_ids[20]
#     home = homepage(browser)
#     my_comment = 'search input field is not present'
#     input_field = home.verify_input_field_MovieOrSeriesName()
#     assert input_field == True, 'search input field is not present'
#     my_comment = 'user should be able to see search field'
#
#
# # # #@allure.title('TC_022: verify search button is clickable ')
# def test_verify_search_button_is_clickable(browser):
#     global test, my_comment
#     test = test_case_ids[21]
#     home = homepage(browser)
#     my_comment = 'search button is not present / search button is not clickable'
#     search_result = home.test_verify_Search_button()
#     assert search_result == True, 'search button is not present / search button is not clickable'
#     my_comment = 'user should be able to see search button'
#
#
# # # #@allure.title('TC_023: Verify user with entered search field and click on search'
# # #               # ' button page will redirect to Films & series page')
# def test_type_movie_or_series(browser):
#     global test, my_comment
#     test = test_case_ids[22]
#     home = homepage(browser)
#     # data = json.load(open('resources/dataFile.json', 'r'))
#     # for key, value in data.items():
#     #     print(key, value)
#     my_comment = 'Search Input field is not present'
#     movie_name = home.typeMovieOrSeriesName()
#     my_comment = 'Search button is not present / search button is not clickable'
#     search_result = home.clickSearchButton()
#     assert movie_name in search_result, 'Search button is not clickable'
#     my_comment = 'Page should redirected to films & series page after clicking on search button'
#
#
# # # #@allure.title('TC_024: Verify on click of Logout button, user is successfully logged out')
# def test_click_logoutButton(browser):
#     global test, my_comment
#     test = test_case_ids[23]
#     home = homepage(browser)
#     my_comment = 'logout button is not clickable'
#     verify = home.ClickLogoutButton()
#     assert verify == True, "logout button is not clickable"
#     user.LoginPage(_url_)
#     user.EnterEmail(email)
#     verify = user.ClickNext()
#     assert verify == True, "user not proceed to next step with valid email id"
#     user.EnterPassword(password)
#     user.verifyButton()
#     user.confrimation_page_without_elements()
#     user.confrimation_page_elements()
#     verify = user.VerifyLogin()
#     assert verify == True, "User is not able to login with valid credentials"
#     my_comment = 'On click of Logout button user should logged out of app and redirected to Login page'
#
#
# # # #@allure.title('TC_025: Verify Element Present in homepage')
# def test_verify_home_page_elements(browser):
#     global test, my_comment
#     test = test_case_ids[24]
#     home = homepage(browser)
#     home_page = homePageObj(browser)
#     my_comment = 'Global Header is not present'
#     global_header = home.HomepageElementHeader()
#     assert global_header == True, "Global Header is not present"
#     test_verify_home_page_global_header_elements(browser)
#     home.gotohomepage(_url_)
#     my_comment = 'Main carousel is not present'
#     # time.sleep(10)
#     main_carousel = home.HomepageMainCarousel()
#     assert main_carousel == True, "Main carousel is not present"
#     my_comment = " Footer not found / Footer Elements are not present"
#     assert home_page.verify_Privacypolicy() == True, "Privacy policy is not displaying in global footer. It should be " \
#                                                      "displayed in footer. "
#     my_comment = 'My list Section is not present in homepage'
#     verify_logo = home.verify_welcome_text_home_page_elements()
#     assert verify_logo == True, 'MGM ROAR logo is not clickable'
#     list1 = home.HomepageMovieList1()
#     assert list1 == True, "My list Section is not present in homepage"
#     my_comment = "Recently watched list is not present in homepage"
#     list2 = home.HomepageMovieList2()
#     assert list2 == True, "Recently watched list is not present in homepage"
#     my_comment = 'Recently list is not present in homepage'
#
# # #     # Alive List Removed
# # #     # list3 = home.HomepageMovieList3()
# # #     # assert list3 == True, "alive list is not present in homepage"
# # #     # my_comment = 'alive movie list is not present in homepage'
# # #
# # #     # Black History Month list removed
# # #     # list4 = home.HomepageMovieList4()
# # #     # assert list4 == True, "black history movie list is not present in homepage"
# # #     # my_comment = 'black history list is not present in homepage'
# # #
# # #     list5 = home.HomepageMovieList5()
# # #     assert list5 == True, "bond movie list is not present in homepage"
# # #     my_comment = 'Bond Movie list is not present in homepage'
# # #     list7 = home.HomepageMovieList7()
# # #     assert list7 == True, "Action Movie list is not present in homepage"
# # #     my_comment = 'Action Movie list is not present in homepage'
# # #
# # #     # Hallowen Movie list removed
# # #     # list8 = home.HomepageMovieList8()
# # #     # assert list8 == True, "Halloween Movie list is not present in homepage"
# # #     # my_comment = 'Halloween Movie list is not present in homepage'
# # #
# # #     # list9 = home.HomepageMovieList9()
# # #     # assert list9 == True, "Late Night Movie list is not present in homepage"
# # #     # my_comment = 'Late Night Movie list is not present in homepage'
# # #
# # #     # list10 = home.HomepageMovieList10()
# # #     # assert list10 == True, "Fight Night Movie list is not present in homepage"
# # #     # my_comment = 'Footer logo is not present in homepage'
# # #
# # #     Logo = home.HomepageFooterLogo()
# # #     assert Logo == True, "Footer logo is not present in homepage"
# # #     my_comment = 'Privacy button not present in homepage'
# # #     privacy = home.HomepageFooterPrivacy()
# # #     assert privacy == True, "Privacy button not present in homepage"
# # #     my_comment = "Footer Terms is not present in homepage"
# # #     terms = home.HomepageFooterTerms()
# # #     assert terms == True, "Footer Terms is not present in homepage"
# # #     my_comment = 'Footer support button is not present in homepage'
# # #     support = home.HomepageFooterSupport()
# # #     assert support == True, "Footer support button is not present in homepage"
# # #     my_comment = '''Homepage should have the following elements:
# # #                     1. Global Header
# # #                     2  Welcome text
# # #                     3. Main Carousel
# # #                     4. Movie Lists
# # #                     5. Global Footer'''
# # #
# # #
# # # #@allure.title('TC_026: Verify welcome text is visible ')
# def test_verify_welcome_text(browser):
#     global test, my_comment
#     test = test_case_ids[25]
#     home = homepage(browser)
#     my_comment = 'MGM ROAR logo is not clickable / Welcome Text is not present '
#     verify_logo = home.verify_welcome_text()
#     assert verify_logo == True, 'MGM ROAR logo is not clickable'
#     my_comment = 'user should able to  see welcome text'
#
#
# # # #@allure.title('TC_027: Verify elements present in Carousel')
# def test_home_page_carousel_elements(browser):
#     global test, my_comment
#     test = test_case_ids[26]
#     home = homepage(browser)
#     my_comment = 'Movies image slider not found in carousel section'
#     slider = home.MovieImageSlider()
#     assert slider == True, "Movies image slider not found in carousel section"
#     my_comment = "Progress bar not found in carousel section"
#     progress = home.ProgressBar()
#     assert progress == True, "Progress bar not found in carousel section"
#     my_comment = "Left navigation button not found in carousel section"
#     left = home.ProgressBarPreviousArrow()
#     assert left == True, "Left navigation button not found in carousel section"
#     my_comment = 'Right navigation button not found in carousel section'
#     right = home.ProgressBarNextArrow()
#     assert right == True, "Right navigation button not found in carousel section"
#     my_comment = '''Carousel should have the following elements:
#                     1. Movie Image Sliders
#                     2. Progress Bar with Slider Titles
#                     3. Right Navigation Arrow
#                     4. Left Navigation Arrow'''
#
#
# # # # #@allure.title('TC_028: Verify elements present in Movie image slider')
# # # # def test_verify_movie_image_slider_elements_movie_image_slider(browser):
# # # #     global test, my_comment
# # # #     test = test_case_ids[27]
# # # #     home = homepage(browser)
# # # #     home.gotohomepage(_url_)
# # # #     my_comment = 'Slider Background image not found'
# # # #     image = home.SliderBackgroundImage()
# # # #     assert image == True, "Slider Background image not found"
# # # #     home.Refresh()
# # # #     my_comment = "Logo of Movie not found"
# # # #     logo = home.movie_logoCarousel()
# # # #     assert logo == True, "Logo of Movie not found"
# # # #     home.Refresh()
# # # #     my_comment = 'Watch now button not found'
# # # #     watch = home.WatchNowButton()
# # # #     assert watch == True, "Watch now button not found"
# # # #     home.Refresh()
# # # #     my_comment = "Add to list button not found"
# # # #     add = home.AddToListButton()
# # # #     assert add == True, "Add to list button not found"
# # # #     home.Refresh()
# # # #     my_comment = "View details button not found"
# # # #     details = home.ViewDetailsButton()
# # # #     assert details == True, "View details button not found"
# # # #     my_comment = '''Each Movie Image Slider should have the following:
# # # #                     1. Slider background image
# # # #                     2. Logo
# # # #                     3. Watch Now [Button]
# # # #                     4. Add To List [Button]
# # # #                     5. View Details [Button]'''
# # # #
# # #
# # # # #@allure.title('TC_029: Verify Watch Now button is clickable and on click of it opens layout pop up')
# # # # def test_click_watch_now_carousel(browser):
# # # #     global test, my_comment
# # # #     test = test_case_ids[28]
# # # #     home = homepage(browser)
# # # #     video_player = videoplayer(browser)
# # # #     home.Refresh()
# # # #     my_comment = 'Watch Now button is not present / Watch Now button is not clickable '
# # # #     home.ClickWatchNowButton()
# # # #     video_player.MovieAlreadyPlayed()
# # # #     my_comment = 'Video Player Close Button is not present'
# # # #     zoom_button = video_player.zoomINButton()
# # # #     assert zoom_button == True, 'Video Player Close Button is not present'
# # # #     video_player.ClickCloseButton()
# # # #     my_comment = '''On click of Watch Now button, playout pop up should be opened
# # # #                     Pop Up should consist of the following:
# # # #                     1. Player should be available in the pop up
# # # #                     2. Player controls
# # # #                     3. Close button'''
# # #
# # #
# # # # #@allure.title('TC_032: Verify View Details button is clickable and on click redirect to movie details page')
# # # # def test_carousel_view_details_button(browser):
# # # #     global test, my_comment
# # # #     test = test_case_ids[31]
# # # #     home = homepage(browser)
# # # #     my_comment = 'View Details button is not clickable / on click view detail button is not redirect to movie detail page '
# # # #     title = home.MovieListViewDetailButton()
# # # #     assert "ROAR | " in title, "Clicking on view detaild / movie detail page is not opening."
# # # #     synopsis = home.VerifySynopsisTitle()
# # # #     assert synopsis == True
# # # #     my_comment = 'View Details should be clickable on sliders and on click of view details button user should be ' \
# # # #                  'redirected to the details page of that movie'
# # #
# # #
# # # #@allure.title('TC_033: Verify the titles are clickable and clicking them take the carousel to that slider ')
# def test_carousel_click_slider(browser):
#     global test, my_comment
#     test = test_case_ids[32]
#     home = homepage(browser)
#     home.gotohomepage(_url_)
#     my_comment = 'Carousel title is not clickable'
#     titel_text, active_text = home.click_on_carousel_title()
#     assert titel_text == active_text, "Carousel title is not clickable "
#     my_comment = 'On click of Title, carousel should show the clicked Slider'
#
#
# # # #@allure.title('TC_034: Verify the Title is underlined(highlighted) when carousel moves to that slider')
# def test_carousel_slider(browser):
#     global test, my_comment
#     test = test_case_ids[33]
#     home = homepage(browser)
#     my_comment = 'Carousel Slider is not present'
#     slider = home.verify_carousel_slider()
#     assert slider == True, "Carousel Slider is not present"
#     my_comment = 'Title should be underlined when carousel is at the title slider'
#
#
# # # #@allure.title('TC_035: Verify user is able to move to next slider by clicking Right Navigation Arrow')
# def test_home_right_navigation(browser):
#     global test, my_comment
#     test = test_case_ids[34]
#     home = homepage(browser)
#     my_comment = 'can not Click on right navigation button / movie slider is not present'
#     first_slider, second_slider = home.click_carousel_next()
#     assert first_slider != second_slider, "can not Click on right navigation button / movie slider is not present "
#     my_comment = '''On Click of Right Navigation Arrow,
#                     1. Carousel should move to next slider
#                     2. Progress bar should progress forward
#                     3. Slider title should be highlighted'''
#
#
# # # #@allure.title('TC_036: Verify user is able to move to previous slider by clicking Left Navigation Arrow')
# def test_home_left_navigation(browser):
#     global test, my_comment
#     test = test_case_ids[35]
#     home = homepage(browser)
#     my_comment = 'Right navigation button is not clickable'
#     first_slider, second_slider = home.click_carousel_prev()
#     assert first_slider != second_slider, "Right navigation button is not clickable"
#     my_comment = '''On Click of Left Navigation Arrow,
#                     1. Carousel should move to previous slider
#                     2. Progress bar should progress backward
#                     3. Slider title should be highlighted'''
#
#
# # # #@allure.title('TC_037: Verify elements for each list')
# # def test_verify_each_element_movie_list(browser):
# #     global test, my_comment
# #     test = test_case_ids[36]
# #     home = homepage(browser)
# #     home_page = homePageObj(browser)
# #     # time.sleep(2)
# #     my_comment = 'See all buttons are not present in homepage'
# #     see_all_count = home.SeeAllButton()
# #     assert see_all_count >= 10, "See all buttons are not present in homepage"
# #     my_comment = 'List Sections are not present in homepage'
# #     list1 = home.HomepageMovieList1()
# #     assert list1 == True, "Movie list not found"
# #     list2 = home.HomepageMovieList2()
# #     assert list2 == True, "Movie list not found"
# # #     # list3 = home.HomepageMovieList3()
# # #     # assert list3 == True, "Movie list not found"
# # #     # list4 = home.HomepageMovieList4()
# # #     # assert list4 == True, "Movie list not found"
# # #     # list5 = home.HomepageMovieList5()
# # #     # assert list5 == True, "Movie list not found"
# # #     # list7 = home.HomepageMovieList7()
# # #     # assert list7 == True, "Movie list not found"
# # #     # list8 = home.HomepageMovieList8()
# # #     # assert list8 == True, "Movie list not found"
# # #     # list9 = home.HomepageMovieList9()
# # #     # assert list9 == True, "Movie list not found"
# # #     # list10 = home.HomepageMovieList10()
# # #     # assert list10 == True, "Movie list not found"
# # #     # my_comment = 'Posters are not present in lis section'
# # #     poster = home.PosterImage()
# # #     assert poster > 50, 'Posters are not present'
# # #     # time.sleep(2)
# # #     my_comment = 'movies title are not present in the list'
# # #     movie_title = home.MovieTitle()
# # #     assert movie_title == True, 'movies title are not present in the list'
# # #     my_comment = 'Right navigation button is not present'
# # #     right_navigation = home_page.click_list_right_arrow()
# # #     assert right_navigation == True, 'Right navigation button is not present'
# # #     my_comment = 'Left navigation button is not present'
# # #     left_navigation = home_page.click_list_left_arrow()
# # #     assert left_navigation == True, 'Left navigation button is not present'
# # #     my_comment = 'list Slider is not present in list section '
# # #     slider = home_page.verify_list_slider()
# # #     assert slider == True, 'list Slider is not present in list section '
# # #     my_comment = '''Following Elements should be present for lists
# # #                     1. List Name
# # #                     2. See all [button]
# # #                     3. Title Cards
# # #                     4. Slider
# # #                     5. Right Navigation Arrow
# # #                     6. Left Navigation Arrow
# # #                     7  Horizontal scroller'''
# # #
# # #
# # # # #@allure.title('New TC_038: Verify click functionality of See All button')
# def test_click_list_see_all(browser):
#     global test, my_comment
#     test = test_case_ids[37]
#     home = homepage(browser)
#     home_page = homePageObj(browser)
#     my_comment = " Footer not found / Footer Elements are not present"
#     assert home_page.verify_Privacypolicy() == True, "Privacy policy is not displaying in global footer. It should be " \
#                                                      "displayed in footer. "
#     my_comment = 'See All button is not clickable / Action title is not present'
#     list_title = home_page.click_action_list_see_all()
#     assert list_title == True, 'See All button is not clickable /Action title is not present'
#     my_comment = 'On click of See All button user should be redirected to that list page'
#
#
# # # #@allure.title('TC_039: Verify elements for each Movie card')
# def test_verify_each_movie_card_element(browser):
#     global test, my_comment
#     test = test_case_ids[38]
#     home = homepage(browser)
#     home.headerRoarLogo()
#     my_comment = 'poster images are not present'
#     poster_image = home.PosterImage()
#     assert poster_image > 12, 'poster images are not present'
#     my_comment = 'movies titles are not present'
#     movie_title = home.verify_list_title()
#     assert movie_title > 12, 'movies titles are not present '
#     my_comment = 'movie genre are not present'
#     movie_genre = home.MovieGenre()
#     assert movie_genre > 2, 'movie genre are not present'
#     my_comment = '''Following Elements should be present for Movie Cards
#                     1. Poster Image
#                     2. Movie Title
#                     3. Genres'''
#
#
# # # #@allure.title('TC_040: Verify hover behavior on movie cards')
# def test_verify_hover_behaviour_movie_card(browser):
#     global test, my_comment
#     test = test_case_ids[39]
#     home = homepage(browser)
#     my_comment = 'view detail button is not present'
#     details = home.viewDetails_moviecardfunc()
#     assert details == True, 'view detail button is not present'
#     my_comment = 'Add-to-list button is not present'
#     list = home.addList_moviecardfunc()
#     assert list == True, 'Add-to-list button is not present'
#     my_comment = 'Watch Now is not present'
#     watch = home.watchmovie_moviecrdfunc()
#     assert watch == True, 'Watch Now is not present'
#     my_comment = 'Trailer button is not present'
#     trailer = home.verify_watchTrailer_cards()
#     assert trailer == True, 'Trailer button is not present'
#     my_comment = '''On hover on movie cards following buttons should be shown
#                     1. Add to Lists
#                     2. Watch Movie
#                     3. Watch Trailer
#                     4. View Details'''
#
#
# # # #@allure.title('TC_041: Verify functionality of Add to List button')
# def test_click_action_add_to_list_button(browser):
#     global test, my_comment
#     test = test_case_ids[40]
#     home = homepage(browser)
#     my_comment = 'add to list popup is not open'
#     add_list = home.click_add_to_list_movies()
#     assert add_list == True, 'add to list popup is not open'
#     my_comment = 'Clicking add to list should open add to list pop up'
#
#
# # # #@allure.title('TC_042: Verify functionality of Watch Movie button')
# def test_click_action_watch_now_list_button(browser):
#     global test, my_comment
#     test = test_case_ids[41]  # 154
#     home = homepage(browser)
#     home.Refresh()
#     my_comment = 'Watch Now button is not clickable'
#     zoom_button = home.click_watch_now()
#     assert zoom_button == True, 'Watch Now button is not clickable'
#     my_comment = '''On click of Watch Movie  button following should happen:
#                     1. Play out pop up should be opened'''
#
#
# # # #@allure.title('TC_044: Verify functionality of Watch Trailer button')
# def test_click_action_trailer(browser):
#     global test, my_comment
#     test = test_case_ids[43]  # 156
#     home = homepage(browser)
#     my_comment = 'Trailer button is not clickable'
#     trailer = home.click_trailer()
#     assert trailer == True, 'Trailer button is not clickable'
#     my_comment = '''On click of Watch Trailer button following should happen:
#                     1. Play out pop up should be opened
#                     2. Trailer of that movie should be played'''
#
#
# # # #@allure.title('TC_046: Verify functionality of View Details button')
# def test_action_functionality_view_details_button_home_page(browser):
#     global test, my_comment
#     test = test_case_ids[45]  # 158
#     home = homepage(browser)
#     my_comment = 'view details is not clickable / view details page is not open'
#     view_details = home.click_viewdetails_movieCard()
#     assert view_details == True, 'view details is not clickable / view details page is not open'
#     my_comment = 'On click of View Details button user should be redirected to the details page of that movie'
#
#
# # # #@allure.title('TC_047: Verify user is able to scroll cards thorough the horizontal scroller')
# def test_horizontal_scroller_action_list(browser):
#     global test, my_comment
#     test = test_case_ids[46]  # 159
#     home = homepage(browser)
#     home.gotohomepage(_url_)
#     my_comment = 'total 10 cards are not present / Horizontal Scroller is not working'
#     action_movie_fifth_card = home.click_and_move_horizontal_scroller()
#     assert action_movie_fifth_card == True, 'total 10 cards are not present / Horizontal Scroller is not working'
#     my_comment = 'User should be able to scroll title cards through horizontal scroller'
# # #
# # #
# # # #@allure.title('TC_048: Verify Right Navigation Arrow is visible only when we hover on the last card on the right')
# def test_verify_right_navigation_arrow_action_list(browser):
#     global test, my_comment
#     test = test_case_ids[47]  # 160
#     home = homepage(browser)
#     home_page = homePageObj(browser)
#     my_comment = 'right navigation is not present in list section'
#     right_arrow = home_page.verify_right_navigation_arrow()
#     assert right_arrow == True, 'right navigation is not present in list section'
#     my_comment = 'Right Navigation Arrow should only be enabled when user hovers on last movie card from right'
#
# #
# # # #@allure.title('TC_049: Verify click behavior of Right Navigation arrow')
# def test_click_right_navigation_arrow_action_list(browser):
#     global test, my_comment
#     test = test_case_ids[48]  # 161
#     home = homepage(browser)
#     home_page = homePageObj(browser)
#     my_comment = 'Right navigation is not clickable'
#     right_navigation = home_page.click_list_right_arrow()
#     assert right_navigation == True, 'Right navigation is not clickable'
#     my_comment = 'On click of Right Navigation Arrow, the movie slider should progress 3 cards towards right'
#
#
# # # #@allure.title('TC_050: Verify Right Navigation Arrow is disabled when we are on the last card in the list')
# def test_click_second_right_navigation_arrow_action_list(browser):
#     global test, my_comment
#     test = test_case_ids[49]  # 162
#     home = homepage(browser)
#     home_page = homePageObj(browser)
#     my_comment = 'Right navigation is present'
#     right_navigation = home_page.click_list_second_right_arrow()
#     assert right_navigation == False, 'Right navigation is present'
#     my_comment = 'Right Navigation Arrow should be disabled when user is on last movie card in the list'
#
#
# # # #@allure.title(
# # #     # 'TC_051: Verify Left Navigation Arrow is visible when we click Right Navigation arrow and then hover on left card')
# # def test_verify_left_navigation_arrow_action_list(browser):
# #     global test, my_comment
# #     test = test_case_ids[50]  # 163
# #     home = homepage(browser)
# #     home_page = homePageObj(browser)
# #     home.Refresh()
# #     my_comment = 'Right navigation is not clickable / Action list is not present'
# #     home.scroll_to_action_list()
# #     right_navigation = home_page.click_list_right_arrow()
# #     assert right_navigation == True, 'Right navigation is not clickable'
# #     my_comment = 'left navigation button is not present'
# #     left_navigation = home_page.click_list_left_arrow()
# #     assert left_navigation == True, 'left navigation button is not present'
# #     my_comment = 'Left Navigation Arrow should only be enabled when user hovers on first movie card from left'
# #
# #
# # # #@allure.title('TC_052: Verify click behavior of Left Navigation arrow')
# def test_click_left_navigation_arrow_action_list(browser):
#     global test, my_comment
#     test = test_case_ids[51]  # 164
#     home = homepage(browser)
#     home_page = homePageObj(browser)
#     my_comment = 'Left navigation is not clickable'
#     left_navigation = home_page.click_left_navigation_arrow()
#     assert left_navigation == False, 'left navigation is not clickable'
#     my_comment = 'On click of Left Navigation Arrow, the movie slider should progress 3 cards towards left'
#
# #
# # # #@allure.title('TC_053: Verify Left Navigation Arrow is disabled when we are on the first card in the list')
# def test_verify_left_navigation_action_list(browser):
#     global test, my_comment
#     test = test_case_ids[52]  # 165
#     home = homepage(browser)
#     home_page = homePageObj(browser)
#     my_comment = 'left navigation is visible'
#     left_navigation = home_page.verify_left_navigation_arrow()
#     assert left_navigation == False, 'left navigation is visible'
#     my_comment = 'Left Navigation Arrow should be disabled when user is on first movie card in the list'
#
#
# # # #@allure.title('TC_054, Verify elements for My List section')
# def test_verify_my_list_elements(browser):
#     global test, my_comment
#     test = test_case_ids[53]  # 166
#     elements = homePagemylistsObj(browser)
#     # time.sleep(2)
#     my_comment = "Title is not showing in my Lists section. It should show on movie cards"
#     assert elements.verify_Mylists_title() == True, "Title is not showing in my Lists section. It should show on " \
#                                                     "movie cards "
#     my_comment = "See all button is not displayed. button should show in right ."
#     assert elements.verify_seeAll() == True, "See all button is not displayed. button should show in right ."
#     assert elements.verify_my_list_slider() == True, "Slider is not present in My List section"
#     my_comment = "Right navigation arrow is not showing . it should show on last list"
#     assert elements.verify_rightNav() == True, "Right navigation arrow is not showing . it should show on last list " \
#                                                "card "
#     elements.click_rightNav()
#     my_comment = "Left navigation arrow is not showing . it should show on first list card"
#     assert elements.verify_LeftNav() == True, "Left navigation arrow is not showing . it should show on first list card"
#     # time.sleep(2)
#     my_comment = """Following Elements should be present for lists
#                     1. My List text
#                     2. See Lists  [button]
#                     3. Lists Cards
#                     4. Slider
#                     5. Right Navigation Arrow
#                     6. Left Navigation Arrow
#                     7. Horizontal scroller"""
#
#
# # # #@allure.title('TC_055,Verify click functionality of See lists button ')
# def test_click_my_list_see_all_button(browser):
#     global test, my_comment
#     test = test_case_ids[54]  # 167
#     home = homepage(browser)
#     elements = homePagemylistsObj(browser)
#     my_comment = "See All is not clickable in my list section"
#     list_page = elements.click_myList_see_all()
#     assert list_page == True, "See All is not clickable in my list section"
#     my_comment = 'On click of See lists button user should be redirected to My lists page'


# # #@allure.title('TC_056, Verify click functionality of list cards ')
# def test_click_my_list_card(browser):
#     global test, my_comment
#     test = test_case_ids[55]  # 168
#     home = homepage(browser)
#     home_page = homePageObj(browser)
#     elements = homePagemylistsObj(browser)
#     home.gotohomepage(_url_)
#     assert home_page.verify_Privacypolicy() == True, "Privacy policy is not displaying in global footer. It should be " \
#                                                      "displayed in footer. "
#     my_comment = 'My list Section is not present in homepage'
#     # time.sleep(15)
#     verify_logo = home.verify_welcome_text_home_page_elements()
#     assert verify_logo == True, 'MGM ROAR logo is not clickable'
#     my_comment = 'my list card are not clickable'
#     # time.sleep(15)
#     assert elements.verify_Mylists_title() == True, "Title is not showing in my Lists section. It should show on " \
#                                                     "movie cards "
#     list_page = elements.click_myList_card()
#     assert 'list' in list_page, 'my list card are not clickable'
#     my_comment = 'On click of list cards user should be redirected to that list page'
#
# #
# # # #@allure.title('TC_057: Verify user is able to scroll cards thorough the horizontal scroller ')
# def test_verify_horizontal_my_list_slider(browser):
#     global test, my_comment
#     test = test_case_ids[56]  # 169
#     home = homepage(browser)
#     home_page = homePageObj(browser)
#     elements = homePagemylistsObj(browser)
#     home.gotohomepage(_url_)
#     assert home_page.verify_Privacypolicy() == True, "Privacy policy is not displaying in global footer. It should be " \
#                                                      "displayed in footer. "
#     my_comment = 'My list Section is not present in homepage'
#     # time.sleep(15)
#     verify_logo = home.verify_welcome_text_home_page_elements()
#     assert verify_logo == True, 'MGM ROAR logo is not clickable'
#     # time.sleep(15)
#     my_comment = 'Horizontal slider is not present / Horizontal slider is not scrolled'
#     assert elements.verify_Mylists_title() == True, "Title is not showing in my Lists section. It should show on " \
#                                                     "movie cards "
#     # time.sleep(12)
#     my_list_slider = home.click_and_move_my_list_horizontal_scroller()
#     assert my_list_slider == True, 'Horizontal slider is not present / Horizontal slider is not scrolled '
#     my_comment = 'User should be able to scroll title cards through horizontal scroller'
#
#
# # # #@allure.title('TC_058: Verify Right Navigation Arrow is visible only when we hover on the last card on the right')
# def test_verify_my_list_right_navigation_arrow(browser):
#     global test, my_comment
#     test = test_case_ids[57]  # 170
#     home = homepage(browser)
#     home_page = homePageObj(browser)
#     elements = homePagemylistsObj(browser)
#     my_comment = 'Right navigation arrow is not Present'
#     home.gotohomepage(_url_)
#     assert home_page.verify_Privacypolicy() == True, "Privacy policy is not displaying in global footer. It should be " \
#                                                      "displayed in footer. "
#     my_comment = 'My list Section is not present in homepage'
#     # time.sleep(15)
#     verify_logo = home.verify_welcome_text_home_page_elements()
#     assert verify_logo == True, 'MGM ROAR logo is not clickable'
#     # time.sleep(15)
#     assert elements.verify_Mylists_title() == True, "Title is not showing in my Lists section. It should show on " \
#                                                     "movie cards "
#     # assert elements.verify_Mylists_title() == True, "Title is not showing in my Lists section"
#     assert elements.verify_rightNav() == True, "Right navigation arrow is not showing "
#     my_comment = 'Right Navigation Arrow should only be enabled when user hovers on last list card from right'
#
#
# # # #@allure.title('TC_059: Verify click behavior of Right Navigation arrow')
# def test_click_my_list_right_navigation_arrow(browser):
#     global test, my_comment
#     test = test_case_ids[58]  # 171
#     home = homepage(browser)
#     home_page = homePageObj(browser)
#     elements = homePagemylistsObj(browser)
#     my_comment = 'Right Navigation button is not Clickable / Right Navigation button is not present'
#     home.gotohomepage(_url_)
#     assert home_page.verify_Privacypolicy() == True, "Privacy policy is not displaying in global footer. It should be " \
#                                                      "displayed in footer. "
#     my_comment = 'My list Section is not present in homepage'
#     # time.sleep(15)
#     verify_logo = home.verify_welcome_text_home_page_elements()
#     assert verify_logo == True, 'MGM ROAR logo is not clickable'
#     # time.sleep(15)
#     assert elements.verify_Mylists_title() == True, "Title is not showing in my Lists section. It should show on " \
#                                                     "movie cards "
#     # assert elements.verify_Mylists_title() == True, "Title is not showing in my Lists section"
#     assert elements.verify_rightNav() == True, "Right navigation arrow is not showing "
#     elements.click_rightNav()
#     assert elements.verify_LeftNav() == True, "Left navigation arrow is not showing . it should show on first list card"
#     my_comment = 'On click of Right Navigation Arrow, the list slider should progress towards right'
#
# #
# # #@allure.title('TC_060: Verify Right Navigation Arrow is disabled when we are on the last card in the list')
# def test_click_my_list_second_right_navigation_arrow(browser):
#     global test, my_comment
#     test = test_case_ids[59]  # 172
#     elements = homePagemylistsObj(browser)
#     my_comment = 'Right navigation arrow is present'
#     assert elements.verify_second_rightNav() == False, "Right navigation arrow is present "
#     my_comment = 'Right Navigation Arrow should be disabled when user is on last list card in the list'
#
# #
# # # #@allure.title('TC_061: Verify Left Navigation Arrow is visible only when we hover on the first card on the left')
# def test_verify_my_list_left_navigation_arrow(browser):
#     global test, my_comment
#     test = test_case_ids[60]  # 173
#     home = homepage(browser)
#     elements = homePagemylistsObj(browser)
#     home_page = homePageObj(browser)
#     home.gotohomepage(_url_)
#     assert home_page.verify_Privacypolicy() == True, "Privacy policy is not displaying in global footer. It should be " \
#                                                      "displayed in footer. "
#     my_comment = 'My list Section is not present in homepage'
#     # time.sleep(15)
#     verify_logo = home.verify_welcome_text_home_page_elements()
#     assert verify_logo == True, 'MGM ROAR logo is not clickable'
#     # time.sleep(15)
#     my_comment = 'Left Navigation button is not present / Right Navigation button is not Clickable'
#     assert elements.verify_Mylists_title() == True, "Title is not showing in my Lists section"
#     assert elements.verify_rightNav() == True, "Right navigation arrow is not showing "
#     elements.click_rightNav()
#     assert elements.verify_LeftNav() == True, "Left navigation arrow is not showing "
#     my_comment = 'Left Navigation Arrow should only be enabled when user hovers on first list card from left'
#
#
# # # #@allure.title('TC_062: Verify click behavior of Left Navigation arrow')
# def test_click_my_list_left_navigation_arrow(browser):
#     global test, my_comment
#     test = test_case_ids[61]  # 174
#     home = homepage(browser)
#     elements = homePagemylistsObj(browser)
#     my_comment = 'Left Navigation arrow is not present / Left Navigation button is not clickable'
#     elements.click_leftNav()
#     assert elements.verify_left_navigation() == False, "Left Navigation arrow is not present / " \
#                                                        "Left Navigation button is not clickable"
#     my_comment = 'On click of Left Navigation Arrow, the list slider should progress towards left'
#
#
# # # #@allure.title('TC_063: Verify Left Navigation Arrow is disabled when we are on the first card in the list')
# def test_verify_mylist_left_navigation_arrow(browser):
#     global test, my_comment
#     test = test_case_ids[62]  # 175
#     home = homepage(browser)
#     elements = homePagemylistsObj(browser)
#     my_comment = "Left Navigation arrow is present"
#     assert elements.verify_left_navigation() == False, "Left Navigation arrow is present"
#     my_comment = 'Left Navigation Arrow should be disabled when user is on first list card in the list'
#
# # #
# # # #@allure.title('TC_068: Verify elements for Recently Watched section')
# def test_verify_recently_list_elements(browser):
#     global test, my_comment
#     test = test_case_ids[67]  # 180
#     home = homepage(browser)
#     home_page = homePageObj(browser)
#     home.gotohomepage(_url_)
#     my_comment = 'Title text for movie in recently watched is not displaying / Recently Watch section is not Present'
#     assert home_page.verify_Privacypolicy() == True, "Privacy policy is not displaying in global footer. It should be " \
#                                                      "displayed in footer. "
#     # time.sleep(15)
#     my_comment = 'My list Section is not present in homepage'
#     verify_logo = home.verify_welcome_text_home_page_elements()
#     assert verify_logo == True, 'MGM ROAR logo is not clickable'
#     # time.sleep(15)
#     assert home_page.verify_titleText() == True, "Title text for movie in recently watched is not displaying"
#     my_comment = 'Movie poster is not Present in Recently watch section'
#     assert home_page.verify_recently_watch_first_poster() == True, "First poster is not Present"
#     assert home.verify_recently_horizontal_slider() == True, "horizontal slider is not present in recently section"
#     my_comment = 'horizontal slider is not present in recently section'
#     assert home_page.verify_rightarrow() == True, "Right Navigation bar is not showing "
#     home_page.click_rightarrow()
#     assert home_page.verify_leftarrow() == True, "Left navigation bar is not showing "
#     my_comment = '''Recently Watched section should have the following elements
#                     1. Title Text
#                     2. Movie Cards
#                     3. Horizontal Scroll Bar
#                     4. Right Navigation Arrow
#                     5. Left Navigation Arrow
#                  '''
#
#
# # # #@allure.title('TC_070: Verify movies are sorted in correct order')
# def test_correct_order_recently_list(browser):
#     global test, my_comment
#     test = test_case_ids[69]  # 182
#     home = homepage(browser)
#     home.Refresh()
#     home_page = homePageObj(browser)
#     my_comment = "The video played from action/adventure has not been added in recently " \
#                  "watched playlist in correct ordered "
#     home_page.click_watchmovie()
#     # time.sleep(25)
#     home_page.click_crossimg()
#     time.sleep(2)
#     global played_moviename, rec_addedmovie, play_2movie
#     played_moviename = home_page.play_moviename()
#     # time.sleep(2)
#     play_2movie = home_page.play_2movieCard_name()
#     # time.sleep(2)
#     rec_addedmovie = home_page.recent_moviename()
#     # time.sleep(2)
#     # print("played_moviename---", played_moviename, "rec_addedmovie------", rec_addedmovie, "play_2movie-------", play_2movie)
#     assert played_moviename == rec_addedmovie, "The video played from action/adventure has not been added in recently " \
#                                                "watched playlist in correct ordered "
#     my_comment = 'As user the user progress to watching movies, then recently watched section should have all entries' \
#                  ' in decending order based on view time. i.e. First watched movie should be at last and Latest' \
#                  ' watched movie should be at first'
#
# #
# # # #@allure.title('TC_071: Verify elements for each Movie card in recently watched')
# def test_verify_recently_list_movie_card_element(browser):
#     global test, my_comment
#     test = test_case_ids[70]  # 183
#     home = homepage(browser)
#     home_page = homePageObj(browser)
#     my_comment = 'Movie title is not displaying in recently watched Section '
#     assert home_page.verifyMovieTitle() == True, "Movie title is not displaying in recently watched " \
#                                                              "section "
#     my_comment = 'Movie generes not displayed in recently watched '
#     assert home_page.MovieGenre() == True, "Movie generes not displayed in recently watched "
#     my_comment = 'Movie poster is not Present'
#     assert home_page.verify_recently_watch_first_poster() == True, "First poster is not Present"
#     my_comment = '''Following Elements should be present for Movie Cards
#                     1. Poster Image
#                     2. Movie Title
#                     3. Genres'''
#
# #
# # # #@allure.title('TC_072: Verify hover behavior on movie cards')
# def test_recently_list_hover_card1(browser):
#     global test, my_comment
#     test = test_case_ids[71]  # 184
#     home = homepage(browser)
#     home_page = homePageObj(browser)
#     my_comment = 'Add to list is not showing on hover of movie card '
#     assert home_page.addTolist() == "ADD TO LIST", 'Add to list is not showing on hover of movie card '
#     # time.sleep(2)
#     my_comment = "Watch movie is not showing on hover of movie card. "
#     assert home_page.watchMoviesoption() == "WATCH NOW", "Watch movie is not showing on hover of movie card. "
#     my_comment = "Watch movie is not showing on hover of movie card. "
#     assert home_page.watchTraileroption() == "WATCH TRAILER", "Watch movie is not showing on hover of movie card. "
#     my_comment = "Watch movie is not showing on hover of movie card. "
#     assert home_page.viewDetailsoption() == "VIEW DETAILS", "Watch movie is not showing on hover of movie card. "
#     my_comment = """On hover on movie cards following buttons should be shown
#                     1. Add to Lists
#                     2. Watch Movie
#                     3. Watch Trailer
#                     4. View Details"""
#
#
# # # #@allure.title('TC_073: Verify functionality of Add to List button')
# def test_verify_add_list_functionality_movie_recently_list(browser):
#     global test, my_comment
#     # home = homepage(browser)
#     test = test_case_ids[72]  # 185
#     home_page = homePageObj(browser)
#     my_comment = "After clicking on add to list button Pop is not opening. "
#     home_page.click_addList()
#     assert home_page.verifyAlert() == "CREATE A NEW LIST", "After clicking on add to list button Pop is not opening. "
#     my_comment = "Clicking add to list should open add to list pop up"
#
#
# # # #@allure.title('TC_074: Verify functionality of Watch Movie button')
# def test_watch_movie_functionality_recently_list(browser):
#     home = homepage(browser)
#     global test, my_comment
#     test = test_case_ids[73]  # 186
#     home.gotohomepage(_url_)
#     my_comment = 'Pop up is not opening for Watch Now-Movie'
#     home_page = homePageObj(browser)
#     home_page.click_recwatch_movie()
#     # time.sleep(2)
#     home_page.choose_click()
#     zoom_button = home_page.Validate_crossimg_button()
#     assert zoom_button == True, 'Pop up is not opening for Watch Now-Movie '
#     # time.sleep(2)
#     home_page.click_crossimg()
#     my_comment = 'On click of Watch now button following should happen-> Playout pop up should be opened'
#
#
# # #@allure.title('TC_076: Verify functionality of Watch Trailer button')
# def test_watch_trailer_functionality_movie_recently_list(browser):
#     home = homepage(browser)
#     global test, my_comment
#     test = test_case_ids[75]  # 188
#     home_page = homePageObj(browser)
#     # time.sleep(2)
#     my_comment = 'Pop up is not opening for Watch Trailer'
#     home_page.click_recwatch_trailer()
#     # time.sleep(2)
#     home_page.choose_click()
#     cross_button = home_page.Validate_crossimg_button()
#     assert cross_button == True, 'Pop up is not opening for Watch Trailer'
#     # time.sleep(2)
#     home_page.click_crossimg()
#     my_comment = 'On click of Watch Trailer button following should happen -> Playout pop up should be opened'

# #@allure.title('TC_078: Verify functionality of View Details button')
# def test_view_details_functionality_movie_recently_list(browser):
#     home = homepage(browser)
#     global test, my_comment
#     test = test_case_ids[77]  # 190
#     home_page = homePageObj(browser)
#     my_comment = '"After clicking on view details button Movie de tails page is not getting open.'
#     home_page.click_viewdetails()
#     # time.sleep(6)
#     assert home_page.verify_pagetitle() == rec_addedmovie, "After clicking on view details button Movie " \
#                                                                        "details page is not opeing. "
#     my_comment = 'On click of View Details button user should be redirected to the details page of that movie'
#
#
# #@allure.title('TC_079: Verify user is able to scroll cards thorough the horizontal scroller')
# def test_click_recently_horizontal_slider(browser):
#     home = homepage(browser)
#     global test, my_comment
#     test = test_case_ids[78]  # 191
#     home.gotohomepage(_url_)
#     my_comment = 'slider is not present in recently watch section'
#     slider = home.click_recently_horizontal_slider()
#     assert slider == True, 'slider is not present in recently watch section'
#     my_comment = 'User should be able to scroll cards through horizontal scroller'
#
#
# #@allure.title('TC_080: Verify Right Navigation Arrow is visible only when we hover on the last card on the right')
# def test_right_navigation_recently_list(browser):
#     home = homepage(browser)
#     global test, my_comment
#     test = test_case_ids[79]  # 192
#     home_page = homePageObj(browser)
#     home.gotohomepage(_url_)
#     my_comment = '"Right navigation arrow should displayed when hover over last movie cards. "'
#     assert home_page.verify_rightarrow() == True, "Right navigation arrow should displayed when hover over last movie " \
#                                                   "cards. "
#     my_comment = 'Right Navigation Arrow should only be enabled when user hovers on last movie card from right'
#
#
# #@allure.title('TC_081: Verify click behavior of Right Navigation arrow')
# def test_click_right_navigation_arrow_recently_list(browser):
#     home = homepage(browser)
#     global test, my_comment
#     test = test_case_ids[80]  # 193
#     home_page = homePageObj(browser)
#     my_comment = 'Right Navigation button is not Clickable in Recently Watched section'
#     home_page.click_rightarrow()
#     # time.sleep(2)
#     my_comment = 'On click of Right Navigation Arrow, the movie slider should progress towards right'
#
#
# #@allure.title('TC_082: Verify Right Navigation Arrow is disabled when we are on the last card in the list')
# def test_right_navigation_disabled_arrow_recently_list(browser):
#     home = homepage(browser)
#     global test, my_comment
#     test = test_case_ids[81]  # 194
#     home_page = homePageObj(browser)
#     my_comment = "Right navigation is not disabled when it is on last movie cards. "
#     home_page.second_click_rightarrow()
#     # time.sleep(2)
#     assert home_page.verify_right_disbaled() == False, "Right nav is not disabled when it is on last movie cards. "
#     my_comment = "Right Navigation Arrow should be disabled when user is on last movie card in the list"
#
#
# #@allure.title('TC_083: Verify Left Navigation Arrow is visible only when we hover on the first card on the left')
# def test_left_navigation_arrow_visible_recently_list(browser):
#     home = homepage(browser)
#     global test, my_comment
#     test = test_case_ids[82]  # 195
#     home_page = homePageObj(browser)
#     my_comment = "Left navigation arrow is not displaying after hover on first movie cards"
#     # time.sleep(2)
#     assert home_page.verify_leftarrow() == True, "Left navigation arrow is not displaying after hover on first movie " \
#                                                  "cards "
#     my_comment = "Left Navigation Arrow should only be enabled when user hovers on first movie card from left"
#
#
# #@allure.title('TC_084: Verify click behavior of Left Navigation arrow')
# def test_click_left_navigation_recently_list(browser):
#     home_page = homePageObj(browser)
#     global test, my_comment
#     test = test_case_ids[83]  # 196
#     my_comment = 'Left Navigation button is not Present / Left Navigation button is not clickable'
#     home_page.click_prevarrow()
#     my_comment = 'On click of Left Navigation Arrow, the movie slider should progress towards left'
#
#
# #@allure.title('TC_085: Verify Left Navigation Arrow is disabled when we are on the first card in the list')
# def test_leftnav_disabled(browser):
#     home = homepage(browser)
#     global test, my_comment
#     test = test_case_ids[84]  # 197
#     home_page = homePageObj(browser)
#     home.Refresh()
#     my_comment = 'Left nav is not disabled when it is on first movie cards.'
#     assert home_page.verify_left_disbaled() == False, "Left nav is not disabled when it is on first movie cards. "
#     my_comment = 'Left Navigation Arrow should be disabled when user is on first movie card in the list'
#
#
# #@allure.title('TC_086: Verify only 10 movie card is shown')
# def test_verify_recently_card_counts(browser):
#     home = homepage(browser)
#     home_page = homePageObj(browser)
#     global test, my_comment
#     test = test_case_ids[85]  # 198
#     # time.sleep(2)
#     my_comment = 'Cards are not present in Recently-Watch section / Card count is not 10'
#     recently_cards = home_page.verify_list_count()
#     assert (recently_cards > 1) & (recently_cards < 11), 'Cards are not present in Recently-Watch section'
#     my_comment = 'Only 10 movie card should be shown'
#
#
# #@allure.title('TC_088: Verify on click of Add to List button, Add List popup is opened')
# def test_click_add_to_list_carousel_movie(browser):
#     home = homepage(browser)
#     global test, my_comment
#     test = test_case_ids[87]  # 200
#     home.gotohomepage(_url_)
#     my_comment = 'Add to list button is not Clickable'
#     home.click_add_to_list_carousel()
#     my_comment = 'Clicking on Add to List button for any slider should open the Add to List popup'
#
#
# #@allure.title('TC_087: Add To List pop')
# def test_verify_add_to_list_elements_carousel(browser):
#     home = homepage(browser)
#     global test, my_comment
#     test = test_case_ids[86]  # 199
#     my_comment = 'input search field is not present'
#     search = home.AddToListSearchBox()
#     assert search == True, 'search box is not present'
#     my_comment = 'clear button is not present'
#     clear = home.AddToListClearButton()
#     assert clear == True, 'clear button is not present'
#     my_comment = 'created list option is not present'
#     created_list = home.AddToListCreatedList()
#     assert created_list == True, 'created list option is not present'
#     my_comment = 'toggle button is not present'
#     toggel = home.AddToListToggelButton()
#     assert toggel == True, 'toggle button is not present'
#     my_comment = 'create list option is not present'
#     list = home.AddToListCreateList()
#     assert list == True, 'create list option is not present'
#     name = home.AddToListListName()
#     my_comment = 'list add to list name  is not present'
#     assert name == True, 'list add to list name  is not present'
#     my_comment = 'create list button is not present'
#     button = home.AddToListCreateListButton()
#     assert button == True, 'create list button is not present'
#     my_comment = '''User should be create list by following the below steps:
# 1. Click on Add to List button for any slider
# 2. Click on List Name text field
# 3. Enter name
# 4. Click Create List
#
# Following should also happen along side:
# 1. New List should apppear in the List of Created List
# 2. Clicking Create List button should change the textbox to display "Creating..."
# 3. Success message should be shown in the same textbox "Created"
# 4. New List should get auto selected'''
#
#
# #@allure.title('TC_089: Verify user is able to enter name and create new list from Carousel')
# def test_create_new_list_from_carousel(browser):
#     home = homepage(browser)
#     global test, my_comment
#     test = test_case_ids[88]  # 201
#     my_comment = 'Name Input field is not present / Create list button is not clickable / list name is not Unique'
#     home.ListName("Demo")
#     home.ClickCreateList()
#     # time.sleep(2)
#     assert home.CreatedList() == True, "Success message for creating list is not showing."
#     # time.sleep(2)
#     list = home.NewList()
#     assert list == "Demo"
#     my_comment = '''User should be create list by following the below steps:
# 1. Click on Add to List button for any slider
# 2. Click on List Name text field
# 3. Enter name
# 4. Click Create List
# #
# # Following should also happen along side:
# # 1. New List should apppear in the List of Created List
# # 2. Clicking Create List button should change the textbox to display "Creating..."
# # 3. Success message should be shown in the same textbox "Created"
# # 4. New List should get auto selected'''
#
#
# #@allure.title('TC_090: Verify user is able to add the movie in the created list')
# def test_add_to_list_carousel(browser):
#     home = homepage(browser)
#     global test, my_comment
#     test = test_case_ids[89]  # 202
#     my_comment = 'User is not able to add movie in created list /' \
#                  ' Success message is not showing after adding title to list'
#     home.AddMovieToList()
#     # time.sleep(2)
#     assert home.verify_success_text() == True, "Success message is not showing after adding title to list"
#     my_comment = 'Once the list is created and is auto selected,then clicking on add to list button' \
#                  ' should add the movie to the new list'
#
#
# #@allure.title('TC_091: Verify user is able to select list(s)')
# def test_add_to_list_toggel_Button_carousel(browser):
#     home = homepage(browser)
#     global test, my_comment
#     test = test_case_ids[90]  # 203
#     home.Refresh()
#     my_comment = "Toggle button not selected"
#     home.click_add_to_list_carousel()
#     verify = home.VerifySelectList()
#     assert verify == True, "Toggle button not selected"
#     my_comment = 'Clicking on the toggle button should select the list Toggle button should get highlighted'
#
#
# #@allure.title('TC_092: Verify user is able to un-select any selected list(s)')
# def test_unselect_selected_list_carousel(browser):
#     home = homepage(browser)
#     global test, my_comment
#     test = test_case_ids[91]  # 204
#     my_comment = "Toggle button is selected and user can not able to unselect"
#     verify = home.VerifySelectList()
#     assert verify == False, "Toggle button not selected"
#     my_comment = 'Clicking on the toggle button against the selected list(s) should un-select the' \
#                  ' list(s) Toggle button should get highlighted'
#
#
# #@allure.title('TC_093: Verify user is able to add same movie in multiple lists')
# def test_add_same_movie_multiple_list_carousel(browser):
#     home = homepage(browser)
#     global test, my_comment
#     test = test_case_ids[92]  # 205
#     home.Refresh()
#     my_comment = 'add to list is not open / list name field is not present / list name is not unique'
#     home.click_add_to_list_carousel()
#     home.ListName("test")
#     home.ClickCreateList()
#     # time.sleep(1)
#     assert home.CreatedList() == True, "Success message for creating list is not showing."
#     home.AddMovieToList()
#     # time.sleep(2)
#     assert home.verify_success_text() == True, "Success message is not showing after adding title to list"
#     my_comment = 'User should be able to add same movie in multiple lists'
#
#
# #@allure.title('TC_094: Verify user is abel to search a list from the search bar')
# def test_search_list_carousel(browser):
#     home = homepage(browser)
#     global test, my_comment
#     test = test_case_ids[93]  # 206
#     home.Refresh()
#     my_comment = 'search field is not present / list name is not presnet'
#     home.click_add_to_list_carousel()
#     # time.sleep(1)
#     home.SearchList("test")
#     verify = home.VerifySearchedList_for_test()
#     assert verify == True, 'search field is not present / list name is not presnet'
#     my_comment = 'Enter search term in the search box should perform the search and show correct result'
#
#
# #@allure.title('TC_096: Verify user is able to select list(s) from search result')
# def test_select_searched_list_carousel(browser):
#     home = homepage(browser)
#     global test, my_comment
#     test = test_case_ids[95]  # 208
#     my_comment = 'User is not able to select list form search result'
#     select = home.MovieCardVerifySelectUnselectList()
#     assert select == True, 'User is not able to select list form search result'
#     my_comment = 'User should be able to select list(s) from search result'
#
#
# #@allure.title('TC_097: Verify user is able to un-select list(s) from search result')
# def test_unselect_searched_list_carousel(browser):
#     home = homepage(browser)
#     global test, my_comment
#     test = test_case_ids[96]  # 209
#     my_comment = 'user is not able to unselect list'
#     select = home.MovieCardVerifySelectUnselectList()
#     assert select == False, 'user is not able to unselect list'
#     my_comment = 'User should be able to un-select list(s) from search result'
#
#
# #@allure.title('TC_095: Verify user is able to clear search on click of Clear button')
# def test_clear_searched_list_carousel(browser):
#     home = homepage(browser)
#     global test, my_comment
#     test = test_case_ids[94]  # 207
#     my_comment = 'Clear button is not clickable / clear button is not working'
#     clear_button = home.ClickAddToListClearButton()
#     assert clear_button == True, 'Clear button is not clickable /clear button is not working'
#     my_comment = 'On click of Clear button search should be cleared'
#
#
# #@allure.title('TC_098: Verify user is able to create duplicate lists')
# def test_create_same_name_list(browser):
#     home = homepage(browser)
#     global test, my_comment
#     test = test_case_ids[97]  # 210
#     my_comment = 'User can create list with Duplicate name'
#     home.ListName("test")
#     home.ClickCreateListForDuplicate()
#     duplicate_list = home.verify_duplicate_list()
#     assert duplicate_list == True, 'User can create list with Duplicate name'
#     my_comment = 'User is not able to create duplicate lists a message is shown "Please enter a unique list name."'
#
#
# #@allure.title('TC_099: Verify on click outside the popup window then popup will hide')
# def test_click_outside_popup(browser):
#     home = homepage(browser)
#     global test, my_comment
#     test = test_case_ids[98]  # 211
#     my_comment = 'MGM ROAR logo is not clickable / popup is not getting hide'
#     verify_logo = home.headerRoarLogo()
#     assert verify_logo == True, 'MGM ROAR logo is not clickable / popup is not getting hide'
#     my_comment = 'Popup should hide if we click outside the popup window'
#
#
# #@allure.title('TC_100: Verify on click of Add to List button, Add List pop up is opened')
# def test_alive_movie_card_add_to_list(browser):
#     home = homepage(browser)
#     global test, my_comment
#     test = test_case_ids[99]  # 212
#     my_comment = 'Movie List Pop-up not found / add to list is not clickable'
#     list = home.ClickMovieCardAddToList()
#     assert list == True, "Movie List Pop-up not found"
#     my_comment = 'Popup should hide if we click outside the popup window'
#
#
# #@allure.title('TC_101: Verify user is able to enter name and create new list from movie card')
# def test_MovieCardCreateNewList_Alive_section(browser):
#     home = homepage(browser)
#     global test, my_comment
#     test = test_case_ids[100]  # 213
#     my_comment = 'Create list button is not present or not Clickable / List is not Auto Selected'
#     home.ListName("test1")
#     home.ClickCreateList()
#     created = home.CreatedList()
#     assert created == True
#     name = home.VerifyListCreated()
#     assert name == True
#     list = home.VerifyListAutoSelect()
#     assert list == True, 'List is not Auto Selected'
#     my_comment = '''User should be create list by following the below steps:
# 1. Click on Add to List button for any card
# 2. Click on List Name
# 3. Enter name
# 4. Click Create List
#
# Following should also happen along side:
# 1. New List should apppear in the List of Created List
# 2. Clicking Create List button should change the textbox to display "Creating..."
# 3. Success message should be shown in the same textbox "Created"
# 4. New List should get auto selected'''
#
#
# #@allure.title('TC_102: Verify user is able to add the movie in the created list')
# def test_MovieCardAddMovie_alive_section(browser):
#     home = homepage(browser)
#     global test, my_comment
#     test = test_case_ids[101]  # 214
#     # time.sleep(2)
#     my_comment = "Success message is not showing After Creating list"
#     home.AddMovieToList()
#     assert home.verify_success_text() == True, "Success message is not showing ."
#     my_comment = 'Once the list is created and is auto selected, then clicking on add to ' \
#                  'list button should add the movie to the new list'
#
#
# #@allure.title('TC_103: Verify user is able to select list(s)')
# def test_MovieCard_AddToListToggelButton_alive(browser):
#     home = homepage(browser)
#     global test, my_comment
#     test = test_case_ids[102]  # 215
#     my_comment = "Toggle button not selected"
#     home.ClickMovieCardAddToList()
#     verify = home.VerifyMovieCardSelectList()
#     assert verify == True, "Toggle button not selected"
#     my_comment = 'Clicking on the toggle button should select the listng' \
#                  ' Toggle button should get highlighted in color'
#
#
# #@allure.title('TC_104: Verify user is able to un-select any selected list(s)')
# def test_unselect_any_Selected_list_alive(browser):
#     home = homepage(browser)
#     global test, my_comment
#     test = test_case_ids[103]  # 216
#     my_comment = 'Toggle button not selected'
#     verify = home.VerifyMovieCardSelectList()
#     assert verify == False, "Toggle button not selected"
#     my_comment = 'Clicking on the toggle button against the selected list(s) should un-select the list(s) ' \
#                  'Toggle button should get highlighted in color'
#
#
# #@allure.title('TC_105: Verify user is able to add same movie in multiple lists')
# def test_MovieCardSecondAddedMovie_alive_section(browser):
#     home = homepage(browser)
#     global test, my_comment
#     test = test_case_ids[104]  # 217
#     my_comment = 'Movie List Pop-up not / add to list button is not clickable '
#     list = home.ClickMovieCardAddToList()
#     assert list == True, "Movie List Pop-up not found"
#     home.ListName("test2")
#     my_comment = 'Create List button is not clickable'
#     home.ClickCreateList()
#     my_comment = 'list is not created / list Name is not unique'
#     created = home.CreatedList()
#     assert created == True, 'list is not created / list Name is not unique'
#     home.AddMovieToList()
#     my_comment = 'Success message is not showing after adding title into list'
#     assert home.verify_success_text() == True, "Success message is not showing after adding title into list"
#     my_comment = 'User should be able to add same movie in multiple lists'
#
#
# #@allure.title('TC_106: Verify user is abel to search a list from the search bar')
# def test_MovieCardSearchList_alive(browser):
#     home = homepage(browser)
#     global test, my_comment
#     test = test_case_ids[105]  # 218
#     my_comment = 'search bar is not working / List Name is not present'
#     home.ClickMovieCardAddToList()
#     # time.sleep(1)
#     home.SearchList("test")
#     verify = home.VerifySearchedList_for_test()
#     assert verify == True, 'search bar is not working / List Name is not present '
#     my_comment = 'Enter search term in the search box should perform the search and show correct result'
#
#
# #@allure.title('TC_108: Verify user is able to select list(s) from search result')
# def test_MovieCardSelectSearchedList_alive(browser):
#     home = homepage(browser)
#     global test, my_comment
#     test = test_case_ids[107]  # 220
#     my_comment = 'user is not able to select list/ toggle button is not clickable'
#     select = home.MovieCardVerifySelectUnselectList()
#     assert select == True, 'user is not able to select list/ toggle button is not clickable'
#     my_comment = 'User should be able to select list(s) from search result'
#
#
# #@allure.title('TC_109: Verify user is able to un-select list(s) from search result')
# def test_MovieCardUnselectSearchedList_alive(browser):
#     home = homepage(browser)
#     global test, my_comment
#     test = test_case_ids[108]  # 221
#     my_comment = 'user is not able to unselect any selected list / toggle button is not clickable'
#     select = home.MovieCardVerifySelectUnselectList()
#     assert select == False, 'user is not able to unselect any selected list / toggle button is not clickable'
#     my_comment = 'User should be able to un-select list(s) from search result'
#
#
# #@allure.title('TC_107: Verify user is able to clear search on click of Clear button')
# def test_MovieCardClearSearchedList_alive(browser):
#     home = homepage(browser)
#     global test, my_comment
#     test = test_case_ids[106]  # 219
#     my_comment = 'Clear button is not Present / clear button is not working'
#     clear_button = home.ClickAddToListClearButton()
#     assert clear_button == True, 'Clear button is not Present / clear button is not working'
#     my_comment = 'On click of Clear button search should be cleared'
#
#
# #@allure.title('TC_110: Verify user is able to add to multiple movies in same list')
# def test_MovieCardMultipleMovieToSameList_alive(browser):
#     home = homepage(browser)
#     global test, my_comment
#     test = test_case_ids[109]  # 222
#     home.gotohomepage(_url_)
#     my_comment = 'Add to list button is not clickable / Add to list popup not fount'
#     home.ClickMovieCardAddToListSecondMovie()
#     home.SearchList("test1")
#     # time.sleep(2)
#     my_comment = 'Toggle button is not present'
#     home.ClickToggleButtonTest1()
#     home.AddMovieToList()
#     my_comment = 'Add Movie button is not clickable / user can not add Multiple Movies in same list '
#     button = home.AddToListAddedButton()
#     assert button == True, 'user can not add Multiple Movies in same list'
#     my_comment = 'User should be able to add multiple movies in same list by clicking Add To List  ' \
#                  'and following add to list steps on any movies'
#
#
# #@allure.title('TC_111: Verify user is able to create duplicate lists')
# def test_movie_card_same_name_list_alive(browser):
#     home = homepage(browser)
#     global test, my_comment
#     test = test_case_ids[110]  # 223
#     home.gotohomepage(_url_) # added after getting issues test1 is coming
#     my_comment = 'Add to list button is not found on movie Card'
#     home.ClickMovieCardAddToListSecondMovie()
#     time.sleep(2.5) # it s failing multiple times so need to validate with
#     home.ListName("test")
#     time.sleep(2.5)
#     my_comment = 'User can create list with Duplicate name / Create list button is not found'
#     home.ClickCreateListForDuplicate()
#     duplicate_list = home.verify_duplicate_list()
#     assert duplicate_list == True, 'User can create list with Duplicate name'
#     my_comment = 'User is not able to create duplicate lists a message is shown "Please enter a unique list name."'
#
#
# #@allure.title('TC_112: Verify on click outside the popup window then popup will hide')
# def test_movie_card_click_outside_popup(browser):
#     home = homepage(browser)
#     global test, my_comment
#     test = test_case_ids[111]  # 224
#     my_comment = 'MGM ROAR logo is not clickable when Add to list popup opened'
#     verify_logo = home.headerRoarLogo()
#     assert verify_logo == True, 'MGM ROAR logo is not clickable'
#     my_comment = 'Popup should hide if we click outside the popup window'
#
#
# #@allure.title('TC_113: Verify on click of Add to List button, Add List pop up is opened')
# def test_recently_Addtolist_popup(browser):
#     home = homepage(browser)
#     global test, my_comment
#     test = test_case_ids[112]  # 225
#     home.gotohomepage(_url_)
#     my_comment = 'CREATE A NEW LIST", "After clicking on add to list button on Movie cards Pop is not opening.'
#     add = recaddListObj(browser)
#     assert add.verify_addToList() == True, "After clicking on add to " \
#                                                           "list button on Movie cards Pop is not opening. "
#     my_comment = 'Clicking on Add to List button for any slider should open the Add to List pop up'
#
#
# #@allure.title('TC_114: Verify user is able to enter name and create new list from Recently Movie Card')
# def test_RecentlyCardCreateNewList(browser):
#     home = homepage(browser)
#     global test, my_comment
#     test = test_case_ids[113]  # 226
#     my_comment = 'list name input filed not found / User can not type list name '
#     time.sleep(3.5)
#     home.ListName("recentlyList")
#     time.sleep(4)
#     my_comment = 'Create list button is not present / Create button is  not clickable'
#     home.ClickCreateList()
#     created = home.CreatedList()
#     assert created == True
#     name = home.VerifyListRecentlyCreated()
#     assert name == True, 'After creating recentlyList is not showing in List popup '
#     list = home.VerifyListRecentlyAutoSelect()
#     assert list == True, 'New Created list is not Auto Selected'
#     my_comment = '''User should be create list by following the below steps:
# 1. Click on Add to List button for any slider
# 2. Click on List Name
# 3. Enter name
# 4. Click Create List
#
# Following should also happen along side:
# 1. New List should apppear in the List of Created List
# 2. Clicking Create List button should change the textbox to display "Creating..."
# 3. Success message should be shown in the same textbox "Created"
# 4. New List should get auto selected'''
#
#
# #@allure.title('TC_115: Verify user is able to add the movie in the created list')
# def test_RecentlyCardAddMovie(browser):
#     home = homepage(browser)
#     global test, my_comment
#     test = test_case_ids[114]  # 227
#     # time.sleep(2)
#     my_comment = 'After Adding Movie in list Success message is not showing .'
#     home.AddMovieToList()
#     assert home.verify_success_text() == True, "After Adding Movie in list Success message is not showing ."
#     my_comment = 'Once the list is created and is auto selected, then clicking on ' \
#                  'add to list button should add the movie to the new list'
#
#
# #@allure.title('TC_116: Verify user is able to select list(s)')
# def test_RecentlyCard_AddToListToggelButton(browser):
#     home = homepage(browser)
#     global test, my_comment
#     test = test_case_ids[115]  # 228
#     add = recaddListObj(browser)
#     my_comment = "CREATE A NEW LIST", "After clicking on add to list button on Movie cards Pop is not opening. "
#     assert add.verify_addToList() == True, "After clicking on add to list button on Movie cards Pop is " \
#                                                           "not opening. "
#     my_comment = "Toggle button not selected in list popup"
#     verify = home.VerifyRecentlySelectList()
#     assert verify == True, "Toggle button not selected in lis popup"
#     my_comment = 'Clicking on the toggle button should select the list Toggle button get selected'
#
#
# #@allure.title('TC_117: Verify user is able to un-select any selected list(s)')
# def test_Recently_UnselectSelectedList(browser):
#     home = homepage(browser)
#     global test, my_comment
#     test = test_case_ids[116]  # 229
#     my_comment = 'User Can not unselect the Selected List'
#     verify = home.VerifyRecentlySelectList()
#     assert verify == False, "User Can not unselect the Selected List"
#     my_comment = 'Clicking on the toggle button against the selected list(s) should un-select the list(s)'
#
#
# #@allure.title('TC_118: Verify user is able to add same movie in multiple lists')
# def test_Recently_MovieCardSecondAddedMovie(browser):
#     home = homepage(browser)
#     global test, my_comment
#     test = test_case_ids[117]  # 230
#     add = recaddListObj(browser)
#     my_comment = "CREATE A NEW LIST", "After clicking on add to list button on Movie cards Pop is " \
#                                       "not opening. "
#     assert add.verify_addToList() == True, "After clicking on add to list button on Movie cards Pop is " \
#                                                           "not opening. "
#     home.ListName("recentlyList2")
#     home.ClickCreateList()
#     created = home.CreatedList()
#     assert created == True
#     home.AddMovieToList()
#     my_comment = '"Success message is not showing after adding title into list"'
#     assert home.verify_success_text() == True, "Success message is not showing after adding title into list"
#     my_comment = "User should be able to add same movie in multiple lists"
#
#
# #@allure.title('TC_119: Verify user is abel to search a list from the search bar')
# def test_RecentlyMovieCardSearchList(browser):
#     home = homepage(browser)
#     global test, my_comment
#     test = test_case_ids[118]  # 231
#     my_comment = 'Search input field is not present in list popup / Add to list popup not found'
#     home.ClickMovieCardAddToList()
#     # time.sleep(1)
#     home.SearchList("test")
#     my_comment = 'list name not found '
#     verify = home.VerifySearchedList_for_test()
#     assert verify == True
#     my_comment = 'Enter search term in the search box should perform the search and show correct result'
#
#
# #@allure.title('TC_121: Verify user is able to select list(s) from search result')
# def test_RecentlyMovieCardSelectSearchedList(browser):
#     home = homepage(browser)
#     global test, my_comment
#     test = test_case_ids[120]  # 233
#     my_comment = 'Toggle button not found / Toggle button is not clickable'
#     select = home.MovieCardVerifySelectUnselectList()
#     assert select == True
#     my_comment = 'User should be able to select list(s) from search result'
#
#
# #@allure.title('TC_122: Verify user is able to un-select list(s) from search result')
# def test_RecentlyMovieCardUnselectSearchedList(browser):
#     home = homepage(browser)
#     global test, my_comment
#     test = test_case_ids[121]  # 234
#     my_comment = 'Toggle button not found / Toggle button is not clickable'
#     select = home.MovieCardVerifySelectUnselectList()
#     assert select == False
#     my_comment = 'User should be able to un-select list(s) from search result'
#
#
# #@allure.title('TC_120: Verify user is able to clear search on click of Clear button')
# def test_RecentlyMovieCardClearSearchedList(browser):
#     home = homepage(browser)
#     global test, my_comment
#     test = test_case_ids[119]  # 232
#     my_comment = 'Clear button is not found / Clear button is not Clickable / Clear button is ' \
#                  'not Cleaning the input Field'
#     clear_button = home.ClickAddToListClearButton()
#     assert clear_button == True, 'clear button is not working'
#     my_comment = 'On click of Clear button search should be cleared'
#
#
# #@allure.title('TC_123: Verify user is able to add to multiple movies in same list')
# def test_RecentlyMovieCardMultipleMovieToSameList(browser):
#     home = homepage(browser)
#     global test, my_comment
#     test = test_case_ids[122]  # 235
#     add = recaddListObj(browser)
#     home.gotohomepage(_url_)
#     my_comment = '"CREATE A NEW LIST", "After clicking on add to list button on Movie " \
#                                                                       "cards Pop is not opening. "'
#     assert add.verify_addToList_SecondMovie() == True, "After clicking on add to list button on Movie " \
#                                                                       "cards Pop is not opening. "
#     home.SearchList("recentlyList")
#     # time.sleep(2)
#     home.ClickToggleButtonRecentlyList()
#     home.AddMovieToList()
#     button = home.AddToListAddedButton()
#     assert button == True
#     my_comment = 'On click of Clear button search should be cleared'
#
#
# #@allure.title('TC_124: Verify user is able to create duplicate lists')
# def test_recently_movie_card_same_name_list(browser):
#     home = homepage(browser)
#     add = recaddListObj(browser)
#     global test, my_comment
#     test = test_case_ids[123]  # 236
#     my_comment = '"CREATE A NEW LIST", "After clicking on add to list button on Movie " \
#                                                                       "cards Pop is not opening. "'
#     home.gotohomepage(_url_)
#     assert add.verify_addToList_SecondMovie() == True, "After clicking on add to list button on Movie " \
#                                                                       "cards Pop is not opening. "
#     home.ListName("test")
#     home.ClickCreateListForDuplicate()
#     my_comment = 'User can create list with Duplicate name'
#     duplicate_list = home.verify_duplicate_list()
#     assert duplicate_list == True, 'User can create list with Duplicate name'
#     my_comment = 'User is not able to create duplicate lists a message is shown "Please enter a unique list name."'
#
#
# #@allure.title('TC_125: Verify on click outside the popup window then popup will hide')
# def test_recently_movie_card_click_outside_popup(browser):
#     home = homepage(browser)
#     global test, my_comment
#     test = test_case_ids[124]  # 237
#     my_comment = 'MGM ROAR logo not found  / List popup is not hiding'
#     verify_logo = home.headerRoarLogo()
#     assert verify_logo == True, 'MGM ROAR logo is not clickable'
#     my_comment = 'Popup should hide if we click outside the popup window'
#
#
# #@allure.title('TC_126: Verify global footer is present')
# def test_global_footer(browser):
#     home = homepage(browser)
#     global test, my_comment
#     test = test_case_ids[125]  # 238
#     home_page = homePageObj(browser)
#     home.gotohomepage(_url_)
#     my_comment = " Footer not found / Footer Elements are not present"
#     assert home_page.verify_Privacypolicy() == True, "Privacy policy is not displaying in global footer. It should be " \
#                                                      "displayed in footer. "
#     my_comment = "Terms and Use is not displaying in global footer. It should be displayed in footer. "
#     assert home_page.verify_termsUse() == True, "Terms and Use is not displaying in global footer. It should be " \
#                                                 "displayed in footer. "
#     assert home_page.verify_footerLogo() == True, "MGM logo  is not displaying in global footer. It should be " \
#                                                   "displayed in footer. "
#     my_comment = "Support link is not displaying in global footer. It should be " \
#                  "displayed in footer. "
#     assert home_page.verify_supportLink() == True, "Support link is not displaying in global footer. It should be " \
#                                                    "displayed in footer. "
#     my_comment = "Address text is not displaying in global footer. It should be " \
#                  "displayed in footer. "
#     assert home_page.verify_address() == True, "Address text is not displaying in global footer. It should be " \
#                                                "displayed in footer. "
#     my_comment = "Legal text is not displaying in global footer. It should be " \
#                  "displayed in footer. "
#     assert home_page.verify_legal() == True, "Legal text is not displaying in global footer. It should be " \
#                                              "displayed in footer. "
#     my_comment = "Contact-us is not displaying in global footer. It should be " \
#                  "displayed in footer. "
#     assert home_page.verify_contact_us() == True, "Contact-us is not displaying in global footer. It should be " \
#                                                   "displayed in footer. "
#     my_comment = "Youtube icon is not displaying in global footer. It should be " \
#                  "displayed in footer. "
#     assert home_page.verify_youtubeIcon() == True, "Youtube icon is not displaying in global footer. It should be " \
#                                                    "displayed in footer. "
#     my_comment = "Facebook icon is not displaying in global footer. It should be " \
#                  "displayed in footer. "
#     assert home_page.verify_fbIcon() == True, "Facebook icon is not displaying in global footer. It should be " \
#                                               "displayed in footer. "
#     assert home_page.verify_twitterIcon() == True, "Twitter icon is not displaying in global footer. It should be " \
#                                                    "displayed in footer. "
#     my_comment = "Instagram icon is not displaying in global footer. It should be " \
#                  "displayed in footer. "
#     assert home_page.verify_instaIcon() == True, "Instagram icon is not displaying in global footer. It should be " \
#                                                  "displayed in footer. "
#     my_comment = "Copyright is not displaying in global footer. It should be " \
#                  "displayed in footer. "
#     assert home_page.verify_copyright() == True, "Copyright is not displaying in global footer. It should be " \
#                                                  "displayed in footer. "
#     my_comment = "Connect is not displaying in global footer. It should be " \
#                  "displayed in footer. "
#     assert home_page.verify_connect() == True, "Connect is not displaying in global footer. It should be " \
#                                                "displayed in footer. "
#     my_comment = """Global Footer should consist of following elements:
# 1. Roar Logo
# 2. Legal [Privacy Policy & Terms of Use]
# 3. Contact Us [Support (mailto link) and Address]
# 4. Connect [Facebook,Youtube,Instagram,Twitter]
# 5. Copyright"""
#
#
# #@allure.title('127: Verify functionality of roar logo is clickable ')
# def test_click_footer_roarLogo(browser):
#     home = homepage(browser)
#     global test, my_comment
#     test = test_case_ids[126]  # 239
#     my_comment = 'Film and Series button is not Clickable / Film and Series page not opened'
#     movies = home.ClickFilmsSeries()
#     assert movies == True, "Not redirecting to correct page"
#     my_comment = "Footer Section roar logo is not clickable"
#     roar_logo = home.ClickFooterRoarLogo()
#     assert roar_logo == True, 'roar logo is not clickable'
#     my_comment = 'User should be able to click on roar logo and after clicked page should be redirected to Homepage'
#
#
# #@allure.title('TC_128: Verify Legal [Privacy Policy] is clickable')
# def test_click_footer_privacyPolicy(browser):
#     home = homepage(browser)
#     global test, my_comment
#     test = test_case_ids[127]  # 240
#     home_page = homePageObj(browser)
#     home.gotohomepage(_url_)
#     my_comment = 'Privacy-Policy page is not open / Privacy Policy button is not Clickable'
#     privacy_policy = home_page.privacyPolicy_click()
#     assert 'privacy' in privacy_policy, 'Privacy-Policy page is not open'
#     my_comment = 'user should able to click Legal [Privacy Policy] and after ' \
#                  'click it redirected to https://mgm.com/privacy-policy'
#
#
# #@allure.title('TC_129: Verify Legal [Terms of Use] is clickable')
# def test_click_footer_termsOfUse(browser):
#     home = homepage(browser)
#     home_page = homePageObj(browser)
#     global test, my_comment
#     test = test_case_ids[128]  # 241
#     my_comment = 'Terms-of-use page is not open / Terms of use button is not Clickable'
#     home.gotohomepage(_url_)
#     terms_of_use = home_page.termsOfUse_Click()
#     assert 'terms' in terms_of_use, 'Terms-of-use is not open'
#     my_comment = 'user should able to click Legal [Terms of Use] and after click' \
#                  ' it redirected to https://mgm.com/terms-of-use'
#
#
# #@allure.title('TC_131: verify functionality of [Facebook,Youtube,Instagram,Twitter]')
# def test_click_all_socialMedia_icon_footer(browser):
#     home = homepage(browser)
#     home_page = homePageObj(browser)
#     global test, my_comment
#     test = test_case_ids[130]  # 243
#     my_comment = 'Youtube link broken or change'
#     home.gotohomepage(_url_)
#     youtube_text = home_page.click_youtubeIcon()
#     assert youtube_text == 'MGM', "Youtube link broken or changed"
#     my_comment = 'Facebook link broken or changed'
#     roar_txt = home_page.click_facebookIcon()
#     assert 'ROAR' in roar_txt, 'Facebook link is broken or changed'
#     my_comment = 'Twitter link broken or changed'
#     twitter_text = home_page.click_twitterIcon()
#     assert twitter_text == 'MGM Studios', 'Twitter link broken or changed'
#     my_comment = 'Instagram link broken or changed'
#     roar_title = home_page.click_instagramIcon()
#     assert 'ROAR' in roar_title, 'Instagram link broken or changed'
#     my_comment = 'user should be able to click on [Facebook,Youtube,Instagram,Twitter] ' \
#                  'and after click page should redirected to particular social media page'
#
#
# #@allure.title('TC_064, Verify created lists are shown in the My Lists slider')
# def test_verify_created_list_my_list_section(browser):
#     global test, my_comment
#     test = test_case_ids[63]  # 176
#     home = homepage(browser)
#     elements = homePagemylistsObj(browser)
#     # time.sleep(2)
#     my_comment = "created lists are not shown in the My List section "
#     assert elements.verify_Mylists_title() == True, "Title is not showing in my Lists section. It should show on " \
#                                                     "movie cards "
#     assert elements.verify_my_recently_added_card() == True, 'Newly created lists are not present in my list section'
#     total_cards = elements.verify_my_list_total_cards()
#     assert total_cards <= 10, 'My List slider have more than 10 lists'
#
#     my_comment = '''Created lists should be available in My List slider
# My List slider should show only 10 lists'''
#
#
# #@allure.title('TC_066, Verify user is able to see User Created List in My List section of homepage ')
# def test_verify_created_list_my_list_section_home_page(browser):
#     global test, my_comment
#     test = test_case_ids[65]  # 178
#     elements = homePagemylistsObj(browser)
#     # time.sleep(2)
#     my_comment = "created lists are not shown in the My List section "
#     assert elements.verify_Mylists_title() == True, "Title is not showing in my Lists section. It should show on " \
#                                                     "movie cards "
#     my_comment = "List name are not present in the My List section"
#     assert elements.verify_mylist_list_name() == True, 'List name are not present  in my list Section'
#     my_comment = 'List Title are not present  in my list Section'
#     assert elements.verify_mylist_title() == True, 'List Title are not present  in my list Section'
#     my_comment = '''Created list card should have the following:
# 1. List name
# 2. Number of titles'''
#
#
# #@allure.title('TC_132: Verify global header is present')
# def test_ElementsGlobalHeader_my_list(browser):
#     home = homepage(browser)
#     global test, my_comment
#     test = test_case_ids[131]  # 945
#     my_comment = 'My list page not opened'
#     list_page = home.ClickMyListHeader()
#     assert list_page == True, "Not redirecting to correct page"
#     my_comment = '"Header logo not found"'
#     logo = home.HomePageLogo()
#     assert logo == True, "Header logo not found"
#     films_series = home.HeaderFilmsAndSeries()
#     assert films_series == True, "Header 'Films & Series' link not found"
#     mylist = home.HeaderMylist()
#     assert mylist == True, "My list link not found"
#     my_comment = 'Logout button not found"'
#     logout = home.HeaderLogoutButton()
#     assert logout == True, "Logout button not found"
#     my_comment = 'Marketing rules button not found'
#     marketing_rules = home.HeaderMarketingRules()
#     assert marketing_rules == True, "Marketing rules button not found"
#     my_comment = 'Assets Button not found"'
#     assets = home.HeaderAssets()
#     assert assets == True, "Assets Button not found"
#     my_comment = "My Carts button not found"
#     mycart = home.HeaderMyCarts()
#     assert mycart == True, "My Carts button not found"
#     my_comment = '''Global Header should consist of following elements:
# 1. Roar Logo
# 2. Menu Links [FILMS & SERIES , MY LISTS , ASSETS , MY CARTS , MARKETING RULES]
# 3.Search bar
# 4. Logout [Button]'''
#
#
#
#
# #@allure.title('TC_133: Verify global footer is present')
# def test_global_footer_mylist(browser):
#     home_page = homePageObj(browser)
#     home = homepage(browser)
#     global test, my_comment
#     test = test_case_ids[132]  # 946
#     my_comment = "Privacy policy is not displaying in global footer. It should be " \
#                  "displayed in footer. "
#     assert home_page.verify_Privacypolicy() == True, "Privacy policy is not displaying in global footer. It should be " \
#                                                      "displayed in footer. "
#     my_comment = "Terms and Use is not displaying in global footer. It should be " \
#                  "displayed in footer. "
#     assert home_page.verify_termsUse() == True, "Terms and Use is not displaying in global footer. It should be " \
#                                                 "displayed in footer. "
#     my_comment = "MGM logo  is not displaying in global footer. It should be " \
#                  "displayed in footer. "
#     assert home_page.verify_footerLogo() == True, "MGM logo  is not displaying in global footer. It should be " \
#                                                   "displayed in footer. "
#     my_comment = "MGM logo  is not displaying in global footer. It should be " \
#                  "displayed in footer. "
#     assert home_page.verify_supportLink() == True, "MGM logo  is not displaying in global footer. It should be " \
#                                                    "displayed in footer. "
#     my_comment = "Address text is not displaying in global footer. It should be " \
#                  "displayed in footer. "
#     assert home_page.verify_address() == True, "Address text is not displaying in global footer. It should be " \
#                                                "displayed in footer. "
#     my_comment = "Legal text is not displaying in global footer. It should be " \
#                  "displayed in footer. "
#     assert home_page.verify_legal() == True, "Legal text is not displaying in global footer. It should be " \
#                                              "displayed in footer. "
#     my_comment = "Contact-us is not displaying in global footer. It should be " \
#                  "displayed in footer. "
#     assert home_page.verify_contact_us() == True, "Contact-us is not displaying in global footer. It should be " \
#                                                   "displayed in footer. "
#     my_comment = "Youtube icon is not displaying in global footer. It should be " \
#                  "displayed in footer. "
#     assert home_page.verify_youtubeIcon() == True, "Youtube icon is not displaying in global footer. It should be " \
#                                                    "displayed in footer. "
#     my_comment = "Facebook icon is not displaying in global footer. It should be " \
#                  "displayed in footer. "
#     assert home_page.verify_fbIcon() == True, "Facebook icon is not displaying in global footer. It should be " \
#                                               "displayed in footer. "
#     my_comment = "Twitter icon is not displaying in global footer. It should be " \
#                  "displayed in footer. "
#     assert home_page.verify_twitterIcon() == True, "Twitter icon is not displaying in global footer. It should be " \
#                                                    "displayed in footer. "
#     my_comment = "Twitter icon is not displaying in global footer. It should be " \
#                  "displayed in footer. "
#     assert home_page.verify_instaIcon() == True, "Instagram icon is not displaying in global footer. It should be " \
#                                                  "displayed in footer. "
#     my_comment = "Instagram icon is not displaying in global footer. It should be " \
#                  "displayed in footer. "
#     assert home_page.verify_copyright() == True, "Copyright is not displaying in global footer. It should be " \
#                                                  "displayed in footer. "
#     my_comment = "Copyright is not displaying in global footer. It should be " \
#                  "displayed in footer. "
#     assert home_page.verify_connect() == True, "Connect is not displaying in global footer. It should be " \
#                                                "displayed in footer. "
#     my_comment = '''Global Footer should consist of following elements:
# 1. Roar Logo
# 2. Legal [Privacy Policy & Terms of Use]
# 3. Contact Us [Support (mailto link) and Address]
# 4. Connect [Facebook,Youtube,Instagram,Twitter]
# 5. Copyright'''
#
#
# #@allure.title('TC_134: Verify My List is underlined in Menu')
# def test_verify_my_list_underline(browser):
#     home = homepage(browser)
#     my_list = myListObj(browser)
#     global test, my_comment
#     test = test_case_ids[133]  # 947
#     my_comment = 'My list Under line is not present'
#     my_list_active = my_list.verify_myList_Active()
#     assert 'active' in my_list_active, 'underline is not present'
#     my_comment = 'My List should be underlined in Menu when user is on My List page'
#
#
# #@allure.title('TC_151: Verify elements in User Created Lists section')
# def test_user_elements_yourList(browser):
#     home = homepage(browser)
#     elements = homePagemylistsObj(browser)
#     global test, my_comment
#     test = test_case_ids[150]  # 964
#     my_comment = '"Your Lists", "Title name Your lists is not showing up in lists . Title " \
#                                                          "should show Your Lists. "'
#     assert elements.verify_listsTitle() == "Your Lists", "Title name Your lists is not showing up in lists . Title " \
#                                                          "should show Your Lists. "
#     my_comment = 'Demo', "User created list with name Automation List is " \
#                          "not there in table. List should show in table. "
#     assert elements.verify_userCreated_list() == 'Demo', "User created list with name Automation List is " \
#                                                          "not there in table. List should show in table. "
#     my_comment = '''User Created List section should have the following:
# 1. Title
# 2. User Created List Table'''
#
#
# #@allure.title('TC_152: Verify columns/elements of List table')
# def test_listPage_elements(browser):
#     home = homepage(browser)
#     list = homePagemylistsObj(browser)
#     global test, my_comment
#     test = test_case_ids[151]  # 965
#     my_comment = "Automation List title is not showing in heading . It should show. "
#     home.gotohomepage(_url_)
#     list_page = home.ClickMyListHeader()
#     assert list_page == True, "Not redirecting to correct page"
#     assert list.verify_userCreated_list() == 'Demo', "Automation List title is not showing in heading . It " \
#                                                      "should show. "
#     assert list.verify_shareButton() == True, "Share button should be displayed in User created list page"
#     assert list.verify_yourlist_title() == True, "Title count is not present"
#     assert list.verify_deleteButton() == True, "Delete button should be displayed in user created List page. "
#     # assert list.verify_checkBox() == True, "Check box should be displayed in list page table"
#     # time.sleep(2)
#     my_comment = '''Table should have following Columns/Elements:
# 1. Checkbox
# 2. Name of List
# 3. Delete [button]
# 4. Total Title counts
# 5. Email Spreadsheet [Button]'''
#
#
# #@allure.title('TC_153: Verify user is able to select the list by clicking on the checkbox')
# def test_clickingCheckbox(browser):
#     check = homePagemylistsObj(browser)
#     global test, my_comment
#     test = test_case_ids[152]  # 966
#     my_comment = 'Check box is not selected after clicking on it. '
#     check.click_list_checkBox()
#     # time.sleep(2)
#     assert check.verify_checkselected() == True, "Check box is not selected after clicking on it. "
#     time.sleep(2)
#     my_comment = 'Clicking the checkbox should select that list'
#
#
# #@allure.title('TC_154: Verify user is able to select multiple list by clicking on the checkbox')
# def test_clickMultiple_chekbox(browser):
#     multi = homePagemylistsObj(browser)
#     global test, my_comment
#     test = test_case_ids[153]  # 967
#     my_comment = "First Check box is not selected after clicking on it. Multiple " \
#                  "checkbox should get selected. "
#     multi.Refresh()
#     multi.click_Demo_checkBox()
#     assert multi.verify_checkselected() == True, "First Check box is not selected after clicking on it. Multiple " \
#                                                  "checkbox should get selected. "
#     multi.click_test_checkBox()
#     my_comment = "List selected Text is not displaying in footer pop . " \
#                  "It should show. "
#     assert "Items Selected" in multi.verify_List_text_multi(), "List selected Text is not displaying in footer pop . " \
#                                                                "It should show. "
#     my_comment = 'User should be able to select multiple lists'
#
#
# #@allure.title('TC_155: Verify click on checkbox opens the footer pop up')
# def test_checkbox_footer_popup(browser):
#     multi = homePagemylistsObj(browser)
#     footer = homePagemylistsObj(browser)
#     global test, my_comment
#     test = test_case_ids[154]  # 968
#     my_comment = "List selected Text is not displaying in footer pop . It should show. "
#     multi.click_test_checkBox()
#     assert "Item Selected" in footer.verify_Listtext(), "List selected Text is not displaying in footer pop . It " \
#                                                         "should show. "
#     my_comment = '"Download csv is not present there. Download csv button should be displayed in footer popup. "'
#     assert footer.verify_downloadCsv() == True, "Download csv is not present there. Download csv button should be " \
#                                                 "displayed in footer popup. "
#     my_comment = "Share List is not present there. Share list button should be displayed in footer popup. "
#     assert footer.verify_shareList() == True, "Share List is not present there. Share list button should be displayed " \
#                                               "in footer popup. "
#     my_comment = 'Delete button is not present there. Delete button button should be displayed in footer popup. '
#     assert footer.verify_DeleteFooterpopup() == True, "Delete button is not present there. Delete button button " \
#                                                       "should be displayed in footer popup. "
#     my_comment = '''On click of checkbox footer pop up should open
# Footer pop should have the following:
# 1.Download .XLSX [Button]
# 2. Generate Pdf [Button]
# 3. Email Spreadsheet [Button]
# 4. Delete [Button]'''
#
#
# #@allure.title('TC_156: Verify on click on List name user is redirected to List Detail page')
# def test_list_redirected_detailed(browser):
#     list = homePagemylistsObj(browser)
#     global test, my_comment
#     test = test_case_ids[155]  # 969
#     my_comment = 'In Movie detail Page List name is not showing in heading . Detailed page is not opened'
#     list.Refresh()
#     list.click_Createdlist()
#     # time.sleep(2)
#     assert list.verify_detailedPage() == True, "In detail Page List name is not showing in heading . Detailed page is " \
#                                                "not opened "
#     my_comment = 'On click on List Name user should be redirected to List Detail page of that List'
#
#
# #@allure.title('TC_159: Verify clicking on Delete button, Delete pop up is shown')
# def test_deletePopup(browser):
#     my_list = homePagemylistsObj(browser)
#     list = myListObj(browser)
#     home = homepage(browser)
#     global test, my_comment
#     test = test_case_ids[158]  # 972
#     my_comment = '"Delete icon is not displaying. Delete icon should be displayed in delete popup'
#     home.gotohomepage(_url_)
#     list_page = home.ClickMyListHeader()
#     assert list_page == True, "Not redirecting to correct page"
#     my_list.click_delete_my_list()
#     # time.sleep(2)
#     assert list.verify_delete_close() == True, "Delete icon is not displaying. Delete icon should be displayed in " \
#                                                "delete popup. "
#     my_comment = "Static Text i.e YOU ARE ABOUT TO DELETE  1 LIST button is not " \
#                  "present in popup. static text should be there "
#     assert list.verify_deleteToptext() == True, "Static Text i.e YOU ARE ABOUT TO DELETE  1 LIST button is not " \
#                                                 "present in popup. static text should be there "
#     my_comment = "List title and number of list is not present in popup. list title & list numbers should be there "
#     assert list.verify_deleteTitle() == True, "List title and number of list is not present in popup. list title & " \
#                                               "list numbers should be there "
#     my_comment = '"Delete button is not showing up there. Delete button should be " \
#                                                "displayed in delete popup. "'
#     assert list.verify_deleteBtnPop() == True, "Delete button is not showing up there. Delete button should be " \
#                                                "displayed in delete popup. "
#     my_comment = "Cancel button is not showing up there. Cancel button should be " \
#                  "displayed. "
#     assert list.verify_cancel_button() == True, "Cancel button is not showing up there. Cancel button should be " \
#                                                 "displayed. "
#     my_comment = '''On click of Delete button, delete pop up should be shown
# Delete pop up should have the following element:
# 1. Close button
# 2. Static text
# 3. List Name & number of titles in it
# 5. Delete List [button]
# 6. Cancel [button]'''
#
#
# #@allure.title('TC_160: Verify on click of Cancel button delete pop up gets closed')
# def test_click_on_cancel_delete_button(browser):
#     cancel = myListObj(browser)
#     list = homePagemylistsObj(browser)
#     global test, my_comment
#     test = test_case_ids[159]  # 973
#     my_comment = "Your Lists", "On clicking Cancel button ,cancel popup is not getting closed. It should close and " \
#                                "should come to Your lists page "
#     cancel.click_cancelButton()
#     # time.sleep(2)
#     assert list.verify_listsTitle() == "Your Lists", "On clicking Cancel button ,cancel popup is not getting closed . " \
#                                                      "It should close and should come to Your lists page "
#     my_comment = 'On click of Cancel button Delete should close'
#
#
# #@allure.title('TC_161: Verify user created list is deleted on click of Delete list button in the pop up ')
# def test_delete_test2_list(browser):
#     delete = myListObj(browser)
#     my_list = homePagemylistsObj(browser)
#     global test, my_comment
#     test = test_case_ids[160]  # 974
#     my_comment = "Delete List text is not displayed"
#     my_list.click_delete_test2_my_list()
#     delete.click_direct_deleteButton()
#     assert delete.verify_delete_list_text() == True, "Delete List text is not displayed"
#     my_comment = '"After deleting list, list is displaying in lists table." \
#                                                           " it should get deleted and not be displayed in table. "'
#     assert delete.verify_deleted_test2_MyList() == False, "After deleting list, list is displaying in lists table." \
#                                                           " it should get deleted and not be displayed in table. "
#     my_comment = 'On click of Delete List button selected list should be deleted ' \
#                  'List should get removed from the User Created List table'
#
#
# #@allure.title(
#     # 'TC_162: Verify user is able to download Download .XLSX file on Click of Download .XLSX [Button] from Footer Pop Up '
#     # '')
# def test_download_footer_popup(browser):
#     footer = homePagemylistsObj(browser)
#     global test, my_comment
#     test = test_case_ids[161]  # 975
#     my_comment = 'Footer popup not found / csv file is not Downloading'
#     footer.click_test_checkBox()
#     footer.click_download_csv()
#     csv_download = footer.verify_csv_file_downloaded()
#     assert csv_download == False, 'csv file is not Downloading'
#     my_comment = 'XLSX file should be downloaded on click of Download .XLSX [Button]'
#
#
# #@allure.title('TC_163: Verify user is able to Share List(s) from Share Button in the footer pop up')
# def test_share_to_list_via_email(browser):
#     share = myListObj(browser)
#     footer = homePagemylistsObj(browser)
#     global test, my_comment
#     test = test_case_ids[162]  # 976
#     my_comment = 'Share list popup not found / After clicking on share button , confirmation is not showing.'
#     footer.click_test_checkBox()
#     share.click_shareList()
#     share.enter_email(email_address)
#     share.click_add_email_address()
#     share.click_buttonToshare()
#     assert share.verify_share_list_success() == True, "After clicking on share button , confirmation is not showing."
#     my_comment = '''Clicking Email Spreadsheet button in fotter pop up should open share pop up
#                     User should be able to share list by entering email id in textbox and clicking share
#                     Reciver should recive the email with attachment'''
#
#
# #@allure.title('TC_164: Verify user is able to Delete List(s) from Delete Button in the footer pop up')
# def test_delete_footer_popup(browser):
#     delete = myListObj(browser)
#     footer = homePagemylistsObj(browser)
#     global test, my_comment
#     test = test_case_ids[163]  # 977
#     time.sleep(10)
#     my_comment = 'Delete Popup not found in my list page'
#     footer.click_test_checkBox()
#     footer.click_DeleteFooterpopup()
#     delete.click_direct_deleteButton()
#     my_comment = "After deleting list, list is displaying in lists table. it should " \
#                  "get deleted and not be displayed in table."
#     assert delete.verify_delete_list_text() == True, "Delete List text is not displayed"
#     assert delete.verify_deleted_test1_MyList() == False, "After deleting list, list is displaying in lists table." \
#                                                           " it should get deleted and not be displayed in table. "
#     my_comment = 'User should be able to delete list from footer pop up'
#
#
# #@allure.title('TC_167: Verify when we deselect all checkboxes which is selected footer popup gets closed')
# def test_deselect_checkbox(browser):
#     multi = homePagemylistsObj(browser)
#     global test, my_comment
#     test = test_case_ids[166]  # 980
#     my_comment = 'double click not applied on my list checkbox'
#     multi.Refresh()
#     multi.click_Demo_checkBox()
#     assert multi.verify_checkselected() == True, "First Check box is not selected after clicking on it. Multiple " \
#                                                  "checkbox should get selected. "
#     multi.click_first_test_checkBox()
#     my_comment = "Second Check box is not selected after clicking on it. Multiple " \
#                  "checkbox should get selected. "
#     assert multi.verify_second_checkbox_selected() == True, "Second Check box is not selected after clicking on it. Multiple " \
#                                                             "checkbox should get selected. "
#     multi.click_first_test_checkBox()
#     multi.click_Demo_checkBox()
#     check_box = multi.verify_csv_file_downloaded()
#     assert check_box == False, 'csv file is not Downloading'
#     my_comment = 'when diselected all checkbox footer popup should be close'
#
#
# #@allure.title('TC_168: Verify elements in my list details page')
# def test_list_detail_page(browser):
#     list = homePagemylistsObj(browser)
#     global test, my_comment
#     test = test_case_ids[167]  # 981
#     my_comment = 'list Name is not clickable / List Page not found '
#     list.click_recentlyList()
#     my_comment = "In detail Page List name is not showing in heading . Detailed page is not opened "
#     list.click_list_grid_view_button()  # grid view added
#     assert list.verify_detailedPage() == True, "In detail Page List name is not showing in heading . Detailed page is " \
#                                                "not opened "
#     my_comment = "Grid view button is not present"
#     assert list.verify_grid_view_button() == True, "Grid view button is not present"
#     # assert list.verify_select_all_checkbox() == True, "Select All checkbox is not present"
#     my_comment = "List view button is not present"
#     assert list.verify_list_view_button() == True, "List view is not present"
#     my_comment = "email spreadsheet button is not present"
#     assert list.verify_email_spreadsheet() == True, "email spreadsheet is not present"
#     my_comment = 'delete button is not present in list page header "'
#     assert list.verify_header_delete() == True, "delete button is not present in list page header "
#     my_comment = "sorting filter is not present"
#     assert list.verify_sorting_filter() == True, "sorting filter is not present"
#     my_comment = "checkbox not present on card"
#     assert list.verify_first_card_checkbox() == True, "checkbox not present on card"
#     my_comment = '''List Details page should have the following elements
# 1. Header:
#     i) Checkbox
#     ii) List Name (no. of titles)
#     iii) View selection button (Grid & List)
#     iv) Share and Delete buttons
#     v) Sorting (dropdown)
# #
# # 2. Movie/TV cards for all the titles added in the list with checkbox'''
#
#
# #@allure.title(
#     # 'TC_169: Verify one sheet overlay is present on the movie cards in the grid view and all buttons are visible on '
#     # 'hover')
# def test_list_page_hover(browser):
#     list = homePagemylistsObj(browser)
#     global test, my_comment
#     test = test_case_ids[168]  # 982
#     list.click_grid_view_button() # grid view added
#     my_comment = 'View-Details button is not present'
#     view_details = list.viewDetails_first_movie_card()
#     assert view_details == True, 'View-Details is not present'
#     my_comment = 'Watch-Trailer is not present'
#     watch_trailer = list.watch_trailer_first_movie_card()
#     assert watch_trailer == True, 'Watch-Trailer is not present'
#     my_comment = 'watch now is not present'
#     watch_now = list.watch_now_first_movie_card()
#     assert watch_now == True, 'watch now is not present'
#     my_comment = 'add to list is not present'
#     add_to_list = list.add_to_list_first_movie_card()
#     assert add_to_list == True, 'add to list is not present'
#     my_comment = '''One sheet overlay should be present on each movie/tv card
#
# On hover, it should display the following buttons:
# 1. Add To List
# 2. Watch Movie [Only in case of Movie entity]
# 3. Watch Trailer
# 4. View Details
# '''
#
#
# #@allure.title('TC_171: Verify user is able to switch between grid view and list view')
# def test_list_grid_and_list_view(browser):
#     list = homePagemylistsObj(browser)
#     global test, my_comment
#     test = test_case_ids[170]  # 984
#     my_comment = 'List-View button is not clickable'
#     list_view = list.click_list_view_button()
#     assert list_view == True, 'List-View button is not clickable'
#     my_comment = 'grid-View button is not clickable'
#     grid_view = list.click_grid_view_button()
#     assert grid_view == False, 'grid-View button is not clickable'
#     my_comment = 'On click of the view button, view should change in respect to the button clicked'
#
#
# #@allure.title('TC_172: Verify List view ')
# def test_verify_list_elements_list_page(browser):
#     list = homePagemylistsObj(browser)
#     global test, my_comment
#     test = test_case_ids[171]  # 985
#     my_comment = 'List-View button is not clickable'
#     director_title = list.click_list_view_button()
#     assert director_title == True, 'List-View button is not clickable'
#     my_comment = 'checkbox is not present'
#     list_checkbox = list.verify_list_checkbox_button()
#     assert list_checkbox == True, 'checkbox is not present'
#     my_comment = 'main cast is not present'
#     main_cast = list.verify_list_main_cast()
#     assert main_cast == True, 'main cast is not present'
#     my_comment = 'list synopsis is not present'
#     list_synopsis = list.verify_list_synopsis()
#     assert list_synopsis == True, 'list synopsis is not present'
#     my_comment = '''List view should show tabular structure with following columns
# 1. Title with checkbox on left
# 2. Directed By
# 3. Main Cast
# 4. Synopsis
# '''
#
#
# #@allure.title('TC_173: Verify user is able to select single or multiple titles by clicking the checkbox against each '
#               # 'title in any view')
# def test_click_list_page_checkbox(browser):
#     footer = homePagemylistsObj(browser)
#     global test, my_comment
#     test = test_case_ids[172]  # 986
#     my_comment = "List selected Text is not displaying in footer pop . It should show. "
#     footer.click_list_checkbox_button()
#     assert "Item Selected" in footer.verify_Listtext(), "List selected Text is not displaying in footer pop . It " \
#                                                         "should show. "
#     my_comment = 'User should be able to select single or multiple titles from the list'
#
#
# #@allure.title('TC_174: Verify footer pop up is shown on selecting titles in any view')
# def test_verify_list_details_page_footer(browser):
#     footer = homePagemylistsObj(browser)
#     global test, my_comment
#     test = test_case_ids[173]  # 987
#     my_comment = 'List selected Text is not displaying in footer pop . It should show Text'
#     assert "Item Selected" in footer.verify_Listtext(), "List selected Text is not displaying in footer pop . It " \
#                                                         "should show. "
#     my_comment = "Download csv is not present there. Download csv button should be displayed in footer popup. "
#     assert footer.verify_downloadCsv() == True, "Download csv is not present there. Download csv button should be " \
#                                                 "displayed in foooter popup. "
#     my_comment = "Share List is not present there. Share list button should be displayed in footer popup. "
#     assert footer.verify_shareList() == True, "Share List is not present there. Share list button should be displayed " \
#                                               "in footer popup. "
#     assert footer.verify_DeleteFooterpopup() == True, "Delete button is not present there. Delete button button " \
#                                                       "should be displayed in footer popup. "
#     my_comment = "Delete button is not present there. Delete button button should be displayed in footer popup. "
#     assert footer.verify_AddToListFooterpopup() == True, "Add to list is not present"
#     my_comment = 'Footer section should be shown on selecting title in any view'
#
#
# #@allure.title('TC_175: Verify user is able to add titles(s) to any list')
# def test_add_to_old_list_details_page_footer(browser):
#     home = homepage(browser)
#     global test, my_comment
#     test = test_case_ids[174]  # 988
#     footer = homePagemylistsObj(browser)
#     my_comment = 'add to list is not adding title through old list to new list'
#     footer.verify_click_AddToListFooterpopup()
#     home.SearchList("test")
#     select = home.MovieCardVerifySelectUnselectListForTest()
#     assert select == True
#     my_comment = 'Success message is not showing after adding title into list"'
#     home.AddMovieToList()
#     assert home.verify_success_text() == True, "Success message is not showing after adding title into list"
#     my_comment = '''User should be able to add title(s) to any list by following the below steps.
# 1. Select any title in any view
# 2. Click on Add To List (Footer popup)
# 3. select list and click on add to list button
#
# '''
#
#
# #@allure.title('TC_177: Verify the options of Sorting and their functionality')
# def test_verify_list_sorting_filter_elements(browser):
#     list = homePagemylistsObj(browser)
#     global test, my_comment
#     test = test_case_ids[176]  # 990
#     my_comment = 'New-to-Old sorting option is not present / New-to-Old sorting operation is not applied'
#     list.click_sorting_filter()
#     new_to_old = list.verify_release_date_new_to_old_filter()
#     assert new_to_old == True, 'New-to-Old sorting option is not present'
#     my_comment = 'ld-to-new sorting operation not applied'
#     old_to_new = list.verify_release_date_old_to_new_filter()
#     assert old_to_new == True, 'old-to-new option option is not present'
#     my_comment = 'A to Z sorting is not applied'
#     a_z = list.verify_sorting_az()
#     assert a_z == True, 'A to Z sorting is not present'
#     my_comment = 'Z to A sorting is not applied'
#     z_a = list.verify_sorting_za()
#     assert z_a == True, 'Z to A sorting is not present'
#     my_comment = '''Sorting drop down should have the following options with mentioned behaviour
# 1. Release Date (Old to New) -- Titles should be ordered in Decending order of Release Date
# 2. Release Date (New to Old) -- Titles should be ordered in Ascending order of Release Date
# 3. Sort A-Z  -- Titles should be ordered in Ascending order of Alphabets
# 4. Sort Z-A -- Titles should be ordered in Descending order of Alphabets
# '''
#
#
# #@allure.title('TC_178: Verify user is able to share email spreadsheet from email spreadsheet button')
# def test_click_list_header_email_spreadsheet(browser):
#     list = homePagemylistsObj(browser)
#     share = myListObj(browser)
#     global test, my_comment
#     test = test_case_ids[177]  # 991
#     my_comment = 'Share email popup is not found'
#     list.Refresh_List_page()
#     list.click_list_grid_view_button()  # grid view added
#     list.click_list_header_email_spreadsheet()
#     share.enter_email(email_address)
#     share.click_add_email_address()
#     share.click_buttonToshare()
#     my_comment = 'After clicking on share button , confirmation is not showing.'
#     assert share.verify_share_list_success() == True, "After clicking on share button , confirmation is not showing."
#     my_comment = 'on click email spreadsheet button a popup should be open and user should be able' \
#                  ' to share list throught this popup'
#
#
# #@allure.title('TC_180: Verify select all checkbox on header is working')
# def test_click_list_select_all_button(browser):
#     list = homePagemylistsObj(browser)
#     global test, my_comment
#     test = test_case_ids[179]  # 993
#     time.sleep(12) #30
#     my_comment = 'List selected Text is not displaying in footer pop . It should show.'
#     list.click_select_all_checkbox()
#     assert "Items Selected" in list.verify_List_text_multi(), "List selected Text is not displaying in footer pop . It " \
#                                                               "should show. "
#     my_comment = 'when user click on select all checkbox it should be select all the titles of that page.'
#
#
# #@allure.title('TC_181: Verify Download XLSX button from footer popup')
# def test_download_multi_list_footer_popup(browser):
#     footer = homePagemylistsObj(browser)
#     global test, my_comment
#     test = test_case_ids[180]  # 994
#     my_comment = 'Download Button not found in footer popup'
#     footer.click_list_multi_download_csv()
#     my_comment = 'csv file is not Downloading'
#     csv_download = footer.verify_csv_file_downloaded()
#     assert csv_download == False, 'csv file is not Downloading'
#     my_comment = 'On click email spreadsheet button a popup should be open and ' \
#                  'user should be able to share list throught this popup'
#
#
# #@allure.title('TC_183: Verify email spreadsheet button from footer popup')
# def test_click_list_footer_email_spreadsheet(browser):
#     list = homePagemylistsObj(browser)
#     share = myListObj(browser)
#     global test, my_comment
#     test = test_case_ids[182]  # 996
#     my_comment = 'email spreadsheet button not found in footer popup'
#     list.Refresh_List_page() #please change
#     list.click_select_all_checkbox()
#     my_comment = 'Email share popup not found'
#     list.click_footer_shareList()
#     share.enter_email(email_address)
#     share.click_add_email_address()
#     my_comment = "After clicking on share button , confirmation is not showing."
#     share.click_buttonToshare()
#     assert share.verify_share_list_success() == True, "After clicking on share button , confirmation is not showing."
#     my_comment = 'on click delete button user should be able to delete selected titles '
#
#
# #@allure.title('TC_187: Verify on click Watch now button while hovering on title')
# def test_click_watchnow_list_page_hover(browser):
#     list = homePagemylistsObj(browser)
#     video_player = videoplayer(browser)
#     global test, my_comment
#     test = test_case_ids[186]  # 1000
#     time.sleep(12)
#     my_comment = 'video player is not displayed / Watch now button is not Clickable'
#     list.click_list_grid_view_button()
#     list.click_watch_now_first_movie_card()
#     zoom_button = video_player.zoomINButton()
#     assert zoom_button == True, 'video player is not displayed'
#     video_player.ClickCloseButton()
#     my_comment = 'On click watch now button a video player should be open'
#
#
# #@allure.title('TC_186: Verify on click add to list button while hovering on title')
# def test_click_addToList_list_page_hover(browser):
#     list = homePagemylistsObj(browser)
#     home_page = homePageObj(browser)
#     global test, my_comment
#     test = test_case_ids[185]  # 999
#     my_comment = 'Add to list button is not Clickable / add to list popup not found'
#     list.click_list_grid_view_button()
#     list.click_add_to_list_first_movie_card()
#     assert home_page.verifyAlert() == "CREATE A NEW LIST", "After clicking on add to list button Pop is not opening. "
#     my_comment = 'On click add to list button add to list popup should open'
#
#
# #@allure.title('TC_184: Verify user is able to delete selected titles from footer popup')
# def test_click_on_first_movie_card_delete_footer_checkbox_list(browser):
#     list = homePagemylistsObj(browser)
#     footer = homePagemylistsObj(browser)
#     delete = myListObj(browser)
#     global test, my_comment
#     test = test_case_ids[183]  # 997
#     my_comment = 'Delete button is not present on Footer popup / Delete button is not Clickable'
#     list.Refresh_List_page() #please change
#     list.click_list_grid_view_button()
#     first_card_name = list.list_first_card_movie_name()
#     list.click_list_checkbox_button()
#     footer.click_DeleteFooterpopup()
#     delete.click_direct_deleteButton_title()
#     assert delete.verify_delete_list_text() == True, "Delete List text is not displayed"
#     my_comment = "user is not able to delete the movie"
#     time.sleep(10)#we need to wait
#     after_delete_first_card = list.list_first_card_movie_name()
#     assert first_card_name != after_delete_first_card, "user is not able to delete the movie"
#     my_comment = 'on click delete button user should be able to delete selected titles '
#
# #@allure.title('TC_185: Verify on click view details button while hovering on title ')
# def test_click_view_details_list(browser):
#     list = homePagemylistsObj(browser)
#     home = homepage(browser)
#     global test, my_comment
#     test = test_case_ids[184]  # 998
#     my_comment = 'View Detail button is not Clickable '
#     list.click_list_grid_view_button()
#     list.click_viewDetails_first_movie_card_list()
#     my_comment = 'Movie Page is not open / Synopsis Title is not present'
#     synopsis = home.VerifySynopsisTitle()
#     assert synopsis == True, 'Title Page is not open'
#     my_comment = 'On click view details button page should redirected to title details page'
#
#
# #@allure.title('TC_179: Verify user is able to delete list from delete button')
# def test_click_header_delete_list(browser):
#     list = homePagemylistsObj(browser)
#     home = homepage(browser)
#     delete = myListObj(browser)
#     global test, my_comment
#     test = test_case_ids[178]  # 992
#     my_comment = 'Delete popup not found / Delete button is not clickable'
#     home.gotohomepage(_url_)
#     list_page = home.ClickMyListHeader()
#     assert list_page == True, "Not redirecting to correct page"
#     list.click_recentlyList()
#     list.click_header_delete_list()
#     delete.click_direct_deleteButton_js()
#     assert delete.verify_delete_list_text() == True, "Delete List text is not displayed"
#     my_comment = 'user should be able to delete list through delete button'
#
#
# #@allure.title('TC_170: Watch Movie should not be shown in case of a TV entity')
# def test_verify_tv_card(browser):
#     my_list = homePagemylistsObj(browser)
#     home = homepage(browser)
#     global test, my_comment
#     test = test_case_ids[169]  # 983
#     my_comment = 'Create list button is not present or not Clickable / List is not Auto Selected'
#     home.gotohomepage(_url_)
#     add_list = home.ClickTvCardAddToList()
#     assert add_list == True, "Movie List Pop-up not found"
#     my_comment = 'Create list button is not present or not Clickable / List is not Auto Selected'
#     home.ListName("TvShow")
#     home.ClickCreateList()
#     created = home.CreatedList()
#     assert created == True
#     name = home.VerifyTvListCreated()
#     assert name == True
#     auto_list = home.VerifyTvListAutoSelect()
#     assert auto_list == True, 'List is not Auto Selected'
#     my_comment = "Success message is not showing After Creating list"
#     home.AddMovieToList()
#     assert home.verify_success_text() == True, "Success message is not showing ."
#     my_comment = 'Once the list is created and is auto selected, then clicking on add to ' \
#                  'list button should add the movie to the new list'
#     list_page = home.ClickMyListHeaderlist()
#     assert list_page == True, "Not redirecting to correct page"
#     my_list.click_tvShowList()
#     my_list.click_list_grid_view_button()
#     series_name = my_list.verify_tv_show_my_list()
#     assert series_name == True, 'Series name is not present in TvShow list'
#     my_comment = 'Watch Now button present in tv Show list'
#     watch_now = home.verify_tv_show_watch_now_button()
#     assert watch_now == True, 'Watch Now button present in tv Show list'
#     my_comment = 'Watch Movie should not be shown in case of a TV entity'
#
#
# #@allure.title('TC_176: Verify user is able to add titles(s) to any list')
# def test_add_to_list_details_page_footer(browser):
#     home = homepage(browser)
#     footer = homePagemylistsObj(browser)
#     global test, my_comment
#     test = test_case_ids[175]  # 989
#     my_comment = 'Success message is not showing after adding title into lis'
#     footer.click_list_checkbox_button()
#     footer.verify_click_AddToListFooterpopup()
#     home.ListName("listData")
#     home.ClickCreateList()
#     created = home.CreatedList()
#     assert created == True
#     home.AddMovieToList()
#     assert home.verify_success_text() == True, "Success message is not showing after adding title into list"
#     my_comment = '''User should be able to create list by following the below steps.
# 1. Select any title in any view
# 2. Click on Add To List
# 3. Enter list name
# 4. Click Create List [After creation the list should be auto selected]
# 5. Click Add To List
# '''
#
# # ####################################################################
# #@allure.title('TC_135: Verify two section on My List page')
# def test_verify_my_list_sections(browser):
#     home = homepage(browser)
#     global test, my_comment
#     test = test_case_ids[134]  # 948
#     my_comment = 'My list page not opened'
#     list_page = home.ClickMyListHeader()
#     assert list_page == True, "Not redirecting to correct page"
#     my_comment = 'Your list text is not Present in My-list Section'
#     your_list_text = home.VerifyYourList()
#     assert your_list_text == True, 'Your list text is not Present in My-list Section'
#     my_comment = 'special list text is not present in My-list Section'
#     special_list = home.VerifyShareSpecialList()
#     assert special_list == True, 'special list text is not present in My-list Section'
#     my_comment = '''My List should have two section
# 1. List Made For You [Curated Lists]
# 2. Your Lists [User Created Lists]'''
#
# #
# # #@allure.title('TC_136: Verify elements in Curated List section')
# # def test_verify_curated_list_elements(browser):
# #     home = homepage(browser)
# #     global test, my_comment
# #     test = test_case_ids[135]  # 949
# #     my_comment = 'special list text is not present in My-list Section'
# #     special_list = home.ClickyShareSpecialList()
# #     assert special_list == True, 'special list text is not present in My-list Section'
# #     my_comment = 'Automation Title is not present in Special list section '
# #     automation_one_title_text = home.VerifyAutomationOneTitleText()
# #     assert automation_one_title_text == True, 'Automation1 Title is not present in Special list section '
# #     # automation_two_title_text = home.VerifyAutomationSecondTitleText()
# #     # assert automation_two_title_text == True, 'Automation2 Title is not present in Special list section'
# #     my_comment = '''Curated List section should have the following:
# #     1. Title
# #     2. Curated List Table'''
# #
# #
# # #@allure.title('TC_137: Verify columns/elements of List table')
# # def test_verify_curated_list_columns_elements(browser):
# #     home = homepage(browser)
# #     global test, my_comment
# #     test = test_case_ids[136]  # 950
# #     my_comment = 'Automation Title is not present in Special list section '
# #     automation_one_title_text = home.VerifyAutomationOneTitleText()
# #     assert automation_one_title_text == True, 'Automation1 Title is not present in Special list section '
# #     my_comment = 'Email Spread-Sheet button is not present in Automation1 Row'
# #     email_spread_sheet = home.VerifyAutomationOneSpreadSheetButton()
# #     assert email_spread_sheet == True, 'Email Spread-Sheet button is not present in Automation1 Row'
# #     my_comment = 'Checkbox is not present in curated list section'
# #     # automation1_checkbox = home.VerifyAutomationOneCheckboxButton()
# #     # assert automation1_checkbox == True, 'Checkbox is not present in curated list section'
# #     my_comment = '''Table should have following Columns/Elements:
# # 1. Checkbox
# # 2. Name of List
# # 3. Email Spreadsheet [button]'''
# #
# #
# # #@allure.title('TC_138: Verify user is able to select the list by clicking on the checkbox')
# # def test_click_single_checkbox_curated_list(browser):
# #     home = homepage(browser)
# #     footer = homePagemylistsObj(browser)
# #     global test, my_comment
# #     test = test_case_ids[137]  # 951
# #     my_comment = 'single checkbox is not clickable in curated list '
# #     home.ClickAutomationOneCheckboxButton()
# #     my_comment = "List selected Text is not displaying in footer pop . It should show. "
# #     assert "Item Selected" in footer.verify_Listtext(), "List selected Text is not displaying in footer pop . It " \
# #                                                         "should show. "
# #
# #
# # #@allure.title('TC_139: Verify user is able to select multiple list by clicking on the checkbox')
# # def test_click_multiple_checkbox_curated_list(browser):
# #     home = homepage(browser)
# #     footer = homePagemylistsObj(browser)
# #     global test, my_comment
# #     test = test_case_ids[138]  # 952
# #     my_comment = 'Multiple checkbox is not clickable in curated list '
# #     home.ClickAutomationSecondCheckboxButton()
# #     my_comment = "List selected Text is not displaying in footer pop . It should show. "
# #     assert "Items Selected" in footer.verify_List_text_multi(), "List selected Text is not displaying in footer pop . " \
# #                                                                 "It should show. "
# #
# #
# # #@allure.title('TC_140: Verify click on checkbox opens the footer popup')
# # def test_verify_footer_popup_curated_list(browser):
# #     home = homepage(browser)
# #     footer = homePagemylistsObj(browser)
# #     global test, my_comment
# #     test = test_case_ids[139]  # 953
# #     my_comment = "List selected Text is not displaying in footer pop . It should show. "
# #     assert "2" in footer.verify_List_text_multi(), "List selected Text is not displaying in footer pop . " \
# #                                                     "It should show. "
# #     my_comment = '"Download csv is not present there. Download csv button should be displayed in footer popup. "'
# #     assert footer.verify_downloadCsv() == True, "Download csv is not present there. Download csv button should be " \
# #                                                 "displayed in footer popup. "
# #     my_comment = "Share List is not present there. Share list button should be displayed in footer popup. "
# #     assert footer.verify_shareList() == True, "Share List is not present there. Share list button should be displayed " \
# #                                               "in footer popup. "
# #     my_comment = '''On click of checkbox footer popup should open
# #     Footer popup should have the following:
# #     1. Number of selected lists
# #     2. Download .XLSX Button
# #     3. EMAIL SPREADSHEET BUTTON'''
# #
# #
# # #@allure.title('TC_145: Verify click on checkbox opens the footer popup')
# # def test_click_download_footer_popup_curated_list(browser):
# #     home = homepage(browser)
# #     footer = homePagemylistsObj(browser)
# #     global test, my_comment
# #     test = test_case_ids[144]  # 958
# #     my_comment = '"Download csv is not clickable / Download csv button should be displayed in footer popup. "'
# #     footer.click_download_csv_curated_popup()
# #     downloading_start = footer.verify_downloading_started()
# #     assert downloading_start == True, 'download button is not clickable'
# #     my_comment = '.XLSX file should be downloaded on click of  Download .XLSX button'
# #
# #
# # #@allure.title('TC_141: Verify on click on List name user is redirected to List Detail page')
# # def test_click_curated_list_name(browser):
# #     home = homepage(browser)
# #     footer = homePagemylistsObj(browser)
# #     global test, my_comment
# #     test = test_case_ids[140]  # 954
# #     my_comment = 'Curated Title name is not clickable'
# #     automation_title_text = home.ClickAutomationOneTitleText()
# #     assert automation_title_text == True, 'Curated Title name is not clickable'
# #     my_comment = 'On click on List Name user should be redirected to List Detail page of that List'
# #
# #
# # #@allure.title('TC_142: Verify on click on EMAIL SPREADSHEET BUTTON , share popup is shown')
# # def test_verify_email_spreadsheet_popup(browser):
# #     home = homepage(browser)
# #     global test, my_comment
# #     test = test_case_ids[141]  # 955
# #     my_comment = 'My list page not opened'
# #     list_page = home.ClickMyListHeader()
# #     assert list_page == True, 'my list page not opened'
# #     special_list = home.ClickyShareSpecialList()
# #     assert special_list == True, 'special list text is not present in My-list Section'
# #     home.ClickAutomationOneSpreadSheetButton()
# #     my_comment = 'Close Button is not present in Spreadsheet popup'
# #     # close_button = home.VerifySpreadsheetCloseButton()
# #     # assert close_button == True, 'Close Button is not present in Spreadsheet popup'
# #     my_comment = 'Static Text is not present in Spreadsheet popup'
# #     static_text = home.VerifySpreadsheetStaticText()
# #     assert static_text == True, 'Static Text is not present in Spreadsheet popup'
# #     my_comment = 'Title name is not present in Spreadsheet popup'
# #     title_text = home.VerifySpreadsheetTitleText()
# #     assert title_text == True, 'Title name is not present in Spreadsheet popup'
# #     my_comment = 'Title Count is not present in Spreadsheet popup'
# #     title_count = home.VerifySpreadsheetTitleCountText()
# #     assert '3' in title_count, 'Title Count is not present in Spreadsheet popup'
# #     spreadsheet_input_field = home.VerifySpreadsheetInputField()
# #     assert spreadsheet_input_field == True, 'Spread sheet Input field is not present in popup'
# #     share_button = home.VerifySpreadsheetShareButton()
# #     assert share_button == True, 'share button is not present in spreadsheet button'
# #     my_comment = '''On click of Share button, share pop up should be shown
# # Share pop up should have the following element:
# # 1. Close button
# # 2. Static text
# # 3. List Name & number of titles in it
# # 4. Static text
# # 5. Email [Textbox]
# # 6. Share button'''
# #
# #
# # #@allure.title('TC_143: Verify is able to share list and reciever recieves it')
# # def test_share_to_list_via_email_reciver(browser):
# #     share = myListObj(browser)
# #     footer = homePagemylistsObj(browser)
# #     global test, my_comment
# #     test = test_case_ids[142]  # 956
# #     my_comment = 'Share list popup not found / After clicking on share button , confirmation is not showing.'
# #     share.enter_email(email_address)
# #     share.click_add_email_address()
# #     share.click_buttonToshare()
# #     assert share.verify_share_list_success() == True, "After clicking on share button , confirmation is not showing."
# #     my_comment = '''Clicking Email Spreadsheet button in footer pop up should open share pop up
# #                     User should be able to share list by entering email id in textbox and clicking share
# #                     Receiver should received the email with attachment'''
# #
# #
# # #@allure.title('TC_146: Verify user is able to Share List(s) from EMAIL SPREADSHEET BUTTON in the footer popup')
# # def test_click_share_spreadsheet_footer_curated(browser):
# #     home = homepage(browser)
# #     footer = homePagemylistsObj(browser)
# #     share = myListObj(browser)
# #     global test, my_comment
# #     test = test_case_ids[145]  # 959
# #     time.sleep(18)
# #     my_comment = 'single checkbox is not clickable in curated list '
# #     # time.sleep(4)
# #     home.ClickAutomationOneCheckboxButton()
# #     my_comment = "List selected Text is not displaying in footer pop . It should show. "
# #     assert "Item Selected" in footer.verify_Listtext(), "List selected Text is not displaying in footer pop . It " \
# #                                                         "should show. "
# #     footer.click_footer_shareList()
# #     my_comment = 'Share list popup not found / After clicking on share button , confirmation is not showing.'
# #     share.enter_email(email_address)
# #     share.click_add_email_address()
# #     share.click_buttonToshare()
# #     assert share.verify_share_list_success() == True, "After clicking on share button , confirmation is not showing."
# #     my_comment = '''Clicking Email Spreadsheet button in footer pop up should open share pop up
# #                        User should be able to share list by entering email id in textbox and clicking share
# #                        Receiver should received the email with attachment'''
# #
# #
# # #@allure.title('TC_157: Verify on click on Share list in roar button, share popup is shown')
# # def test_click_share_list_elements(browser):
# #     home = homepage(browser)
# #     footer = homePagemylistsObj(browser)
# #     share = myListObj(browser)
# #     global test, my_comment
# #     test = test_case_ids[156]  # 970
# #     time.sleep(30)
# #     home.gotohomepage(_url_)
# #     list_page = home.ClickMyListHeader()
# #     assert list_page == True, 'List'
# #     home.ClickShareListRoarButton()
# #     my_comment = 'Close Button is not present in Spreadsheet popup'
# #     # close_button = home.VerifySpreadsheetCloseButton()
# #     # assert close_button == True, 'Close Button is not present in Spreadsheet popup'
# #     my_comment = 'Static Text is not present in Spreadsheet popup'
# #     static_text = home.VerifySpreadsheetStaticText()
# #     assert static_text == True, 'Static Text is not present in Spreadsheet popup'
# #     my_comment = 'Title name is not present in Spreadsheet popup'
# #     title_text = home.VerifySpreadsheetTestTitleText()
# #     assert title_text == True, 'Title name is not present in Spreadsheet popup'
# #     my_comment = 'Title Count is not present in Spreadsheet popup'
# #     title_count = home.VerifySpreadsheetTestTitleCountText()
# #     assert ('2' in title_count) or ('1' in title_count), 'Title Count is not present in Spreadsheet popup'
# #     spreadsheet_input_field = home.VerifySpreadsheetInputField()
# #     assert spreadsheet_input_field == True, 'Spread sheet Input field is not present in popup'
# #     share_button = home.VerifySpreadsheetShareButton()
# #     assert share_button == True, 'share button is not present in spreadsheet button'
# #     my_comment = '''On click of Share button, share pop up should be shown
# # Share pop up should have the following element:
# # 1. Close button
# # 2. Static text
# # 3. List Name & number of titles in it
# # 4. Static text
# # 5. Email [Textbox]
# # 6. Share button'''
# #
# #
# # #@allure.title('TC_158: Verify on click on Share list in roar button, share popup is shown')
# # def test_verify_share_list_roar(browser):
# #     home = homepage(browser)
# #     footer = homePagemylistsObj(browser)
# #     share = myListObj(browser)
# #     global test, my_comment
# #     test = test_case_ids[157]  # 971
# #     my_comment = 'Share list popup not found / After clicking on share list button , confirmation is not showing.'
# #     share.enter_email(email_address)
# #     share.click_add_email_address_list()
# #     share.click_buttonToshare()
# #     assert share.verify_share_list_success() == True, "After clicking on share button , confirmation is not showing."
# #     my_comment = 'Curated list not shared'
# #     time.sleep(30)
# #     home.gotohomepage(_url_)
# #     curated_list = footer.RefreshMyList()
# #     assert curated_list == True, 'Curated list not shared'
# #     my_comment = '''User should be able to share list by entering email id in textbox and clicking share
# #                     Receiver should received the email with attachment'''
# #
# #
# # # #@allure.title('TC_165: Verify user is able to select both Curated & User Created lists')
# # # def test_click_curated_and_user_created_checkbox(browser):
# # #     home = homepage(browser)
# # #     footer = homePagemylistsObj(browser)
# # #     global test, my_comment
# # #     test = test_case_ids[164]  # 978
# # #     my_comment = 'single checkbox is not clickable in curated list '
# # #     home.ClickAutomationOneCheckboxButton()
# # #     my_comment = "List selected Text is not displaying in footer pop . It should show. "
# # #     assert "Item Selected" in footer.verify_Listtext(), "List selected Text is not displaying in footer pop . It " \
# # #                                                         "should show. "
# # #     my_comment = 'Multiple checkbox is not clickable with curated and user created section'
# # #     home.ClickUserCreatedAutomationSecondCheckboxButton()
# # #     my_comment = "List selected Text is not displaying in footer pop . It should show. "
# # #     assert "Items Selected" in footer.verify_List_text_multi(), "List selected Text is not displaying in footer pop . " \
# # #                                                                 "It should show. "
# # #     my_comment = 'User should be able to select Curated & User Created lists'
# # #
# # #
# # # #@allure.title('TC_166: Verify user is able to select both Curated & User Created lists ')
# # # def test_verify_curated_and_user_created_delete_button(browser):
# # #     home = homepage(browser)
# # #     footer = homePagemylistsObj(browser)
# # #     global test, my_comment
# # #     test = test_case_ids[165]  # 979
# # #     my_comment = 'Delete button is present when Curated and User Created list are selected '
# # #     delete_button = footer.verify_delete_button_curated()
# # #     assert delete_button == True, 'Delete button is present when Curated and User Created list are selected'
# # #     my_comment = 'Footer pop up should not show Delete button when both list types are selected'
# #
#
# #@allure.title('TC_Raw: logout after all process ')
# def test_raw_logout_button(browser):
#     home = homepage(browser)
#     home.gotohomepage(_url_)
#     verify = home.ClickLogoutButton()
#     assert verify == True, "User is not logged out"
#
#
# #@allure.title('TC_188: Verify Elements present on Marketing Rules Page')
# def test_verify_marketing_rules_page_elements(browser):
#     home = homepage(browser)
#     home_page = homePageObj(browser)
#     market = MarketingRulesPage(browser)
#     global user
#     user = loginpage(browser)
#
#     global test, my_comment
#     test = test_case_ids[187]  # 1311
#     my_comment = 'Marketing Rules page not open / Marketing Rules button is not clickable'
#     user.LoginPage(_url_)
#     user.ClickOnAcceptCookies()
#     user.EnterEmail(email)
#     verify = user.ClickNext()
#     assert verify == True, "user not proceed to next step with valid email id"
#     user.EnterPassword(password)
#     user.verifyButton()
#     # time.sleep(2)
#     # current_url = user.ValidateUrlForNextPage()
#     # assert not 'login' in current_url
#     # time.sleep(2)
#     user.confrimation_page_without_elements()
#     user.confrimation_page_elements()
#     verify = user.VerifyLogin()
#     assert verify == True, "User is not able to login with valid credentials"
#     my_comment = 'On click of Logout button user should logged out of app and redirected to Login page'
#     home.ClickMarketingRules()
#     my_comment = 'Banner-text is not present in Marketing Rules page'
#     banner_text = market.verify_banner_text()
#     assert banner_text == True, 'Banner-text is not present'
#     my_comment = 'Download pdf button is not present in Marketing Rules page'
#     count_download = market.verify_download_button()
#     assert count_download >= 1, 'Download pdf button is not present'
#     my_comment = 'Static text is not present in marketing Rules page'
#     static_text = market.verify_static_text()
#     assert static_text == True, 'Static text is not present'
#     logo = home.HomePageLogo()
#     my_comment = 'Marketing rules Header elements are not present'
#     assert logo == True, "Header logo not found"
#     films_series = home.HeaderFilmsAndSeries()
#     assert films_series == True, "Header 'Films & Series' link not found"
#     mylist = home.HeaderMylist()
#     assert mylist == True, "My list link not found"
#     logout = home.HeaderLogoutButton()
#     assert logout == True, "Logout button not found"
#     marketing_rules = home.HeaderMarketingRules()
#     assert marketing_rules == True, "Search button not found"
#     assets = home.HeaderAssets()
#     assert assets == True, "Assets Button not found"
#     mycart = home.HeaderMyCarts()
#     assert mycart == True, "My Carts button not found"
#     my_comment = 'Marketing Rules footer Elements are not present in Footer Section'
#     assert home_page.verify_Privacypolicy() == True, "Privacy policy is not displaying in global footer. It should be " \
#                                                      "displayed in footer. "
#     assert home_page.verify_termsUse() == True, "Terms and Use is not displaying in global footer. It should be " \
#                                                 "displayed in footer. "
#     assert home_page.verify_footerLogo() == True, "MGM logo  is not displaying in global footer. It should be " \
#                                                   "displayed in footer. "
#     assert home_page.verify_supportLink() == True, "Support link is not displaying in global footer. It should be " \
#                                                    "displayed in footer. "
#     assert home_page.verify_address() == True, "Address text is not displaying in global footer. It should be " \
#                                                "displayed in footer. "
#     assert home_page.verify_legal() == True, "Legal text is not displaying in global footer. It should be " \
#                                              "displayed in footer. "
#     assert home_page.verify_contact_us() == True, "Contact-us is not displaying in global footer. It should be " \
#                                                   "displayed in footer. "
#     assert home_page.verify_youtubeIcon() == True, "Youtube icon is not displaying in global footer. It should be " \
#                                                    "displayed in footer. "
#     assert home_page.verify_fbIcon() == True, "Facebook icon is not displaying in global footer. It should be " \
#                                               "displayed in footer. "
#     assert home_page.verify_twitterIcon() == True, "Twitter icon is not displaying in global footer. It should be " \
#                                                    "displayed in footer. "
#     assert home_page.verify_instaIcon() == True, "Instagram icon is not displaying in global footer. It should be " \
#                                                  "displayed in footer. "
#     assert home_page.verify_copyright() == True, "Copyright is not displaying in global footer. It should be " \
#                                                  "displayed in footer. "
#     assert home_page.verify_connect() == True, "Connect is not displaying in global footer. It should be " \
#                                                "displayed in footer. "
#     my_comment = '''Marketing Rules page should have the following elements:
# 1. Global Header
# 2. Banner with text
# 3. Download pdf button
# 4. Description
# 6. Global Footer'''
#

# #@allure.title('TC_190: Verify banner elements')
# def test_verify_banner_banner_elements_marketing_rules(browser):
#     market = MarketingRulesPage(browser)
#     global test, my_comment
#     test = test_case_ids[189]  # 1313
#     my_comment = 'banner image is not present in Marketing Rules page'
#     banner_image = market.verify_banner_image()
#     assert banner_image == True, 'banner image is not present'
#     my_comment = 'banner text is not present in marketing rules page'
#     banner_text = market.verify_banner_text()
#     assert banner_text == True, 'banner text is not present'
#     my_comment = '''1. Banner image
# 2. Static text'''
#
#
# #@allure.title('TC_191: verify user is able to see full description ')
# def test_verify_description_text_marketing_rules(browser):
#     market = MarketingRulesPage(browser)
#     global test, my_comment
#     test = test_case_ids[190]  # 1314
#     my_comment = 'User Description text is not present in Marketing Rules page'
#     static_text = market.verify_static_text()
#     assert static_text == True, 'description text is not present'
#     my_comment = 'User should be able to see description'
#
#
# #@allure.title('TC_192: Verify Elements present on Films&Series Page')
# def test_verify_film_and_series_page_elements(browser):
#     home = homepage(browser)
#     home_page = homePageObj(browser)
#     film_series = filmSeriesPage(browser)
#     my_list = homePagemylistsObj(browser)
#     global test, my_comment
#     test = test_case_ids[191]  # 1001
#     my_comment = 'Film And Series page not opened after clicking on Film and Series button '
#     list1 = home.ClickLists()
#     assert list1 == True, 'List page is not open'
#     my_list.delete_raw_film_series_second_list(_url_)
#     my_list.delete_raw_film_series_list()
#     my_list.delete_raw_film_series_movies_list()
#     my_list.delete_raw_film_series_second_list(_url_)
#     my_list.delete_raw_film_series_list()
#     my_list.delete_raw_film_series_movies_list()
#     home.gotohomepage(_url_)
#     movies = home.ClickFilmsSeries()
#     assert movies == True, "Not redirecting to correct page"
#     my_comment = 'Header Elements are not found in Film and Series Page'
#     logo = home.HomePageLogo()
#     assert logo == True, "Header logo not found"
#     films_series = home.HeaderFilmsAndSeries()
#     assert films_series == True, "Header 'Films & Series' link not found"
#     mylist = home.HeaderMylist()
#     assert mylist == True, "My list link not found"
#     logout = home.HeaderLogoutButton()
#     assert logout == True, "Logout button not found"
#     marketing_rules = home.HeaderMarketingRules()
#     assert marketing_rules == True, "Search button not found"
#     assets = home.HeaderAssets()
#     assert assets == True, "Assets Button not found"
#     my_cart = home.HeaderMyCarts()
#     assert my_cart == True, "My Carts button not found"
#     my_comment = 'Banner image is not present in Film and Series page'
#     banner_image = film_series.verify_banner_image()
#     assert banner_image == True, 'banner image is not present'
#     my_comment = 'Filters are not present in Film and Series page'
#     filter_button = film_series.verify_filter_button()
#     assert filter_button >= 2, 'filter button is present'
#     my_comment = 'Sorting Button is not present in Film and series page'
#     sorting_button = film_series.verify_sort_filter_button()
#     assert sorting_button >= 1, 'sorting button is not present'
#     pagination = film_series.verify_right_cursor_button()
#     assert pagination == True, 'pagination section is not present'
#     my_comment = 'Footer Elements are not present in Film and Series page'
#     assert home_page.verify_Privacypolicy() == True, "Privacy policy is not displaying in global footer. It should be " \
#                                                      "displayed in footer. "
#     assert home_page.verify_termsUse() == True, "Terms and Use is not displaying in global footer. It should be " \
#                                                 "displayed in footer. "
#     assert home_page.verify_footerLogo() == True, "MGM logo  is not displaying in global footer. It should be " \
#                                                   "displayed in footer. "
#     assert home_page.verify_supportLink() == True, "Support link is not displaying in global footer. It should be " \
#                                                    "displayed in footer. "
#     assert home_page.verify_address() == True, "Address text is not displaying in global footer. It should be " \
#                                                "displayed in footer. "
#     assert home_page.verify_legal() == True, "Legal text is not displaying in global footer. It should be " \
#                                              "displayed in footer. "
#     assert home_page.verify_contact_us() == True, "Contact-us is not displaying in global footer. It should be " \
#                                                   "displayed in footer. "
#     assert home_page.verify_youtubeIcon() == True, "Youtube icon is not displaying in global footer. It should be " \
#                                                    "displayed in footer. "
#     assert home_page.verify_fbIcon() == True, "Facebook icon is not displaying in global footer. It should be " \
#                                               "displayed in footer. "
#     assert home_page.verify_twitterIcon() == True, "Twitter icon is not displaying in global footer. It should be " \
#                                                    "displayed in footer. "
#     assert home_page.verify_instaIcon() == True, "Instagram icon is not displaying in global footer. It should be " \
#                                                  "displayed in footer. "
#     assert home_page.verify_copyright() == True, "Copyright is not displaying in global footer. It should be " \
#                                                  "displayed in footer. "
#     assert home_page.verify_connect() == True, "Connect is not displaying in global footer. It should be " \
#                                                "displayed in footer. "
#     my_comment = '''Films&Series page should have the following elements:
#                     1. Global Header
#                     2. Banner
#                     3. Filters
#                     4. Sorting filter
#                     5. View tabs
#                     6. Title cards
#                     7. Pagination
#                     8. Global Footer'''
#
#
# #@allure.title('TC_193: Verify user is able to see banner image')
# def test_verify_banner_image_film_and_series_page(browser):
#     film_series = filmSeriesPage(browser)
#     global test, my_comment
#     test = test_case_ids[192]  # 1002
#     my_comment = 'banner image is not present in Film And Series page'
#     banner_image = film_series.verify_banner_image()
#     assert banner_image == True, 'banner image is not present'
#     my_comment = 'User should be able  to see banner image'
#
#
# #@allure.title(
    # 'TC_raw: Verify user can create list from search a card')
# def test_create_list_search_card(browser):
#     film_series = filmSeriesPage(browser)
#     home = homepage(browser)
#     film_series.page_refresh()
#     search_movie_name = film_series.type_search_field()
#     film_series.click_search_button()
#     search_result = film_series.verify_search_result()
#     assert search_movie_name in search_result, 'search operation is not working'
#     film_series.mouse_hover_on_search_movie_card()
#     home.ListName("MoviesList")
#     home.ClickCreateList()
#     assert home.CreatedList() == True, "Success message for creating list is not showing."
#     home.AddMovieToList()
#     assert home.verify_success_text() == True, "Success message is not showing ."
#     # time.sleep(2)
#

#
# #@allure.title(
#     # 'TC_194: Verify user is able to search for titles by entering Actor/Character name or FILMS & SERIES name')
# def test_validate_search_field(browser):
#     film_series = filmSeriesPage(browser)
#     global test, my_comment
#     test = test_case_ids[193]  # 1003
#     my_comment = 'search option is not present / search functionality is not working '
#     film_series.page_refresh()
#     search_movie_name = film_series.type_search_field()
#     film_series.click_search_button()
#     search_result = film_series.verify_search_result()
#     assert search_movie_name in search_result, 'search operation is not working'
#     my_comment = 'User should be able to search for title by entering search value On click of Search icon or ' \
#                  'hitting enter, page should automatically scroll to Search Result sectionSearch Result should show' \
#                  ' relevant results'
#
#
# #@allure.title('TC_195: Verify user is able to click on cross button after searching any title')
# def test_verify_cross_button_search_field(browser):
#     film_series = filmSeriesPage(browser)
#     global test, my_comment
#     test = test_case_ids[194]  # 1004
#     my_comment = 'Search Field Cross button is not present / Search Cross button is not Clickable'
#     film_series.click_search_clear()
#     my_comment = 'After clicking on Cross button search history not changed'
#     total_count = film_series.verify_click_search_cross_button()
#     assert total_count > 400, 'After clicking on Cross button search history not changed'
#     my_comment = 'user should be able to click on cross button After click cross button search results should be reset '
#
#
# #@allure.title('TC_196: Verify pagination is present when there are more than 42 titles in search result')
# def test_verify_pagination_elements_search_result(browser):
#     film_series = filmSeriesPage(browser)
#     global test, my_comment
#     test = test_case_ids[195]  # 1005
#     my_comment = 'Movies card count is not more than 42 '
#     film_series.page_refresh()
#     cross_button = film_series.verify_total_movie_card_search_result_button()
#     assert (cross_button > 36) & (cross_button < 44), 'Movies card count is not more than 42 '
#     right_cursor = film_series.verify_right_cursor_button()
#     my_comment = 'Pagination section is not present when card is more than 42'
#     assert right_cursor == True, 'Pagination section is not present'
#     my_comment = 'Pagination should be present when there are more than 42 titles in search result'
#
#
# #@allure.title('TC_197: Verify pagination elements')
# def test_verify_Pagination_elements_clickable(browser):
#     film_series = filmSeriesPage(browser)
#     global test, my_comment
#     test = test_case_ids[196]  # 1006
#     my_comment = 'Right cursor is not Present / Right cursor is not clickable'
#     right_cursor_click = film_series.click_right_cursor_button()
#     assert right_cursor_click == True, 'right cursor is not clickable'
#     film_series.click_left_cursor_button()
#     my_comment = 'Left cursor is not disabled when user on First Page'
#     disable_text = film_series.verify_left_disabled_cursor()
#     assert 'disabled' in disable_text, 'left button cursor is not disabled'
#     my_comment = 'Pagination single page number is not Active(highlight)'
#     active_page = film_series.verify_one_active_page()
#     assert active_page == True, 'page Number is not Active'
#     count_of_disable_pages = film_series.verify_expect_one_disabled_pages_button()
#     assert count_of_disable_pages > 6, 'pages are not disbaled'
#     my_comment = '''Pagination have following elements:-
#                     1. Prev navigation arrow
#                     2. Next navigation arrow
#                     3. Pages number '''
#
#
# #@allure.title('TC_198: Verify Prev navigation arrow functionality')
# def test_verify_Pagination_prev_arrow_clickable(browser):
#     film_series = filmSeriesPage(browser)
#     global test, my_comment
#     test = test_case_ids[197]  # 1007
#     my_comment = 'Left Cursor button is not Disabled'
#     disable_text = film_series.verify_left_disabled_cursor()
#     assert 'disabled' in disable_text, 'left cursor is not disabled'
#     my_comment = 'right cursor is not clickable'
#     right_cursor_click = film_series.click_right_cursor_button()
#     assert right_cursor_click == True, 'right cursor is not clickable'
#     film_series.click_left_cursor_button()
#     my_comment = 'left cursor is not disabled'
#     disable_text = film_series.verify_left_disabled_cursor()
#     assert 'disabled' in disable_text, 'left cursor is not disabled'
#     my_comment = '1. If user is on first page then prev arrow should be hide' \
#                  '2. On click prev arrow page should move to prev page '
#
#
# #@allure.title('TC_199: Verify Next navigation arrow functionality')
# def test_verify_Pagination_next_arrow_clickable(browser):
#     film_series = filmSeriesPage(browser)
#     global test, my_comment
#     test = test_case_ids[198]  # 1008
#     my_comment = 'Right cursor is not clickable'
#     right_cursor_click = film_series.click_right_cursor_button()
#     assert right_cursor_click == True, 'right cursor is not clickable'
#     film_series.click_last_page_button()
#     my_comment = 'right button cursor is not disabled'
#     right_disable_text = film_series.verify_right_disabled_cursor()
#     assert 'disabled' in right_disable_text, 'right button cursor is not disabled'
#     my_comment = '''1. If user is on last page then next arrow should be hide
#                     2. On click Next arrow page should move to Next page'''
#
#
# #@allure.title('TC_200: Verify pages numbers are clickable')
# def test_click_Pagination_page_number_clickable(browser):
#     film_series = filmSeriesPage(browser)
#     global test, my_comment
#     test = test_case_ids[199]  # 1009
#     my_comment = 'Pages Numbers are not Clickable '
#     film_series.click_left_cursor_button()
#     film_series.click_last_page_button()
#     right_disable_text = film_series.verify_right_disabled_cursor()
#     assert 'disabled' in right_disable_text, 'right button cursor is not disabled'
#     my_comment = 'On click any page number user should redirected to that page'
#
#
# #@allure.title('TC_201: Verify the elements of filters')
# def test_verify_filters_elements(browser):
#     film_series = filmSeriesPage(browser)
#     global test, my_comment
#     test = test_case_ids[200]  # 1010
#     my_comment = 'Type Filter, Genre Filter, Rating Filter, Year Filter are not Present'
#     four_filter = film_series.verify_filter_button()
#     assert four_filter == 4, 'Type Filter, Genre Filter, Rating Filter, Year Filter are not Present'
#     my_comment = '''Filters have follwing elements:-
# 1. Type dropdown
# 2. Genre Dropdown
# 3. Ratings Dropdown
# 4. Year dropdown'''
#
#
# #@allure.title('TC_202: Verify Type filter functionality')
# def test_verify_type_filter_movie(browser):
#     global total_movies_series
#     film_series = filmSeriesPage(browser)
#     home = homepage(browser)
#     global test, my_comment
#     test = test_case_ids[201]  # 1011
#     my_comment = 'Type-Filter functionality is not Working in Film and Series page'
#     home.gotohomepage(_url_)
#     movies = home.ClickFilmsSeries()
#     assert movies == True, "Not redirecting to correct page"
#     total_movies_series = film_series.verify_total_movies_series()
#     all_movies = film_series.verify_type_films_filter()
#     assert total_movies_series > all_movies, 'Type-Filter functionality is not Working in Film and Series page'
#     clear_all_total_count = film_series.click_clear_all_filter()
#     assert clear_all_total_count == total_movies_series, 'Clear All button is not working'
#     my_comment = '''1. On click typefilter a dropdown should opened
# 2. There should be radio button
# 3. We can select only one radio button at a time
# 4. After selecting any radio button dropdown should closed and serach results shows according to selected radio filter'''
#
#
# #@allure.title('TC_203: Verify user is able to filters titles by type filter')
# def test_verify_type_filter_series(browser):
#     film_series = filmSeriesPage(browser)
#     global test, my_comment
#     test = test_case_ids[202]  # 1012
#     my_comment = 'Type-Filter functionality is not Working in Film and Series page'
#     all_series = film_series.verify_type_series_filter()
#     assert total_movies_series > all_series, 'Type-Series-Filter is not Working'
#     clear_all_total_count = film_series.click_clear_all_filter()
#     assert clear_all_total_count == total_movies_series, 'Clear All is not working'
#     my_comment = '''User should be able to filter titles by Type by selecting the Type from the drop-down
#                     Search Result should show titles which has the selected Genres'''
#
#
# #@allure.title('TC_204: Verify Genre filter functionality')
# def test_verify_genre_filter_functionality(browser):
#     film_series = filmSeriesPage(browser)
#     global test, my_comment
#     test = test_case_ids[203]  # 1013
#     my_comment = 'Action Genre Filter is not present / user can not Apply Action Genre Filter'
#     action_movie_tags = film_series.verify_genre_Action_filter()
#     assert (action_movie_tags < 43) & (action_movie_tags > 30), 'Action Filter is not apply'
#     clear_all_total_count = film_series.click_clear_all_filter()
#     assert clear_all_total_count == total_movies_series, 'Clear All is not working'
#     my_comment = '''1. On click Genre filter a dropdown should opened
# 2. There should be Checkboxes and genre name
# 3. We can select one or multiple checkboxes at a time
# 4. Apply filter button should present end of the filter
# 5. On click apply filter button after selecting checkboxes Dropdown should closed and results shows according to selected filters'''
#
#
# #@allure.title('TC_205: Verify user is able to filter titles by Genres')
# def test_verify_genre_filter_action(browser):
#     film_series = filmSeriesPage(browser)
#     global test, my_comment
#     test = test_case_ids[204]  # 1014
#     my_comment = 'Action Genre Filter is not present / user can not Apply Action Genre Filter'
#     action_movie_tags = film_series.verify_genre_Action_filter()
#     assert (action_movie_tags < 43) & (action_movie_tags > 30), 'Action Filter is not apply'
#     clear_all_total_count = film_series.click_clear_all_filter()
#     assert clear_all_total_count == total_movies_series, 'Clear All is not working'
#     my_comment = '''User should be able to filter titles by Genres by selecting the Genre from the drop-down
#                     Search Result should show titles which has the selected Genres'''
#
#
# #@allure.title('TC_206: Verify user is able to apply multiple Genres filters')
# def test_verify_genre_multiple_filter_action_adventure(browser):
#     film_series = filmSeriesPage(browser)
#     global test, my_comment
#     test = test_case_ids[205]  # 1015
#     my_comment = 'multiple Genre filter are not apply'
#     action_adventure_movies = film_series.verify_genre_action_adventure_filter()
#     assert total_movies_series > action_adventure_movies, 'multiple Genre filter are not apply'
#     clear_all_total_count = film_series.click_clear_all_filter()
#     assert clear_all_total_count == total_movies_series, 'Clear All is not working'
#     my_comment = '''User should be able to select multiple genres
#                     Search results should show only those titles which has both Genres'''
#
#
# #@allure.title('TC_207: Verify apply filter button is clickable')
# def test_verify_genre_filter_apply_action_text(browser):
#     film_series = filmSeriesPage(browser)
#     global test, my_comment
#     test = test_case_ids[206]  # 1016
#     my_comment = 'Action Genre Filter is not present / user can not Apply Action Genre Filter'
#     action_movie_tags = film_series.verify_genre_Action_filter()
#     assert (action_movie_tags < 43) & (action_movie_tags > 30), 'Action Filter is not apply'
#     action_filter = film_series.verify_genre_Action_filter_applied()
#     assert action_filter == True, 'Action Text is not present in Result Section'
#     clear_all_total_count = film_series.click_clear_all_filter()
#     assert clear_all_total_count == total_movies_series, 'Clear All is not working'
#     my_comment = 'Apply filter button should be clickable , After clicking it should shows the titles' \
#                  ' which has the selected checkboxes'
#
#
# #@allure.title('TC_208:Verify Rating filter functionality')
# def test_verify_rating_filter(browser):
#     film_series = filmSeriesPage(browser)
#     global test, my_comment
#     test = test_case_ids[207]  # 1017
#     my_comment = 'Rating Filter NC17 is present / Rating Filter NC17 is not Apply '
#     action_movie_tags = film_series.verify_rating_NC17_filter()
#     assert (action_movie_tags > 0) & (total_movies_series > action_movie_tags), 'Rating Filter is not Apply'
#     clear_all_total_count = film_series.click_clear_all_filter()
#     assert clear_all_total_count == total_movies_series, 'Clear All is not working'
#     my_comment = '''1. On click Rating filter a dropdown should opened
#                     2. There should be Checkboxes and Ratings name
#                     3. We can select one or multiple checkboxes at a time
#                     4. Apply filter button should present end of the filter
#                     5. On click apply filter button after selecting checkboxes Dropdown should close
#                      and results shows according to selected filters'''
#
#
# #@allure.title('TC_209: Verify user is able to filter titles by Rating')
# def test_verify_rating_filter_N17(browser):
#     film_series = filmSeriesPage(browser)
#     global test, my_comment
#     test = test_case_ids[208]  # 1018
#     my_comment = 'Rating Filter NC17 is present / Rating Filter NC17 is not Apply '
#     action_movie_tags = film_series.verify_rating_NC17_filter()
#     assert (action_movie_tags > 0) & (total_movies_series > action_movie_tags)
#     nc_17 = film_series.verify_genre_nc_17_filter_applied()
#     assert nc_17 == True, 'Rating Filter NC-17 is not Applied'
#     clear_all_total_count = film_series.click_clear_all_filter()
#     assert clear_all_total_count == total_movies_series, 'Clear All is not working'
#     my_comment = '''User should be able to filter titles by Rating by selecting the Rating from the drop-down
#                     Search Result should show titles which has the selected Rating'''
#
#
# #@allure.title('TC_210: Verify user is able to apply multiple Rating filters')
# def test_verify_multiple_rating_filter(browser):
#     film_series = filmSeriesPage(browser)
#     global test, my_comment
#     test = test_case_ids[209]  # 1019
#     my_comment = 'Multiple Rating Filters are not apply'
#     multiple_movies = film_series.verify_rating_NC17_TvMa_multiple_filter()
#     assert (multiple_movies > 0) & (total_movies_series > multiple_movies)
#     clear_all_total_count = film_series.click_clear_all_filter()
#     assert clear_all_total_count == total_movies_series, 'Clear All is not working'
#     my_comment = '''User should be able to select multiple rating
#                     Search results should show all titles which have the selected rating'''
#
#
# #@allure.title('TC_211: Verify apply filter button is clickable')
# def test_verify_rating_filter_apply_button(browser):
#     film_series = filmSeriesPage(browser)
#     global test, my_comment
#     test = test_case_ids[210]  # 1020
#     my_comment = 'Rating Filter NC17 is present / Rating Filter NC17 is not Apply '
#     action_movie_tags = film_series.verify_rating_NC17_filter()
#     assert (action_movie_tags > 0) & (total_movies_series > action_movie_tags)
#     clear_all_total_count = film_series.click_clear_all_filter()
#     assert clear_all_total_count == total_movies_series, 'Clear All is not working'
#     my_comment = 'Apply filter button should be clickable , After clicking it should ' \
#                  'shows the titles which has the selected checkboxes'
#
#
# #@allure.title('TC_212: Verify user is able to filter titles by Year')
# def test_verify_year_filter(browser):
#     film_series = filmSeriesPage(browser)
#     global test, my_comment
#     test = test_case_ids[211]  # 1021
#     my_comment = 'User can not automate titles by Year'
#     year_filter_movies = film_series.verify_year_filter()
#     assert total_movies_series > year_filter_movies, 'user can not automate titles by Year'
#     clear_all_total_count = film_series.click_clear_all_filter()
#     assert clear_all_total_count == total_movies_series, 'Clear All is not working'
#     my_comment = 'User should be able to filter titles by Year by selecting the year range ' \
#                  'Search Result should show titles which were released in the selected year range'
#
#
# #@allure.title('TC_213: Verify user is able to filter with combination of Genre,Rating&Year filters ')
# def test_verify_combination_genre_rating_year(browser):
#     film_series = filmSeriesPage(browser)
#     global test, my_comment
#     test = test_case_ids[212]  # 1022
#     my_comment = 'user is not able to apply filter with combination of Genre,Rating&Year filters'
#     action_movie_tags = film_series.verify_genre_Action_filter()
#     assert (action_movie_tags < 43) & (action_movie_tags > 30), 'Action Filter is not apply'
#     film_series.verify_rating_TvMa_single_filter()
#     year_filter_movies = film_series.verify_year_filter()
#     assert total_movies_series > year_filter_movies
#     clear_all_total_count = film_series.click_clear_all_filter()
#     assert clear_all_total_count == total_movies_series, 'Clear All is not working'
#     my_comment = 'user should be able to filter titles with combination of Genre,Rating & Year filters'
#
#
# #@allure.title('TC_214: Verify year filter functionality')
# def test_verify_year_functionality(browser):
#     film_series = filmSeriesPage(browser)
#     global test, my_comment
#     test = test_case_ids[213]  # 1023
#     my_comment = 'User can not automate titles by Year'
#     year_filter_movies = film_series.verify_year_filter()
#     assert total_movies_series > year_filter_movies
#     clear_all_total_count = film_series.click_clear_all_filter()
#     assert clear_all_total_count == total_movies_series, 'Clear All is not working'
#     my_comment = '''1. On click Year filter a dropdown should be opened
# 2. There should be a range selector for selecting years
# 3, Click on apply filter button after selecting range filter then Dropdown should be
#  closed and results shows according to selected range filter'''
#
#
# #@allure.title('TC_215: Verify Show Advanced Filters button is clickable')
# def test_verify_advance_filter_button(browser):
#     film_series = filmSeriesPage(browser)
#     global test, my_comment
#     test = test_case_ids[214]  # 1024
#     my_comment = 'Advance Filters are not Present / Advance Filters are not Clickable '
#     advance_filter = film_series.verify_advance_filter_button()
#     assert advance_filter == 7, 'Advance Filters are not Present'
#     my_comment = 'Show Advanced Filters button should be clickable and' \
#                  ' after clicking it should be open advanced filters'
#
#
# #@allure.title('TC_216: Verify names of Show Advanced Filters')
# def test_verify_advance_filter_names(browser):
#     film_series = filmSeriesPage(browser)
#     global test, my_comment
#     test = test_case_ids[215]  # 1025
#     my_comment = 'Advance Filter Plot theme is not present'
#     plot_theme = film_series.verify_advance_plot_theme_button()
#     assert plot_theme == True, 'Advance Filter Plot theme is not present'
#     my_comment = 'Advance Filter Community button is not present'
#     community = film_series.verify_advance_community_button()
#     assert community == True, 'Advance Filter Community button is not present'
#     my_comment = 'Advance Filter Holiday button is not present'
#     holiday = film_series.verify_advance_holiday_button()
#     assert holiday == True, 'Advance Filter Holiday button is not present'
#     my_comment = 'Advance Filter based on button is not present'
#     based_on = film_series.verify_advance_based_on_button()
#     assert based_on == True, 'Advance Filter based on button is not present'
#     my_comment = 'Advance Filter Setting Region is not present'
#     setting_region = film_series.verify_advance_setting_region_button()
#     assert setting_region == True, 'Advance Filter Setting Region is not present'
#     my_comment = 'Advance Filter time period is not present'
#     time_period = film_series.verify_advance_time_period_button()
#     assert time_period == True, 'Advance Filter time period is not present'
#     my_comment = '''Show Advanced Filter have following names:-
# 1.Plot Theme Filter
# 2. Setting Region Filter
# 3. Time period Filter
# 4. Holiday filter
# 5. Community Filter
# 6. Based on filter'''
#
#
# #@allure.title('TC_217: Verify Elements of Show Advanced Filters')
# def test_verify_advance_filter_elements(browser):
#     film_series = filmSeriesPage(browser)
#     global test, my_comment
#     test = test_case_ids[216]  # 1026
#     my_comment = 'Checkbox text is not present in Advance Filter'
#     film_series.click_advance_plot_theme_button()
#     agent_text = film_series.verify_plot_theme_agent()
#     assert agent_text == True, 'Agent Text is not present'
#     my_comment = 'Apply Filter is not present in Advance Filter'
#     apply_filter_button = film_series.verify_apply_filter_button()
#     assert apply_filter_button == True, 'Apply-Filter button is not present'
#     my_comment = '''Show Advanced Filter have following Elements:-
# 1. Dropdown
# 2. Vertical scroller
# 3. Apply Filter Button'''
#
#
# #@allure.title('TC_218: Verify user is able to filter titles by plot theme ')
# def test_verify_advance_plot_theme(browser):
#     film_series = filmSeriesPage(browser)
#     global test, my_comment
#     test = test_case_ids[217]  # 1027
#     my_comment = 'Plot Theme is not Present / plot theme not apply '
#     film_series.click_plot_theme_agent()
#     film_series.click_apply_filter_button()
#     search_text = film_series.verify_agent_spies_search()
#     assert search_text == True, 'Plot-Theme search result is not working'
#     clear_all_total_count = film_series.click_clear_all_filter()
#     assert clear_all_total_count == total_movies_series, 'Clear All is not working'
#     my_comment = '''User should be able to filter titles by Plot Theme by selecting the Plot theme from the drop-down
# Search Result should show titles which has the selected Plot theme'''
#
#
# #@allure.title('TC_219: Verify user is able to click on apply filter button')
# def test_verify_plot_theme_search_result(browser):
#     film_series = filmSeriesPage(browser)
#     global test, my_comment
#     test = test_case_ids[218]  # 1028
#     my_comment = 'Plot Theme is not Present / plot theme not apply '
#     film_series.click_advance_plot_theme_button()
#     film_series.click_plot_theme_agent()
#     film_series.click_apply_filter_button()
#     search_text = film_series.verify_agent_spies_search()
#     assert search_text == True, 'Plot-Theme search result is not working'
#     clear_all_total_count = film_series.click_clear_all_filter()
#     assert clear_all_total_count == total_movies_series, 'Clear All is not working'
#     my_comment = '''User should be able to click on apply filter button ,After clicking Result should show titles which
#                     has the selected Plot theme'''
#
#
# #@allure.title('TC_220: Verify user is able to apply multiple plot theme filters')
# def test_verify_multiple_plot_theme_(browser):
#     film_series = filmSeriesPage(browser)
#     global test, my_comment
#     test = test_case_ids[219]  # 1029
#     my_comment = 'multiple Advance Plot theme button is not apply'
#     film_series.click_advance_plot_theme_button()
#     film_series.click_plot_theme_agent()
#     film_series.click_plot_theme_aliens()
#     film_series.click_apply_filter_button()
#     my_comment = 'Agent and Spies text is not present in search Result'
#     search_text = film_series.verify_agent_spies_search()
#     assert search_text == True, 'Agent and Spies text is not present in search Result'
#     alien_text = film_series.verify_aliens_search()
#     assert alien_text == True, 'Alien Text is not present in Search Result '
#     clear_all_total_count = film_series.click_clear_all_filter()
#     assert clear_all_total_count == total_movies_series, 'Clear All is not working'
#     my_comment = 'User should be able to select multiple plot theme ' \
#                  'Search results should show all titles which have the selected plot theme'
#
#
# #@allure.title('TC_221: Verify user is able to filter titles by Setting Region')
# def test_verify_setting_region(browser):
#     film_series = filmSeriesPage(browser)
#     global test, my_comment
#     test = test_case_ids[220]  # 1030
#     my_comment = 'Setting Region Filter is not present / Setting Region Filter not applied'
#     film_series.click_advance_setting_region_button()
#     film_series.click_setting_region_africa_middel_east()
#     film_series.click_apply_filter_button_setting_region()
#     search_result = film_series.verify_setting_region_africa_middle_east_search_result()
#     my_comment = 'Africa and Middle-East text is not present in search Result / Search Result is not Correct'
#     assert search_result == True, 'Africa and Middle-East text is not present in search Result'
#     film_series.click_clear_cross_setting_region_africa()
#     my_comment = '''User should be able to filter titles by Setting Region by
#                     selecting the Setting Region from the drop-down
#                     Search Result should show titles which has the selected Setting Region'''
#
#
# #@allure.title('TC_222: Verify user is able to click on apply filter button ')
# def test_verify_setting_region_apply_filter_button(browser):
#     film_series = filmSeriesPage(browser)
#     global test, my_comment
#     test = test_case_ids[221]  # 1031
#     my_comment = "Setting Region Filter is not present / Setting Region Filter not applied"
#     film_series.click_advance_setting_region_button()
#     film_series.click_setting_region_africa_middel_east()
#     film_series.click_apply_filter_button_setting_region()
#     search_result = film_series.verify_setting_region_africa_middle_east_search_result()
#     assert search_result == True, 'Africa and Middle-East text is not present in search Result'
#     film_series.click_clear_cross_setting_region_africa()
#     my_comment = 'User should be able to click on apply filter button ,After clicking Result ' \
#                  'should show titles which has the selected Setting Region'
#
#
# #@allure.title('TC_223: Verify user is able to apply multiple Setting Region filters')
# def test_verify_multiple_setting_region_apply_filter(browser):
#     film_series = filmSeriesPage(browser)
#     global test, my_comment
#     test = test_case_ids[222]  # 1032
#     my_comment = 'Multiple Setting Region Filters is not apply'
#     film_series.click_advance_setting_region_button()
#     film_series.click_setting_region_africa_middel_east()
#     film_series.click_setting_region_arctic_antarctic()
#     film_series.click_apply_filter_button_setting_region()
#     my_comment = 'Africa and Middle-East text is not present in search Result'
#     search_result = film_series.verify_setting_region_africa_middle_east_search_result()
#     assert search_result == True, 'Africa and Middle-East text is not present in search Result'
#     my_comment = 'Antarctic text is not present in search Result'
#     search_result_antarctic = film_series.verify_setting_region_antarctic_search_result()
#     assert search_result_antarctic == True, 'Antarctic text is not present in search Result'
#     clear_all_total_count = film_series.click_clear_all_filter()
#     assert clear_all_total_count == total_movies_series, 'Clear All is not working'
#     my_comment = '''User should be able to select multiple Setting Region
#                     Search results should show all titles which have the selected Setting Region'''
#
#
# #@allure.title('TC_224: Verify user is able to filter titles by Time Period')
# def test_verify_time_period_filter_button(browser):
#     film_series = filmSeriesPage(browser)
#     global test, my_comment
#     test = test_case_ids[223]  # 1033
#     my_comment = 'Time Period Filter not applied'
#     film_series.click_advance_time_period_button()
#     film_series.click_time_period_medieval()
#     film_series.click_apply_filter_button()
#     my_comment = 'Africa and Middle-East text is not present in search Result/Time Period Search Result is not Correct'
#     search_result = film_series.verify_time_period_medieval_search_result()
#     assert search_result == True, 'Africa and Middle-East text is not present in search Result'
#     clear_all_total_count = film_series.click_clear_all_filter()
#     assert clear_all_total_count == total_movies_series, 'Clear All is not working'
#     my_comment = '''User should be able to filter titles by Time Period by selecting the Time Period from the drop-down
#                     Search Result should show titles which has the selected Time Period'''
#
#
# #@allure.title('TC_225: Verify user is able to click on apply filter button ')
# def test_verify_time_period_apply_filter_button(browser):
#     film_series = filmSeriesPage(browser)
#     global test, my_comment
#     test = test_case_ids[224]  # 1034
#     my_comment = 'Time Period Filter not applied'
#     film_series.click_advance_time_period_button()
#     film_series.click_time_period_medieval()
#     film_series.click_apply_filter_button()
#     my_comment = 'Africa and Middle-East text is not present in search Result/Time Period Search Result is not Correct'
#     search_result = film_series.verify_time_period_medieval_search_result()
#     assert search_result == True, 'Africa and Middle-East text is not present in search Result'
#     clear_all_total_count = film_series.click_clear_all_filter()
#     assert clear_all_total_count == total_movies_series, 'Clear All is not working'
#     my_comment = 'User should be able to click on apply filter button ,After clicking Result should show ' \
#                  'titles which has the selected Time Period'
#
#
# #@allure.title('TC_226: Verify user is able to apply multiple Time Period filters')
# def test_verify_multiple_time_period_apply_filter_button(browser):
#     film_series = filmSeriesPage(browser)
#     global test, my_comment
#     test = test_case_ids[225]  # 1035
#     my_comment = 'Multiple Time Period Filter not applied'
#     film_series.click_advance_time_period_button()
#     film_series.click_time_period_medieval()
#     film_series.click_time_period_prehistory()
#     film_series.click_apply_filter_button()
#     my_comment = 'Africa and Middle-East text is not present in search Result/Time Period Search Result is not Correct'
#     search_result = film_series.verify_time_period_medieval_search_result()
#     assert search_result == True, 'Africa and Middle-East text is not present in search Result'
#     prehistory_text = film_series.verify_time_period_prehistory_search_result()
#     assert prehistory_text == True, 'Prehistory text is not present in search Result'
#     clear_all_total_count = film_series.click_clear_all_filter()
#     assert clear_all_total_count == total_movies_series, 'Clear All is not working'
#     my_comment = '''User should be able to select multiple Time Period
#                     Search results should show all titles which have the selected Time Period'''
#
#
# #@allure.title('TC_227: Verify user is able to filter titles by Holiday')
# def test_verify_holiday_filter_button(browser):
#     film_series = filmSeriesPage(browser)
#     global test, my_comment
#     test = test_case_ids[226]  # 1036
#     my_comment = 'Holiday filter titles not applied'
#     film_series.click_advance_holiday_button()
#     film_series.click_holiday_christmas()
#     film_series.click_apply_filter_button()
#     my_comment = 'Christmas text is not present in search Result / Holiday Filter Result is not correct '
#     christmas_text = film_series.verify_holiday_christmas_search_result()
#     assert christmas_text == True, 'Christmas text is not present in search Result'
#     clear_all_total_count = film_series.click_clear_all_filter()
#     assert clear_all_total_count == total_movies_series, 'Clear All is not working'
#     my_comment = '''User should be able to filter titles by Holiday by selecting the Holiday from the drop-down
#                     Search Result should show titles which has the selected Holiday'''
#
#
# #@allure.title('TC_228: Verify user is able to click on apply filter button ')
# def test_verify_holiday_apply_filter_button(browser):
#     film_series = filmSeriesPage(browser)
#     global test, my_comment
#     test = test_case_ids[227]  # 1037
#     my_comment = 'Holiday filter titles not applied'
#     film_series.click_advance_holiday_button()
#     film_series.click_holiday_christmas()
#     film_series.click_apply_filter_button()
#     my_comment = 'Christmas text is not present in search Result / Holiday Filter Result is not correct '
#     christmas_text = film_series.verify_holiday_christmas_search_result()
#     assert christmas_text == True, 'Christmas text is not present in search Result'
#     clear_all_total_count = film_series.click_clear_all_filter()
#     assert clear_all_total_count == total_movies_series, 'Clear All is not working'
#     my_comment = 'User should be able to click on apply filter button ' \
#                  ',After clicking Result should show titles which has the selected Holiday'
#
#
# #@allure.title('TC_229: Verify user is able to click on apply filter button ')
# def test_verify_multiple_holiday_filter(browser):
#     film_series = filmSeriesPage(browser)
#     global test, my_comment
#     test = test_case_ids[228]  # 1038
#     my_comment = 'Holiday filter titles not applied'
#     film_series.click_advance_holiday_button()
#     film_series.click_holiday_christmas()
#     film_series.click_holiday_easter()
#     film_series.click_apply_filter_button()
#     my_comment = 'Christmas text is not present in search Result / Holiday Filter Result is not correct '
#     christmas_text = film_series.verify_holiday_christmas_search_result()
#     assert christmas_text == True, 'Christmas text is not present in search Result'
#     easter_text = film_series.verify_holiday_easter_search_result()
#     assert easter_text == True, 'Easter text is not present in search result'
#     clear_all_total_count = film_series.click_clear_all_filter()
#     assert clear_all_total_count == total_movies_series, 'Clear All is not working'
#     my_comment = 'User should be able to select multiple Holiday Search results should ' \
#                  'show all titles which have the selected Holiday'
#
#
# #@allure.title('TC_230: Verify user is able to filter titles by Community')
# def test_verify_community_filter_button(browser):
#     film_series = filmSeriesPage(browser)
#     global test, my_comment
#     test = test_case_ids[229]  # 1039
#     my_comment = 'Community Filter not applied'
#     film_series.click_advance_community_button()
#     film_series.click_community_black_african()
#     film_series.click_apply_filter_button()
#     my_comment = 'Black American African text is present in search result / Community Filter result is not correct '
#     community_black_text = film_series.verify_community_black_search_result()
#     assert community_black_text == True, 'Black American African text is present in search result'
#     clear_all_total_count = film_series.click_clear_all_filter()
#     assert clear_all_total_count == total_movies_series, 'Clear All is not working'
#     my_comment = '''User should be able to filter titles by Community by selecting the Community from the drop-down
#                     Search Result should show titles which has the selected Community'''
#
#
# #@allure.title('TC_231: Verify user is able to click on apply filter button ')
# def test_verify_apply_community_filter_button(browser):
#     film_series = filmSeriesPage(browser)
#     global test, my_comment
#     test = test_case_ids[230]  # 1040
#     my_comment = 'Community Filter not applied'
#     film_series.click_advance_community_button()
#     film_series.click_community_black_african()
#     film_series.click_apply_filter_button()
#     my_comment = 'Black American African text is present in search result / Community Filter result is not correct '
#     community_black_text = film_series.verify_community_black_search_result()
#     assert community_black_text == True, 'Black American African text is present in search result'
#     clear_all_total_count = film_series.click_clear_all_filter()
#     assert clear_all_total_count == total_movies_series, 'Clear All is not working'
#     my_comment = 'User should be able to click on apply filter button ' \
#                  ',After clicking Result should show titles which has the selected Community'
#
#
# #@allure.title('TC_232: Verify user is able to apply multiple Community filters ')
# def test_verify_multiple_community_filter_button(browser):
#     film_series = filmSeriesPage(browser)
#     global test, my_comment
#     test = test_case_ids[231]  # 1041
#     my_comment = 'Multiple Community filters  not applied'
#     film_series.click_advance_community_button()
#     film_series.click_community_black_african()
#     film_series.click_community_latinx()
#     film_series.click_apply_filter_button()
#     my_comment = 'Black American African text is present in search result / Filter Result is not Correct'
#     community_black_text = film_series.verify_community_black_search_result()
#     assert community_black_text == True, 'Black American African text is present in search result'
#     community_latinx_text = film_series.verify_community_latinx_search_result()
#     assert community_latinx_text == True, 'Latinx text is not present in search result'
#     clear_all_total_count = film_series.click_clear_all_filter()
#     assert clear_all_total_count == total_movies_series, 'Clear All is not working'
#     my_comment = '''User should be able to select multiple Community
#                     Search results should show all titles which have the selected Community'''
#
#
# #@allure.title('TC_233: Verify user is able to filter titles by Bases On')
# def test_verify_based_on_filter_button(browser):
#     film_series = filmSeriesPage(browser)
#     global test, my_comment
#     test = test_case_ids[232]  # 1042
#     my_comment = 'Bases on Novel Filter title not Applied '
#     film_series.click_advance_based_on_button()
#     film_series.click_based_on_novel_story()
#     film_series.click_apply_filter_button()
#     my_comment = 'Novel text is present in search result/ filter Result is not correct'
#     novel_story_text = film_series.verify_based_novel_story_search_result()
#     assert novel_story_text == True, 'Novel text is present in search result'
#     clear_all_total_count = film_series.click_clear_all_filter()
#     assert clear_all_total_count == total_movies_series, 'Clear All is not working'
#     my_comment = '''User should be able to filter titles by Bases On by selecting the Bases On from the drop-down
#                     Search Result should show titles which has the selected Bases On'''
#
#
# #@allure.title('TC_234: Verify user is able to click on apply filter button ')
# def test_verify_based_on_apply_filter_button(browser):
#     film_series = filmSeriesPage(browser)
#     global test, my_comment
#     test = test_case_ids[233]  # 1043
#     my_comment = 'Bases on Novel Filter title not Applied '
#     film_series.click_advance_based_on_button()
#     film_series.click_based_on_novel_story()
#     film_series.click_apply_filter_button()
#     my_comment = 'Novel text is present in search result/ filter Result is not correct'
#     novel_story_text = film_series.verify_based_novel_story_search_result()
#     assert novel_story_text == True, 'Bases on Novel text is present in search result'
#     clear_all_total_count = film_series.click_clear_all_filter()
#     assert clear_all_total_count == total_movies_series, 'Clear All is not working'
#     my_comment = 'User should be able to click on apply filter button ,' \
#                  'After clicking Result should show titles which has the selected Bases On'
#
#
# #@allure.title('TC_235: Verify user is able to apply multiple Bases On filters')
# def test_verify_multiple_based_on_apply_filter_button(browser):
#     film_series = filmSeriesPage(browser)
#     global test, my_comment
#     test = test_case_ids[234]  # 1044
#     my_comment = 'multiple Filters based on not applied'
#     film_series.click_advance_based_on_button()
#     film_series.click_based_on_novel_story()
#     film_series.click_based_on_real_people()
#     film_series.click_apply_filter_button()
#     my_comment = 'Novel or Real people text is present in search result/ filter Result is not correct'
#     novel_story_text = film_series.verify_based_novel_story_search_result()
#     assert novel_story_text == True, 'novel text is present in search result'
#     real_people_text = film_series.verify_based_real_people_search_result()
#     assert real_people_text == True, 'Real people text is not present in list section'
#     clear_all_total_count = film_series.click_clear_all_filter()
#     assert clear_all_total_count == total_movies_series, 'Clear All is not working'
#     my_comment = 'User should be able to select multiple Bases On Search results should' \
#                  ' show all titles which have the selected Bases On'
#
#
# #@allure.title('TC_236: Verify filter chips functionality')
# def test_verify_filter_chips_functionality(browser):
#     film_series = filmSeriesPage(browser)
#     global test, my_comment
#     test = test_case_ids[236]  # 1046
#     my_comment = 'Multiple filters are not applied'
#     film_series.click_advance_setting_region_button()
#     film_series.click_setting_region_africa_middel_east()
#     film_series.click_apply_filter_button_setting_region()
#     my_comment = 'Filter Results are not Correct'
#     search_result = film_series.verify_setting_region_africa_middle_east_search_result()
#     assert search_result == True, 'Africa and Middle-East text is not present in search Result'
#     before_click = film_series.click_filter_chips_setting_region_africa()
#     assert before_click == True, 'Filter chips is not clickable'
#     after_click = film_series.verify_filter_chips_clickable()
#     assert after_click == False, 'Filter chips is not Removed after on click'
#     my_comment = 'User should be able to click on Hide advanced filters, After clicking advanced filters should be hide'
#
#
# #@allure.title('TC_237: Verify user is able to click on Hide advanced filters')
# def test_verify_advance_filter_hide_button(browser):
#     film_series = filmSeriesPage(browser)
#     global test, my_comment
#     test = test_case_ids[235]  # 1045
#     my_comment = 'user is not able to click on Hide advanced filter button'
#     advance_filter = film_series.verify_hide_advance_filter_button()
#     assert advance_filter == True, 'user is not able to click on Hide advanced filter button'
#     my_comment = '''1 On click cross button chips should be deleted and this filter is also unchecked from filters
#                     2. On click clear all button all the chips should removed and all the selected checboxes are unchecked'''
#
#
# #@allure.title('TC_238: Verify user is able to switch between grid view and list view')
# def test_verify_list_button_functionality(browser):
#     film_series = filmSeriesPage(browser)
#     global test, my_comment
#     home = homepage(browser)
#     test = test_case_ids[237]  # 1047
#     home.gotohomepage(_url_)
#     movies = home.ClickFilmsSeries()
#     assert movies == True, "Not redirecting to correct page"
#     my_comment = 'List Button is not Clickable'
#     table_head = film_series.verify_list_button()
#     assert table_head == True, 'List Button is not Clickable'
#     my_comment = 'On click of the view button, view should change in respect to the button clicked'
#
#
# #@allure.title('TC_239: Verify List view')
# def test_verify_list_tabular_structure(browser):
#     film_series = filmSeriesPage(browser)
#     global test, my_comment
#     test = test_case_ids[238]  # 1048
#     my_comment = 'Heading Title is not present'
#     list_title = film_series.verify_list_title()
#     assert list_title == True, 'Heading Title is not present'
#     my_comment = 'Directed By heading is not present'
#     directed_by = film_series.verify_list_directed_by()
#     assert directed_by == True, 'Directed By heading is not present'
#     my_comment = 'Main-Cast heading is not present'
#     main_cast = film_series.verify_list_main_cast()
#     assert main_cast == True, 'Main-Cast heading is not present'
#     my_comment = 'Synopsis heading is not present'
#     synopsis_text = film_series.verify_list_synopsis()
#     assert synopsis_text == True, 'Synopsis heading is not present'
#     my_comment = '''List view should show tabular structure with following columns
# 1. Title
# 2. Directed By
# 3. Main Cast
# 4. Synopsis
# '''
#
#
# #@allure.title('TC_240: Verify the options of Sorting and their functionality')
# def test_verify_sorting_filter(browser):
#     film_series = filmSeriesPage(browser)
#     global test, my_comment
#     test = test_case_ids[239]  # 1049
#     my_comment = 'Sorting functionality are  not working'
#     film_series.verify_sorting_button()
#     after_sort = film_series.verify_sorting_a_to_z()
#     assert total_movies_series == after_sort, 'Sorting are not completed'
#     film_series.verify_sorting_button()
#     after_sort = film_series.verify_sorting_z_to_a()
#     assert total_movies_series == after_sort, 'Sorting are not completed'
#     film_series.verify_sorting_button()
#     after_sort = film_series.verify_sorting_down_apply()
#     assert total_movies_series == after_sort, 'Sorting are not completed'
#     film_series.verify_sorting_button()
#     after_sort = film_series.verify_sorting_up()
#     assert total_movies_series == after_sort, 'Sorting are not completed'
#     my_comment = '''Sorting drop down should have the following options with mentioned behaviour
# 1. Release Date (Old to New) -- Titles should be ordered in Decending order of Release Date
# 2. Release Date (New to Old) -- Titles should be ordered in Ascending order of Release Date
# 3. Sort A-Z  -- Titles should be ordered in Ascending order of Alphabets
# 4. Sort Z-A -- Titles should be ordered in Descending order of Alphabets
# '''
#
#
# #@allure.title('TC_241: Verify user is able to see correct total result counts')
# def test_verify_sorting_filter_to_see_result(browser):
#     film_series = filmSeriesPage(browser)
#     global test, my_comment
#     test = test_case_ids[240]  # 1050
#     my_comment = 'total result count is not present'
#     result_count = film_series.verify_total_count_text()
#     assert result_count == total_movies_series, 'total result count is not present'
#     my_comment = 'user should able to see correct results found'
#
#
# #@allure.title('TC_242: Verify user is able to select all the Titles on click select all checkbox')
# def test_verify_select_all_checkbox_movie_and_series(browser):
#     film_series = filmSeriesPage(browser)
#     global test, my_comment
#     test = test_case_ids[241]  # 1051
#     my_comment = 'All movies are not selected'
#     all_text_footer = film_series.verify_select_all()
#     assert '42' in all_text_footer, 'All movies are not selected'
#     my_comment = 'User should be able to select all titles on clicking select all checkbox'
#
#
# #@allure.title('TC_243: Verify the elements of cards')
# def test_verify_film_and_series_cards_all_element(browser):
#     home = homepage(browser)
#     film_series = filmSeriesPage(browser)
#     global test, my_comment
#     test = test_case_ids[242]  # 1052
#     my_comment = 'Not redirecting to Film & Series page'
#     film_series.visit_home_url(_url_)
#     movies = home.ClickFilmsSeries()
#     assert movies == True, "Not redirecting to Film & Series page"
#     my_comment = 'Poster image is not present in movie card'
#     card_poster = film_series.verify_first_card_poster()
#     assert card_poster == True, 'Poster image is not present in movie card'
#     my_comment = 'Title text is not present in movie card'
#     card_title = film_series.verify_first_card_title()
#     assert card_title == True, 'Title text is not present in movie card'
#     my_comment = 'Genre Title is not present in movie card'
#     card_genre = film_series.verify_first_card_genre()
#     assert card_genre == True, 'Genre Title is not present in movie card'
#     film_series.mouse_hover_on_movie()
#     my_comment = 'add to list is not visible'
#     add_to_list = film_series.mouse_hover_on_add_to_list()
#     assert add_to_list == True, 'add to list is not visible'
#     my_comment = 'watch now is not visible'
#     watch_now = film_series.mouse_hover_on_Watch_now()
#     assert watch_now == True, 'watch now is not visible'
#     watch_trailer = film_series.mouse_hover_on_watch_trailer()
#     my_comment = 'watch trailer is not visible'
#     assert watch_trailer == True, 'watch trailer is not visible'
#     my_comment = 'view details is not visible'
#     view_details = film_series.mouse_hover_on_view_details()
#     assert view_details == True, 'view details is not visible'
#     my_comment = '''Cards have following elements
#
# 1. Card with Title image
# 2. Tile name
# 3. Genre of title
# 4.Add to list button
# 5. watch now button[Only in case of Movie entity]
# 6. watch trailer button
# 7. view details button'''
#
#
# #@allure.title('TC_244: Verify global header Films & series tab is highlited or not')
# def test_verify_film_and_series_underline(browser):
#     film_series = filmSeriesPage(browser)
#     global test, my_comment
#     test = test_case_ids[243]  # 1053
#     my_comment = 'underline is not present'
#     my_list_active = film_series.verify_film_and_series_Active()
#     assert 'active' in my_list_active, 'underline is not present'
#     my_comment = 'When we are on  Films & series page then  Films & series tab should be underlined on Global header'
#
#
# #@allure.title('TC_245: Verify user is able to play movie by clicking Watch Movie button')
# def test_click_grid_view_watch_now_button(browser):
#     film_series = filmSeriesPage(browser)
#     video_player = videoplayer(browser)
#     global test, my_comment
#     test = test_case_ids[244]  # 1054
#     my_comment = 'video player is not working'
#     film_series.mouse_hover_on_movie()
#     film_series.click_on_watch_now_button()
#     zoomInOut_button = video_player.zoomINButton()
#     assert zoomInOut_button == True, 'video player is not working'
#     # video_player.MovieAlreadyPlayed()
#     video_player.ClickCloseButton()
#     my_comment = 'Movie should be played in the player pop up on click of Watch Movie button'
#
#
# #@allure.title('TC_246: Verify user is able to play trailer by clicking Watch Trailer button')
# def test_click_grid_view_watch_trailer_button(browser):
#     video_player = videoplayer(browser)
#     film_series = filmSeriesPage(browser)
#     global test, my_comment
#     test = test_case_ids[245]  # 1055
#     my_comment = 'watch trailer is not visible'
#     film_series.mouse_hover_on_movie()
#     film_series.click_on_watch_trailer()
#     zoomInOut_button = video_player.zoomINButton()
#     assert zoomInOut_button == True, 'video player is not working'
#     video_player.ClickCloseButton()
#     my_comment = 'Movie Trailer should be played in the player pop up on click of Watch Trailer button'
#
#
# #@allure.title('TC_247: Verify user is able to reach details page by clicking View Details button')
# def test_click_grid_view_details_button(browser):
#     home = homepage(browser)
#     film_series = filmSeriesPage(browser)
#     global test, my_comment
#     test = test_case_ids[246]  # 1056
#     my_comment = 'Movies page is not open'
#     film_series.mouse_hover_on_movie()
#     create_new_list = film_series.click_on_view_details()
#     assert create_new_list == True, 'Movies page is not open'
#     my_comment = 'User should be redirected to Movie/TV details page of that title'
#
#
# #@allure.title('TC_248: Verify user is able to add the title in a list by clicking add to list')
# def test_click_grid_view_add_to_list_button(browser):
#     home = homepage(browser)
#     film_series = filmSeriesPage(browser)
#     global test, my_comment
#     test = test_case_ids[247]  # 1057
#     my_comment = 'Not redirecting to Film & Series page'
#     movies = home.ClickFilmsSeries()
#     assert movies == True, "Not redirecting to correct page"
#     film_series.mouse_hover_on_movie()
#     my_comment = 'Add to list button is not Clickable / Add to list popup is not present'
#     film_series.click_on_add_to_list()
#     home.SearchList("MoviesList")
#     select = home.MovieCardVerifySelectUnselectListMyListMovies()
#     assert select == True
#     home.AddMovieToList()
#     assert home.verify_success_text() == True, "Success message is not showing after adding title into list"
#     my_comment = '''On click of Add to List button, Add to list pop up should open
# User should be able to select any list or create a list from the pop up
# On click of Add to List button after selecting list(s), the title should get added in the selected list(s)'''
#
#
# #@allure.title('TC_249: Verify on click of Title name redirects to Title details page')
# def test_click_grid_title(browser):
#     film_series = filmSeriesPage(browser)
#     global test, my_comment
#     test = test_case_ids[248]  # 1058
#     my_comment = 'List Button is not Clickable'
#     table_head = film_series.verify_list_button()
#     assert table_head == True, 'List Button is not Clickable'
#     my_comment = 'Title detail page is not open'
#     title_text = film_series.click_grid_title()
#     assert title_text == True, 'Title detail page is not open'
#     my_comment = 'On click of Title name in list view it should take user to title details page of that title'
#
#
# #@allure.title('TC_250: Verify one sheet overlay is present on the movie cards in the grid view and all buttons are '
#               # 'visible on hover')
# def test_verify_grid_mouse_hover(browser):
#     home = homepage(browser)
#     film_series = filmSeriesPage(browser)
#     global test, my_comment
#     test = test_case_ids[249]  # 1059
#     my_comment = 'Not redirecting to Film & Series page'
#     film_series.visit_home_url(_url_)
#     movies = home.ClickFilmsSeries()
#     assert movies == True, "Not redirecting to correct page"
#     my_comment = 'Poster image is not present in movie card'
#     card_poster = film_series.verify_first_card_poster()
#     assert card_poster == True, 'Poster image is not present in movie card'
#     my_comment = 'Title text is not present in movie card'
#     card_title = film_series.verify_first_card_title()
#     assert card_title == True, 'Title text is not present in movie card'
#     my_comment = 'Genre Title is not present in movie card'
#     card_genre = film_series.verify_first_card_genre()
#     assert card_genre == True, 'Genre Title is not present in movie card'
#     film_series.mouse_hover_on_movie()
#     my_comment = 'add to list is not visible'
#     add_to_list = film_series.mouse_hover_on_add_to_list()
#     assert add_to_list == True, 'add to list is not visible'
#     my_comment = 'watch now is not visible'
#     watch_now = film_series.mouse_hover_on_Watch_now()
#     assert watch_now == True, 'watch now is not visible'
#     my_comment = 'watch trailer is not visible'
#     watch_trailer = film_series.mouse_hover_on_watch_trailer()
#     assert watch_trailer == True, 'watch trailer is not visible'
#     my_comment = 'view details is not visible'
#     view_details = film_series.mouse_hover_on_view_details()
#     assert view_details == True, 'view details is not visible'
#     my_comment = '''One sheet overlay should be present on each movie/tv card
#                     On hover, it should display the following buttons:
#                     1. Add To List
#                     2. Watch Movie [Only in case of Movie entity]
#                     3. Watch Trailer
#                     4. View Details
#                 '''
#
#
# #@allure.title('TC_251: Verify user is able to select single or multiple titles by clicking the checkbox against each  '
#               # 'title in any view')
# def test_verify_grid_first_checkbox_selected(browser):
#     film_series = filmSeriesPage(browser)
#     global test, my_comment
#     test = test_case_ids[250]  # 1060
#     my_comment = 'checkbox is not selected'
#     check_box = film_series.click_first_checkbox()
#     assert check_box == True, 'checkbox is not selected'
#     my_comment = 'User should be able to select single or multiple titles from the list'
#
#
# #@allure.title('TC_252: Verify footer pop up is shown on selecting titles in any view')
# def test_verify_footer_popup_film_and_series(browser):
#     film_series = filmSeriesPage(browser)
#     global test, my_comment
#     test = test_case_ids[251]  # 1061
#     my_comment = 'footer popup is not present'
#     check_box = film_series.verify_footer_popup_for_single_checkbox()
#     assert check_box == True, 'footer popup is not present'
#     my_comment = 'Footer section should be shown on selecting title in any view'
#
#
# #@allure.title('TC_256: verify Elements of footer popup')
# def test_checkbox_footer_popup_film_and_series(browser):
#     footer = homePagemylistsObj(browser)
#     film_series = filmSeriesPage(browser)
#     global test, my_comment
#     test = test_case_ids[255]  # 1065
#     my_comment = 'All movies are not selected'
#     check_box = film_series.verify_footer_popup_for_single_checkbox()
#     assert check_box == True, 'All movies are not selected'
#     my_comment = 'List selected Text is not displaying in footer pop . It should show'
#     assert "Item Selected" in footer.verify_Listtext(), "List selected Text is not displaying in footer pop . It " \
#                                                         "should show."
#     my_comment = 'Download csv is not present there. Download csv button should be displayed in footer popup.'
#     assert footer.verify_downloadCsv() == True, "Download csv is not present there. Download csv button should be " \
#                                                 "displayed in footer popup."
#     my_comment = 'Share List is not present there. Share list button should be displayed in footer popup.'
#     assert footer.verify_shareList() == True, "Share List is not present there. Share list button should be displayed " \
#                                               "in footer popup."
#     my_comment = "Add to list is not present there"
#     assert footer.verify_AddToListFooterpopup() == True, "Add to list is not present there"
#     my_comment = '''Footer popup have following elements:-
# 1.Total selected counts
# 2. Download .XLSX button
# 4. Email spreadsheet button
# 5. Add to list Button'''
#
#
# #@allure.title('TC_257: Verify is user deselect the checkbox footer popup is hide')
# def test_verify_grid_first_checkbox_unselected(browser):
#     film_series = filmSeriesPage(browser)
#     global test, my_comment
#     test = test_case_ids[256]  # 1066
#     my_comment = 'checkbox is selected User is not able to Deselect'
#     check_box = film_series.click_first_checkbox_again()
#     assert check_box == False, 'checkbox is selected User is not able to Deselect'
#     my_comment = 'Footer popup should be hide if user deselect all the checkboxes'
#
#
# #@allure.title('TC_258: Verify Download XLSX button from footer popup')
# def test_verify_download_footer_popup_film_and_series(browser):
#     film_series = filmSeriesPage(browser)
#     footer = homePagemylistsObj(browser)
#     global test, my_comment
#     test = test_case_ids[257]  # 1067
#     my_comment = 'footer popup is not present'
#     check_box = film_series.click_first_checkbox()
#     assert check_box == True, 'footer popup is not present'
#     footer.click_download_csv()
#     my_comment = 'csv file is not Downloading'
#     csv_download = footer.verify_csv_file_downloaded()
#     assert csv_download == False, 'csv file is not Downloading'
#     my_comment = 'On click download xlsx button a csv file should download'
#
#
# #@allure.title('TC_260: Verify email spreadsheet button from footer popup')
# def test_verify_footer_spreadsheet_functionality_film_series(browser):
#     share = myListObj(browser)
#     film_series = filmSeriesPage(browser)
#     global test, my_comment
#     test = test_case_ids[259]  # 1069
#     my_comment = 'footer popup is not present'
#     check_box = film_series.click_first_checkbox()
#     assert check_box == True, 'footer popup is not present'
#     share.click_shareList()
#     share.enter_email(email_address)
#     share.click_add_email_address()
#     my_comment = 'After clicking on share button , confirmation is not showing.'
#     share.click_buttonToshare()
#     assert share.verify_share_list_success() == True, "After clicking on share button , confirmation is not showing."
#     my_comment = 'On click email spreadsheet button a popup should be open and' \
#                  ' user should be able to share list throught this popup'
#
#
# #@allure.title('TC_261: Verify add to list button from footer popup')
# def test_click_footer_add_to_list_film_series(browser):
#     footer = homePagemylistsObj(browser)
#     film_series = filmSeriesPage(browser)
#     global test, my_comment
#     test = test_case_ids[260]  # 1070
#     # time.sleep(60)
#     my_comment = 'footer popup is not present'
#     check_box = film_series.click_first_checkbox()
#     assert check_box == True, 'footer popup is not present'
#     footer.click_add_to_list_footer()
#     my_comment = 'Add to list popup is not open After clicking on add to list from footer'
#     add_to_list_popup = film_series.verify_add_to_list_popup()
#     assert add_to_list_popup == True, 'Add to list popup is not open After clicking on add to list from footer'
#     my_comment = 'On click add to list button add to list popup should open'
#
#
# #@allure.title('TC_262: Verify email spreadsheet popup elements')
# def test_verify_footer_spreadsheet_elements_film_series(browser):
#     share = myListObj(browser)
#     film_series = filmSeriesPage(browser)
#     global test, my_comment
#     test = test_case_ids[261]  # 1071
#     my_comment = 'footer popup is not present'
#     film_series.page_refresh()
#     check_box = film_series.click_first_checkbox()
#     assert check_box == True, 'footer popup is not present'
#     share.click_shareList()
#     my_comment = 'Title text is not present on spreadsheet-popup'
#     title_text = film_series.verify_spreadsheet_title()
#     assert title_text == True, 'Title text is not present on spreadsheet-popup'
#     my_comment = 'Static-Text is not present on spreadsheet-popup'
#     static_text = film_series.verify_spreadsheet_static_text()
#     assert static_text == True, 'Static-Text is not present on spreadsheet-popup'
#     my_comment = 'Email-Input is not present on spreadsheet-popup'
#     input_field = film_series.verify_spreadsheet_email_input_field()
#     assert input_field == True, 'Email-Input is not present on spreadsheet-popup'
#     share_button = film_series.verify_spreadsheet_share_button()
#     my_comment = 'Share button is not present on spreadsheet-popup'
#     assert share_button == True, 'Share button is not present on spreadsheet-popup'
#     my_comment = 'Close button is present on spreadsheet-popup'
#     share_close = film_series.verify_spreadsheet_close_button()
#     assert share_close == True, 'Close button is present on spreadsheet-popup'
#     my_comment = '''Email spreadsheet popup have following elements:-
# 1.Count of total titles should be shared
# 2. Title names
# 3. Static text
# 4. Email field
# 5. Share button
# 6. Close button'''
#
#
# #@allure.title('TC_265: Verify on click of Add to List button, Add List pop up is opened')
# def test_click_add_to_list_film_series(browser):
#     home = homepage(browser)
#     film_series = filmSeriesPage(browser)
#     global test, my_comment
#     test = test_case_ids[264]  # 1074
#     my_comment = 'search box is not present'
#     film_series.page_refresh()
#     film_series.mouse_hover_on_movie()
#     film_series.click_on_add_to_list()
#     search = home.AddToListSearchBox()
#     assert search == True, 'search box is not present'
#     my_comment = 'Clicking on Add to List button for any Title should open the Add to List pop up'
#
#
# #@allure.title('TC_264: Add To List pop')
# def test_verify_add_tolist_popup_elements_film_series(browser):
#     home = homepage(browser)
#     global test, my_comment
#     test = test_case_ids[263]  # 1073
#     my_comment = 'Search box is not present'
#     search = home.AddToListSearchBox()
#     assert search == True, 'search box is not present'
#     my_comment = 'clear box is not present'
#     clear = home.AddToListClearButton()
#     assert clear == True, 'clear box is not present'
#     my_comment = 'created list option is not present'
#     created_list = home.AddToListCreatedList()
#     assert created_list == True, 'created list option is not present'
#     my_comment = 'toggle button is not present'
#     toggel = home.AddToListToggelButton()
#     assert toggel == True, 'toggle button is not present'
#     my_comment = 'create list option is not present'
#     list = home.AddToListCreateList()
#     assert list == True, 'create list option is not present'
#     my_comment = 'list add to list name  is not present'
#     name = home.AddToListListName()
#     assert name == True, 'list add to list name  is not present'
#     my_comment = 'create list button is not present'
#     button = home.AddToListCreateListButton()
#     assert button == True, 'create list button is not present'
#     my_comment = '''Add to List pop up should have the following elements:
# 1. Search box
# 2. Clear [button]
# 3. List of created lists
# 4. Toggle button for list selection against each list name
# 5. Add to List [Button]
# 6. List Name [Text box]
# 7. Create List [Button]'''
#
#
# #@allure.title('TC_266: Verify user is able to enter name and create new list from film and series card')
# def test_create_new_list_from_film_series(browser):
#     home = homepage(browser)
#     global test, my_comment
#     test = test_case_ids[265]  # 1075
#     my_comment = 'Add tp list popup is not Present'
#     home.ListName("filmSeriesList")
#     my_comment = 'Create list button is not Clickable / list name is not unique'
#     home.ClickCreateList()
#     my_comment = 'New list is not Created'
#     created = home.CreatedList()
#     assert created == True, 'New list is not Created'
#     name = home.VerifyFilmSeriesListCreated()
#     assert name == True
#     my_comment = 'New Created list is not Auto selected'
#     list_auto = home.VerifyFilmSeriesAutoSelect()
#     assert list_auto == True, 'New Created list is not Auto selected'
#     my_comment = '''User should be create list by following the below steps:
# 1. Click on Add to List button for any title or footer popup
# 2. Click on List Name
# 3. Enter name
# 4. Click Create List
# Following should also happen along side:
# 1. New List should apppear in the List of Created List
# 2. Clicking Create List button should change the textbox to display "Creating..."
# 3. Success message should be shown in the same textbox "Created"
# 4. New List should get auto selected'''
#
#
# #@allure.title('TC_267: Verify user is able to add the Title in the created list')
# def test_film_series_card_add_movie(browser):
#     home = homepage(browser)
#     global test, my_comment
#     test = test_case_ids[266]  # 1076
#     time.sleep(2)
#     my_comment = 'Success message is not showing .'
#     home.AddMovieToList()
#     assert home.verify_success_text() == True, "Success message is not showing ."
#     my_comment = 'Once the list is created and is auto selected, then' \
#                  ' clicking on add to list button should add the title to the new list'
#
#
# #@allure.title('TC_268: Verify user is able to select list(s)')
# def test_select_list_toggel_button_film_series_page(browser):
#     home = homepage(browser)
#     global test, my_comment
#     test = test_case_ids[267]  # 1077
#     my_comment = 'Toggle button not selected / Toggle button is not Clickable'
#     home.click_movie_card_addToList_filmseries()
#     verify = home.verify_film_series_movie_card_selected()
#     assert verify == True, "Toggle button not selected"
#     my_comment = 'Clicking on the toggle button should select the list Toggle button should get highlighted'
#
#
# #@allure.title('TC_269: Verify user is able to un-select any selected list(s)')
# def test_unselect_selected_list_film_series_page(browser):
#     home = homepage(browser)
#     global test, my_comment
#     test = test_case_ids[268]  # 1078
#     my_comment = 'Toggle button not selected'
#     verify = home.verify_movie_card_unselect_list()
#     assert verify == False, "Toggle button not selected"
#     my_comment = 'Clicking on the toggle button against the selected list(s) should un-select' \
#                  ' the list(s) Toggle button should get highlighted'
#
#
# #@allure.title('TC_270: Verify user is able to add same title in multiple lists')
# def test_create_multiple_list_from_film_series(browser):
#     home = homepage(browser)
#     film_series = filmSeriesPage(browser)
#     global test, my_comment
#     test = test_case_ids[269]  # 1079
#     my_comment = 'search box is not present'
#     film_series.page_refresh()
#     film_series.mouse_hover_on_movie()
#     film_series.click_on_add_to_list()
#     search = home.AddToListSearchBox()
#     assert search == True, 'search box is not present'
#     my_comment = 'Create list button is not Clickable / list name is not unique'
#     home.ListName("filmSeriesSecondList")
#     home.ClickCreateList()
#     my_comment = 'New list is not Created '
#     created = home.CreatedList()
#     assert created == True, 'New list is not Created'
#     name = home.VerifyFilmSeriesSecondListCreated()
#     assert name == True
#     my_comment = 'new created list is not Auto Selected'
#     list = home.VerifyFilmSeriesSecondAutoSelect()
#     assert list == True, 'new created list is not Auto Selected'
#     time.sleep(2)
#     home.AddMovieToList()
#     assert home.verify_success_text() == True, "Success message is not showing ."
#     my_comment = 'User should be able to add same title in multiple lists'
#
#
# #@allure.title('TC_271: Verify user is abel to search a list from the search bar')
# def test_film_series_movie_card_search_list(browser):
#     home = homepage(browser)
#     film_series = filmSeriesPage(browser)
#     global test, my_comment
#     test = test_case_ids[270]  # 1080
#     my_comment = 'List name is not present / User is not able to search a list'
#     film_series.mouse_hover_on_movie()
#     film_series.click_on_add_to_list()
#     home.SearchList("MoviesList")
#     verify = home.VerifySearchedList()
#     assert verify == True, 'List name is not present / User is not able to search a list'
#     my_comment = 'Enter search term in the search box should perform the search and show correct result'
#
#
# #@allure.title('TC_273: Verify user is able to select list(s) from search result')
# def test_film_series_select_searched_list(browser):
#     home = homepage(browser)
#     global test, my_comment
#     test = test_case_ids[272]  # 1082
#     my_comment = 'Toggle button is not Clickable'
#     select = home.MovieCardVerifySelectUnselectListMyListMovies()
#     assert select == True, 'Toggle button is not Clickable'
#     my_comment = 'User should be able to select list(s) from search result'
#
#
# #@allure.title('TC_274: Verify user is able to un-select list(s) from search result')
# def test_film_series_movie_card_unselect_searched_list(browser):
#     home = homepage(browser)
#     global test, my_comment
#     test = test_case_ids[273]  # 1083
#     my_comment = 'Toggle button is not Clickable'
#     select = home.MovieCardVerifySelectUnselectListMyListMovies()
#     assert select == False, 'Toggle button is not Clickable'
#     my_comment = 'User should be able to un-select list(s) from search result'
#
#
# #@allure.title('TC_272: Verify user is able to clear search on click of Clear button')
# def test_film_series_movie_card_clear_searched_list(browser):
#     home = homepage(browser)
#     global test, my_comment
#     test = test_case_ids[271]  # 1081
#     my_comment = 'clear button is not working'
#     clear_button = home.ClickAddToListClearButton()
#     assert clear_button == True, 'clear button is not working'
#     my_comment = 'On click of Clear button search should be cleared'
#
#
# #@allure.title('TC_275: Verify user is able to add to multiple movies in same list')
# def test_film_series_multiple_movie_to_same_list(browser):
#     home = homepage(browser)
#     film_series = filmSeriesPage(browser)
#     global test, my_comment
#     test = test_case_ids[274]  # 1084
#     my_comment = 'Candyman movie is not present in Film & Series page '
#     film_series.page_refresh()
#     film_series.mouse_hover_on_about_fate_movie()
#     film_series.click_on_add_to_list_about_fate_movie()
#     my_comment = 'list name is not unique / Add to list popup is not present '
#     home.SearchList("filmSeriesList")
#     # time.sleep(2)
#     home.ClickToggleButtonFilmSeries1()
#     home.AddMovieToList()
#     button = home.AddToListAddedButton()
#     assert button == True, 'New Created lis is not Auto selected '
#     my_comment = 'User should be able to add multiple titles in same list by clicking ' \
#                  'Add To List  and following add to list steps on each titles'
#
#
# #@allure.title('TC_276: Verify the sections on Movie Details page')
# def test_verify_movie_detail_page_elements(browser):
#     film_series = filmSeriesPage(browser)
#     global test, my_comment
#     test = test_case_ids[275]  # 1085
#     my_comment = 'Movies page is not open / Movie do not have Synopsis Title'
#     movie_page = ViewDetailsMoviePage(browser)
#     home = homepage(browser)
#     film_series.page_refresh()
#     film_series.mouse_hover_on_about_fate_movie()
#     candy_man = film_series.click_on_about_fate_view_details()
#     assert candy_man == True, 'Movies page is not open / Movie do not have Synopsis Title'
#     my_comment = 'logo image is not present on Movie Page'
#     logo_image = movie_page.verify_logo_image()
#     assert logo_image == True, 'logo image is not present on Movie Page'
#     my_comment = "Header logo not found in header"
#     logo = home.HomePageLogo()
#     assert logo == True, "Header logo not found in header"
#     my_comment = "Header 'Films & Series' link not found in header"
#     films_series = home.HeaderFilmsAndSeries()
#     assert films_series == True, "Header 'Films & Series' link not found in header"
#     my_comment = "My list link not found in header"
#     mylist = home.HeaderMylist()
#     assert mylist == True, "My list link not found in header"
#     my_comment = "Logout button not found in header"
#     logout = home.HeaderLogoutButton()
#     assert logout == True, "Logout button not found in header"
#     my_comment = "Search button not found in header"
#     marketing_rules = home.HeaderMarketingRules()
#     assert marketing_rules == True, "Search button not found in header"
#     my_comment = "Assets Button not found"
#     assets = home.HeaderAssets()
#     assert assets == True, "Assets Button not found"
#     my_cart = home.HeaderMyCarts()
#     assert my_cart == True, "My Carts button not found in header"
#     my_comment = 'Movie page Do not have Cast, Crew and Production Title'
#     production_title = movie_page.verify_cast_crew_production_title()
#     assert production_title == True, 'Movie page Do not have Cast, Crew and Production Title'
#     my_comment = '''Movie Details page should have the following sections:
# 1. Header
# 2. Synopsis
# 3. Photos
# 4. Cast, Crew and Production '''
#
#
# #@allure.title('TC_277: Verify elements in header of Movie Details page')
# def test_verify_header_movie_detail_page(browser):
#     movie_page = ViewDetailsMoviePage(browser)
#     global test, my_comment
#     test = test_case_ids[276]  # 1086
#     my_comment = 'Banner image is not present on Movie Detail page'
#     # banner_image = movie_page.bannerImage()
#     # assert banner_image == True, 'Banner image is not present on Movie Detail page'
#     my_comment = 'logo image is not present on Movie Page'
#     logo_image = movie_page.verify_logo_image()
#     assert logo_image == True, 'logo image is not present on Movie Page'
#     my_comment = 'Watch Trailer is not present on Movie-Details page'
#     watch_trailer = movie_page.verify_watch_trailer_button()
#     assert watch_trailer == True, 'Watch Trailer is not present on Movie-Details page'
#     my_comment = 'Watch Now is not present on Movie-Details page'
#     watch_now = movie_page.verify_watch_now_button()
#     assert watch_now == True, 'Watch Now is not present on Movie-Details page'
#     my_comment = 'Add-To-List is not present on Movie-Details page'
#     add_to_list = movie_page.verify_add_to_list_button()
#     assert add_to_list == True, 'Add-To-List is not present on Movie-Details page'
#     my_comment = 'Sell-Sheet is not present on Movie_Details page'
#     sell_sheet = movie_page.verify_sell_sheet_button()
#     assert sell_sheet == True, 'Sell-Sheet is not present on Movie_Details page'
#     my_comment = '''Movie Details header should have the following:
# 1. Hero Image
# 2. Title Treatment (logo)
# 3. Buttons [Watch Movie, Watch Trailer , Add to List and sell sheet]'''
#
#
# #@allure.title('TC_278: Verify user movie is played on click of Watch Movie button')
# def test_click_watch_now_button_movie_details_page(browser):
#     movie_page = ViewDetailsMoviePage(browser)
#     video_player = videoplayer(browser)
#     global test, my_comment
#     test = test_case_ids[277]  # 1087
#     movie_page.click_on_watch_now()
#     my_comment = 'Watch Now is not Clickable / video player is not open'
#     zoomInOutButton = video_player.zoomINButton()
#     assert zoomInOutButton == True, 'Watch Now is not Clickable / video player is not open'
#     video_player.ClickCloseButton()
#     my_comment = 'On click of Watch Movie button, Movie should start playing in the player pop up'
#
#
# #@allure.title('TC_279: Verify user is able to watch the trailer of the movie')
# def test_click_watch_trailer_button_movie_details_page(browser):
#     movie_page = ViewDetailsMoviePage(browser)
#     video_player = videoplayer(browser)
#     global test, my_comment
#     test = test_case_ids[278]  # 1088
#     my_comment = 'Watch Trailer is not clickable / Video player is not open'
#     movie_page.click_on_watch_trailer()
#     zoomInOutButton = video_player.zoomINButton()
#     assert zoomInOutButton == True, 'Watch Trailer is not Clickable / video player is not open'
#     video_player.ClickCloseButton()
#     my_comment = 'On click of Watch Trailer button, Trailer should start playing in the player pop up'
#
#
# #@allure.title('TC_280: Verify user is able to add the movie in a list')
# def test_click_add_to_list_movie_details_page(browser):
#     movie_page = ViewDetailsMoviePage(browser)
#     home = homepage(browser)
#     global test, my_comment
#     test = test_case_ids[279]  # 1089
#     my_comment = 'Add to List popup is not present / add to list button is not clickable'
#     add_to_list_popup = movie_page.click_on_add_to_list()
#     assert add_to_list_popup == True, 'Add to List popup is not present / add to list button is not clickable'
#     home.SearchList("filmSeriesSecondList")
#     time.sleep(2)
#     home.ClickToggleButtonFilmSeries2()
#     home.AddMovieToList()
#     button = home.AddToListAddedButton()
#     assert button == True
#     my_comment = '''User should be able to add the movie in a list by the following steps:
# 1. Click Add to List
# 2. Select List(s)
# 3. Click Add To List'''
#
#
# #@allure.title('TC_281: Verify sell sheet button is clickable')
# def test_click_on_sell_sheet_movie_details_page(browser):
#     movie_page = ViewDetailsMoviePage(browser)
#     global test, my_comment
#     test = test_case_ids[280]  # 1090
#     my_comment = 'SellSheet is not clickable /SellSheet is not clickable / Download button is not present'
#     sell_sheet = movie_page.click_on_sell_sheet()
#     assert sell_sheet == True, 'SellSheet is not clickable /SellSheet is not clickable / Download button is not present'
#     my_comment = '''sell sheet button should be clickable
#                     After click sell sheet button a popup window should opened'''
#
#
# #@allure.title('TC_282: Verify sell sheet popup elements')
# def test_elements_of_sell_sheet_movie_details_page(browser):
#     movie_page = ViewDetailsMoviePage(browser)
#     global test, my_comment
#     test = test_case_ids[281]  # 1091
#     my_comment = 'Download button is not present on Sell-Sheet'
#     download_button = movie_page.verify_sell_sheet_download_button()
#     assert download_button == True, 'Download button is not present on Sell-Sheet'
#     my_comment = 'Close button is not present on sell-sheet'
#     close_button = movie_page.verify_sell_sheet_close_button()
#     assert close_button == True, 'Close button is not present on sell-sheet'
#     my_comment = '''Sell sheet have following elements:-
# 1. Close button
# 4. Downlaod button:- On click download user should be able to download sell sheet pdf'''
#
#
# #@allure.title('TC_283: Verify elements in Synopsis section of Movie Details page')
# def test_synopsis_section_movie_details_page(browser):
#     movie_page = ViewDetailsMoviePage(browser)
#     global test, my_comment
#     test = test_case_ids[282]  # 1092
#     my_comment = 'Movie Description is not present in movie detail page'
#     movie_page.refresh_movie()
#     movie_description = movie_page.verify_movie_description()
#     assert movie_description == True, 'Movie Description is not present in movie detail page'
#     my_comment = 'Title Image is not present in movie detail page'
#     title_image = movie_page.verify_title_overview_image()
#     assert title_image == True, 'Title Image is not present in movie detail page'
#     my_comment = 'movie Rate is not present in movie detail page'
#     movie_rated = movie_page.verify_movie_rated()
#     assert movie_rated == True, 'movie Rate is not present in movie detail page'
#     my_comment = 'Movie Cast is not present in movie detail page'
#     movie_cast = movie_page.verify_movie_cast()
#     assert movie_cast == True, 'Movie Cast is not present in movie detail page'
#     my_comment = 'Movie Genre is not present in movie detail page'
#     movie_genre = movie_page.verify_movie_genre()
#     assert movie_genre == True, 'Movie Genre is not present in movie detail page'
#     my_comment = "Director title is not present"
#     director_text = movie_page.verify_movie_director()
#     assert director_text == True, "Director title is not present"
#     release_date = movie_page.verify_movie_release_date()
#     my_comment = 'Release Date is not present in movie detail page'
#     assert release_date == True, 'Release Date is not present in movie detail page'
#     copyright_des = movie_page.verify_movie_copyright()
#     assert copyright_des == True, 'Copyright text is present in movie detail page'
#     my_comment = '''Synopsis section should show the following:
# 1. Poster Image
# 2. Description
# 3. Rating, Genre and Release Date
# 4. Director
# 5. Casts
# 6. Copy Right text'''
#
#
# #@allure.title('TC_284: Verify elements in Photos section of Movie Details page')
# def test_verify_photo_elements_movie_detail(browser):
#     home = homepage(browser)
#     movie_page = ViewDetailsMoviePage(browser)
#     global test, my_comment
#     test = test_case_ids[283]  # 1093
#     my_comment = 'Not redirecting to Movie page'
#     film_series = filmSeriesPage(browser)
#     home.gotohomepage(_url_)
#     movies = home.ClickFilmsSeries()
#     assert movies == True, "Not redirecting to correct page"
#     my_comment = 'Photo Title is not present in movie detail page'
#     film_series.mouse_hover_cyrano()
#     # photo_title = movie_page.verify_photo_title()
#     # assert photo_title == True, 'Photo Title is not present in movie detail page'
#     my_comment = 'View Port is not present in movie detail page'
#     view_port = movie_page.verify_view_port_first_image()
#     assert view_port == True, 'View Port is not present in movie detail page'
#     my_comment = 'Right Arrow is not present in view port'
#     right_arrow = movie_page.verify_view_port_right_cross_arrow()
#     assert right_arrow == True, 'Right Arrow is not present in view port'
#     my_comment = 'Image is not present in active area'
#     active_image = movie_page.verify_slider_image()
#     assert active_image == True, 'Image is not present in active area'
#     my_comment = '''Photos section should have the following:
# 1. Title
# 2. View port for the Images
# 3. Right/Left Scroll arrows on view port
# 4. Thumbnail Gallery'''
#
#
# #@allure.title('TC_285: Verify user is able to navigate between photos by clicking the scroll arrows')
# def test_verify_navigate_active_image(browser):
#     movie_page = ViewDetailsMoviePage(browser)
#     global test, my_comment
#     test = test_case_ids[284]  # 1094
#     my_comment = 'Right cross button is not Clickable'
#     image_change = movie_page.verify_active_image_right_cross_button()
#     assert image_change == True, 'Right cross button is not Clickable'
#     my_comment = 'User should be able to navigate between photos by clicking the arrows'
#
#
# #@allure.title('TC_286: Verify clicking on the thumbnail from gallery shows in the view port')
# def test_click_view_port_image_(browser):
#     movie_page = ViewDetailsMoviePage(browser)
#     global test, my_comment
#     test = test_case_ids[285]  # 1095
#     my_comment = 'Right cross button is not Clickable'
#     image_change = movie_page.verify_view_port_clickable()
#     assert image_change == True, 'Right cross button is not Clickable'
#     my_comment = 'On click of any thumbnail in the gallery should open the image in the viewport '
#
#
# #@allure.title('TC_287: Verify elements of Cast, Crew & Production')
# def test_title_elements_movie_details_page(browser):
#     movie_page = ViewDetailsMoviePage(browser)
#     global test, my_comment
#     test = test_case_ids[286]  # 1096
#     my_comment = 'movie Rate is not present in movie detail page'
#     movie_rated = movie_page.verify_movie_rated()
#     assert movie_rated == True, 'movie Rate is not present in movie detail page'
#     my_comment = 'movie Rate is not present in movie detail page'
#     movie_rated_name = movie_page.verify_movie_rated_name()
#     assert movie_rated_name == True, 'movie Rate is not present in movie detail page'
#     my_comment = 'Movie Cast is not present in movie detail page'
#     movie_cast = movie_page.verify_movie_cast()
#     assert movie_cast == True, 'Movie Cast is not present in movie detail page'
#     movie_cast_name = movie_page.verify_movie_cast_name()
#     assert movie_cast_name == True, 'Movie Cast is not present in movie detail page'
#     my_comment = 'Movie Genre is not present in movie detail page'
#     movie_genre = movie_page.verify_movie_genre()
#     assert movie_genre == True, 'Movie Genre is not present in movie detail page'
#     my_comment = 'Movie Genre is not present in movie detail page'
#     movie_genre_name = movie_page.verify_movie_genre_name()
#     assert movie_genre_name == True, 'Movie Genre is not present in movie detail page'
#     my_comment = "Director title is not present"
#     director_text = movie_page.verify_movie_director()
#     assert director_text == True, "Director title is not present"
#     director_text_name = movie_page.verify_movie_director_name()
#     assert director_text_name == True, "Director title is not present"
#     my_comment = 'Release Date is not present in movie detail page'
#     release_date = movie_page.verify_movie_release_date()
#     assert release_date == True, 'Release Date is not present in movie detail page'
#     release_date_name = movie_page.verify_movie_release_date_name()
#     assert release_date_name == True, 'Release Date is not present in movie detail page'
#     copyright_des = movie_page.verify_movie_copyright()
#     assert copyright_des == True, 'Copyright text is present in movie detail page'
#     my_comment = 'Cast, Crew & Prodcution section should display the names of' \
#                  ' Casts, Director, Producer(s) & Executive producers'
#
#
# #@allure.title('TC_288: Verify the sections on Series Details page')
# def test_verify_series_section_movie_detail(browser):
#     home = homepage(browser)
#     movie_page = ViewDetailsMoviePage(browser)
#     film_series = filmSeriesPage(browser)
#     series_page = ViewDetailsSeriesPage(browser)
#     global test, my_comment
#     test = test_case_ids[287]  # 1097
#     my_comment = 'Movie and Series page is not open'
#     home.gotohomepage(_url_)
#     movies_page = home.ClickFilmsSeries()
#     assert movies_page == True, 'Movie and Series page is not open'
#     film_series.type_series_name_in_search_field()
#     film_series.click_search_button()
#     film_series.mouse_hover_on_big_shot()
#     my_comment = 'Banner-Image is not present in Series page'
#     banner_image = series_page.verify_banner_image()
#     assert banner_image == True, 'Banner-Image is not present in Series page'
#     my_comment = 'Title Text is not present in Series page'
#     title_text = series_page.verify_title_text()
#     assert title_text == True, 'Title Text is not present in Series page'
#     my_comment = "Header logo not found in header"
#     logo = home.HomePageLogo()
#     assert logo == True, "Header logo not found in header"
#     my_comment = "Header 'Films & Series' link not found in header"
#     films_series = home.HeaderFilmsAndSeries()
#     assert films_series == True, "Header 'Films & Series' link not found in header"
#     my_comment = "My list link not found in header"
#     mylist = home.HeaderMylist()
#     assert mylist == True, "My list link not found in header"
#     my_comment = "Logout button not found in header"
#     logout = home.HeaderLogoutButton()
#     assert logout == True, "Logout button not found in header"
#     marketing_rules = home.HeaderMarketingRules()
#     assert marketing_rules == True, "Search button not found in header"
#     assets = home.HeaderAssets()
#     assert assets == True, "Assets Button not found"
#     my_comment = ' my cart is not present in header section'
#     my_cart = home.HeaderMyCarts()
#     assert my_cart == True, ' my cart is not present in header section'
#     title_overview = series_page.click_title_text()
#     assert title_overview == True, 'Title Overview page is not open'
#     movie_cast = movie_page.verify_movie_cast()
#     assert movie_cast == True, 'Movie Cast is not present in movie detail page'
#     movie_genre = movie_page.verify_movie_genre()
#     assert movie_genre == True, 'Movie Genre is not present in movie detail page'
#     release_date = movie_page.verify_movie_release_date()
#     assert release_date == True, 'Release Date is not present in movie detail page'
#     copyright_des = movie_page.verify_movie_copyright()
#     assert copyright_des == True, 'Copyright text is present in movie detail page'
#     my_comment = '''Television Details page should have the following sections:
# 1. Header
# 2. Title Overview [Synopsis[As per Levels] & Episodes(only for season level)]
# 3. Photos
# 4. Cast, Crew and Production '''
#
#
# #@allure.title('TC_289: Verify elements in header of  Series Level')
# def test_verify_series_header_elements(browser):
#     movie_page = ViewDetailsMoviePage(browser)
#     series_page = ViewDetailsSeriesPage(browser)
#     global test, my_comment
#     test = test_case_ids[288]  # 1098
#     my_comment = 'logo image is not present on Movie Page'
#     logo_image = movie_page.verify_logo_image()
#     assert logo_image == True, 'logo image is not present on Movie Page'
#     my_comment = 'Watch Trailer is not present on Movie-Details page'
#     watch_trailer = movie_page.verify_watch_trailer_button()
#     assert watch_trailer == True, 'Watch Trailer is not present on Movie-Details page'
#     my_comment = 'Add-To-List is not present on Movie-Details page'
#     add_to_list = movie_page.verify_add_to_list_button()
#     assert add_to_list == True, 'Add-To-List is not present on Movie-Details page'
#     my_comment = 'Season Dropdown is not present in Series-Page'
#     season_dropdown = series_page.verify_season_dropdown()
#     assert season_dropdown == True, 'Season Dropdown is not present in Series-Page'
#     my_comment = 'Episode button is not present in Series-Page'
#     episode_title = series_page.verify_season_episode_button()
#     assert episode_title == True, 'Episode button is not present in Series-Page'
#     my_comment = ''' Series Level should have the following:
# 1. Hero Image
# 2. Title Treatment (logo)
# 3. Number of Seasons & Episodes
# 4. All Seasons [Drop-down]
# 5. Add To List
# 6 watch trailer Button'''
#
#
# #@allure.title('TC_290: Verify values of All Seasons dropdown')
# def test_verify_season_dropdown_elements(browser):
#     series_page = ViewDetailsSeriesPage(browser)
#     global test, my_comment
#     test = test_case_ids[289]  # 1099
#     my_comment = 'Select Season Text is not present in Series Button'
#     series_page.click_title_season_button()
#     select_season = series_page.verify_select_season_text()
#     assert select_season == True, 'Select Season Text is not present in Series Button'
#     my_comment = 'Season One text is not present in series button'
#     season_one = series_page.verify_season_season_one()
#     assert season_one == True, 'Season One text is not present in series button'
#     my_comment = '''All Season dropdown should have all seasons as drop-down values
# Example: All Seasons, Season 1, Season 2, etc.
# All Season represents Series level and should be selected by default'''
#
#
# #@allure.title('TC_291: Verify user is able to go to Season level from Series level')
# def test_click_season_dropdown(browser):
#     series_page = ViewDetailsSeriesPage(browser)
#     global test, my_comment
#     test = test_case_ids[290]  # 1100
#     my_comment = 'Season One text is not present in series button'
#     season_one = series_page.click_on_season_one()
#     assert season_one == True, 'Season One text is not present in series button'
#     my_comment = 'User should be able to reach Season level by selecting any season from the All Season dropdown'
#
#
# #@allure.title('TC_292: Verify user is able to watch the trailer of the movie')
# def test_click_watch_trailer_button_movie_series_page(browser):
#     movie_page = ViewDetailsMoviePage(browser)
#     video_player = videoplayer(browser)
#     global test, my_comment
#     test = test_case_ids[291]  # 1101
#     my_comment = 'Watch Trailer is not clickable / Video player is not open'
#     movie_page.click_on_watch_trailer()
#     zoom_in_zoom_out_button = video_player.zoomINButton()
#     assert zoom_in_zoom_out_button == True, 'Watch Trailer is not clickable / Video player is not open'
#     video_player.ClickCloseButton()
#     my_comment = 'On click of Watch Trailer button, Trailer should start playing in the player pop up'
#
#
# #@allure.title('TC_293: Verify user is able to Add TV Series to list(s)')
# def test_click_add_to_list_series_details_page(browser):
#     movie_page = ViewDetailsMoviePage(browser)
#     home = homepage(browser)
#     global test, my_comment
#     test = test_case_ids[292]  # 1102
#     my_comment = 'Add to List popup is not present / add to list button is not clickable'
#     add_to_list_popup = movie_page.click_on_add_to_list()
#     assert add_to_list_popup == True, 'Add to List popup is not present / add to list button is not clickable'
#     home.SearchList("filmSeriesSecondList")
#     my_comment = 'List Name is not present in Add to list popup '
#     # time.sleep(2)
#     home.ClickToggleButtonFilmSeries2()
#     home.AddMovieToList()
#     button = home.AddToListAddedButton()
#     assert button == True, 'add movie button is not clickable'
#     my_comment = '''User should be able to add the series in a list by the following steps:
# 1. Click Add to List
# 2. Select List(s)
# 3. Click Add To List'''
#
#
# #@allure.title('TC_294: Verify Episodes tab is visible when user is at Season level')
# def test_verify_episode_tab_series_page(browser):
#     series_page = ViewDetailsSeriesPage(browser)
#     global test, my_comment
#     test = test_case_ids[293]  # 1103
#     my_comment = 'Episode tab is not present in Film and series page'
#     episode_tab = series_page.verify_episode_tab()
#     assert episode_tab == True, 'Episode tab is not present in Film and series page'
#     my_comment = 'Episodes tab should be available when user is on ' \
#                  'Season level User should be able to go to Episodes tab '
#
#
# #@allure.title('TC_295: Verify elements in Episodes Tab at Season level')
# def test_verify_episode_card_elements(browser):
#     series_page = ViewDetailsSeriesPage(browser)
#     global test, my_comment
#     test = test_case_ids[294]  # 1104
#     my_comment = 'Episode image is not present in Season Level'
#     card_image = series_page.verify_first_card_image_tab()
#     assert card_image == True, 'Episode image is not present in Season Level'
#     my_comment = 'Episode Number is not present in Season Level'
#     episode_number = series_page.verify_first_card_episode_number()
#     assert episode_number == True, 'Episode Number is not present in Season Level'
#     my_comment = 'Episode Name is not present in Season Level'
#     episode_name = series_page.verify_first_card_episode_name()
#     assert episode_name == True, 'Episode Name is not present in Season Level'
#     my_comment = 'Description is not present in movie card '
#     card_description = series_page.verify_first_card_description()
#     assert card_description == True, 'Description is not present in movie card '
#     my_comment = 'Episode card is not clickable'
#     episode_page = series_page.click_first_episode_card()
#     assert episode_page == True, 'Episode card is not clickable'
#     my_comment = '''Episodes tab should show the Episodes cards of that season
# Each Episode card should have the following:
# 1. Image
# 2. Episode Number & Episode Name
# 3. Description
# Clicking on Episode card should take user to Episode Level'''
#
#
# #@allure.title('TC_296: Verify elements in Episodes Tab at Episode level')
# def test_verify_episode_page_elements(browser):
#     series_page = ViewDetailsSeriesPage(browser)
#     global test, my_comment
#     test = test_case_ids[295]  # 1105
#     my_comment = 'Back Button is not present in Episode page'
#     back_button = series_page.verify_back_to_episode_button()
#     assert back_button == True, 'Back Button is not present in Episode page'
#     my_comment = 'Synopsis Title is not present in Episode page'
#     synopsis_text = series_page.verify_episode_page_synopsis()
#     assert synopsis_text == True, 'Synopsis Title is not present in Episode page'
#     my_comment = 'Episode Image is not present in Episode page'
#     episode_image = series_page.verify_episode_page_image()
#     assert episode_image == True, 'Episode Image is not present in Episode page'
#     my_comment = 'Episode Play button is not present in Episode page'
#     play_button = series_page.verify_episode_play_button()
#     assert play_button == True, 'Episode Play button is not present in Episode page'
#     my_comment = '''Episodes tab should show the following:
# 1. Primary Landsacpe Image with Play button
# 2. Synopsis
# 3. Back bto episode button'''
#
#
# #@allure.title('TC_297: Verify user is able to play episode by clicking the play button ')
# def test_click_episode_play_button(browser):
#     series_page = ViewDetailsSeriesPage(browser)
#     video_player = videoplayer(browser)
#     global test, my_comment
#     test = test_case_ids[296]  # 1106
#     my_comment = 'Close Button is not present in Video-Player'
#     series_page.click_episode_play_button()
#     zoom_in_out_button = video_player.zoomINButton()
#     assert zoom_in_out_button == True, 'Close Button is not present in Video-Player'
#     video_player.ClickCloseButton()
#     my_comment = 'On click of Play button, Episode should be played in the player pop up'
#
#
# #@allure.title('TC_299: Verify back to episode button on particular episode page')
# def test_click_back_to_episode_button(browser):
#     series_page = ViewDetailsSeriesPage(browser)
#     global test, my_comment
#     test = test_case_ids[298]  # 1108
#     my_comment = 'Back-To-Episode button is not Clickable'
#     back_page = series_page.click_back_to_episode_button()
#     assert back_page == True, 'Back-To-Episode button is not Clickable'
#     my_comment = 'On click back to episode button page should redirected to season level page'
#
#
# #@allure.title('TC_Raw: logout after all process ')
# def test_raw_logout_button_film_srs(browser):
#     home = homepage(browser)
#     home.gotohomepage(_url_)
#     verify = home.ClickLogoutButton()
#     assert verify == True, "User is not logged out"
#
#
# #@allure.title('TC_001:
# #@allure.title('TC_300: Verify Elements present on Assets Page')
# def test_assets_page_elements(browser):
#     home = homepage(browser)
#     home_page = homePageObj(browser)
#     assets_page = AssetsPage(browser)
#     film_series = filmSeriesPage(browser)
#     user = loginpage(browser)
#     my_list = homePagemylistsObj(browser)
#     global test, my_comment
#     test = test_case_ids[299]  # 1109
#     my_comment = 'Header logo not found'
#     user.LoginPage(_url_)
#     user.ClickOnAcceptCookies()
#     user.EnterEmail(email)
#     verify = user.ClickNext()
#     assert verify == True, "user not proceed to next step with valid email id"
#     user.EnterPassword(password)
#     user.verifyButton()
#     # time.sleep(2)
#     # current_url = user.ValidateUrlForNextPage()
#     # assert not 'login' in current_url
#     # time.sleep(2)
#     user.confrimation_page_without_elements()
#     user.confrimation_page_elements()
#     verify = user.VerifyLogin()
#     assert verify == True, "User is not able to login with valid credentials"
#     my_comment = 'On click of Logout button user should logged out of app and redirected to Login page'
#     mycart = home.ClickMyCarts()
#     assert mycart == True, "Not redirecting to correct page"
#     my_list.delete_Testing_cart2_carts()
#     my_list.delete_Testing_cart_carts()
#     home.click_header_assets()
#     logo = home.HomePageLogo()
#     assert logo == True, "Header logo not found"
#     my_comment = "Header 'Films & Series' link not found"
#     films_series = home.HeaderFilmsAndSeries()
#     assert films_series == True, "Header 'Films & Series' link not found"
#     my_list = home.HeaderMylist()
#     assert my_list == True, "My list link not found"
#     my_comment = "Logout button not found"
#     logout = home.HeaderLogoutButton()
#     assert logout == True, "Logout button not found"
#     marketing_rules = home.HeaderMarketingRules()
#     assert marketing_rules == True, "Search button not found"
#     assets = home.HeaderAssets()
#     assert assets == True, "Assets Button not found"
#     my_comment = "My Carts button not found"
#     my_cart = home.HeaderMyCarts()
#     assert my_cart == True, "My Carts button not found"
#     my_comment = 'Title Cards are not present in Assets page'
#     title_card = assets_page.verify_first_title_card()
#     assert title_card == True, 'Title Cards are not present in Assets page'
#     my_comment = 'banner image is not present'
#     banner_image = film_series.verify_banner_image()
#     assert banner_image == True, 'banner image is not present'
#     filter_button = film_series.verify_filter_button()
#     assert filter_button >= 2, 'filter button is present'
#     sorting_button = film_series.verify_sort_filter_button()
#     assert sorting_button >= 1, 'sorting button is not present'
#     my_comment = 'pagination section is not present'
#     pagination = film_series.verify_right_cursor_button()
#     assert pagination == True, 'pagination section is not present'
#     my_comment = 'Privacy policy is not displaying in global footer. It should be displayed in footer. '
#     assert home_page.verify_Privacypolicy() == True, "Privacy policy is not displaying in global footer. It should be " \
#                                                      "displayed in footer. "
#     assert home_page.verify_termsUse() == True, "Terms and Use is not displaying in global footer. It should be " \
#                                                 "displayed in footer. "
#     my_comment = 'Terms and Use is not displaying in global footer. It should be displayed in footer. '
#     assert home_page.verify_footerLogo() == True, "MGM logo  is not displaying in global footer. It should be " \
#                                                   "displayed in footer. "
#     my_comment = "Support link is not displaying in global footer. It should be displayed in footer. "
#     assert home_page.verify_supportLink() == True, "Support link is not displaying in global footer. It should be " \
#                                                    "displayed in footer. "
#     assert home_page.verify_address() == True, "Address text is not displaying in global footer. It should be " \
#                                                "displayed in footer. "
#     assert home_page.verify_legal() == True, "Legal text is not displaying in global footer. It should be " \
#                                              "displayed in footer. "
#     assert home_page.verify_contact_us() == True, "Contact-us is not displaying in global footer. It should be " \
#                                                   "displayed in footer. "
#     my_comment = 'Youtube icon is not displaying in global footer. It should be displayed in footer. '
#     assert home_page.verify_youtubeIcon() == True, "Youtube icon is not displaying in global footer. It should be " \
#                                                    "displayed in footer. "
#     assert home_page.verify_fbIcon() == True, "Facebook icon is not displaying in global footer. It should be " \
#                                               "displayed in footer. "
#     assert home_page.verify_twitterIcon() == True, "Twitter icon is not displaying in global footer. It should be " \
#                                                    "displayed in footer. "
#     assert home_page.verify_instaIcon() == True, "Instagram icon is not displaying in global footer. It should be " \
#                                                  "displayed in footer. "
#     assert home_page.verify_copyright() == True, "Copyright is not displaying in global footer. It should be " \
#                                                  "displayed in footer. "
#     my_comment = 'Connect is not displaying in global footer. It should be displayed in footer. '
#     assert home_page.verify_connect() == True, "Connect is not displaying in global footer. It should be " \
#                                                "displayed in footer. "
#     my_comment = '''Assets page should have the following elements:
# 1. Global Header
# 2. Banner
# 3. Filters
# 4. Sorting filter
# 5. View tabs
# 6. Title cards
# 7. Pagination
# 8. Global Footer'''
#
#
# #@allure.title('TC_301: Verify banner elements ')
# def test_assets_banner_elements(browser):
#     assets_page = AssetsPage(browser)
#     global test, my_comment
#     test = test_case_ids[300]  # 1110 #428
#     my_comment = 'Banner Image is not present in Assets Page'
#     banner_image = assets_page.verify_banner_image()
#     assert banner_image == True, 'Banner Image is not present in Assets Page'
#     my_comment = 'Banner Text is not present in Assets Page'
#     banner_text = assets_page.verify_banner_text()
#     assert banner_text == True, 'Banner Text is not present in Assets Page'
#     my_comment = 'Search Field is not present in Assets Page'
#     search_field = assets_page.verify_banner_search_field()
#     assert search_field == True, 'Search Field is not present in Assets Page'
#     my_comment = '''Banner should have following elements
#
# 1. Banner image
# 2. Our Titles text
# 3. Search bar'''
#
#
# #@allure.title('TC_302: Verify search bar is working')
# def test_validate_search_field_assets(browser):
#     film_series = filmSeriesPage(browser)
#     global test, my_comment
#     test = test_case_ids[301]  # 1111 #429
#     my_comment = 'Search button is not clickable / search option is not working'
#     film_series.page_refresh()
#     film_series.type_search_field()
#     film_series.click_search_button()
#     search_result = film_series.verify_search_result()
#     assert search_result, 'search option is not working'
#     my_comment = 'user should be able to search movie or tv titles through search bar'
#
#
# #@allure.title('TC_304: Verify search cross button inside search bar')
# def test_verify_cross_button_search_assets(browser):
#     film_series = filmSeriesPage(browser)
#     global test, my_comment
#     test = test_case_ids[303]  # 1113 #431
#     my_comment = 'Search Clear button is not present'
#     search_clear = film_series.verify_search_clear_button()
#     assert search_clear == True, 'Search Clear button is not present'
#     my_comment = 'When we searched any title a cross button should appear in search bar ' \
#                  'On click cross button search filter should be reset'
#
#
# #@allure.title('TC_303: Verify user is able to click on cross button after searching any title')
# def test_verify_cross_button_search_field_assets(browser):
#     film_series = filmSeriesPage(browser)
#     global test, my_comment
#     test = test_case_ids[302]  # 1112 #430
#     my_comment = 'Search cross button is not Clickable'
#     film_series.click_search_clear()
#     assetsNumbers = film_series.verify_click_search_cross_button()
#     assert assetsNumbers >= 52, 'Search cross button is not Working'
#     my_comment = '''User should able to click on search icon inside the search bar
# On click search icon user is able to see searched tites'''
#
#
# #@allure.title('TC_305: Verify elements present on Filters')
# def test_verify_filters_elements_assets(browser):
#     film_series = filmSeriesPage(browser)
#     global test, my_comment
#     test = test_case_ids[304]  # 1114 #432
#     my_comment = 'Type Filter, Genre Filter, Rating Filter, Year Filter are not Present'
#     four_filter = film_series.verify_filter_button()
#     assert four_filter == 4, 'Type Filter, Genre Filter, Rating Filter, Year Filter are not Present'
#     my_comment = '''Filters should have following elements:-
# 1. Type filter
# 2. Genre Filter
# 3. Rating filter
# 4. Year Filter
# '''
#
#
# #@allure.title('TC_306: Verify Type filter functionality')
# def test_verify_type_filter_assets(browser):
#     global total_title_card
#     global test, my_comment
#     test = test_case_ids[305]  # 1115 #433
#     my_comment = 'Type-Films-Filter is not Working'
#     film_series = filmSeriesPage(browser)
#     home = homepage(browser)
#     home.gotohomepage(_url_)
#     home.click_header_assets()
#     total_title_card = film_series.verify_total_movies_series()
#     all_movies = film_series.verify_type_films_filter()
#     assert total_title_card > all_movies, 'Type-Films-Filter is not Working'
#     my_comment = 'Clear All is not working'
#     clear_all_total_count = film_series.click_clear_all_filter()
#     assert clear_all_total_count == total_title_card, 'Clear All is not working'
#     my_comment = '''1. On click type filter a dropdown should opened
# 2. There should be radio button
# 3. We can select only one radio button at a time
# 4. After selecting any radio button dropdown should closed and search results shows according to selected radio filter'''
#
#
# #@allure.title('TC_307: Verify Genre filter functionality')
# def test_verify_genre_filter_functionality_assets(browser):
#     film_series = filmSeriesPage(browser)
#     global test, my_comment
#     test = test_case_ids[306]  # 1116
#     my_comment = 'Action Filter is not apply'
#     action_movie_tags = film_series.verify_genre_Action_filter()
#     assert (action_movie_tags < 43) & (action_movie_tags > 30), 'Action Filter is not apply'
#     my_comment = 'Clear All is not working'
#     clear_all_total_count = film_series.click_clear_all_filter()
#     assert clear_all_total_count == total_title_card, 'Clear All is not working'
#     my_comment = '''1. On click Genre filter a dropdown should opened
# 2. There should be Checkboxes and genre name
# 3. We can select one or multiple checkboxes at a time
# 4. Apply filter button should present end of the filter
# 5. On click apply filter button after selecting checkboxes Dropdown should close and results shows according to selected filters'''
#
#
# #@allure.title('TC_308:Verify Rating filter functionality')
# def test_verify_rating_filter_assets(browser):
#     film_series = filmSeriesPage(browser)
#     global test, my_comment
#     test = test_case_ids[307]  # 1117
#     my_comment = 'Rating Filter NC_17 is not working'
#     action_movie_tags = film_series.verify_rating_NC17_filter()
#     assert (action_movie_tags > 0) & (total_title_card > action_movie_tags), 'Rating Filter NC_17 is not working'
#     clear_all_total_count = film_series.click_clear_all_filter()
#     assert clear_all_total_count == total_title_card, 'Clear All is not working'
#     my_comment = '''1. On click Rating filter a dropdown should opened
# 2. There should be Checkboxes and Ratings name
# 3. We can select one or multiple checkboxes at a time
# 4. Apply filter button should present end of the filter
# 5. On click apply filter button after selecting checkboxes Dropdown should close and results shows according to selected filters'''
#
#
# #@allure.title('TC_309: Verify user is able to filter titles by Year')
# def test_verify_year_filter_assets(browser):
#     film_series = filmSeriesPage(browser)
#     global test, my_comment
#     test = test_case_ids[308]  # 1118
#     my_comment = 'Year Filter is not working'
#     year_filter_movies = film_series.verify_year_filter()
#     assert total_title_card > year_filter_movies, 'Year Filter is not working'
#     clear_all_total_count = film_series.click_clear_all_filter()
#     assert clear_all_total_count == total_title_card, 'Clear All is not working'
#     my_comment = '''1. On click Year filter a dropdown should be opened
# 2. There should be a range selector for selecting years
# 3, Click on apply filter button after selecting range filter then Dropdown
# should be closed and results shows according to selected range filter'''
#
#
# #@allure.title('TC_310: Verify filter chips functionality')
# def test_verify_filter_chips_functionality_assets(browser):
#     film_series = filmSeriesPage(browser)
#     global test, my_comment
#     test = test_case_ids[309]  # 1119
#     my_comment = 'Action Filter is not apply'
#     assets_page = AssetsPage(browser)
#     action_movie_tags = film_series.verify_genre_Action_filter()
#     assert (action_movie_tags < 43) & (action_movie_tags > 30), 'Action Filter is not apply'
#     my_comment = 'Filter chips is not clickable'
#     before_click = assets_page.click_filter_chips_action()
#     assert before_click == True, 'Filter chips is not clickable'
#     my_comment = 'Filter chips is not Removed After click'
#     after_click = assets_page.verify_filter_chips_clickable_assets()
#     assert after_click == False, 'Filter chips is not Removed After click'
#     my_comment = '''1. on click cross button chips should be deleted and this filter is also unchecked from  filter
#                     2. On click clear all button all the chips should removed
#                      and all the selected checboxes are unchecked'''
#
#
# #@allure.title('TC_311: Verify user is able to switch between grid view and list view')
# def test_verify_list_button_functionality_assets(browser):
#     film_series = filmSeriesPage(browser)
#     global test, my_comment
#     test = test_case_ids[310]  # 1120
#     my_comment = 'List Button is not Clickable'
#     table_head = film_series.verify_list_button()
#     assert table_head == True, 'List Button is not Clickable'
#     my_comment = 'On click of the view button, view should change in respect to the button clicked'
#
#
# #@allure.title('TC_312: Verify List view')
# def test_verify_list_tabular_structure_assets(browser):
#     film_series = filmSeriesPage(browser)
#     global test, my_comment
#     test = test_case_ids[311]  # 1121
#     my_comment = 'Title heading is not present'
#     list_title = film_series.verify_list_title()
#     assert list_title == True, 'Title heading is not present'
#     my_comment = 'Directed By heading is not present'
#     directed_by = film_series.verify_list_directed_by()
#     assert directed_by == True, 'Directed By heading is not present'
#     my_comment = 'Main-Cast heading is not present'
#     main_cast = film_series.verify_list_main_cast()
#     assert main_cast == True, 'Main-Cast heading is not present'
#     my_comment = 'Synopsis heading is not present'
#     synopsis_text = film_series.verify_list_synopsis()
#     assert synopsis_text == True, 'Synopsis heading is not present'
#     my_comment = '''List view should show tabular structure with following columns
# 1. Title
# 2. Directed By
# 3. Main Cast
# 4. Synopsis
# '''
#
#
# #@allure.title('TC_313: Verify the options of Sorting and their functionality')
# def test_verify_sorting_filter_assets(browser):
#     film_series = filmSeriesPage(browser)
#     global test, my_comment
#     test = test_case_ids[312]  # 1122
#     my_comment = 'Sorting A to Z are not working'
#     film_series.verify_sorting_button()
#     after_sort = film_series.verify_sorting_a_to_z()
#     assert total_title_card == after_sort, 'Sorting A to Z are not completed / Movies are not in Correct Order'
#     film_series.verify_sorting_button()
#     my_comment = 'Sorting Z to A are not working'
#     after_sort = film_series.verify_sorting_z_to_a()
#     assert total_title_card == after_sort, 'Sorting Z to A are not completed'
#     film_series.verify_sorting_button()
#     my_comment = 'Down Sorting are not working'
#     after_sort = film_series.verify_sorting_down_apply()
#     assert total_title_card == after_sort, 'Down Sorting are not completed'
#     film_series.verify_sorting_button()
#     my_comment = 'Up Sorting are not completed'
#     after_sort = film_series.verify_sorting_up()
#     assert total_title_card == after_sort, 'Up Sorting are not completed'
#     my_comment = '''Sorting drop down should have the following options with mentioned behaviour
# 1. Release Date (Old to New) -- Titles should be ordered in Decending order of Release Date
# 2. Release Date (New to Old) -- Titles should be ordered in Ascending order of Release Date
# 3. Sort A-Z  -- Titles should be ordered in Ascending order of Alphabets
# 4. Sort Z-A -- Titles should be ordered in Descending order of Alphabets
#
# '''
#
#
# #@allure.title('TC_314: Verify the elements of cards')
# def test_verify_film_and_series_cards_all_element_assets(browser):
#     home = homepage(browser)
#     global test, my_comment
#     test = test_case_ids[313]  # 1123
#     my_comment = 'Poster image is not present in movie card'
#     film_series = filmSeriesPage(browser)
#     film_series.visit_home_url(_url_)
#     home.click_header_assets()
#     card_poster = film_series.verify_first_card_poster()
#     assert card_poster == True, 'Poster image is not present in movie card'
#     my_comment = 'Title text is not present in movie card'
#     card_title = film_series.verify_first_card_title()
#     assert card_title == True, 'Title text is not present in movie card'
#     my_comment = 'Genre Title is not present in movie card'
#     card_genre = film_series.verify_first_card_genre()
#     assert card_genre == True, 'Genre Title is not present in movie card'
#     my_comment = '''Cards have following elements
#
# 1.Card with Title image
# 2. Tile name
# 3. Genre of title'''
#
#
# #@allure.title('TC_315:Verify pagination elements')
# def test_verify_pagination_elements_clickable_assets(browser):
#     film_series = filmSeriesPage(browser)
#     global test, my_comment
#     test = test_case_ids[314]  # 1124
#     my_comment = 'right cursor is not clickable'
#     right_cursor_click = film_series.click_right_cursor_button()
#     assert right_cursor_click == True, 'right cursor is not clickable'
#     film_series.click_left_cursor_button()
#     my_comment = 'left button cursor is not disabled'
#     disable_text = film_series.verify_left_disabled_cursor()
#     assert 'disabled' in disable_text, 'left button cursor is not disabled'
#     active_page = film_series.verify_one_active_page()
#     assert active_page == True, 'One page is not Active'
#     my_comment = 'pages are not disbaled'
#     count_of_disable_pages = film_series.verify_expect_one_disabled_pages_button()
#     assert count_of_disable_pages > 6, 'pages are not disbaled'
#     my_comment = '''Pagination have following elements:-
#
# 1. Prev navigation arrow
# 2. Next navigation arrow
# 3. Pages number '''
#
#
# #@allure.title('TC_316: Verify Prev navigation arrow functionality')
# def test_verify_pagination_prev_arrow_clickable_assets(browser):
#     film_series = filmSeriesPage(browser)
#     global test, my_comment
#     test = test_case_ids[315]  # 1125
#     my_comment = 'left button cursor is not disabled'
#     disable_text = film_series.verify_left_disabled_cursor()
#     assert 'disabled' in disable_text, 'left button cursor is not disabled'
#     my_comment = 'right cursor is not clickable'
#     right_cursor_click = film_series.click_right_cursor_button()
#     assert right_cursor_click == True, 'right cursor is not clickable'
#     film_series.click_left_cursor_button()
#     my_comment = 'left button cursor is not disabled'
#     disable_text = film_series.verify_left_disabled_cursor()
#     assert 'disabled' in disable_text, 'left button cursor is not disabled'
#     my_comment = '''1. If user is on first page then prev arrow should be disabled
#                     2. On click prev arrow page should move to prev page'''
#
#
# #@allure.title('TC_317: Verify Next navigation arrow functionality')
# def test_verify_pagination_next_arrow_clickable_assets(browser):
#     film_series = filmSeriesPage(browser)
#     global test, my_comment
#     test = test_case_ids[316]  # 1126
#     assets_page = AssetsPage(browser)
#     my_comment = 'right cursor is not clickable'
#     right_cursor_click = film_series.click_right_cursor_button()
#     assert right_cursor_click == True, 'right cursor is not clickable'
#     assets_page.click_last_page_button()
#     my_comment = 'right button cursor is not disabled'
#     right_disable_text = film_series.verify_right_disabled_cursor()
#     assert 'disabled' in right_disable_text, 'right button cursor is not disabled'
#     my_comment = '''1. If user is on last page then next arrow should be disabled
# 2. On click Next arrow page should move to Next page'''
#
#
# #@allure.title('TC_318: Verify pages numbers are clickable')
# def test_click_pagination_page_number_clickable_assets(browser):
#     film_series = filmSeriesPage(browser)
#     assets_page = AssetsPage(browser)
#     global test, my_comment
#     my_comment = 'right button cursor is not disabled'
#     test = test_case_ids[317]  # 1127
#     film_series.click_left_cursor_button()
#     assets_page.click_last_page_button()
#     right_disable_text = film_series.verify_right_disabled_cursor()
#     assert 'disabled' in right_disable_text, 'right button cursor is not disabled'
#     my_comment = 'On click any page number user should redirected to that page'
#
#
# #@allure.title('TC_319: Verify global header assets tab is highlited or not')
# def test_verify_assets_underline(browser):
#     assets_page = AssetsPage(browser)
#     global test, my_comment
#     test = test_case_ids[318]  # 1128
#     my_comment = 'underline is not present'
#     assets_active = assets_page.verify_assets_active()
#     assert 'active' in assets_active, 'underline is not present'
#     my_comment = 'When we are on assets page then Assets tab should be underlined on Global header'
#
#
# #@allure.title('TC_320: Verify cards are clickable')
# def test_click_respect_assets_card(browser):
#     home = homepage(browser)
#     global test, my_comment
#     test = test_case_ids[319]  # 1129
#     my_comment = 'Poster image is not present in movie card'
#     assets_page = AssetsPage(browser)
#     film_series = filmSeriesPage(browser)
#     film_series.visit_home_url(_url_)
#     home.click_header_assets()
#     card_poster = film_series.verify_first_card_poster()
#     assert card_poster == True, 'Poster image is not present in movie card'
#     my_comment = 'search option is not working'
#     film_series.type_search_assets_field()
#     film_series.click_search_button()
#     search_result = assets_page.verify_assets_search_result()
#     assert search_result, 'search option is not working'
#     assets_page.click_respect_movie()
#     my_comment = 'On click cards page should redirected to titles assets details page'
#
#
# #@allure.title('TC_321: Verify elements of assets details page')
# def test_verify_Banner_tabs_field(browser):
#     assets_page = AssetsPage(browser)
#     global test, my_comment
#     test = test_case_ids[320]  # 1130
#     my_comment = 'Banner Image is not present in Card Detail section'
#     banner_image = assets_page.verify_card_banner_image()
#     assert banner_image == True, 'Banner Image is not present in Card Detail section'
#     my_comment = 'Tabs are not present in card detail section'
#     card_tabs = assets_page.verify_card_tabs()
#     assert card_tabs == True, 'Tabs are not present in card detail section'
#     my_comment = '''Assets details page have following elements:-
# 1. Banner
# 2. Tabs
# '''
#
#
# #@allure.title('TC_322: Verify elements of assets details page')
# def test_click_card_back_button(browser):
#     assets_page = AssetsPage(browser)
#     global test, my_comment
#     test = test_case_ids[321]  # 1131
#     my_comment = 'Banner Image is not present in Card Detail section'
#     banner_image = assets_page.verify_card_banner_image()
#     assert banner_image == True, 'Banner Image is not present in Card Detail section'
#     my_comment = 'Tabs are not present in card detail section'
#     card_tabs = assets_page.verify_card_tabs()
#     assert card_tabs == True, 'Tabs are not present in card detail section'
#     my_comment = 'Back Button is not clickable '
#     back_button = assets_page.click_card_back_button()
#     assert back_button == True, 'Back Button is not clickable '
#     my_comment = '''1. Back button --> On click back button page should redirected to assets page
# 2. Title name
# 3  Tabs'''
#
#
# #@allure.title('TC_323: Verify tabs name ')
# def test_verify_tabs(browser):
#     assets_page = AssetsPage(browser)
#     film_series = filmSeriesPage(browser)
#     global test, my_comment
#     test = test_case_ids[322]  # 1132
#     my_comment = 'search option is not working'
#     film_series.type_search_assets_field()
#     film_series.click_search_button()
#     search_result = assets_page.verify_assets_search_result()
#     assert search_result, 'search option is not working'
#     my_comment = 'Title Overview button is not present in Header-Section'
#     assets_page.click_respect_movie()
#     title_overview = assets_page.verify_tab_title_overview()
#     assert title_overview == True, 'Title Overview button is not present in Header-Section'
#     my_comment = 'All Assets button is not present in Header-Section'
#     all_assets = assets_page.verify_tab_all_assets()
#     assert all_assets == True, 'All Assets button is not present in Header-Section'
#     my_comment = 'Images/Photo button is not present in Header-Section'
#     image_photo = assets_page.verify_tab_images_photo()
#     assert image_photo == True, 'Images/Photo button is not present in Header-Section'
#     my_comment = 'Documents button is not present in Header-Section'
#     tab_documents = assets_page.verify_tab_documents()
#     assert tab_documents == True, 'Documents button is not present in Header-Section'
#     my_comment = 'Paid Ad Memo is not present in Header-section'
#     paid_ad_memo = assets_page.verify_tab_paid_ad_memo()
#     assert paid_ad_memo == True, 'Paid Ad Memo is not present in Header-section'
#     my_comment = '''There are following tabs:-
#
# 1. Title overview ( should be selected by default)
# 2. All Assets
# 3. Images/Photos
# 4. Videos
# 5. Documents
# 6. Paid ad demo'''
#
#
# #@allure.title('TC_324: Verify Title overview Tab')
# def test_verify_title_overview_elements(browser):
#     movie_page = ViewDetailsMoviePage(browser)
#     global test, my_comment
#     test = test_case_ids[323]  # 1133
#     my_comment = 'movie Rate is not present in movie detail page'
#     movie_rated = movie_page.verify_movie_rated()
#     assert movie_rated == True, 'movie Rate is not present in movie detail page'
#     movie_rated_name = movie_page.verify_movie_rated_name()
#     assert movie_rated_name == True, 'movie Rate is not present in movie detail page'
#     my_comment = 'Movie Cast is not present in movie detail page'
#     movie_cast = movie_page.verify_movie_cast()
#     assert movie_cast == True, 'Movie Cast is not present in movie detail page'
#     movie_cast_name = movie_page.verify_movie_cast_name()
#     assert movie_cast_name == True, 'Movie Cast is not present in movie detail page'
#     my_comment = 'Movie Genre is not present in movie detail page'
#     movie_genre = movie_page.verify_movie_genre()
#     assert movie_genre == True, 'Movie Genre is not present in movie detail page'
#     movie_genre_name = movie_page.verify_movie_genre_name()
#     assert movie_genre_name == True, 'Movie Genre is not present in movie detail page'
#     my_comment = "Director title is not present"
#     director_text = movie_page.verify_movie_director()
#     assert director_text == True, "Director title is not present"
#     director_text_name = movie_page.verify_movie_director_name()
#     assert director_text_name == True, "Director title is not present"
#     my_comment = 'Release Date is not present in movie detail page'
#     release_date = movie_page.verify_movie_release_date()
#     assert release_date == True, 'Release Date is not present in movie detail page'
#     release_date_name = movie_page.verify_movie_release_date_name()
#     assert release_date_name == True, 'Release Date is not present in movie detail page'
#     my_comment = 'Copyright text is present in movie detail page'
#     copyright_des = movie_page.verify_movie_copyright()
#     assert copyright_des == True, 'Copyright text is present in movie detail page'
#     my_comment = '''Title over view tab have following elements:0
#
# 1. Title Image
# 2.Synopsis
# 3. Cast, Production and Crew Description'''
#
#
# #@allure.title('TC_325: Verify All Assets tab elements')
# def test_verify_all_assets_elements(browser):
#     assets_page = AssetsPage(browser)
#     global test, my_comment
#     test = test_case_ids[324]  # 1134
#     my_comment = 'Reset Filter is not Present in All Assets Header-Section'
#     assets_page.click_all_assets_button()
#     reset_filter = assets_page.verify_reset_filter_button()
#     assert reset_filter == True, 'Reset Filter is not Present in All Assets Header-Section'
#     my_comment = 'Collapse-All is not Present in All Assets Header-Section'
#     collapse_all = assets_page.verify_collapse_all_button()
#     assert collapse_all == True, 'Collapse-All is not Present in All Assets Header-Section'
#     my_comment = 'Select All is not Present in all Assets Header-Section'
#     select_all = assets_page.verify_select_all_button()
#     assert select_all == True, 'Select All is not Present in all Assets Header-Section'
#     my_comment = 'Grid-View button is not Present in All Assets Header-Section'
#     grid_view = assets_page.verify_grid_view_button()
#     assert grid_view == True, 'Grid-View button is not Present in All Assets Header-Section'
#     my_comment = 'List-View button is not Present in all Assets Header_Section'
#     list_view = assets_page.verify_list_view_button()
#     assert list_view == True, 'List-View button is not Present in all Assets Header_Section'
#     my_comment = 'Sorting Button is not Present in All Assets Header-Section '
#     sorting_button = assets_page.verify_sorting_filter()
#     assert sorting_button == True, 'Sorting Button is not Present in All Assets Header-Section '
#     my_comment = 'File Type Filter is not Present in All-Assets Page'
#     file_type = assets_page.verify_file_type_text()
#     assert file_type == True, 'File Type Filter is not Present in All-Assets Page'
#     my_comment = 'movie card is not present in All-Assets page'
#     movie_card = assets_page.verify_all_assets_first_card()
#     assert movie_card == True, 'movie card is not present in All-Assets page'
#     my_comment = 'Total Result count is not present in All-Assets page '
#     result_count = assets_page.verify_all_assets_result()
#     assert result_count == True, 'Total Result count is not present in All-Assets page '
#     my_comment = 'Pagination Section is not present / Next button is not present'
#     pagination_next = assets_page.verify_pagination_next_button()
#     assert pagination_next == True, 'Pagination Section is not present / Next button is not present'
#     my_comment = '''All Assets tab Have following elements:-
#
# 1. Reset filter button
# 2. Collapse all button
# 3. Select all button
# 4. View tabs
# 5. Sorting filter
# 6. Filter
# 7. Results
# 8. Images cards
# 9. Pagination
# '''
#
#
# #@allure.title('TC_326: Verify reset filter button is resetting filter')
# def test_click_reset_filter_button(browser):
#     assets_page = AssetsPage(browser)
#     global test, my_comment
#     test = test_case_ids[325]  # 1135
#     my_comment = 'Select All button is not clickable / All Items are not Selected '
#     assets_page.click_photo_images_checkbox()
#     my_comment = 'Count-Number is not present in Video properties / Asset Type clear Filter is not Working'
#     count_text = assets_page.verify_selected_checkbox_count()
#     assert count_text == '1', 'Count-Number is not present in Video properties'
#     my_comment = 'reset filter is not clickable / All Items are Selected'
#     reset_button = assets_page.click_reset_filter_button_all_assets()
#     assert reset_button == False, 'reset filter is not clickable / All Items are still Selected'
#     my_comment = 'On click reset filter button all selected filter should be reset'
#
#
# #@allure.title('TC_327: Verify collapse all button is collapsing all filter dropdown')
# def test_click_collapse_all_button(browser):
#     assets_page = AssetsPage(browser)
#     global test, my_comment
#     test = test_case_ids[326]  # 1136
#     my_comment = 'Collapse-All button is not clickable/collapse button is not hiding Filter Section'
#     collapse_all = assets_page.click_all_assets_collapse_all_button()
#     assert collapse_all == False, 'Collapse-All button is not clickable/collapse button is not hiding Filter Section'
#     my_comment = '''If any of the  filter item is not expanded then "collapsing " option should be enabled, on click of which all the filter items should get expanded at once.
#
# If All the filters are expanded already then "collapse all" button should be enable, on click of which all the filter items should get collapse at once.'''
#
#
# #@allure.title('TC_328: Verify select all button is selecting all Results ')
# def test_click_select_all_button_selecting_assets(browser):
#     assets_page = AssetsPage(browser)
#     global test, my_comment
#     test = test_case_ids[327]  # 1137
#     my_comment = 'Select All button is not clickable / All Items are not Selected'
#     select_all = assets_page.click_all_assets_select_all_button()
#     assert select_all == True, 'Select All button is not clickable / All Items are not Selected '
#     my_comment = 'On click select all button all the results of that page should be selected'
#
#
# #@allure.title('TC_329: Verify user is able to deselect all results')
# def test_click_select_all_button_unselecting_assets(browser):
#     assets_page = AssetsPage(browser)
#     global test, my_comment
#     test = test_case_ids[328]  # 1138
#     my_comment = 'Select All button is not clickable / All Items are not Selected'
#     select_all = assets_page.click_again_all_assets_select_all_button()
#     assert select_all == False, 'Select All button is not clickable / All Items are not Selected'
#     my_comment = 'On double click checkboxes should be deselect'
#
#
# #@allure.title('TC_330: Verify user is able to switch between grid view and list view')
# def test_click_list_and_grid_button_assets(browser):
#     assets_page = AssetsPage(browser)
#     global test, my_comment
#     test = test_case_ids[329]  # 1139
#     my_comment = 'List View is not present / File Name text is not present in list view '
#     list_view = assets_page.click_list_view_button()
#     assert list_view == True, 'List View is not present / File Name text is not present in list view '
#     my_comment = 'Grid View is not present / File Name text is not present in grid view'
#     grid_view = assets_page.click_grid_view_button()
#     assert grid_view == False, 'Grid View is not present / File Name text is not present in grid view'
#     my_comment = 'On click of the view button, view should change in respect to the button clicked'
#
#
# #@allure.title('TC_331: Verify List view')
# def test_verify_list_view_elements_assets(browser):
#     assets_page = AssetsPage(browser)
#     global test, my_comment
#     test = test_case_ids[330]  # 1140
#     my_comment = 'List View is not present / File Name Text is not present in list view '
#     file_name = assets_page.click_list_view_button()
#     assert file_name == True, 'List View is not present / File Name Text is not present in list view '
#     my_comment = ' File Size Text is not present in list view '
#     file_size = assets_page.verify_file_size_text()
#     assert file_size == True, ' File Size Text is not present in list view '
#     my_comment = 'Asset Type Text is not Present in list View'
#     asset_type = assets_page.verify_asset_type_text()
#     assert asset_type == True, 'Asset Type Text is not Present in list View'
#     my_comment = 'checkbox is not present in All Assets list view'
#     check_box = assets_page.verify_list_first_checkbox()
#     assert check_box == True, 'checkbox is not present in All Assets list view'
#     my_comment = 'Add to cart button is not clickable / Add To Cart popup is not open'
#     add_to_cart = assets_page.verify_add_to_cart_clickable()
#     assert add_to_cart == True, 'Add to cart button is not clickable / Add To Cart popup is not open'
#     my_comment = '''List view should show tabular structure with following columns
# 1.File name
# 2. File size
# 3. Asset Type
# 5. Cart icon button:- on click add to cart icon add to cart popup should be opened'''
#
#
# #@allure.title('TC_332: Verify the options of Sorting and their functionality')
# def test_verify_all_sorting_functionality_assets(browser):
#     assets_page = AssetsPage(browser)
#     global test, my_comment
#     test = test_case_ids[331]  # 1141
#     my_comment = 'Reset Filter is not Present in All Assets Header-Section'
#     assets_page.assets_page_refresh()
#     assets_page.click_all_assets_button()
#     reset_filter = assets_page.verify_reset_filter_button()
#     assert reset_filter == True, 'Reset Filter is not Present in All Assets Header-Section'
#     my_comment = 'List View is not present / File Name text is not present in list view '
#     list_view = assets_page.click_list_view_button()
#     assert list_view == True, 'List View is not present / File Name text is not present in list view '
#     assets_page.click_sorting_filter()
#     my_comment = 'Larger to smaller Size Filter is not working'
#     first_file, second_file = assets_page.click_sorting_file_size_up_filter()
#     assert first_file > second_file, 'Larger to smaller Size Filter is not working'
#     assets_page.click_sorting_filter()
#     my_comment = 'smaller to larger Size Filter is not working'
#     first_file_down, second_file_down = assets_page.click_sorting_file_size_down_filter()
#     assert first_file_down <= second_file_down, 'smaller to larger Size Filter is not working'
#     assets_page.click_sorting_filter()
#     assets_page.verify_file_sorting_a_to_z()
#     assets_page.click_sorting_filter()
#     assets_page.verify_file_sorting_z_to_a()
#     assets_page.click_sorting_filter()
#     my_comment = 'Down Date Filter is not working '
#     date_time_up = assets_page.mouse_hover_on_first_file_image()
#     assert date_time_up == True, 'Down Date Filter is not working '
#     assets_page.click_sorting_filter()
#     my_comment = 'Up Date Filter is not working'
#     date_time_down = assets_page.mouse_hover_on_Second_file_image()
#     assert date_time_down == True, 'Up Date Filter is not working'
#     my_comment = '''Sorting drop down should have the following options with mentioned behaviour
# 1. File size (Low to high)  -- Titles should be ordered in Increasing order
# 2. File size (highTo low)  -- Titles should be ordered in Decreasing corder
# 3. Sort A-Z  -- Assets should be ordered in Ascending order of Alphabets
# 4. Sort Z-A -- Assets should be ordered in Descending order of Alphabets
# 5. Sort by Date (Old to New) -- Titles should be ordered in Descending order of Added Date
# 6. Sort by Date (New to Old) -- Titles should be ordered in Ascending order of Added Date
#
# '''
#
#
# #@allure.title('TC_333: Verify Filter Elements')
# def test_verify_left_filter_elements_assets(browser):
#     assets_page = AssetsPage(browser)
#     global test, my_comment
#     test = test_case_ids[332]  # 1142
#     my_comment = 'Reset Filter is not Present in All Assets Header-Section'
#     assets_page.assets_page_refresh()
#     assets_page.click_all_assets_button()
#     reset_filter = assets_page.verify_reset_filter_button()
#     assert reset_filter == True, 'Reset Filter is not Present in All Assets Header-Section'
#     my_comment = 'File Type Dropdown is not present in Asset page'
#     file_type = assets_page.verify_file_type_filter_dropdown()
#     assert file_type == True, 'File Type Dropdown is not present in Asset page'
#     my_comment = 'Asset Type is not present in Asset page'
#     asset_type = assets_page.verify_asset_type_filter_dropdown()
#     assert asset_type == True, 'Asset Type is not present in Asset page'
#     my_comment = 'File-Size is not present in Asset Page'
#     video_properties = assets_page.verify_video_properties_dropdown()
#     assert video_properties == True, 'Video Properties are not present in Asset page'
#     file_size = assets_page.verify_file_size_filter_dropdown()
#     assert file_size == True, 'File-Size is not present in Asset Page'
#     my_comment = '''Filter have following elements:-
# 1. File Type filter
# 2. Video properties filter
# 3. Assets Type filter
# 4, File size filter
# '''
#
#
# #@allure.title('TC_334: Verify File type filter functionality')
# def test_verify_file_type_functionality_assets(browser):
#     assets_page = AssetsPage(browser)
#     global test, my_comment
#     global total_asset
#     test = test_case_ids[333]  # 1143
#     my_comment = 'Count-Number is not present in File type Filter / File Type filter is not working'
#     total_asset = assets_page.verify_total_count_asset()
#     assets_page.click_pdf_checkbox_file_type()
#     after_filter = assets_page.verify_total_count_asset()
#     count_text = assets_page.verify_selected_checkbox_count()
#     assert count_text == '1', 'Count-Number is not present in file type filter'
#     assets_page.click_file_type_clear_button()
#     my_comment = 'clear button is not clickable'
#     after_clear = assets_page.verify_total_count_asset()
#     assert (after_clear > after_filter) & (total_asset == after_clear), 'clear button is not clickable'
#     my_comment = '''1. On click file type filter a dropdown should opened
# 2. Clear Button:- On click Clear button File type filters should be reseted
# 3. Checkboxes with mention file Type
# 4 Total checkboxes selected count
# '''
#
#
# #@allure.title('TC_335: Verify user is able to filter Assets by File type')
# def test_verify_single_file_filter_assets(browser):
#     assets_page = AssetsPage(browser)
#     global test, my_comment
#     test = test_case_ids[334]  # 1144
#     my_comment = 'Count-Number is not present in File type Filter / File Type filter is not working'
#     assets_page.click_pdf_checkbox_file_type()
#     after_filter = assets_page.verify_total_count_asset()
#     count_text = assets_page.verify_selected_checkbox_count()
#     assert count_text == '1', 'Count-Number is not present in File type filter'
#     assets_page.click_file_type_clear_button()
#     after_clear = assets_page.verify_total_count_asset()
#     assert (after_clear > after_filter) & (total_asset == after_clear), 'Type File Filter is not present or not working'
#     my_comment = '''User should be able to filter assets by File type by selecting the Checkboxes from the drop-down
# Search Result should show assets which has the selected Checkboxes'''
#
#
# #@allure.title('TC_336: Verify user is able to apply multiple Checkboxes filters')
# def test_verify_multiple_file_filter_assets(browser):
#     assets_page = AssetsPage(browser)
#     global test, my_comment
#     test = test_case_ids[335]  # 1145
#     my_comment = 'Count-Number is not present in file type / Type File Filter is not present or not working'
#     assets_page.click_pdf_checkbox_file_type()
#     assets_page.click_jpeg_checkbox_file_type()
#     after_filter = assets_page.verify_total_count_asset()
#     count_text = assets_page.verify_selected_checkbox_count()
#     assert count_text == '2', 'Count-Number is not present in File type filter'
#     assets_page.click_file_type_clear_button()
#     after_clear = assets_page.verify_total_count_asset()
#     assert (after_clear > after_filter) & (total_asset == after_clear), 'Type File Filter is not present or not working'
#     my_comment = 'User should be able to select multiple File Type filters ' \
#                  'Search results should show all Assets which have the selected Checboxes'
#
#
# #@allure.title('TC_337: Verify Video Properties filter elements')
# def test_verify_video_properties_elements(browser):
#     assets_page = AssetsPage(browser)
#     global test, my_comment
#     test = test_case_ids[336]  # 1146
#     my_comment = 'Video Properties heading is not Present in Asset Section'
#     video_text = assets_page.verify_video_properties_text()
#     assert video_text == True, 'Video Properties heading is not Present in Asset Section'
#     my_comment = 'Video Resolution checkbox is not present in Video Properties'
#     video_resolution = assets_page.verify_video_resolution_text()
#     assert video_resolution == True, 'Video Resolution checkbox is not present in Video Properties'
#     my_comment = 'Video frame-rate checkbox is not present in Video Properties'
#     video_frame_rate = assets_page.verify_video_frame_rate_text()
#     assert video_frame_rate == True, 'Video frame-rate checkbox is not present in Video Properties'
#     assets_page.click_video_frame_rate_checkbox()
#     my_comment = 'Count-Number is not present in Video properties'
#     count_text = assets_page.verify_selected_checkbox_count()
#     assert count_text == '1', 'Count-Number is not present in Video properties / Type ' \
#                               'File Filter is not present or not working'
#     after_filter = assets_page.verify_total_count_asset()
#     assets_page.click_clear_button_video_property()
#     after_clear = assets_page.verify_total_count_asset()
#     assert (after_clear > after_filter) & (total_asset == after_clear), 'Type File Filter is not present or not working'
#     my_comment = '''1. On click Video Properties filter a dropdown should opened
# 2. Clear Button:- On click Clear button Video Properties filters should be rested
# 3. Checkboxes with mention Video Properties
# 4 Total checkboxes selected count
# 5. Resolution filters
# 6. Frame rate filters'''
#
#
# #@allure.title('TC_338: Verify user is able to filter assets by Video Properties')
# def test_verify_single_filter_video_properties_asset(browser):
#     assets_page = AssetsPage(browser)
#     global test, my_comment
#     test = test_case_ids[337]  # 1147
#     my_comment = 'Count-Number is not present in Video properties / Type File Filter is not present or not working'
#     assets_page.click_video_frame_rate_checkbox()
#     count_text = assets_page.verify_selected_checkbox_count()
#     assert count_text == '1', 'Count-Number is not present in Video properties'
#     after_filter = assets_page.verify_total_count_asset()
#     assets_page.click_clear_button_video_property()
#     after_clear = assets_page.verify_total_count_asset()
#     assert (after_clear > after_filter) & (total_asset == after_clear), 'Type File Filter is not present or not working'
#     my_comment = '''User should be able to filter assets by Video Properties by selecting the Checkboxes from the drop-down
# Search Result should show assets which has the selected Checkboxes'''
#
#
# #@allure.title('TC_339: Verify user is able to apply multiple Checkboxes filters')
# def test_verify_multiple_filter_video_properties_asset(browser):
#     assets_page = AssetsPage(browser)
#     global test, my_comment
#     test = test_case_ids[338]  # 1148
#     my_comment = 'Count-Number is not present in Video properties/ Type File Filter is not present or not working'
#     assets_page.click_video_frame_rate_checkbox()
#     assets_page.click_video_resolution_checkbox()
#     count_text = assets_page.verify_selected_checkbox_count()
#     assert count_text == '2', 'Count-Number is not present in Video properties'
#     after_filter = assets_page.verify_total_count_asset()
#     assets_page.click_clear_button_video_property()
#     after_clear = assets_page.verify_total_count_asset()
#     assert (after_clear > after_filter) & (total_asset == after_clear), 'Type File Filter is not present or not working'
#     my_comment = 'User should be able to select multiple Video Properties filters Search results' \
#                  ' should show all Assets which have the selected Checboxes'
#
#
# #@allure.title('TC_340: Verify Assets Type filter elements')
# def test_verify_assets_type_filter_elements(browser):
#     assets_page = AssetsPage(browser)
#     global test, my_comment
#     test = test_case_ids[339]  # 1149
#     my_comment = 'Video Properties heading is not Present in Asset Section'
#     video_text = assets_page.verify_asset_type_heading_text()
#     assert video_text == True, 'Video Properties heading is not Present in Asset Section'
#     my_comment = 'Document text is not present in asset type Section'
#     documents_text = assets_page.verify_asset_type_documents()
#     assert documents_text == True, 'Document text is not present in asset type Section'
#     my_comment = 'Image Filter text is not present in asset type section'
#     image_photo = assets_page.verify_asset_type_photo_image()
#     assert image_photo == True, 'Image Filter text is not present in asset type section'
#     my_comment = 'Ads Filter is not Present in asset type Section'
#     ads_type = assets_page.verify_asset_type_ads()
#     assert ads_type == True, 'Ads Filter is not Present in asset type Section'
#     my_comment = 'Video Filter is not present in asset type Section'
#     video_filter = assets_page.verify_asset_type_video()
#     assert video_filter == True, 'Video Filter is not present in asset type Section'
#     assets_page.click_document_script_checkbox()
#     after_filter = assets_page.verify_total_count_asset()
#     my_comment = 'Asset Type clear Filter is not Working'
#     count_text = assets_page.verify_selected_checkbox_count()
#     assert count_text == '1', 'Count-Number is not present in Video properties'
#     assets_page.click_clear_button_asset_type_property()
#     after_clear = assets_page.verify_total_count_asset()
#     assert (after_clear > after_filter) & (total_asset == after_clear), 'Asset Type clear Filter is not Working'
#     my_comment = '''1. On click Assets Type filter a dropdown should opened
# 2. Clear Button:- On click Clear button Assets Type filters should be reseted
# 3. Checkboxes with mention Assets Type
# 4 Total checkboxes selected count
# 5. Documents filters
# 6. Photos/Images filter
# 7. Ads Filter
# 8. Videos filter'''
#
#
# #@allure.title('TC_341: Verify user is able to filter assets by Assets Type')
# def test_verify_single_assets_type(browser):
#     assets_page = AssetsPage(browser)
#     global test, my_comment
#     test = test_case_ids[340]  # 1150
#     my_comment = 'Count-Number is not present in Asset Type filter / Asset Type clear Filter is not Working'
#     assets_page.click_document_script_checkbox()
#     after_filter = assets_page.verify_total_count_asset()
#     count_text = assets_page.verify_selected_checkbox_count()
#     assert count_text == '1', 'Count-Number is not present in Asset type filter'
#     assets_page.click_clear_button_asset_type_property()
#     after_clear = assets_page.verify_total_count_asset()
#     assert (after_clear > after_filter) & (total_asset == after_clear), 'Asset Type clear Filter is not Working'
#     my_comment = 'User should be able to filter assets by Assets Type by selecting the Checkboxes from ' \
#                  'the drop-down Search Result should show assets which has the selected Checkboxes'
#
#
# #@allure.title('TC_342: Verify user is able to apply multiple Checkboxes filters')
# def test_verify_multiple_assets_type(browser):
#     assets_page = AssetsPage(browser)
#     global test, my_comment
#     test = test_case_ids[341]  # 1151
#     my_comment = 'Count-Number is not present in Asset Type filter / Asset Type clear Filter is not Working'
#     assets_page.click_document_script_checkbox()
#     assets_page.click_document_paid_ad_memo_checkbox()
#     after_filter = assets_page.verify_total_count_asset()
#     count_text = assets_page.verify_selected_checkbox_count()
#     assert count_text == '2', 'Count-Number is not present in Video properties'
#     assets_page.click_clear_button_asset_type_property()
#     after_clear = assets_page.verify_total_count_asset()
#     assert (after_clear > after_filter) & (total_asset == after_clear), 'Asset Type clear Filter is not Working'
#     my_comment = 'User should be able to select multiple Assets Type filters Search ' \
#                  'results should show all Assets which have the selected Checboxes'
#
#
# #@allure.title('TC_343: Verify file size filter functionality')
# def test_verify_size_filter_functionality_asset(browser):
#     assets_page = AssetsPage(browser)
#     global test, my_comment
#     test = test_case_ids[342]  # 1152
#     my_comment = 'File-Size heading text is not present'
#     file_size = assets_page.verify_file_size_heading_text()
#     assert file_size == True, 'File-Size heading text is not present'
#     assets_page.verify_size_filter()
#     after_filter = assets_page.verify_total_count_asset()
#     assets_page.click_reset_button_files_size_property()
#     my_comment = 'Asset Type clear Filter is not Working'
#     after_clear = assets_page.verify_total_count_asset()
#     assert (after_clear > after_filter) & (total_asset == after_clear), 'Asset Type clear Filter is not Working'
#     my_comment = '''1. On clickFile size  filter a dropdown should opened
# 2. Reset Button:- On click Clear button File size  filters should be reseted
# 3. Range selector
# '''
#
#
# #@allure.title('TC_344: Verify user is able to apply range selector ')
# def test_verify_range_selector_functionality_asset(browser):
#     assets_page = AssetsPage(browser)
#     global test, my_comment
#     test = test_case_ids[343]  # 1153
#     my_comment = 'File-Size heading text is not present'
#     file_size = assets_page.verify_file_size_heading_text()
#     assert file_size == True, 'File-Size heading text is not present'
#     assets_page.verify_size_filter()
#     after_filter = assets_page.verify_total_count_asset()
#     assets_page.click_reset_button_files_size_property()
#     my_comment = 'Asset Type clear Filter is not Working'
#     after_clear = assets_page.verify_total_count_asset()
#     assert (after_clear > after_filter) & (total_asset == after_clear), 'Asset Type clear Filter is not Working'
#     my_comment = 'User should be able to apply range selector on assets '
#
#
# #@allure.title('TC_345: Verify assets cards elements')
# def test_verify_card_elements_asset(browser):
#     assets_page = AssetsPage(browser)
#     global test, my_comment
#     test = test_case_ids[344]  # 1154
#     my_comment = 'Preview button is not present on First-Card'
#     preview_button = assets_page.mouse_hover_first_card_preview_button()
#     assert preview_button == True, 'Preview button is not present on First-Card'
#     my_comment = 'Download button is not present in card'
#     download_button = assets_page.mouse_hover_first_card_download_button()
#     assert download_button == True, 'Download button is not present in card'
#     my_comment = 'Add to Cart button is not present'
#     add_to_cart = assets_page.mouse_hover_first_card_add_to_cart_button()
#     assert add_to_cart == True, 'Add to Cart button is not present'
#     my_comment = 'Checkbox is present on Card'
#     card_checkbox = assets_page.verify_grid_card_checkbox()
#     assert card_checkbox == True, 'Checkbox is present on Card'
#     my_comment = '''Assets cards have following elements:-
#
# 1. Checkbox
# 2, Preview button
# 3.Add to cart button
# 4. Download button'''
#
#
# #@allure.title('TC_346: Verify user is able to select checkbox on any asset')
# def test_click_first_card_checkbox_asset(browser):
#     assets_page = AssetsPage(browser)
#     global test, my_comment
#     test = test_case_ids[345]  # 1155
#     my_comment = 'Checkbox is not clickable / footer popup is not open after clicking on checkbox'
#     assets_page.click_first_grid_card_checkbox()
#     single_item = assets_page.verify_single_item_selected()
#     assert single_item == True, 'Checkbox is not clickable / footer popup is not open after clicking on checkbox'
#     my_comment = 'user should be able to select checkbox of any asset'
#
#
# #@allure.title('TC_347: Verify user is able to select checkbox on any asset')
# def test_click_second_card_checkbox_asset(browser):
#     assets_page = AssetsPage(browser)
#     global test, my_comment
#     test = test_case_ids[346]  # 1156
#     my_comment = 'Checkbox is not clickable / footer popup is not open after clicking on checkbox'
#     assets_page.click_second_grid_card_checkbox()
#     single_item = assets_page.verify_two_items_selected()
#     assert single_item == True, 'Checkbox is not clickable / footer popup is not open after clicking on checkbox'
#     my_comment = 'User should be able to select multiple assets  checkboxes at same time'
#
#
# #@allure.title('TC_348: Verify footer popup is shown after selecting checkboxes')
# def test_verify_checkbox_footer_asset(browser):
#     assets_page = AssetsPage(browser)
#     global test, my_comment
#     test = test_case_ids[347]  # 1157
#     my_comment = 'Checkbox is not clickable / footer popup is not open after clicking on checkbox'
#     multiple_item = assets_page.verify_two_items_selected()
#     assert multiple_item == True, 'Checkbox is not clickable / footer popup is not open after clicking on checkbox'
#     my_comment = 'While click on checkboxes a footer popup should be opened'
#
#
# #@allure.title('TC_349: Verify footer popup elements')
# def test_verify_card_footer_elements_asset(browser):
#     assets_page = AssetsPage(browser)
#     global test, my_comment
#     test = test_case_ids[348]  # 1158
#     my_comment = 'Add to Cart is not present in Footer popup'
#     add_to_cart = assets_page.verify_footer_add_to_cart()
#     assert add_to_cart == True, 'Add to Cart is not present in Footer popup'
#     my_comment = 'Download button is not present in footer popup'
#     download_button = assets_page.verify_footer_download()
#     assert download_button == True, 'Download button is not present in footer popup'
#     my_comment = 'Checkbox is not clickable / footer popup is not open after clicking on checkbox'
#     item_count = assets_page.verify_two_items_selected()
#     assert item_count == True, 'Checkbox is not clickable / footer popup is not open after clicking on checkbox'
#     my_comment = '''Footer popup have following elements:-
# 1. Total selected assets count
# 2. Download cart button
# 3. Add to cart button
# '''
#
#
# #@allure.title('TC_351: Verify count of selected checkboxes on footer popup')
# def test_footer_selected_item_count_asset(browser):
#     assets_page = AssetsPage(browser)
#     global test, my_comment
#     test = test_case_ids[350]  # 1160
#     my_comment = 'Checkbox is not clickable / footer popup is not open after clicking on checkbox'
#     item_count = assets_page.verify_two_items_selected()
#     assert item_count == True, 'Checkbox is not clickable / footer popup is not open after clicking on checkbox'
#     my_comment = 'User is able to see counts of selected checkboxes '
#
#
# #@allure.title('TC_352: Verify add to cart button from footer popup')
# def test_footer_add_to_cart_clickable_asset(browser):
#     assets_page = AssetsPage(browser)
#     global test, my_comment
#     test = test_case_ids[351]  # 1161
#     my_comment = 'Add to cart is not clickable'
#     add_to_cart = assets_page.click_footer_add_to_cart_button()
#     assert add_to_cart == True, 'Add to cart is not clickable'
#     my_comment = 'On click add to cart button add to cart  popup should be opened'
#
#
# #@allure.title('TC_350: Verify footer popup download cart button is clickable')
# def test_verify_footer_download_button_asset(browser):
#     assets_page = AssetsPage(browser)
#     global test, my_comment
#     test = test_case_ids[349]  # 1159
#     my_comment = 'Footer Download button is not clickable'
#     assets_page.assets_page_refresh()
#     assets_page.click_all_assets_button()
#     assets_page.click_first_grid_card_checkbox_download()
#     assets_page.click_footer_download_button()
#     footer_download = assets_page.verify_footer_download_clickable()
#     assert footer_download == True, 'Footer Download button is not clickable'
#     my_comment = 'On click download cart button then download cart popup should be opened'
#
#
# #@allure.title('TC_356: Verify preview button is clickable')
# def test_verify_preview_button_clickable_asset(browser):
#     assets_page = AssetsPage(browser)
#     global test, my_comment
#     test = test_case_ids[355]  # 1165
#     my_comment = 'Updated date is not present on Preview page'
#     assets_page.assets_page_refresh()
#     assets_page.click_all_assets_button()
#     assets_page.click_first_card_preview_button()
#     date_time = assets_page.verify_date_preview_page()
#     assert date_time == True, 'Updated date is not present on Preview page'
#     my_comment = 'On click prevoew button a popup should be opened for preview images and pdf'
#
#
# #@allure.title('TC_359: Verify preview popup elements ')
# def test_verify_preview_page_elements_asset(browser):
#     assets_page = AssetsPage(browser)
#     global test, my_comment
#     test = test_case_ids[358]  # 1168
#     my_comment = 'Close button is not present on Preview-Page'
#     close_button = assets_page.verify_preview_close_button()
#     assert close_button == True, 'Close button is not present on Preview-Page'
#     my_comment = 'image or pdf is not present on Preview-Page'
#     preview_image = assets_page.verify_preview_image_pdf()
#     assert preview_image == True, 'image or pdf is not present on Preview-Page'
#     my_comment = 'Download Button is not present on Preview-Page'
#     # download_button = assets_page.verify_preview_download_button() #elements are not present
#     # assert download_button == True, 'Download Button is not present on Preview-Page'
#     my_comment = 'Add To Cart button is not Present on Preview-Page'
#     add_to_cart = assets_page.verify_preview_add_to_cart_button()
#     assert add_to_cart == True, 'Add To Cart button is not Present on Preview-Page'
#     my_comment = 'Next Icon button is not present on Preview-Page'
#     next_icon = assets_page.verify_preview_next_icon_button()
#     assert next_icon == True, 'Next Icon button is not present on Preview-Page'
#     my_comment = 'Description Text is not present in Preview-Page'
#     description_text = assets_page.verify_preview_page_description()
#     assert description_text == True, 'Description Text is not present in Preview-Page'
#     my_comment = 'Previous button is not present in preview-page'
#     previous_button = assets_page.verify_previous_icon_button()
#     assert previous_button == True, 'Previous button is not present in preview-page'
#     my_comment = '''Preview popup have following elements:-
# 1. Close button
# 2. Asset image or pdf
# 3 next navigation arrow
# 4. prev navigation arrow
# 5. Download asset icon
# 6. Add to cart icon
# 7 Asset description'''
#
#
# #@allure.title('TC_360: verify close button is clickable')
# def test_verify_preview_close_button_asset(browser):
#     assets_page = AssetsPage(browser)
#     global test, my_comment
#     test = test_case_ids[359]  # 1169
#     my_comment = 'Close button is not clickable'
#     close_button = assets_page.click_preview_close_button()
#     assert close_button == False, 'Close button is not clickable'
#     my_comment = 'On click close button popup should be closed'
#
#
# #@allure.title('TC_361: Verify Prev navigation arrow')
# def test_verify_preview_previous_navigation_asset(browser):
#     assets_page = AssetsPage(browser)
#     global test, my_comment
#     test = test_case_ids[360]  # 1170
#     my_comment = 'Previous button is not clickable in preview-page'
#     assets_page.click_first_card_preview_button()
#     next_button_clickable = assets_page.verify_previous_icon_button_clickable()
#     assert next_button_clickable == False, 'Previous button is not clickable in preview-page'
#     my_comment = '''1. If user is on first asset then prev arrow should be hidden
# 2. On click prev arrow user is able to redirect previous asset
# '''
#
#
# #@allure.title('TC_362: Verify Next navigation arrow')
# def test_verify_preview_next_navigation_asset(browser):
#     assets_page = AssetsPage(browser)
#     global test, my_comment
#     test = test_case_ids[361]  # 1171
#     my_comment = 'Next button is not clickable in preview-page'
#     next_button_clickable = assets_page.verify_previous_icon_button()
#     assert next_button_clickable == True, 'Next button is not clickable in preview-page'
#     my_comment = '''1. If user is on Last asset then next arrow should be hidden
# 2. On click Next arrow user is able to redirect Next asset
# '''
#
#
# #@allure.title('TC_365: Verify Add to cart button is clickable ')
# def test_click_preview_add_to_cart_asset(browser):
#     assets_page = AssetsPage(browser)
#     global test, my_comment
#     test = test_case_ids[364]  # 1174
#     my_comment = 'Add To Cart button is not present / add to cart button is not clickable'
#     cart_popup = assets_page.click_preview_add_to_cart_button()
#     assert cart_popup == True, 'Add To Cart button is not present / add to cart button is not clickable'
#     my_comment = 'On click add to cart button add to cart  popup should be opened'
#
#
# #@allure.title('TC_357: verify add to cart button is clickable')
# def test_verify_card_add_to_cart_button(browser):
#     assets_page = AssetsPage(browser)
#     global test, my_comment
#     test = test_case_ids[356]  # 1166
#     my_comment = 'Add to cart button is not clickable'
#     assets_page.assets_page_refresh()
#     assets_page.click_all_assets_button()
#     cart_pop_up = assets_page.click_first_card_add_to_cart_button()
#     assert cart_pop_up == True, 'Add to cart button is not clickable'
#     my_comment = 'On click add to cart button add to cart  popup should be opened'
#
#
# #@allure.title('TC_366: Verify Download cart popup Elements:-')
# def test_verify_footer_download_cart_popup_button_asset(browser):
#     assets_page = AssetsPage(browser)
#     global test, my_comment
#     test = test_case_ids[365]  # 1175
#     my_comment = 'Download button is not present in footer popup'
#     assets_page.assets_page_refresh()
#     assets_page.click_all_assets_button()
#     assets_page.click_first_grid_card_checkbox_download()
#     assets_page.click_footer_download_button()
#     footer_download = assets_page.verify_footer_download_button()
#     assert footer_download == True, 'Download button is not present in footer popup'
#     my_comment = 'Cancel button is not present in Footer popup'
#     footer_cancel = assets_page.verify_footer_cancel_button()
#     assert footer_cancel == True, 'Cancel button is not present in Footer popup'
#     my_comment = 'close button is not present in Footer popup'
#     close_button = assets_page.verify_footer_close_button()
#     assert close_button == True, 'close button is not present in Footer popup'
#     my_comment = 'Description text is not present in Footer popup'
#     description_text = assets_page.verify_footer_download_description()
#     assert description_text == True, 'Description text is not present in Footer popup'
#     my_comment = '''Download cart have following elements:-
#
# 1.Close button
# 2. Static text with total selected assets count and file size
# 3. Start download button
# 4. Cancel button'''
#
#
# #@allure.title('TC_368: Verify count of selected items is correct')
# def test_verify_footer_count_selected_item_asset(browser):
#     assets_page = AssetsPage(browser)
#     global test, my_comment
#     test = test_case_ids[367]  # 1177
#     my_comment = 'count of selected item is not same/ selected item is not present'
#     selected_count = assets_page.verify_footer_download_selected_count()
#     assert selected_count == '1', 'count of selected item is not same/ selected item is not present'
#     my_comment = 'Count of selected asstes should be correct'
#
#
# #@allure.title('TC_367: Verify close button is clickable')
# def test_click_footer_close_button_asset(browser):
#     assets_page = AssetsPage(browser)
#     global test, my_comment
#     test = test_case_ids[366]  # 1176
#     my_comment = 'Close button is not Clickable in footer popup'
#     close_button = assets_page.click_footer_close_button()
#     assert close_button == False, 'Close button is not Clickable in footer popup'
#     my_comment = 'On click close button popup should be closed'
#
#
# #@allure.title('TC_369: Verify user is able to download asset')
# def test_click_footer_start_download_button_asset(browser):
#     assets_page = AssetsPage(browser)
#     global test, my_comment
#     test = test_case_ids[368]  # 1178
#     my_comment = 'Download button is not present in footer popup / Download button is not click able'
#     assets_page.click_first_grid_card_checkbox_download()
#     assets_page.click_footer_download_button()
#     footer_download = assets_page.verify_footer_download_button()
#     assert footer_download == True, 'Download button is not present in footer popup'
#     download_text = assets_page.click_footer_start_download_button()
#     assert download_text == True, 'Download button is not click able'
#     my_comment = 'On click start download button downloading should be start'
#
#
# #@allure.title('TC_370: Verify cancel button is clickable')
# def test_click_footer_cancel_button_asset(browser):
#     assets_page = AssetsPage(browser)
#     global test, my_comment
#     test = test_case_ids[369]  # 1179
#     my_comment = 'Cancel button is not present in footer popup / Cancel button is not Clickable in footer Section'
#     assets_page.click_first_grid_card_checkbox_download()
#     assets_page.click_footer_download_button()
#     # footer_download = assets_page.verify_footer_download_button()
#     # assert footer_download == True, 'Download button is not present in footer popup'
#     ##Now Cancel button is not present in footer section
#     cancel_button = assets_page.click_footer_cancel_button()
#     assert cancel_button == False, 'Cancel button is not Clickable in footer Section'
#     my_comment = 'On click cancel button download cart popup should be closed'
#
#
# #@allure.title('TC_371: Verify user is able to enter name and create new cart')
# def test_footer_add_to_cart_Functionality_asset(browser):
#     assets_page = AssetsPage(browser)
#     home = homepage(browser)
#     global test, my_comment
#     test = test_case_ids[370]  # 1180
#     my_comment = 'All Assets button is not clickable'
#     assets_page.assets_page_refresh()
#     assets_page.click_all_assets_button()
#     my_comment = 'Add to cart is not clickable'
#     assets_page.click_first_grid_card_checkbox_download()
#     add_to_cart = assets_page.click_footer_add_to_cart_button()
#     assert add_to_cart == True, 'Add to cart is not clickable'
#     assets_page.enter_cart_name("testingCart")
#     my_comment = 'Create cart button is not clickable / new cart is not Creating'
#     create_cart = assets_page.click_create_cart()
#     assert create_cart == True, 'Create cart button is not clickable / new cart is not Creating'
#     created_text = assets_page.created_cart_text()
#     assert created_text == True, 'Created Text is not visible'
#     my_comment = 'new cart is not Present in Add to cart popup '
#     cart_name = assets_page.verify_cart_created()
#     assert cart_name == True, 'new cart is not Present in Add to cart popup '
#     my_comment = ' cart auto select feature is not working'
#     cart_auto_selected = assets_page.verify_cart_is_auto_select()
#     assert cart_auto_selected == True, ' cart auto select feature is not working'
#     my_comment = '''User should be create cart by following the below steps:
# 1. Click on Add to cart button for any asset
# 2. Enter name
# 3. Click Create cart
#
# Following should also happen along side:
# 1. New cart should appear in the List of Created cart
# 2. Clicking Create cart button should change the textbox to display "Creating..."
# 3. Success message should be shown in the same textbox "Created"
# 4. New cart should get auto selected'''
#
#
# #@allure.title('TC_372: Verify user is able to add the Assets in the created cart')
# def test_card_add_testing_cart_asset(browser):
#     home = homepage(browser)
#     global test, my_comment
#     test = test_case_ids[371]  # 1181
#     time.sleep(2)
#     my_comment = 'add to cart button is not clickable'
#     home.AddMovieToList()
#     assert home.verify_success_text() == True, "add to cart button is not clickable"
#     my_comment = 'Once the cart is created and is auto selected, then clicking on ' \
#                  'add to list button should add the asset to the new cart'
#
#
# #@allure.title('TC_373: Verify user is able to select cart(s)')
# def test_new_cart_testing_cart_selectable(browser):
#     assets_page = AssetsPage(browser)
#     global test, my_comment
#     test = test_case_ids[372]  # 1182
#     my_comment = 'Cart is not selected / cart name is not clickable'
#     assets_page.click_first_grid_card_checkbox_download()
#     add_to_cart = assets_page.click_footer_add_to_cart_button()
#     assert add_to_cart == True, 'Add to cart is not clickable'
#     cart_selected = assets_page.verify_cart_selectable()
#     assert cart_selected == True, 'cart is not selected / cart name is not clickable'
#     my_comment = 'Clicking on the toggle button should select the cart Toggle button should get highlighted'
#
#
# #@allure.title('TC_374: Verify user is able to un-select any selected cart(s)')
# def test_new_cart_testing_cart_un_selectable(browser):
#     assets_page = AssetsPage(browser)
#     global test, my_comment
#     test = test_case_ids[373]  # 1183
#     my_comment = 'cart is Selected / cart name is not clickable'
#     cart_selected = assets_page.verify_cart_selectable()
#     assert cart_selected == False, 'cart is Selected / cart name is not clickable'
#     my_comment = '''Clicking on the toggle button against the selected cart(s) should un-select the cart(s)
# Toggle button should get highlighted'''
#
#
# #@allure.title('TC_375: Verify user is able to add same asset in multiple cart')
# def test_footer_add_to_multiple_cart_Functionality_asset(browser):
#     assets_page = AssetsPage(browser)
#     home = homepage(browser)
#     global test, my_comment
#     test = test_case_ids[374]  # 1184
#     my_comment = 'Create cart button is not clickable / new cart is not Creating'
#     assets_page.enter_cart_name("testingCart2")
#     create_cart = assets_page.click_create_cart()
#     assert create_cart == True, 'Create cart button is not clickable / new cart is not Creating'
#     my_comment = 'Created Text is not visible'
#     created_text = assets_page.created_cart_text()
#     assert created_text == True, 'Created Text is not visible'
#     my_comment = 'new cart is not Present in Add to cart popup '
#     cart_name = assets_page.verify_second_cart_created()
#     assert cart_name == True, 'new cart is not Present in Add to cart popup '
#     my_comment = ' cart auto select feature is not working'
#     cart_auto_selected = assets_page.verify_second_cart_is_auto_select()
#     assert cart_auto_selected == True, ' cart auto select feature is not working'
#     my_comment = "add to cart button is not clickable"
#     home.AddMovieToList()
#     assert home.verify_success_text() == True, "add to cart button is not clickable"
#     my_comment = 'User should be able to add same asset in multiple carts'
#
#
# #@allure.title('TC_376: Verify user is abe to search a cart from the search bar')
# def test_search_testing_cart_name(browser):
#     assets_page = AssetsPage(browser)
#     home = homepage(browser)
#     global test, my_comment
#     test = test_case_ids[375]  # 1185
#     my_comment = 'Enter search term in the search box should perform the search and show correct result'
#     assets_page.click_first_grid_card_checkbox_download()
#     add_to_cart = assets_page.click_footer_add_to_cart_button()
#     assert add_to_cart == True, 'Add to cart is not clickable'
#     home.SearchList("testingCart")
#     search_name = assets_page.verify_search_testing_cart_name()
#     assert search_name == True, 'search bar is not working '
#     my_comment = 'Enter search term in the search box should perform the search and show correct result'
#
#
# #@allure.title('TC_378: Verify user is able to select cart(s) from search result')
# def test_new_cart_testing_search_cart_selectable(browser):
#     assets_page = AssetsPage(browser)
#     global test, my_comment
#     test = test_case_ids[377]  # 1187
#     my_comment = 'cart is not selected / cart name is not clickable'
#     cart_selected = assets_page.verify_cart_selectable()
#     assert cart_selected == True, 'cart is not selected / cart name is not clickable'
#     my_comment = 'User should be able to select cart(s) from search result'
#
#
# #@allure.title('TC_379: Verify user is able to un-select cart(s) from search result')
# def test_new_cart_testing_search_cart_un_selectable(browser):
#     assets_page = AssetsPage(browser)
#     global test, my_comment
#     test = test_case_ids[378]  # 1188
#     my_comment = 'cart is Selected / cart name is not clickable'
#     cart_selected = assets_page.verify_cart_selectable()
#     assert cart_selected == False, 'cart is Selected / cart name is not clickable'
#     my_comment = ' User should be able to un-select cart(s) from search result'
#
#
# #@allure.title('TC_377: Verify user is able to clear search on click of Clear button')
# def test_clear_search_cart_field(browser):
#     home = homepage(browser)
#     global test, my_comment
#     test = test_case_ids[376]  # 1186
#     my_comment = 'clear button is not working'
#     clear_button = home.ClickAddToListClearButton()
#     assert clear_button == True, 'clear button is not working'
#     my_comment = 'On click of Clear button search should be cleared'
#
#
# #@allure.title('TC_380: verify user is  not able to create duplicate cart')
# def test_verify_duplicate_cart_asset(browser):
#     assets_page = AssetsPage(browser)
#     home = homepage(browser)
#     global test, my_comment
#     my_comment = 'User can create Duplicate Cart'
#     test = test_case_ids[379]  # 1189
#     assets_page.enter_cart_name("testingCart")
#     assets_page.click_create_cart_duplicate()
#     duplicate_cart = assets_page.verify_duplicate_cart_name()
#     assert duplicate_cart == True, 'User can create Duplicate Cart'
#     my_comment = 'User is not able to create duplicate cart message is shown "Please enter a unique list name."'
#
#
# #@allure.title('TC_381: Verify on click outside the popup window then popup will hide')
# def test_verify_add_cart_popup_hide_asset(browser):
#     assets_page = AssetsPage(browser)
#     global test, my_comment
#     test = test_case_ids[380]  # 1190
#     my_comment = 'Add to cart popup is present'
#     assets_page.click_reset_text() #removed all assests click methode
#     add_to_cart = assets_page.verify_add_to_cart_footer_not_present()
#     assert add_to_cart == False, 'Add to cart popup is present'
#     my_comment = 'Popup should hide if we click outside the popup window'
#
#
# #@allure.title('TC_382: Verify pagination elements')
# def test_verify_Pagination_elements_asset(browser):
#     film_series = filmSeriesPage(browser)
#     assets_page = AssetsPage(browser)
#     global test, my_comment
#     test = test_case_ids[381]  # 1191
#     assets_page.assets_page_refresh()
#     assets_page.click_all_assets_button()
#     my_comment = 'right cursor is not clickable'
#     right_cursor_click = film_series.click_right_cursor_button()
#     assert right_cursor_click == True, 'right cursor is not clickable'
#     film_series.click_left_cursor_button()
#     my_comment = 'left button cursor is not disabled'
#     disable_text = film_series.verify_left_disabled_cursor()
#     assert 'disabled' in disable_text, 'left button cursor is not disabled'
#     my_comment = 'One page is not Active'
#     active_page = film_series.verify_one_active_page()
#     assert active_page == True, 'One page is not Active'
#     my_comment = 'pages are not disabled'
#     count_of_disable_pages = film_series.verify_expect_one_disabled_pages_button()
#     assert count_of_disable_pages > 1, 'pages are not disabled'
#     my_comment = '''Pagination have following elements:-
# 1. Prev navigation arrow
# 2. Next navigation arrow
# 3. Pages number '''
#
#
# #@allure.title('TC_383: Verify Prev navigation arrow functionality')
# def test_verify_Pagination_prev_arrow_clickable_asset(browser):
#     film_series = filmSeriesPage(browser)
#     global test, my_comment
#     test = test_case_ids[382]  # 1192
#     my_comment = 'left button cursor is not disabled'
#     disable_text = film_series.verify_left_disabled_cursor()
#     assert 'disabled' in disable_text, 'left button cursor is not disabled'
#     my_comment = 'right cursor is not clickable'
#     right_cursor_click = film_series.click_right_cursor_button()
#     assert right_cursor_click == True, 'right cursor is not clickable'
#     film_series.click_left_cursor_button()
#     my_comment = 'left button cursor is not disabled'
#     disable_text = film_series.verify_left_disabled_cursor()
#     assert 'disabled' in disable_text, 'left button cursor is not disabled'
#     my_comment = '''1. If user is on first page then prev arrow should be hide
# 2. On click prev arrow page should move to prev page'''
#
#
# #@allure.title('TC_384: Verify Next navigation arrow functionality')
# def test_verify_Pagination_next_arrow_clickable_asset(browser):
#     film_series = filmSeriesPage(browser)
#     global test, my_comment
#     test = test_case_ids[383]  # 1193
#     my_comment = 'right cursor is not clickable'
#     right_cursor_click = film_series.click_right_cursor_button()
#     assert right_cursor_click == True, 'right cursor is not clickable'
#     film_series.click_last_respect_last_page_button_asset()
#     my_comment = 'right button cursor is not disabled'
#     right_disable_text = film_series.verify_right_disabled_cursor_asset()
#     assert 'disabled' in right_disable_text, 'right button cursor is not disabled'
#     my_comment = '''1. If user is on last page then next arrow should be hide
# 2. On click Next arrow page should move to Next page'''
#
#
# #@allure.title('TC_385: Verify pages numbers are clickable')
# def test_click_Pagination_page_number_clickable_asset(browser):
#     film_series = filmSeriesPage(browser)
#     global test, my_comment
#     test = test_case_ids[384]  # 1194
#     my_comment = 'right button cursor is not disabled'
#     film_series.click_left_cursor_button()
#     film_series.click_last_respect_last_page_button_asset()
#     right_disable_text = film_series.verify_right_disabled_cursor_asset()
#     assert 'disabled' in right_disable_text, 'right button cursor is not disabled'
#     my_comment = 'On click any page number user should redirected to that page'
#
#
# #@allure.title('TC_386: Verify Images /Photos tab elements')
# def test_verify_image_photo_elements(browser):
#     assets_page = AssetsPage(browser)
#     global test, my_comment
#     test = test_case_ids[385]  # 1195
#     my_comment = 'Reset Filter is not Present in All Assets Header-Section'
#     assets_page.click_all_images_photo_button()
#     reset_filter = assets_page.verify_reset_filter_button()
#     assert reset_filter == True, 'Reset Filter is not Present in All Assets Header-Section'
#     my_comment = 'Collapse-All is not Present in All Assets Header-Section'
#     collapse_all = assets_page.verify_collapse_all_button()
#     assert collapse_all == True, 'Collapse-All is not Present in All Assets Header-Section'
#     my_comment = 'Select All is not Present in all Assets Header-Section'
#     select_all = assets_page.verify_select_all_button()
#     assert select_all == True, 'Select All is not Present in all Assets Header-Section'
#     my_comment = 'Grid-View button is not Present in All Assets Header-Section'
#     grid_view = assets_page.verify_grid_view_button()
#     assert grid_view == True, 'Grid-View button is not Present in All Assets Header-Section'
#     my_comment = 'List-View button is not Present in all Assets Header_Section'
#     list_view = assets_page.verify_list_view_button()
#     assert list_view == True, 'List-View button is not Present in all Assets Header_Section'
#     my_comment = 'Sorting Button is not Present in All Assets Header-Section '
#     sorting_button = assets_page.verify_sorting_filter()
#     assert sorting_button == True, 'Sorting Button is not Present in All Assets Header-Section '
#     my_comment = 'File Type Filter is not Present in All-Assets Page'
#     file_type = assets_page.verify_file_type_text()
#     assert file_type == True, 'File Type Filter is not Present in All-Assets Page'
#     my_comment = 'movie card is not present in All-Assets page'
#     movie_card = assets_page.verify_all_assets_first_card()
#     assert movie_card == True, 'movie card is not present in All-Assets page'
#     my_comment = 'Total Result count is not present in All-Assets page '
#     result_count = assets_page.verify_all_assets_result()
#     assert result_count == True, 'Total Result count is not present in All-Assets page '
#     my_comment = 'Pagination Section is not present / Next button is not present'
#     pagination_next = assets_page.verify_pagination_next_button()
#     assert pagination_next == True, 'Pagination Section is not present / Next button is not present'
#     my_comment = '''Images /Photos tab Have following elements:-
#
# 1. Reset filter button
# 2. Collapse all button
# 3. Select all button
# 4. View tabs
# 5. Sorting filter
# 6. Filter
# 7. Results
# 8. Images cards
# 9. Pagination
# '''
#
#
# #@allure.title('TC_387: Verify reset filter button is resetting filter')
# def test_click_reset_filter_button_image_photo(browser):
#     assets_page = AssetsPage(browser)
#     global test, my_comment
#     test = test_case_ids[386]  # 1196
#     my_comment = 'Select All button is not clickable / All Items are not Selected '
#     assets_page.click_photo_images_checkbox()
#     my_comment = 'Count-Number is not present in Video properties / Asset Type clear Filter is not Working'
#     count_text = assets_page.verify_selected_checkbox_count()
#     assert count_text == '1', 'Count-Number is not present in Video properties'
#     my_comment = 'reset filter is not clickable / All Items are Selected'
#     reset_button = assets_page.click_reset_filter_button_video()
#     assert reset_button == False, 'reset filter is not clickable / All Items are Selected'
#     my_comment = 'On click reset filter button all selected filter should be reset'
#
#
# #@allure.title('TC_388: Verify collapse all button is collapsing all filter dropdown')
# def test_click_collapse_all_button_images(browser):
#     assets_page = AssetsPage(browser)
#     global test, my_comment
#     test = test_case_ids[387]  # 1197
#     my_comment = 'Collapse-All button is not clickable/collapse button is not hiding Filter Section'
#     collapse_all = assets_page.click_all_images_collapse_all_button()
#     assert collapse_all == False, 'Collapse-All button is not clickable/collapse button is not hiding Filter Section'
#     my_comment = 'On click collapse button all open filters should be collapsed'
#
#
# #@allure.title('TC_389: Verify user is able to select all images on click select all checkbox from header')
# def test_click_select_all_button_selecting_images(browser):
#     assets_page = AssetsPage(browser)
#     global test, my_comment
#     test = test_case_ids[388]  # 1198
#     my_comment = 'Select All button is not clickable / All Items are not Selected'
#     select_all = assets_page.click_all_assets_select_all_button()
#     assert select_all == True, 'Select All button is not clickable / All Items are not Selected '
#     my_comment = 'On click select all button all the results of that page should be selected'
#
#
# #@allure.title('TC_390: Verify user is able to deselect all results')
# def test_click_select_all_button_unselecting_images(browser):
#     assets_page = AssetsPage(browser)
#     global test, my_comment
#     test = test_case_ids[389]  # 1199
#     my_comment = 'Select All button is not clickable / All Items are not Selected'
#     select_all = assets_page.click_again_all_assets_select_all_button()
#     assert select_all == False, 'Select All button is not clickable / All Items are not Selected'
#     my_comment = 'on double click chckboxes should be deselect'
#
#
# #@allure.title('TC_391: Verify user is able to switch between grid view and list view')
# def test_click_list_and_grid_button_images(browser):
#     assets_page = AssetsPage(browser)
#     global test, my_comment
#     test = test_case_ids[390]  # 1200
#     my_comment = 'List View is not present / File Name text is not present in list view'
#     list_view = assets_page.click_list_view_button()
#     assert list_view == True, 'List View is not present / File Name text is not present in list view '
#     my_comment = 'Grid View is not present / File Name text is not present in grid view'
#     grid_view = assets_page.click_grid_view_button()
#     assert grid_view == False, 'Grid View is not present / File Name text is not present in grid view'
#     my_comment = 'On click of the view button, view should change in respect to the button clicked'
#
#
# #@allure.title('TC_392: Verify List view')
# def test_verify_list_view_elements_images(browser):
#     assets_page = AssetsPage(browser)
#     global test, my_comment
#     test = test_case_ids[391]  # 1201
#     my_comment = 'List View is not present / File Name Text is not present in list view '
#     file_name = assets_page.click_list_view_button()
#     assert file_name == True, 'List View is not present / File Name Text is not present in list view '
#     my_comment = ' File Size Text is not present in list view '
#     file_size = assets_page.verify_file_size_text()
#     assert file_size == True, ' File Size Text is not present in list view '
#     my_comment = 'Asset Type Text is not Present in list View'
#     asset_type = assets_page.verify_asset_type_text()
#     assert asset_type == True, 'Asset Type Text is not Present in list View'
#     my_comment = 'checkbox is not present in All Assets list view'
#     check_box = assets_page.verify_list_first_checkbox()
#     assert check_box == True, 'checkbox is not present in All Assets list view'
#     my_comment = 'Add to cart button is not clickable / Add To Cart popup is not open'
#     add_to_cart = assets_page.verify_add_to_cart_clickable()
#     assert add_to_cart == True, 'Add to cart button is not clickable / Add To Cart popup is not open'
#     my_comment = '''List view should show tabular structure with following columns
# 1.File name with checkbox
# 2. File size
# 3. Asset Type
# 4. Download icon button:- On click Icon user should be able to download that asset
# 5. Cart icon button:- on click add to cart icon add to cart popup should be opened'''
#
#
# #@allure.title('TC_393: Verify the options of Sorting and their functionality')
# def test_verify_all_sorting_functionality_images(browser):
#     assets_page = AssetsPage(browser)
#     global test, my_comment
#     test = test_case_ids[392]  # 1202
#     my_comment = 'Reset Filter is not Present in All Assets Header-Section'
#     assets_page.assets_page_refresh()
#     assets_page.click_all_images_photo_button()
#     reset_filter = assets_page.verify_reset_filter_button()
#     assert reset_filter == True, 'Reset Filter is not Present in All Assets Header-Section'
#     my_comment = 'List View is not present / File Name text is not present in list view '
#     list_view = assets_page.click_list_view_button()
#     assert list_view == True, 'List View is not present / File Name text is not present in list view '
#     assets_page.click_sorting_filter()
#     my_comment = 'Larger to smaller Size Filter is not working'
#     first_file, second_file = assets_page.click_sorting_file_size_up_filter()
#     assert first_file > second_file, 'Larger to smaller Size Filter is not working'
#     assets_page.click_sorting_filter()
#     my_comment = 'smaller to larger Size Filter is not working'
#     first_file_down, second_file_down = assets_page.click_sorting_file_size_down_filter_respect()
#     assert first_file_down <= second_file_down, 'smaller to larger Size Filter is not working'
#     assets_page.click_sorting_filter()
#     assets_page.verify_file_sorting_a_to_z()
#     assets_page.click_sorting_filter()
#     assets_page.verify_file_sorting_z_to_a()
#     assets_page.click_sorting_filter()
#     my_comment = 'Down Date Filter is not working '
#     date_time_up = assets_page.mouse_hover_on_first_file_image()
#     assert date_time_up == True, 'Down Date Filter is not working '
#     assets_page.click_sorting_filter()
#     my_comment = 'Up Date Filter is not working'
#     date_time_down = assets_page.mouse_hover_on_Second_file_image()
#     assert date_time_down == True, 'Up Date Filter is not working'
#     my_comment = '''Sorting drop down should have the following options with mentioned behaviour
# 1. File size (Low to high)  -- Titles should be ordered in Increasing order
# 2. File size (highTo low)  -- Titles should be ordered in Decreasing order
# 3. Sort A-Z  -- Assets should be ordered in Ascending order of Alphabets
# 4. Sort Z-A -- Assets should be ordered in Descending order of Alphabets
# 5. Sort by Date (Old to New) -- Titles should be ordered in Decending order of Added Date
# 6. Sort by Date (New to Old) -- Titles should be ordered in Ascending order of Added Date
# '''
#
#
# #@allure.title('TC_394: Verify Filter Elements')
# def test_verify_left_filter_elements_images(browser):
#     assets_page = AssetsPage(browser)
#     global test, my_comment
#     test = test_case_ids[393]  # 1203
#     my_comment = 'Reset Filter is not Present in All Assets Header-Section'
#     assets_page.assets_page_refresh()
#     assets_page.click_all_images_photo_button()
#     reset_filter = assets_page.verify_reset_filter_button()
#     assert reset_filter == True, 'Reset Filter is not Present in All Assets Header-Section'
#     my_comment = 'File Type Dropdown is not present in Asset page'
#     file_type = assets_page.verify_file_type_filter_dropdown()
#     assert file_type == True, 'File Type Dropdown is not present in Asset page'
#     my_comment = 'Asset Type is not present in Asset page'
#     asset_type = assets_page.verify_asset_type_filter_dropdown()
#     assert asset_type == True, 'Asset Type is not present in Asset page'
#     my_comment = 'File-Size is not present in Asset Page'
#     file_size = assets_page.verify_file_size_filter_dropdown()
#     assert file_size == True, 'File-Size is not present in Asset Page'
#     my_comment = '''Filter have following elements:-
#
# 1. File Type filter
# 2. Video properties filter
# 3. Assets Type filter
# 4, File size filter
# '''
#
#
# #@allure.title('TC_395: Verify File type filter functionality')
# def test_verify_file_type_functionality_images(browser):
#     assets_page = AssetsPage(browser)
#     global test, my_comment
#     global total_images
#     test = test_case_ids[394]  # 1204
#     my_comment = 'Count-Number is not present in Video properties'
#     total_images = assets_page.verify_total_count_asset()
#     assets_page.click_jpeg_checkbox_file_type()
#     after_filter = assets_page.verify_total_count_asset()
#     count_text = assets_page.verify_selected_checkbox_count()
#     assert count_text == '1', 'Count-Number is not present in Video properties'
#     assets_page.click_file_type_clear_button()
#     after_clear = assets_page.verify_total_count_asset()
#     assert (after_clear > after_filter) & (total_images == after_clear), 'clear button is not clickable'
#     my_comment = '''1. On click file type filter a dropdown should opened
# 2. Clear Button:- On click Clear button File type filters should be reseted
# 3. Checkboxes with mention file Type
# 4 Total checkboxes selected count
# '''
#
#
# #@allure.title('TC_396: Verify user is able to filter Assets by File type')
# def test_verify_single_file_filter_assets_by_file_type(browser):
#     assets_page = AssetsPage(browser)
#     global test, my_comment
#     test = test_case_ids[395]  # 1205 #523
#     my_comment = 'Count-Number is not present in Video properties/ Type File Filter is not present or not working'
#     assets_page.click_jpeg_checkbox_file_type()
#     after_filter = assets_page.verify_total_count_asset()
#     count_text = assets_page.verify_selected_checkbox_count()
#     assert count_text == '1', 'Count-Number is not present in Video properties'
#     assets_page.click_file_type_clear_button()
#     after_clear = assets_page.verify_total_count_asset()
#     assert (after_clear > after_filter) & (
#             total_images == after_clear), 'Type File Filter is not present or not working'
#     my_comment = 'User should be able to filter assets by File type by selecting the ' \
#                  'Checkboxes from the drop-down Search Result should show assets which has the selected Checkboxes'
#
#
# #@allure.title('TC_399: Verify Assets Type filter elements')
# def test_verify_assets_type_filter_elements_images(browser):
#     assets_page = AssetsPage(browser)
#     global test, my_comment
#     test = test_case_ids[397]  # 1208 #526
#     my_comment = 'Image Filter text is not present in asset type section'
#     image_photo = assets_page.verify_asset_type_photo_image()
#     assert image_photo == True, 'Image Filter text is not present in asset type section'
#     assets_page.click_photo_images_checkbox()
#     my_comment = 'Count-Number is not present in Video properties / Asset Type clear Filter is not Working'
#     after_filter = assets_page.verify_total_count_asset()
#     count_text = assets_page.verify_selected_checkbox_count()
#     assert count_text == '1', 'Count-Number is not present in Video properties'
#     assets_page.click_clear_button_asset_type_property()
#     after_clear = assets_page.verify_total_count_asset()
#     assert (after_clear > after_filter) & (total_images == after_clear), 'Asset Type clear Filter is not Working'
#     my_comment = '''1. On click Assets Type filter a dropdown should opened
# 2. Clear Button:- On click Clear button Assets Type filters should be reseted
# 3. Checkboxes with mention Assets Type
# 4 Total checkboxes selected count
# 5. Photos/Images filter
# '''
#
#
# #@allure.title('TC_400: Verify user is able to filter images by Assets Type')
# def test_assets_type_filter_images(browser):
#     assets_page = AssetsPage(browser)
#     global test, my_comment
#     test = test_case_ids[398]  # 1209  #527
#     my_comment = 'Count-Number is not present in Asset Type Filter Section / Asset Type clear Filter is not Working'
#     assets_page.click_photo_images_checkbox()
#     after_filter = assets_page.verify_total_count_asset()
#     count_text = assets_page.verify_selected_checkbox_count()
#     assert count_text == '1', 'Count-Number is not present in Asset Type Filter Section'
#     assets_page.click_clear_button_asset_type_property()
#     after_clear = assets_page.verify_total_count_asset()
#     assert (after_clear > after_filter) & (total_images == after_clear), 'Asset Type clear Filter is not Working'
#     my_comment = '''User should be able to filter assets by Assets Type by selecting the Checkboxes from the drop-down
# Search Result should show assets which has the selected Checkboxes'''
#
#
# #@allure.title('TC_401: Verify user is able to apply multiple Checkboxes filters')
# def test_multiple_assets_type_filter_images(browser):
#     assets_page = AssetsPage(browser)
#     global test, my_comment
#     test = test_case_ids[399]  # 1210   #528
#     assets_page.click_photo_images_checkbox()
#     assets_page.click_key_art_checkbox()
#     after_filter = assets_page.verify_total_count_asset()
#     my_comment = 'Count-Number is not present in Asset Type Filter Section'
#     count_text = assets_page.verify_selected_checkbox_count()
#     assert count_text == '2', 'Count-Number is not present in Asset Type Filter Section'
#     assets_page.click_clear_button_asset_type_property()
#     my_comment = 'User should be able to select multiple Assets Type filters Search results ' \
#                  'should show all Assets which have the selected Checboxes'
#
#
# #@allure.title('TC_402: Verify file size filter functionality')
# def test_verify_size_filter_functionality_images(browser):
#     assets_page = AssetsPage(browser)
#     global test, my_comment
#     test = test_case_ids[400] # 1211 #529
#     my_comment = 'File-Size heading text is not present'
#     file_size = assets_page.verify_file_size_heading_text()
#     assert file_size == True, 'File-Size heading text is not present / Asset Type clear Filter is not Working '
#     assets_page.verify_size_filter()
#     after_filter = assets_page.verify_total_count_asset()
#     assets_page.click_reset_button_files_size_property()
#     after_clear = assets_page.verify_total_count_asset()
#     assert (after_clear > after_filter) & (total_images == after_clear), 'Asset Type clear Filter is not Working'
#     my_comment = '''1. On clickFile size  filter a dropdown should opened
# 2. Reset Button:- On click Clear button File size  filters should be reseted
# 3. Range selector
# '''
#
#
# #@allure.title('TC_403: Verify user is able to apply range selector ')
# def test_verify_range_selector_functionality_images(browser):
#     assets_page = AssetsPage(browser)
#     global test, my_comment
#     test = test_case_ids[401]  # 1212 #530
#     my_comment = 'File-Size heading text is not present'
#     file_size = assets_page.verify_file_size_heading_text()
#     assert file_size == True, 'File-Size heading text is not present / sset Type clear Filter is not Working'
#     assets_page.verify_size_filter()
#     after_filter = assets_page.verify_total_count_asset()
#     assets_page.click_reset_button_files_size_property()
#     after_clear = assets_page.verify_total_count_asset()
#     assert (after_clear > after_filter) & (total_images == after_clear), 'Asset Type clear Filter is not Working'
#     my_comment = 'User should be able to apply range selector on assets '
#
#
# #@allure.title('TC_404: Verify pagination elements')
# def test_verify_Pagination_elements_assets_images(browser):
#     film_series = filmSeriesPage(browser)
#     global test, my_comment
#     test = test_case_ids[402]  # 1213 #531
#     my_comment = 'right cursor is not clickable'
#     right_cursor_click = film_series.click_right_cursor_button()
#     assert right_cursor_click == True, 'right cursor is not clickable'
#     film_series.click_left_cursor_button()
#     my_comment = 'left button cursor is not disabled'
#     disable_text = film_series.verify_left_disabled_cursor()
#     assert 'disabled' in disable_text, 'left button cursor is not disabled'
#     my_comment = 'One page is not Active'
#     active_page = film_series.verify_one_active_page()
#     assert active_page == True, 'One page is not Active'
#     my_comment = 'pages are not disabled'
#     count_of_disable_pages = film_series.verify_expect_one_disabled_pages_button()
#     assert count_of_disable_pages > 1, 'pages are not disabled'
#     my_comment = '''Pagination have following elements:-
#
# 1. Prev navigation arrow
# 2. Next navigation arrow
# 3. Pages number '''
#
#
# #@allure.title('TC_405: Verify Prev navigation arrow functionality')
# def test_verify_Pagination_prev_arrow_clickable_assets_images(browser):
#     film_series = filmSeriesPage(browser)
#     global test, my_comment
#     test = test_case_ids[403]  # 1214 #532
#     my_comment = 'left button cursor is not disabled'
#     disable_text = film_series.verify_left_disabled_cursor()
#     assert 'disabled' in disable_text, 'left button cursor is not disabled'
#     my_comment = 'right cursor is not clickable'
#     right_cursor_click = film_series.click_right_cursor_button()
#     assert right_cursor_click == True, 'right cursor is not clickable'
#     film_series.click_left_cursor_button()
#     my_comment = 'left button cursor is not disabled'
#     disable_text = film_series.verify_left_disabled_cursor()
#     assert 'disabled' in disable_text, 'left button cursor is not disabled'
#     my_comment = '''1. If user is on first page then prev arrow should be hide
# 2. On click prev arrow page should move to prev page'''
#
#
# #@allure.title('TC_406: Verify Next navigation arrow functionality')
# def test_verify_Pagination_next_arrow_clickable_assets_images(browser):
#     film_series = filmSeriesPage(browser)
#     global test, my_comment
#     test = test_case_ids[404]  # 1215 #533
#     my_comment = 'right cursor is not clickable'
#     right_cursor_click = film_series.click_right_cursor_button()
#     assert right_cursor_click == True, 'right cursor is not clickable'
#     film_series.click_last_respect_last_page_button_asset()
#     my_comment = 'right cursor button is not disabled'
#     right_disable_text = film_series.verify_right_disabled_cursor_asset()
#     assert 'disabled' in right_disable_text, 'right cursor button is not disabled'
#     my_comment = '''1. If user is on last page then next arrow should be hide
# 2. On click Next arrow page should move to Next page'''
#
#
# #@allure.title('TC_407: Verify pages numbers are clickable')
# def test_click_Pagination_page_number_clickable_assets_images(browser):
#     film_series = filmSeriesPage(browser)
#     global test, my_comment
#     test = test_case_ids[405]  # 1216 #534
#     my_comment = 'right button cursor is not disabled / page Number is not Clickable'
#     film_series.click_left_cursor_button()
#     film_series.click_last_respect_last_page_button_asset()
#     right_disable_text = film_series.verify_right_disabled_cursor_asset()
#     assert 'disabled' in right_disable_text, 'right button cursor is not disabled / page Number is not Clickable'
#     my_comment = 'On click any page number user should redirected to that page'
#
#
# #@allure.title('TC_408: Verify Videos  tab elements')
# def test_verify_video_tab_elements_videos(browser):
#     assets_page = AssetsPage(browser)
#     global test, my_comment
#     test = test_case_ids[406]  # 1217 #535
#     my_comment = 'Reset Filter is not Present in All Assets Header-Section'
#     assets_page.click_video_tab_button()
#     reset_filter = assets_page.verify_reset_filter_button()
#     assert reset_filter == True, 'Reset Filter is not Present in All Assets Header-Section'
#     my_comment = 'Collapse-All is not Present in All Assets Header-Section'
#     collapse_all = assets_page.verify_collapse_all_button()
#     assert collapse_all == True, 'Collapse-All is not Present in All Assets Header-Section'
#     my_comment = 'Select All is not Present in all Assets Header-Section'
#     select_all = assets_page.verify_select_all_button()
#     assert select_all == True, 'Select All is not Present in all Assets Header-Section'
#     my_comment = 'Grid-View button is not Present in All Assets Header-Section'
#     grid_view = assets_page.verify_grid_view_button()
#     assert grid_view == True, 'Grid-View button is not Present in All Assets Header-Section'
#     my_comment = 'List-View button is not Present in all Assets Header_Section'
#     list_view = assets_page.verify_list_view_button()
#     assert list_view == True, 'List-View button is not Present in all Assets Header_Section'
#     my_comment = 'Sorting Button is not Present in All Assets Header-Section '
#     sorting_button = assets_page.verify_sorting_filter()
#     assert sorting_button == True, 'Sorting Button is not Present in All Assets Header-Section '
#     my_comment = 'File Type Filter is not Present in All-Assets Page'
#     file_type = assets_page.verify_file_type_text()
#     assert file_type == True, 'File Type Filter is not Present in All-Assets Page'
#     my_comment = 'movie card is not present in All-Assets page'
#     movie_card = assets_page.verify_all_assets_first_card()
#     assert movie_card == True, 'movie card is not present in All-Assets page'
#     my_comment = 'Total Result count is not present in All-Assets page '
#     result_count = assets_page.verify_total_result_text()
#     assert result_count == True, 'Total Result count is not present in All-Assets page '
#     my_comment = 'Pagination Section is not present / Next button is not present'
#     pagination_next = assets_page.verify_pagination_next_button()
#     assert pagination_next == True, 'Pagination Section is not present / Next button is not present'
#     my_comment = '''Videos  tab Have following elements:-
#
# 1. Reset filter button
# 2. Collapse all button
# 3. Select all button
# 4. View tabs
# 5. Sorting filter
# 6. Filter
# 7. Results
# 8. Videos  cards
# 9. Pagination
# '''
#
#
# #@allure.title('TC_409: Verify reset filter button is resetting filter')
# def test_click_reset_filter_button_video(browser):
#     assets_page = AssetsPage(browser)
#     global test, my_comment
#     test = test_case_ids[407]  # 1218  #536
#     my_comment = 'Select All button is not clickable / Item are not Selected '
#     assets_page.click_video_frame_rate_checkbox()
#     count_text = assets_page.verify_selected_checkbox_count()
#     assert count_text == '1', 'Count-Number is not present in Video properties'
#     my_comment = 'reset filter is not clickable / Item are Selected'
#     reset_button = assets_page.click_reset_filter_button_video()
#     assert reset_button == False, 'reset filter is not clickable / Item are Selected'
#     my_comment = 'On click reset filter button all selected filter should be reset'
#
#
# #@allure.title('TC_410: Verify collapse all button is collapsing all filter dropdown')
# def test_click_collapse_all_button_video(browser):
#     assets_page = AssetsPage(browser)
#     global test, my_comment
#     test = test_case_ids[408]  # 1219 #537
#     my_comment = 'Collapse-All button is not clickable/collapse button is not hiding Filter Section'
#     collapse_all = assets_page.click_videos_collapse_all_button()
#     assert collapse_all == False, 'Collapse-All button is not clickable/collapse button is not hiding Filter Section'
#     my_comment = 'On click collapse button all open filters should be collapsed'
#
#
# #@allure.title('TC_411: Verify user is able to select all images on click select all checkbox from header')
# def test_click_select_all_button_selecting_video(browser):
#     assets_page = AssetsPage(browser)
#     global test, my_comment
#     test = test_case_ids[409]  # 1220 #538
#     my_comment = 'Select All button is not clickable / Item are not Selected '
#     select_all = assets_page.click_video_select_all_button()
#     assert select_all == True, 'Select All button is not clickable / Item are not Selected '
#     my_comment = 'On click select all button all the results of that page should be selected'
#
#
# #@allure.title('TC_412: Verify user is able to deselect all results')
# def test_click_select_all_button_unselecting_video(browser):
#     assets_page = AssetsPage(browser)
#     global test, my_comment
#     test = test_case_ids[410]  # 1221 #539
#     my_comment = 'Select All button is not clickable / All Items are not Selected'
#     select_all = assets_page.click_again_video_select_all_button()
#     assert select_all == False, 'Select All button is not clickable / All Items are not Selected'
#     my_comment = 'on double click chckboxes should be deselect'
#
#
# #@allure.title('TC_413: Verify user is able to switch between grid view and list view')
# def test_click_list_and_grid_button_video(browser):
#     assets_page = AssetsPage(browser)
#     global test, my_comment
#     test = test_case_ids[411]  # 1222 #540
#     my_comment = 'List View is not present / File Name text is not present in list view '
#     list_view = assets_page.click_list_view_button()
#     assert list_view == True, 'List View is not present / File Name text is not present in list view '
#     my_comment = 'Grid View is not present / File Name text is not present in grid view'
#     grid_view = assets_page.click_grid_view_button()
#     assert grid_view == False, 'Grid View is not present / File Name text is not present in grid view'
#     my_comment = 'On click of the view button, view should change in respect to the button clicked'
#
#
# #@allure.title('TC_414: Verify List view')
# def test_verify_list_view_elements_videos(browser):
#     assets_page = AssetsPage(browser)
#     global test, my_comment
#     test = test_case_ids[412]  # 1223 #541
#     my_comment = 'List View is not present / File Name Text is not present in list view '
#     file_name = assets_page.click_list_view_button()
#     assert file_name == True, 'List View is not present / File Name Text is not present in list view '
#     my_comment = ' File Size Text is not present in list view '
#     file_size = assets_page.verify_file_size_text()
#     assert file_size == True, ' File Size Text is not present in list view '
#     my_comment = 'Asset Type Text is not Present in list View'
#     asset_type = assets_page.verify_asset_type_text()
#     assert asset_type == True, 'Asset Type Text is not Present in list View'
#     my_comment = 'checkbox is not present in All Assets list view'
#     check_box = assets_page.verify_list_first_checkbox()
#     assert check_box == True, 'checkbox is not present in All Assets list view'
#     my_comment = 'Add to cart button is not clickable / Add To Cart popup is not open'
#     add_to_cart = assets_page.verify_add_to_cart_clickable()
#     assert add_to_cart == True, 'Add to cart button is not clickable / Add To Cart popup is not open'
#     my_comment = '''List view should show tabular structure with following columns
# 1.File name with checkbox
# 2. File size
# 3. Asset Type
# 4. Download icon button:- On click Icon user should be able to download that asset
# 5. Cart icon button:- on click add to cart icon add to cart popup should be opened'''
#
#
# #@allure.title('TC_416: Verify Filter Elements')
# def test_verify_filter_elements_videos(browser):
#     assets_page = AssetsPage(browser)
#     global test, my_comment
#     test = test_case_ids[414]  # 1225 #543
#     my_comment = 'File Type Dropdown is not present in Asset video Tab'
#     assets_page.assets_page_refresh()
#     assets_page.click_video_tab_button()
#     reset_filter = assets_page.verify_reset_filter_button()
#     assert reset_filter == True, 'Reset Filter is not Present in All Assets Header-Section'
#     file_type = assets_page.verify_file_type_filter_dropdown()
#     assert file_type == True, 'File Type Dropdown is not present in Asset video Tab'
#     my_comment = 'Asset Type is not present in Asset page'
#     asset_type = assets_page.verify_asset_type_filter_dropdown()
#     assert asset_type == True, 'Asset Type is not present Asset video Tab'
#     my_comment = 'File-Size is not present in Asset Page'
#     video_properties = assets_page.verify_video_properties_dropdown()
#     assert video_properties == True, 'Video Properties are not present in Asset video Tab'
#     file_size = assets_page.verify_file_size_filter_dropdown()
#     assert file_size == True, 'File-Size is not present in Asset video Tab'
#     my_comment = '''Filter have following elements:-
#
# 1. File Type filter
# 2. Video properties filter
# 3. Assets Type filter
# 4, File size filter
# '''
#
#
# #@allure.title('TC_417: Verify File type filter functionality')
# def test_verify_single_file_filter_Videos(browser):
#     assets_page = AssetsPage(browser)
#     global test, my_comment
#     test = test_case_ids[415]  # 1226 #544
#     my_comment = 'Count-Number is not present in Video properties / Video checkbox is not present in FileType Dropdown'
#     assets_page.click_video_mp4_3gp_checkbox_file_type()
#     count_text = assets_page.verify_selected_checkbox_count()
#     assert count_text == '1', 'Count-Number is not present in Video properties'
#     assets_page.click_file_type_clear_button()
#     my_comment = '''User should be able to filter assets by File type by selecting the Checkboxes from the drop-down
# Search Result should show assets which has the selected Checkboxes'''
#
#
# #@allure.title('TC_420: Verify Video Properties filter elements')
# def test_verify_video_properties_elements_filter(browser):
#     assets_page = AssetsPage(browser)
#     global test, my_comment
#     test = test_case_ids[418]  # 1229 #547
#     my_comment = 'Video Properties heading is not Present in Asset Section'
#     video_text = assets_page.verify_video_properties_text()
#     assert video_text == True, 'Video Properties heading is not Present in Asset Section'
#     my_comment = 'Video Resolution checkbox is not present in Video Properties'
#     video_resolution = assets_page.verify_video_resolution_text()
#     assert video_resolution == True, 'Video Resolution checkbox is not present in Video Properties'
#     my_comment = 'Video frame-rate checkbox is not present in Video Properties'
#     video_frame_rate = assets_page.verify_video_frame_rate_text()
#     assert video_frame_rate == True, 'Video frame-rate checkbox is not present in Video Properties'
#     assets_page.click_video_frame_rate_checkbox()
#     my_comment = 'Count-Number is not present in Video properties'
#     count_text = assets_page.verify_selected_checkbox_count()
#     assert count_text == '1', 'Count-Number is not present in Video properties / Type ' \
#                               'File Filter is not present or not working'
#     assets_page.click_clear_button_video_property()
#     my_comment = 'Clear button is not Clickable in video-tab'
#     clear_button = assets_page.verify_click_clear_selected_checkbox_count()
#     assert clear_button == False, 'Clear button is not Clickable in video-tab'
#     my_comment = '''1. On click Video Properties filter a dropdown should opened
# 2. Clear Button:- On click Clear button Video Properties filters should be rested
# 3. Checkboxes with mention Video Properties
# 4 Total checkboxes selected count
# 5. Resolution filters
# 6. Frame rate filters'''
#
#
# #@allure.title('TC_421: Verify user is able to filter assets by Video Properties')
# def test_verify_single_filter_video_properties_videos(browser):
#     assets_page = AssetsPage(browser)
#     global test, my_comment
#     test = test_case_ids[419]  # 1230 #548
#     my_comment = 'Count-Number is not present in Video properties / Type File Filter is not present or not working'
#     assets_page.click_video_frame_rate_checkbox()
#     count_text = assets_page.verify_selected_checkbox_count()
#     assert count_text == '1', 'Count-Number is not present in Video properties'
#     after_filter = assets_page.verify_total_count_asset()
#     assets_page.click_clear_button_video_property()
#     after_clear = assets_page.verify_total_count_asset()
#     assert (after_clear >= after_filter), 'Type File Filter is not present or not working'
#     clear_button = assets_page.verify_click_clear_selected_checkbox_count()
#     assert clear_button == False, 'Clear button is not Clickable in video-tab'
#     my_comment = '''User should be able to filter assets by Video Properties by selecting the Checkboxes from the drop-down
# Search Result should show assets which has the selected Checkboxes'''
#
#
# #@allure.title('TC_422: Verify user is able to apply multiple Checkboxes filters')
# def test_verify_multiple_filter_video_properties_videos(browser):
#     assets_page = AssetsPage(browser)
#     global test, my_comment
#     test = test_case_ids[420]  # 1231 #549
#     my_comment = 'Count-Number is not present in Video properties/ Type File Filter is not present or not working'
#     assets_page.click_video_frame_rate_checkbox()
#     assets_page.click_video_resolution_checkbox()
#     count_text = assets_page.verify_selected_checkbox_count()
#     assert count_text == '2', 'Count-Number is not present in Video properties'
#     after_filter = assets_page.verify_total_count_asset()
#     assets_page.click_clear_button_video_property()
#     after_clear = assets_page.verify_total_count_asset()
#     assert (after_clear >= after_filter), 'Type File Filter is not present or not working'
#     clear_button = assets_page.verify_click_clear_selected_checkbox_count()
#     assert clear_button == False, 'Clear button is not Clickable in video-tab'
#     my_comment = 'User should be able to select multiple Video Properties filters Search results' \
#                  ' should show all Assets which have the selected Checkboxes'
#
#
# #@allure.title('TC_423: Verify Assets Type filter elements')
# def test_verify_assets_type_filter_elements_videos(browser):
#     assets_page = AssetsPage(browser)
#     global test, my_comment
#     test = test_case_ids[421]  # 1232  #550
#     my_comment = 'Asset Type heading is not Present in Asset Section'
#     video_text = assets_page.verify_asset_type_heading_text()
#     assert video_text == True, 'Asset Type heading is not Present in Asset Section'
#     my_comment = 'Video Filter is not present in asset type Section'
#     video_filter = assets_page.verify_asset_type_video()
#     assert video_filter == True, 'Video Filter is not present in asset type Section'
#     assets_page.click_video_trailer_checkbox()
#     after_filter = assets_page.verify_total_count_asset()
#     my_comment = 'Asset Type clear Filter is not Working'
#     count_text = assets_page.verify_selected_checkbox_count()
#     assert count_text == '1', 'Count-Number is not present in Video properties'
#     assets_page.click_clear_button_asset_type_property()
#     after_clear = assets_page.verify_total_count_asset()
#     assert (after_clear >= after_filter), 'Asset Type clear Filter is not Working'
#     clear_button = assets_page.verify_click_clear_selected_checkbox_count()
#     assert clear_button == False, 'Clear button is not Clickable in video-tab'
#     my_comment = '''1. On click Assets Type filter a dropdown should opened
# 2. Clear Button:- On click Clear button Assets Type filters should be reseted
# 3. Checkboxes with mention Assets Type
# 4 Total checkboxes selected count
# 5. Documents filters
# 6. Photos/Images filter
# 7. Ads Filter
# 8. Videos filter'''
#
#
# #@allure.title('TC_424: Verify user is able to filter assets by Assets Type')
# def test_verify_single_filter_assets_type(browser):
#     assets_page = AssetsPage(browser)
#     global test, my_comment
#     test = test_case_ids[422]  # 1233 #551
#     my_comment = 'Count-Number is not present in Video properties / Asset Type clear Filter is not Working'
#     assets_page.click_video_trailer_checkbox()
#     after_filter = assets_page.verify_total_count_asset()
#     count_text = assets_page.verify_selected_checkbox_count()
#     assert count_text == '1', 'Count-Number is not present in Video properties'
#     assets_page.click_clear_button_asset_type_property()
#     after_clear = assets_page.verify_total_count_asset()
#     assert (after_clear >= after_filter), 'Asset Type clear Filter is not Working'
#     clear_button = assets_page.verify_click_clear_selected_checkbox_count()
#     assert clear_button == False, 'Clear button is not Clickable in video-tab'
#     my_comment = 'User should be able to filter assets by Assets Type by selecting the Checkboxes from ' \
#                  'the drop-down Search Result should show assets which has the selected Checkboxes'
#
#
# #@allure.title('TC_426: Verify file size filter functionality')
# def test_verify_size_filter_functionality_videos(browser):
#     assets_page = AssetsPage(browser)
#     global test, my_comment
#     test = test_case_ids[424]  # 1235 #553
#     my_comment = 'File-Size heading text is not present'
#     file_size = assets_page.verify_file_size_heading_text()
#     assert file_size == True, 'File-Size heading text is not present'
#     range_filter = assets_page.verify_range_filter()
#     assert range_filter == True, "Range Filter is not Present in Video tab section"
#     assets_page.verify_reset_button_files_size_property()
#     my_comment = '''1. On clickFile size  filter a dropdown should opened
# 2. Reset Button:- Reset button is present
# 3. Range selector'''
#
#
# #@allure.title('TC_428: Verify pagination elements')
# def test_verify_Pagination_elements_videos(browser):
#     film_series = filmSeriesPage(browser)
#     global test, my_comment
#     test = test_case_ids[426]  # 1237 #555
#     my_comment = 'right cursor is not clickable'
#     right_cursor = film_series.verify_right_cursor_button_disabled()
#     assert 'disabled' in right_cursor, 'Right cursor is not disabled'
#     disable_text = film_series.verify_left_disabled_cursor()
#     assert 'disabled' in disable_text, 'left cursor is not disabled'
#     my_comment = 'One page is not Active'
#     active_page = film_series.verify_one_active_page()
#     assert active_page == True, 'All pages are disabled'
#     my_comment = '''Pagination have following elements:-
# 1. Prev navigation arrow
# 2. Next navigation arrow
# 3. Page number '''
#
#
# #@allure.title('TC_432: Verify Documents  tab elements')
# def test_verify_document_elements_documents(browser):
#     assets_page = AssetsPage(browser)
#     global test, my_comment
#     test = test_case_ids[430]  # 1241 #559
#     my_comment = 'Reset Filter is not Present in All Assets Header-Section'
#     assets_page.click_document_tab_button()
#     reset_filter = assets_page.verify_reset_filter_button()
#     assert reset_filter == True, 'Reset Filter is not Present in All Assets Header-Section'
#     my_comment = 'Collapse-All is not Present in All Assets Header-Section'
#     collapse_all = assets_page.verify_collapse_all_button()
#     assert collapse_all == True, 'Collapse-All is not Present in All Assets Header-Section'
#     my_comment = 'Select All is not Present in all Assets Header-Section'
#     select_all = assets_page.verify_select_all_button()
#     assert select_all == True, 'Select All is not Present in all Assets Header-Section'
#     my_comment = 'Grid-View button is not Present in All Assets Header-Section'
#     grid_view = assets_page.verify_grid_view_button()
#     assert grid_view == True, 'Grid-View button is not Present in All Assets Header-Section'
#     my_comment = 'List-View button is not Present in all Assets Header_Section'
#     list_view = assets_page.verify_list_view_button()
#     assert list_view == True, 'List-View button is not Present in all Assets Header_Section'
#     my_comment = 'Sorting Button is not Present in All Assets Header-Section '
#     sorting_button = assets_page.verify_sorting_filter()
#     assert sorting_button == True, 'Sorting Button is not Present in All Assets Header-Section '
#     my_comment = 'File Type Filter is not Present in All-Assets Page'
#     file_type = assets_page.verify_file_type_text()
#     assert file_type == True, 'File Type Filter is not Present in All-Assets Page'
#     my_comment = 'movie card is not present in All-Assets page'
#     movie_card = assets_page.verify_all_assets_first_card()
#     assert movie_card == True, 'movie card is not present in All-Assets page'
#     my_comment = 'Total Result count is not present in All-Assets page '
#     result_count = assets_page.verify_total_result_text()
#     assert result_count == True, 'Total Result count is not present in All-Assets page '
#     my_comment = 'Pagination Section is not present / Next button is not present'
#     pagination_next = assets_page.verify_pagination_next_button()
#     assert pagination_next == True, 'Pagination Section is not present / Next button is not present'
#     my_comment = '''Videos  tab Have following elements:-
#
# 1. Reset filter button
# 2. Collapse all button
# 3. Select all button
# 4. View tabs
# 5. Sorting filter
# 6. Filter
# 7. Results
# 8. Videos  cards
# 9. Pagination
# '''
#
#
# #@allure.title('TC_433: Verify reset filter button is resetting filter')
# def test_click_reset_filter_button_documents(browser):
#     assets_page = AssetsPage(browser)
#     global test, my_comment
#     test = test_case_ids[431]  # 1242 #560
#     my_comment = 'Filter button is not clickable / reset filter button is not working '
#     assets_page.click_pdf_checkbox_file_type()
#     count_number = assets_page.verify_selected_checkbox_count()
#     assert count_number== '1','Filter button is not clickable / reset filter button is not working '
#     my_comment = 'Filter button is not clickable / reset filter button is not working '
#     reset_button = assets_page.click_reset_filter_button_documents()
#     assert reset_button == False, 'Filter button is not clickable / reset filter button is not working '
#     filter_reset = assets_page.verify_click_clear_selected_checkbox_count()
#     assert filter_reset == False, 'Filter button is not clickable / reset filter button is not working '
#     my_comment = 'On click reset filter button filter should be reset'
#
#
# #@allure.title('TC_434: Verify collapse all button is collapsing all filter dropdown')
# def test_click_collapse_all_button_documents(browser):
#     assets_page = AssetsPage(browser)
#     global test, my_comment
#     test = test_case_ids[432]  # 1243 #561
#     my_comment = 'Collapse-All button is not clickable/collapse button is not hiding Filter Section'
#     collapse_all = assets_page.click_all_assets_collapse_all_button()
#     assert collapse_all == False, 'Collapse-All button is not clickable/collapse button is not hiding Filter Section'
#     my_comment = 'On click collapse button all open filters should be collapsed'
#
#
# #@allure.title('TC_435: Verify user is able to select all images on click select all checkbox from header')
# def test_click_select_all_button_selecting_documents(browser):
#     assets_page = AssetsPage(browser)
#     global test, my_comment
#     test = test_case_ids[433]  # 1244 #562
#     my_comment = 'Select All button is not clickable / Item are not Selected '
#     select_all = assets_page.click_documents_select_all_button()
#     assert select_all == True, 'Select All button is not clickable / Item are not Selected '
#     my_comment = 'On click select all button all the results of that page should be selected'
#
#
# #@allure.title('TC_436: Verify user is able to deselect all results')
# def test_click_select_all_button_unselecting_documents(browser):
#     assets_page = AssetsPage(browser)
#     global test, my_comment
#     test = test_case_ids[434]  # 1245 #563
#     my_comment = 'Select All button is not clickable / All Items are not Selected'
#     select_all = assets_page.click_again_documents_select_all_button()
#     assert select_all == False, 'Select All button is not clickable / All Items are not Selected'
#     my_comment = 'on double click checkboxes should be deselect'
#
#
# #@allure.title('TC_437: Verify user is able to switch between grid view and list view')
# def test_click_list_and_grid_button_documents(browser):
#     assets_page = AssetsPage(browser)
#     global test, my_comment
#     test = test_case_ids[435]  # 1246 #564
#     my_comment = 'List View is not present / File Name text is not present in list view '
#     list_view = assets_page.click_list_view_button()
#     assert list_view == True, 'List View is not present / File Name text is not present in list view '
#     my_comment = 'Grid View is not present / File Name text is not present in grid view'
#     grid_view = assets_page.click_grid_view_button()
#     assert grid_view == False, 'Grid View is not present / File Name text is not present in grid view'
#     my_comment = 'On click of the view button, view should change in respect to the button clicked'
#
#
# #@allure.title('TC_438: Verify List view')
# def test_verify_list_view_elements_documents(browser):
#     assets_page = AssetsPage(browser)
#     global test, my_comment
#     test = test_case_ids[436]  # 1247 #565
#     my_comment = 'List View is not present / File Name Text is not present in list view '
#     file_name = assets_page.click_list_view_button()
#     assert file_name == True, 'List View is not present / File Name Text is not present in list view '
#     my_comment = ' File Size Text is not present in list view '
#     file_size = assets_page.verify_file_size_text()
#     assert file_size == True, ' File Size Text is not present in list view '
#     my_comment = 'Asset Type Text is not Present in list View'
#     asset_type = assets_page.verify_asset_type_text()
#     assert asset_type == True, 'Asset Type Text is not Present in list View'
#     my_comment = 'checkbox is not present in All Assets list view'
#     check_box = assets_page.verify_list_first_checkbox()
#     assert check_box == True, 'checkbox is not present in All Assets list view'
#     my_comment = 'Add to cart button is not clickable / Add To Cart popup is not open'
#     add_to_cart = assets_page.verify_add_to_cart_clickable()
#     assert add_to_cart == True, 'Add to cart button is not clickable / Add To Cart popup is not open'
#     my_comment = '''List view should show tabular structure with following columns
# 1. File name with checkbox
# 2. File size
# 3. Asset Type
# 4. Download icon button:- On click Icon user should be able to download that asset
# 5. Cart icon button:- on click add to cart icon add to cart popup should be opened'''
#
#
# #@allure.title('TC_439: Verify the options of Sorting and their functionality')
# def test_verify_all_sorting_functionality_documents(browser):
#     assets_page = AssetsPage(browser)
#     global test, my_comment
#     test = test_case_ids[437]  # 1248 #566
#     my_comment = 'Reset Filter is not Present in All Assets Header-Section'
#     assets_page.assets_page_refresh()
#     assets_page.click_document_tab_button()
#     reset_filter = assets_page.verify_reset_filter_button()
#     assert reset_filter == True, 'Reset Filter is not Present in All Assets Header-Section'
#     my_comment = 'List View is not present / File Name text is not present in list view '
#     list_view = assets_page.click_list_view_button()
#     assert list_view == True, 'List View is not present / File Name text is not present in list view '
#     assets_page.click_sorting_filter()
#     my_comment = 'Larger to smaller Size Filter is not working'
#     first_file, second_file = assets_page.click_sorting_file_size_up_filter_documents()
#     assert first_file > second_file, 'Larger to smaller Size Filter is not working'
#     assets_page.click_sorting_filter()
#     my_comment = 'smaller to larger Size Filter is not working'
#     first_file_down, second_file_down = assets_page.click_sorting_file_size_respect_movie_down_filter_documents()
#     assert first_file_down <= second_file_down, 'smaller to larger Size Filter is not working'
#     assets_page.click_sorting_filter()
#     assets_page.verify_file_sorting_a_to_z()
#     assets_page.click_sorting_filter()
#     assets_page.verify_file_sorting_z_to_a()
#     assets_page.click_sorting_filter()
#     my_comment = 'Down Date Filter is not working '
#     date_time_up = assets_page.mouse_hover_on_first_file_image()
#     assert date_time_up == True, 'Down Date Filter is not working '
#     assets_page.click_sorting_filter()
#     my_comment = 'Up Date Filter is not working'
#     date_time_down = assets_page.mouse_hover_on_Second_file_image()
#     assert date_time_down == True, 'Up Date Filter is not working'
#     my_comment = '''Sorting drop down should have the following options with mentioned behaviour
# 1. File size (Low to high)  -- Titles should be ordered in Increasing order
# 2. File size (highTo low)  -- Titles should be ordered in Decreasing corder
# 3. Sort A-Z  -- Assets should be ordered in Ascending order of Alphabets
# 4. Sort Z-A -- Assets should be ordered in Descending order of Alphabets
# 5. Sort by Date (Old to New) -- Titles should be ordered in Decending order of Added Date
# 6. Sort by Date (New to Old) -- Titles should be ordered in Ascending order of Added Date'''
#
#
# #@allure.title('TC_440: Verify Filter Elements')
# def test_verify_left_filter_elements_documents(browser):
#     assets_page = AssetsPage(browser)
#     global test, my_comment
#     test = test_case_ids[438]  # 1249 #567
#     my_comment = 'Reset Filter is not Present in All Assets Header-Section'
#     assets_page.assets_page_refresh()
#     assets_page.click_document_tab_button()
#     reset_filter = assets_page.verify_reset_filter_button()
#     assert reset_filter == True, 'Reset Filter is not Present in All Assets Header-Section'
#     my_comment = 'File Type Dropdown is not present in Asset page'
#     file_type = assets_page.verify_file_type_filter_dropdown()
#     assert file_type == True, 'File Type Dropdown is not present in Asset page'
#     my_comment = 'Asset Type is not present in Asset page'
#     asset_type = assets_page.verify_asset_type_filter_dropdown()
#     assert asset_type == True, 'Asset Type is not present in Asset page'
#     my_comment = 'File-Size is not present in Asset Page'
#     file_size = assets_page.verify_file_size_filter_dropdown()
#     assert file_size == True, 'File-Size is not present in Asset Page'
#     my_comment = '''Filter have following elements:-
# 1. File Type filter
# 2. Assets Type filter
# 3, File size filter
# '''
#
#
# #@allure.title('TC_441: Verify File type filter functionality')
# def test_verify_file_type_functionality_documents(browser):
#     assets_page = AssetsPage(browser)
#     global test, my_comment
#     test = test_case_ids[439]  # 1250 #568
#     my_comment = 'Type File Filter is not present or not working'
#     assets_page.click_pdf_checkbox_file_type()
#     after_filter = assets_page.verify_total_count_asset()
#     count_text = assets_page.verify_selected_checkbox_count()
#     assert count_text == '1', 'Count-Number is not present in File Type'
#     assets_page.click_file_type_clear_button()
#     my_comment = 'clear button is not clickable'
#     after_clear = assets_page.verify_total_count_asset()
#     assert (after_clear >= after_filter), 'clear button is not clickable'
#     my_comment = '''1. On click file type filter a dropdown should opened
# 2. Clear Button:- On click Clear button File type filters should be reseted
# 3. Checkboxes with mention file Type
# 4 Total checkboxes selected count
# '''
#
#
# #@allure.title('TC_442: Verify user is able to filter Assets by File type')
# def test_verify_single_file_filter_documents(browser):
#     assets_page = AssetsPage(browser)
#     global test, my_comment
#     test = test_case_ids[440]  # 1251  #569
#     my_comment = ' Type File Filter is not present or not working'
#     assets_page.click_pdf_checkbox_file_type()
#     after_filter = assets_page.verify_total_count_asset()
#     count_text = assets_page.verify_selected_checkbox_count()
#     my_comment = 'Count-Number is not present in File Type'
#     assert count_text == '1', 'Count-Number is not present in File TYpe'
#     assets_page.click_file_type_clear_button()
#     after_clear = assets_page.verify_total_count_asset()
#     assert (after_clear >= after_filter), 'Type File Filter is not present or not working'
#     my_comment = '''User should be able to filter assets by File type by selecting the Checkboxes from the drop-down
#                     Search Result should show assets which has the selected Checkboxes'''
#
#
# #@allure.title('TC_445: Verify Assets Type filter elements')
# def test_verify_assets_type_filter_elements_documents(browser):
#     assets_page = AssetsPage(browser)
#     global test, my_comment
#     test = test_case_ids[442]  # 1254 #572
#     my_comment = 'Video Properties heading is not Present in Asset Section'
#     video_text = assets_page.verify_asset_type_heading_text()
#     assert video_text == True, 'Video Properties heading is not Present in Asset Section'
#     my_comment = 'Document text is not present in asset type Section'
#     documents_text = assets_page.verify_asset_type_documents()
#     assert documents_text == True, 'Document text is not present in asset type Section'
#     my_comment = 'Ads Filter is not Present in asset type Section'
#     ads_type = assets_page.verify_asset_type_ads()
#     assert ads_type == True, 'Ads Filter is not Present in asset type Section'
#     my_comment = 'Video Filter is not present in asset type Section'
#     assets_page.click_document_script_checkbox()
#     after_filter = assets_page.verify_total_count_asset()
#     my_comment = 'Asset Type clear Filter is not Working'
#     count_text = assets_page.verify_selected_checkbox_count()
#     assert count_text == '1', 'Count-Number is not present in Video properties'
#     assets_page.click_clear_button_asset_type_property()
#     after_clear = assets_page.verify_total_count_asset()
#     assert (after_clear >= after_filter), 'Asset Type clear Filter is not Working'
#     my_comment = '''1. On click Assets Type filter a dropdown should opened
# 2. Clear Button:- On click Clear button Assets Type filters should be reseted
# 3. Checkboxes with mention Assets Type
# 4 Total checkboxes selected count
# 5. Documents filters
# 6. Ads Filter'''
#
#
# #@allure.title('TC_446: Verify user is able to filter assets by Assets Type')
# def test_verify_single_assets_type_documents(browser):
#     assets_page = AssetsPage(browser)
#     global test, my_comment
#     test = test_case_ids[443]  # 1255  #573
#     my_comment = 'Count-Number is not present in Asset Type filter / Asset Type clear Filter is not Working'
#     assets_page.click_document_script_checkbox()
#     after_filter = assets_page.verify_total_count_asset()
#     count_text = assets_page.verify_selected_checkbox_count()
#     assert count_text == '1', 'Count-Number is not present in Asset type filter'
#     assets_page.click_clear_button_asset_type_property()
#     after_clear = assets_page.verify_total_count_asset()
#     assert (after_clear > after_filter), 'Asset Type clear Filter is not Working'
#     my_comment = 'User should be able to filter assets by Assets Type by selecting the Checkboxes from ' \
#                  'the drop-down Search Result should show assets which has the selected Checkboxes'
#
#
# #@allure.title('TC_447: Verify user is able to apply multiple Checkboxes filters')
# def test_verify_multiple_assets_type_documents(browser):
#     assets_page = AssetsPage(browser)
#     global test, my_comment
#     test = test_case_ids[444]  # 1256 #574
#     my_comment = 'Count-Number is not present in Asset Type filter / multiple filters are not applied'
#     assets_page.click_document_script_checkbox()
#     assets_page.click_document_paid_ad_memo_checkbox()
#     after_filter = assets_page.verify_total_count_asset()
#     count_text = assets_page.verify_selected_checkbox_count()
#     assert count_text == '2', 'Count-Number is not present in Video properties'
#     assets_page.click_clear_button_asset_type_property()
#     after_clear = assets_page.verify_total_count_asset()
#     assert (after_clear >= after_filter), 'Asset Type clear Filter is not Working'
#     my_comment = 'User should be able to select multiple Assets Type filters Search ' \
#                  'results should show all Assets which have the selected Checkboxes'
#
#
# #@allure.title('TC_448: Verify file size filter functionality')
# def test_verify_size_filter_functionality_documents(browser):
#     assets_page = AssetsPage(browser)
#     global test, my_comment
#     test = test_case_ids[445]  # 1257 #575
#     my_comment = 'File-Size heading text is not present'
#     file_size = assets_page.verify_file_size_heading_text()
#     assert file_size == True, 'File-Size heading text is not present'
#     assets_page.verify_size_filter()
#     after_filter = assets_page.verify_total_count_asset()
#     assets_page.click_reset_button_files_size_property()
#     my_comment = 'Asset Type clear Filter is not Working'
#     after_clear = assets_page.verify_total_count_asset()
#     assert (after_clear > after_filter), 'Asset Type clear Filter is not Working'
#     my_comment = '''1. On clickFile size  filter a dropdown should opened
# 2. Reset Button:- On click Clear button File size  filters should be reseted
# 3. Range selector
# '''
#
#
# #@allure.title('TC_449: Verify user is able to apply range selector ')
# def test_verify_range_selector_functionality_documents(browser):
#     assets_page = AssetsPage(browser)
#     global test, my_comment
#     test = test_case_ids[446]  # 1258 #576
#     my_comment = 'File-Size heading text is not present'
#     file_size = assets_page.verify_file_size_heading_text()
#     assert file_size == True, 'File-Size heading text is not present'
#     assets_page.verify_size_filter()
#     after_filter = assets_page.verify_total_count_asset()
#     assets_page.click_reset_button_files_size_property()
#     my_comment = 'Asset Type clear Filter is not Working'
#     after_clear = assets_page.verify_total_count_asset()
#     assert (after_clear > after_filter), 'Asset Type clear Filter is not Working'
#     my_comment = 'User should be able to apply range selector on assets '
#
#
# #@allure.title('TC_450: Verify pagination elements')
# def test_verify_Pagination_elements_documents(browser):
#     film_series = filmSeriesPage(browser)
#     global test, my_comment
#     test = test_case_ids[447]  # 1259 #577
#     my_comment = 'right cursor is not clickable'
#     right_cursor = film_series.verify_right_cursor_button_disabled()
#     assert 'disabled' in right_cursor, 'Right cursor is not disabled'
#     disable_text = film_series.verify_left_disabled_cursor()
#     assert 'disabled' in disable_text, 'left cursor is not disabled'
#     my_comment = 'One page is not Active'
#     active_page = film_series.verify_one_active_page()
#     assert active_page == True, 'All pages are disabled'
#     my_comment = '''Pagination have following elements:-
# 1. Prev navigation arrow
# 2. Next navigation arrow
# 3. Page number '''
#
#
# #@allure.title('TC_454: Verify Paid Ad Demo tab elements')
# def test_verify_document_elements_paid_ad_memo(browser):
#     assets_page = AssetsPage(browser)
#     global test, my_comment
#     test = test_case_ids[451]  # 1263 #581
#     my_comment = 'Reset Filter is not Present in All Assets Header-Section'
#     assets_page.click_paid_ad_memo_tab_button()
#     reset_filter = assets_page.verify_reset_filter_button()
#     assert reset_filter == True, 'Reset Filter is not Present in All Assets Header-Section'
#     my_comment = 'Collapse-All is not Present in All Assets Header-Section'
#     collapse_all = assets_page.verify_collapse_all_button()
#     assert collapse_all == True, 'Collapse-All is not Present in All Assets Header-Section'
#     my_comment = 'Select All is not Present in all Assets Header-Section'
#     select_all = assets_page.verify_select_all_button()
#     assert select_all == True, 'Select All is not Present in all Assets Header-Section'
#     my_comment = 'Grid-View button is not Present in All Assets Header-Section'
#     grid_view = assets_page.verify_grid_view_button()
#     assert grid_view == True, 'Grid-View button is not Present in All Assets Header-Section'
#     my_comment = 'List-View button is not Present in all Assets Header_Section'
#     list_view = assets_page.verify_list_view_button()
#     assert list_view == True, 'List-View button is not Present in all Assets Header_Section'
#     my_comment = 'Sorting Button is not Present in All Assets Header-Section '
#     sorting_button = assets_page.verify_sorting_filter()
#     assert sorting_button == True, 'Sorting Button is not Present in All Assets Header-Section '
#     my_comment = 'File Type Filter is not Present in All-Assets Page'
#     file_type = assets_page.verify_file_type_text()
#     assert file_type == True, 'File Type Filter is not Present in All-Assets Page'
#     my_comment = 'movie card is not present in All-Assets page'
#     movie_card = assets_page.verify_all_assets_first_card()
#     assert movie_card == True, 'movie card is not present in All-Assets page'
#     my_comment = 'Total Result count is not present in All-Assets page '
#     result_count = assets_page.verify_total_result_text()
#     assert result_count == True, 'Total Result count is not present in All-Assets page '
#     my_comment = 'Pagination Section is not present / Next button is not present'
#     pagination_next = assets_page.verify_pagination_next_button()
#     assert pagination_next == True, 'Pagination Section is not present / Next button is not present'
#     my_comment = '''Videos  tab Have following elements:-
#
# 1. Reset filter button
# 2. Collapse all button
# 3. Select all button
# 4. View tabs
# 5. Sorting filter
# 6. Filter
# 7. Results
# 8. Document cards
# 9. Pagination
# '''
#
#
# #@allure.title('TC_455: Verify reset filter button is resetting filter')
# def test_click_reset_filter_button_paid_ad_memo(browser):
#     assets_page = AssetsPage(browser)
#     global test, my_comment
#     test = test_case_ids[452]  # 1264 #582
#     my_comment = 'Select All button is not clickable / Items are not Selected '
#     select_all = assets_page.click_video_select_all_button()
#     assert select_all == True, 'Select All button is not clickable / Item are not Selected '
#     my_comment = 'reset filter is not clickable / Item are Selected'
#     reset_button = assets_page.click_reset_filter_button_documents()
#     assert reset_button == False, 'reset filter is not clickable / Item are Selected'
#     my_comment = 'On click reset filter button all selected filter should be reset'
#
#
# #@allure.title('TC_456: Verify collapse all button is collapsing all filter dropdown')
# def test_click_collapse_all_button_documents_filter_dropdown(browser):
#     assets_page = AssetsPage(browser)
#     global test, my_comment
#     test = test_case_ids[453] # 1265 #583
#     my_comment = 'Collapse-All button is not clickable/collapse button is not hiding Filter Section'
#     collapse_all = assets_page.click_all_assets_collapse_all_button()
#     assert collapse_all == False, 'Collapse-All button is not clickable/collapse button is not hiding Filter Section'
#     my_comment = 'On click collapse button all open filters should be collapsed'
#
#
# #@allure.title('TC_457: Verify user is able to select all images on click select all checkbox from header')
# def test_click_select_all_button_selecting_paid_ad_memo(browser):
#     assets_page = AssetsPage(browser)
#     global test, my_comment
#     test = test_case_ids[454]  # 1266 #584
#     my_comment = 'Select All button is not clickable / Item are not Selected '
#     select_all = assets_page.click_video_select_all_button()
#     assert select_all == True, 'Select All button is not clickable / Item are not Selected '
#     my_comment = 'On click select all button all the results of that page should be selected'
#
#
# #@allure.title('TC_458: Verify user is able to deselect all results')
# def test_click_select_all_button_unselecting_paid_ad_memo(browser):
#     assets_page = AssetsPage(browser)
#     global test, my_comment
#     test = test_case_ids[455] # 1267 #585
#     my_comment = 'Select All button is not clickable / All Items are not Selected'
#     select_all = assets_page.click_again_video_select_all_button()
#     assert select_all == False, 'Select All button is not clickable / All Items are not Selected'
#     my_comment = 'on double click checkboxes should be deselect'
#
#
# #@allure.title('TC_459: Verify user is able to switch between grid view and list view')
# def test_click_list_and_grid_button_paid_ad_memo(browser):
#     assets_page = AssetsPage(browser)
#     global test, my_comment
#     test = test_case_ids[456]  # 1268  #586
#     my_comment = 'List View is not present / File Name text is not present in list view '
#     list_view = assets_page.click_list_view_button()
#     assert list_view == True, 'List View is not present / File Name text is not present in list view '
#     my_comment = 'Grid View is not present / File Name text is not present in grid view'
#     grid_view = assets_page.click_grid_view_button()
#     assert grid_view == False, 'Grid View is not present / File Name text is not present in grid view'
#     my_comment = 'On click of the view button, view should change in respect to the button clicked'
#
#
# #@allure.title('TC_460: Verify List view')
# def test_verify_list_view_elements_paid_ad_memo(browser):
#     assets_page = AssetsPage(browser)
#     global test, my_comment
#     test = test_case_ids[457]  # 1269  #587
#     my_comment = 'List View is not present / File Name Text is not present in list view '
#     file_name = assets_page.click_list_view_button()
#     assert file_name == True, 'List View is not present / File Name Text is not present in list view '
#     my_comment = ' File Size Text is not present in list view '
#     file_size = assets_page.verify_file_size_text()
#     assert file_size == True, ' File Size Text is not present in list view '
#     my_comment = 'Asset Type Text is not Present in list View'
#     asset_type = assets_page.verify_asset_type_text()
#     assert asset_type == True, 'Asset Type Text is not Present in list View'
#     my_comment = 'checkbox is not present in All Assets list view'
#     check_box = assets_page.verify_list_first_checkbox()
#     assert check_box == True, 'checkbox is not present in All Assets list view'
#     my_comment = 'Add to cart button is not clickable / Add To Cart popup is not open'
#     add_to_cart = assets_page.verify_add_to_cart_clickable()
#     assert add_to_cart == True, 'Add to cart button is not clickable / Add To Cart popup is not open'
#     my_comment = '''List view should show tabular structure with following columns
# 1. File name with checkbox
# 2. File size
# 3. Asset Type
# 4. Download icon button:- On click Icon user should be able to download that asset
# 5. Cart icon button:- on click add to cart icon add to cart popup should be opened'''
#
#
# #@allure.title('TC_462: Verify Filter Elements')
# def test_verify_left_filter_elements_paid_ad_memo(browser):
#     assets_page = AssetsPage(browser)
#     global test, my_comment
#     test = test_case_ids[459]  # 1271 #589
#     my_comment = 'Reset Filter is not Present in All Assets Header-Section'
#     assets_page.assets_page_refresh()
#     assets_page.click_paid_ad_memo_tab_button()
#     reset_filter = assets_page.verify_reset_filter_button()
#     assert reset_filter == True, 'Reset Filter is not Present in All Assets Header-Section'
#     my_comment = 'File Type Dropdown is not present in Asset page'
#     file_type = assets_page.verify_file_type_filter_dropdown()
#     assert file_type == True, 'File Type Dropdown is not present in Asset page'
#     my_comment = 'Asset Type is not present in Asset page'
#     asset_type = assets_page.verify_asset_type_filter_dropdown()
#     assert asset_type == True, 'Asset Type is not present in Asset page'
#     my_comment = 'File-Size is not present in Asset Page'
#     file_size = assets_page.verify_file_size_filter_dropdown()
#     assert file_size == True, 'File-Size is not present in Asset Page'
#     my_comment = '''Filter have following elements:-
# 1. File Type filter
# 2. Assets Type filter
# 3, File size filter
# '''
#
#
# #@allure.title('TC_463: Verify File type filter functionality')
# def test_verify_file_type_functionality_paid_ad_memo(browser):
#     assets_page = AssetsPage(browser)
#     global test, my_comment
#     test = test_case_ids[460]  # 1272 #590
#     my_comment = 'Type File Filter is not present or not working'
#     assets_page.click_pdf_checkbox_file_type()
#     after_filter = assets_page.verify_total_count_asset()
#     count_text = assets_page.verify_selected_checkbox_count()
#     assert count_text == '1', 'Count-Number is not present in File Type'
#     assets_page.click_file_type_clear_button()
#     my_comment = 'clear button is not clickable'
#     after_clear = assets_page.verify_total_count_asset()
#     assert (after_clear >= after_filter), 'clear button is not clickable'
#     clear_button = assets_page.verify_click_clear_selected_checkbox_count()
#     assert clear_button == False, 'Clear button is not Clickable in video-tab'
#     my_comment = '''1. On click file type filter a dropdown should opened
# 2. Clear Button:- On click Clear button File type filters should be rested
# 3. Checkboxes with mention file Type
# 4 Total checkboxes selected count
# '''
#
#
# #@allure.title('TC_464: Verify user is able to filter Assets by File type')
# def test_verify_single_file_filter_paid_as_memo(browser):
#     assets_page = AssetsPage(browser)
#     global test, my_comment
#     test = test_case_ids[461]  # 1273  #591
#     my_comment = ' Type File Filter is not present or not working'
#     assets_page.click_pdf_checkbox_file_type()
#     after_filter = assets_page.verify_total_count_asset()
#     count_text = assets_page.verify_selected_checkbox_count()
#     my_comment = 'Count-Number is not present in File Type'
#     assert count_text == '1', 'Count-Number is not present in File TYpe'
#     assets_page.click_file_type_clear_button()
#     after_clear = assets_page.verify_total_count_asset()
#     assert (after_clear >= after_filter), 'Type File Filter is not present or not working'
#     clear_button = assets_page.verify_click_clear_selected_checkbox_count()
#     assert clear_button == False, 'Clear button is not Clickable in video-tab'
#     my_comment = '''User should be able to filter assets by File type by selecting the Checkboxes from the drop-down
#                     Search Result should show assets which has the selected Checkboxes'''
#
#
# #@allure.title('TC_467: Verify Assets Type filter functionality')
# def test_verify_assets_type_filter_elements_paid_as_memo(browser):
#     assets_page = AssetsPage(browser)
#     global test, my_comment
#     test = test_case_ids[463]  # 1276 #594
#     my_comment = 'Video Properties heading is not Present in Asset Section'
#     video_text = assets_page.verify_asset_type_heading_text()
#     assert video_text == True, 'Video Properties heading is not Present in Asset Section'
#     my_comment = 'Document text is not present in asset type Section'
#     documents_text = assets_page.verify_asset_type_documents()
#     assert documents_text == True, 'Document text is not present in asset type Section'
#     my_comment = 'Ads Filter is not Present in asset type Section'
#     ads_type = assets_page.verify_asset_type_ads()
#     assert ads_type == True, 'Ads Filter is not Present in asset type Section'
#     my_comment = 'Video Filter is not present in asset type Section'
#     assets_page.click_paid_tab_paid_ad_memo_checkbox()
#     after_filter = assets_page.verify_total_count_asset()
#     my_comment = 'Asset Type clear Filter is not Working'
#     count_text = assets_page.verify_selected_checkbox_count()
#     assert count_text == '1', 'Count-Number is not present in Video properties'
#     assets_page.click_clear_button_asset_type_property()
#     after_clear = assets_page.verify_total_count_asset()
#     assert (after_clear >= after_filter), 'Asset Type clear Filter is not Working'
#     clear_button = assets_page.verify_click_clear_selected_checkbox_count()
#     assert clear_button == False, 'Clear button is not Clickable in video-tab'
#     clear_button = assets_page.verify_click_clear_selected_checkbox_count()
#     assert clear_button == False, 'Clear button is not Clickable in video-tab'
#     my_comment = '''1. On click Assets Type filter a dropdown should opened
# 2. Clear Button:- On click Clear button Assets Type filters should be rested
# 3. Checkboxes with mention Assets Type
# 4 Total checkboxes selected count
# 5. Documents filters
# 6. Ads Filter'''
#
#
# #@allure.title('TC_468: Verify user is able to filter assets by Assets Type')
# def test_verify_single_assets_type_paid_as_memo(browser):
#     assets_page = AssetsPage(browser)
#     global test, my_comment
#     test = test_case_ids[464]  # 1277 #595
#     my_comment = 'Count-Number is not present in Asset Type filter /  '
#     assets_page.click_document_script_checkbox()
#     after_filter = assets_page.verify_total_count_asset()
#     count_text = assets_page.verify_selected_checkbox_count()
#     assert count_text == '1', 'Count-Number is not present in Asset type filter'
#     assets_page.click_paid_tab_paid_ad_memo_checkbox()
#     my_comment = 'Asset Type clear Filter is not Working'
#     after_clear = assets_page.verify_total_count_asset()
#     assert (after_clear >= after_filter), 'Asset Type clear Filter is not Working'
#     clear_button = assets_page.verify_click_clear_selected_checkbox_count()
#     assert clear_button == False, 'Clear button is not Clickable in video-tab'
#     my_comment = 'User should be able to filter assets by Assets Type by selecting the Checkboxes from ' \
#                  'the drop-down Search Result should show assets which has the selected Checkboxes'
#
#
# #@allure.title('TC_469: Verify user is able to apply multiple Checkboxes filters')
# def test_verify_multiple_assets_type_paid_as_memo(browser):
#     assets_page = AssetsPage(browser)
#     global test, my_comment
#     test = test_case_ids[465]  # 1278 #596
#     my_comment = 'Count-Number is not present in Asset Type filter / multiple filters are not applied'
#     assets_page.click_paid_tab_paid_ad_memo_checkbox()
#     assets_page.click_paid_tab_ads_paid_ad_memo_checkbox()
#     after_filter = assets_page.verify_total_count_asset()
#     count_text = assets_page.verify_selected_checkbox_count()
#     assert count_text == '2', 'Count-Number is not present in Video properties'
#     assets_page.click_clear_button_asset_type_property()
#     after_clear = assets_page.verify_total_count_asset()
#     assert (after_clear >= after_filter), 'Asset Type clear Filter is not Working'
#     clear_button = assets_page.verify_click_clear_selected_checkbox_count()
#     assert clear_button == False, 'Clear button is not Clickable in video-tab'
#     my_comment = 'User should be able to select multiple Assets Type filters Search ' \
#                  'results should show all Assets which have the selected Checkboxes'
#
#
# #@allure.title('TC_470: Verify file size filter functionality')
# def test_verify_size_filter_functionality_paid_as_memo(browser):
#     assets_page = AssetsPage(browser)
#     global test, my_comment
#     test = test_case_ids[466]  # 1279 #597
#     my_comment = 'File-Size heading text is not present'
#     file_size = assets_page.verify_file_size_heading_text()
#     assert file_size == True, 'File-Size heading text is not present'
#     range_filter = assets_page.verify_range_mb_filter()
#     assert range_filter == True, "Range Filter is not Present in Video tab section"
#     assets_page.verify_reset_button_files_size_property()
#     my_comment = '''1. On clickFile size  filter a dropdown should opened
# 2. Reset Button:- Reset button is present
# 3. Range selector'''
#
#
# #@allure.title('TC_472: Verify pagination elements')
# def test_verify_Pagination_elements_paid_as_memo(browser):
#     film_series = filmSeriesPage(browser)
#     global test, my_comment
#     test = test_case_ids[468]  # 1281 #599
#     my_comment = 'right cursor is not clickable'
#     right_cursor = film_series.verify_right_cursor_button_disabled()
#     assert 'disabled' in right_cursor, 'Right cursor is not disabled'
#     disable_text = film_series.verify_left_disabled_cursor()
#     assert 'disabled' in disable_text, 'left cursor is not disabled'
#     my_comment = 'One page is not Active'
#     active_page = film_series.verify_one_active_page()
#     assert active_page == True, 'All pages are disabled'
#     my_comment = '''Pagination have following elements:-
# 1. Prev navigation arrow
# 2. Next navigation arrow
# 3. Page number '''
#
#
# #@allure.title('TC_476: Verify Elements present on My Carts Page')
# def test_my_cart_page_elements(browser):
#     home = homepage(browser)
#     home_page = homePageObj(browser)
#     my_cart_obj = MyCartsPage(browser)
#     global test, my_comment
#     test = test_case_ids[472]  # 1285 #603
#     my_comment = 'My Carts title is not clickable /  Your Cart text is not present in My-cart page'
#     home.gotohomepage(_url_)
#     cart_page = my_cart_obj.click_my_carts_header_title()
#     assert cart_page == True, 'My Carts title is not clickable /  Your Cart text is not present in My-cart page'
#     my_comment = "Header 'Films & Series' link not found"
#     films_series = home.HeaderFilmsAndSeries()
#     assert films_series == True, "Header 'Films & Series' button not found"
#     my_list = home.HeaderMylist()
#     assert my_list == True, "My list link not found"
#     my_comment = "Logout button not found"
#     logout = home.HeaderLogoutButton()
#     assert logout == True, "Logout button not found"
#     marketing_rules = home.HeaderMarketingRules()
#     assert marketing_rules == True, "Marketing Rules button not found"
#     assets = home.HeaderAssets()
#     assert assets == True, "Assets Button not found"
#     my_comment = "My Carts button not found"
#     my_cart = home.HeaderMyCarts()
#     assert my_cart == True, "My Carts button not found"
#     my_comment = 'Delete button is not present in My Cart page'
#     delete_button = my_cart_obj.verify_delete_button()
#     assert delete_button == True, 'Delete button is not present in My Cart page'
#     my_comment = 'cart name is not Present in My-Cart page'
#     cart_name = my_cart_obj.verify_cart_name()
#     assert cart_name == True, "cart name is not Present in My-Cart page"
#     cart_count_text = my_cart_obj.verify_cart_count_text()
#     assert cart_count_text == True, "cart count text is not present in My-Cart Page"
#     my_comment = 'Privacy policy is not displaying in global footer. It should be displayed in footer. '
#     assert home_page.verify_Privacypolicy() == True, "Privacy policy is not displaying in global footer. It should be " \
#                                                      "displayed in footer. "
#     assert home_page.verify_termsUse() == True, "Terms and Use is not displaying in global footer. It should be " \
#                                                 "displayed in footer. "
#     my_comment = 'Terms and Use is not displaying in global footer. It should be displayed in footer. '
#     assert home_page.verify_footerLogo() == True, "MGM logo  is not displaying in global footer. It should be " \
#                                                   "displayed in footer. "
#     my_comment = "Support link is not displaying in global footer. It should be displayed in footer. "
#     assert home_page.verify_supportLink() == True, "Support link is not displaying in global footer. It should be " \
#                                                    "displayed in footer. "
#     assert home_page.verify_address() == True, "Address text is not displaying in global footer. It should be " \
#                                                "displayed in footer. "
#     assert home_page.verify_legal() == True, "Legal text is not displaying in global footer. It should be " \
#                                              "displayed in footer. "
#     assert home_page.verify_contact_us() == True, "Contact-us is not displaying in global footer. It should be " \
#                                                   "displayed in footer. "
#     my_comment = 'Youtube icon is not displaying in global footer. It should be displayed in footer. '
#     assert home_page.verify_youtubeIcon() == True, "Youtube icon is not displaying in global footer. It should be " \
#                                                    "displayed in footer. "
#     assert home_page.verify_fbIcon() == True, "Facebook icon is not displaying in global footer. It should be " \
#                                               "displayed in footer. "
#     assert home_page.verify_twitterIcon() == True, "Twitter icon is not displaying in global footer. It should be " \
#                                                    "displayed in footer. "
#     assert home_page.verify_instaIcon() == True, "Instagram icon is not displaying in global footer. It should be " \
#                                                  "displayed in footer. "
#     assert home_page.verify_copyright() == True, "Copyright is not displaying in global footer. It should be " \
#                                                  "displayed in footer. "
#     my_comment = 'Connect is not displaying in global footer. It should be displayed in footer. '
#     assert home_page.verify_connect() == True, "Connect is not displaying in global footer. It should be " \
#                                                "displayed in footer. "
#     my_comment = '''My Carts page should have the following elements:
# 1. Global Header
# 2. Your Cart text
# 3. Cart name with total counts
# 5. Cart Delete button
# 6. Global Footer'''
#
#
# #@allure.title('TC_477: Verify user is able to open carts details page')
# def test_cart_detail_page(browser):
#     my_cart_obj = MyCartsPage(browser)
#     global test, my_comment
#     test = test_case_ids[473]  # 1286 #604
#     my_comment = 'Cart-Name is not clickable / Cart Title name is not Present in cart page'
#     cart_title = my_cart_obj.click_cart_title_text()
#     assert cart_title == True, 'Cart-Name is not clickable / Cart Title name is not Present in cart page'
#     my_comment = 'On click any cart list page should redirected to cart details page'
#
# #
# #@allure.title('TC_478: Verify delete popup is open when user click on delete button')
# def test_click_cart_delete_button(browser):
#     home = homepage(browser)
#     my_cart_obj = MyCartsPage(browser)
#     global test, my_comment
#     test = test_case_ids[474]  # 1287 #605
#     my_comment = 'My Carts title is not clickable /  Your Cart text is not present in My-cart page'
#     home.gotohomepage(_url_)
#     cart_page = my_cart_obj.click_my_carts_header_title()
#     assert cart_page == True, 'My Carts title is not clickable /  Your Cart text is not present in My-cart page'
#     my_cart_obj.click_delete_button()
#     my_comment = 'Delete cart popup is not present / Cart Delete button is not Clickable '
#     delete_cart = my_cart_obj.verify_delete_popup_delete_cart_button()
#     assert delete_cart == True, 'Delete cart popup is not present'
#     my_comment = 'on click delete button a popup window should be opened'
#
#
# #@allure.title('TC_479: Verify delete popup elements')
# def test_verify_delete_cart_popup_elements(browser):
#     my_cart_obj = MyCartsPage(browser)
#     global test, my_comment
#     test = test_case_ids[475]  # 1288 #606
#     my_comment = 'Delete cart popup is not present / cart delete button is not present'
#     delete_cart = my_cart_obj.verify_delete_popup_delete_cart_button()
#     assert delete_cart == True, 'cart Delete button is not present'
#     cancel_button = my_cart_obj.verify_delete_popup_cancel_button()
#     assert cancel_button == True, 'Cancel button is not present in delete popup'
#     my_comment = 'Close button is not present in delete popup'
#     close_button = my_cart_obj.verify_delete_popup_close_button()
#     assert close_button == True, 'Close button is not present in delete popup'
#     my_comment = 'Static Text is not present in delete popup'
#     static_text = my_cart_obj.verify_delete_popup_static_text()
#     assert static_text == True, 'Static Text is not present in delete popup'
#     my_comment = '''Delete popup have following elements:-
#
# 1.Close button
# 2. static text
# 3. Cart name
# 4. Delete button
# 5. Cancel button'''
#
#
# #@allure.title('TC_480: Verify close button is clickable')
# def test_click_close_button_cart_popup_(browser):
#     my_cart_obj = MyCartsPage(browser)
#     global test, my_comment
#     test = test_case_ids[476]  # 1289 #607
#     my_comment = 'Delete cart popup is not present / close button is not clickable in delete cart popup'
#     close_button = my_cart_obj.click_close_button_delete_popup()
#     assert close_button == True, 'close button is not clickable in delete cart popup'
#     my_comment = 'On click close button popup should be closed'
#
#
# #@allure.title('TC_482: Verify cancel button is clickable')
# def test_click_cart_delete_button_for_cancel_button(browser):
#     my_cart_obj = MyCartsPage(browser)
#     global test, my_comment
#     test = test_case_ids[478]  # 1291 #609
#     my_cart_obj.click_delete_button()
#     my_comment = 'Delete cart popup is not present / Cart Delete button is not Clickable '
#     delete_cart = my_cart_obj.verify_delete_popup_delete_cart_button()
#     assert delete_cart == True, 'Delete cart popup is not present'
#     my_comment = 'cancel button is not clickable in delete cart popup'
#     cancel_button = my_cart_obj.click_cancel_button_delete_popup()
#     assert cancel_button == True, 'cancel button is not clickable in delete cart popup'
#     my_comment = 'on Click cancel button popup should be closed'
#
#
# #@allure.title('TC_481: Verify user is able to delete the cart')
# def test_click_cart_delete_button_for_delete_cart(browser):
#     my_cart_obj = MyCartsPage(browser)
#     global test, my_comment
#     test = test_case_ids[477]  # 1290 #608
#     my_cart_obj.click_delete_button_testing_cart2()
#     my_comment = 'Delete cart popup is not present / Cart Delete button is not Clickable '
#     delete_cart = my_cart_obj.verify_delete_popup_delete_cart_button()
#     assert delete_cart == True, 'Delete cart popup is not present'
#     my_comment = 'user is not able to delete any cart'
#     click_delete_cart = my_cart_obj.verify_click_delete_cart_button_delete_popup()
#     assert click_delete_cart == True, 'user is not able to delete any cart'
#     testing_cart = my_cart_obj.verify_testing_cart2_delete()
#     assert testing_cart == True, 'user is not able to delete any cart'
#     my_comment = 'On click delete cart button cart is deleted successfully'
#
#
# #@allure.title('TC_483: Verify Elements present on Cart details page')
# def test_verify_cart_elements_cart_page(browser):
#     my_cart_obj = MyCartsPage(browser)
#     home_page = homePageObj(browser)
#     global test, my_comment
#     test = test_case_ids[479]  # 1293 #610
#     home = homepage(browser)
#     my_comment = 'My Carts title is not clickable /  Your Cart text is not present in My-cart page'
#     home.gotohomepage(_url_)
#     cart_page = my_cart_obj.click_my_carts_header_title()
#     assert cart_page == True, 'My Carts title is not clickable /  Your Cart text is not present in My-cart page'
#     my_cart_obj.click_test_elements_cart()
#     films_series = home.HeaderFilmsAndSeries()
#     assert films_series == True, "Header 'Films & Series' button not found"
#     my_list = home.HeaderMylist()
#     assert my_list == True, "My list link not found"
#     my_comment = "Logout button not found"
#     logout = home.HeaderLogoutButton()
#     assert logout == True, "Logout button not found"
#     marketing_rules = home.HeaderMarketingRules()
#     assert marketing_rules == True, "Marketing Rules button not found"
#     assets = home.HeaderAssets()
#     assert assets == True, "Assets Button not found"
#     my_comment = "My Carts button not found"
#     my_cart = home.HeaderMyCarts()
#     assert my_cart == True, "My Carts button not found"
#     my_comment = 'Cart Title name is not present in my cart page'
#     cart_name = my_cart_obj.verify_cart_title_name()
#     assert cart_name == True, 'Cart Title name is not present in my cart page'
#     my_comment = 'Edit cart name button is not present in my cart page'
#     edit_button = my_cart_obj.verify_cart_edit_name()
#     assert edit_button == True, 'Edit cart name button is not present in my cart page'
#     my_comment = 'Delete button is not present in Cart Detail page'
#     delete_button = my_cart_obj.verify_cart_page_delete_button()
#     assert delete_button == True, 'Delete button is not present in Cart Detail page'
#     my_comment = 'Download button is not present in cart detail page'
#     download_button = my_cart_obj.verify_cart_page_download_button()
#     assert download_button == True, 'Download button is not present in cart detail page'
#     sorting_button = my_cart_obj.verify_cart_page_sorting_button()
#     assert sorting_button == True, 'Sorting button are not present in cart detail page'
#     tabular_form = my_cart_obj.verify_cart_tabular_structure()
#     assert tabular_form == True, 'Cart detail page is not contain any Tabular Structure'
#     my_comment = 'Privacy policy is not displaying in global footer. It should be displayed in footer. '
#     assert home_page.verify_Privacypolicy() == True, "Privacy policy is not displaying in global footer. It should be " \
#                                                      "displayed in footer. "
#     assert home_page.verify_termsUse() == True, "Terms and Use is not displaying in global footer. It should be " \
#                                                 "displayed in footer. "
#     my_comment = 'Terms and Use is not displaying in global footer. It should be displayed in footer. '
#     assert home_page.verify_footerLogo() == True, "MGM logo  is not displaying in global footer. It should be " \
#                                                   "displayed in footer. "
#     my_comment = "Support link is not displaying in global footer. It should be displayed in footer. "
#     assert home_page.verify_supportLink() == True, "Support link is not displaying in global footer. It should be " \
#                                                    "displayed in footer. "
#     assert home_page.verify_address() == True, "Address text is not displaying in global footer. It should be " \
#                                                "displayed in footer. "
#     assert home_page.verify_legal() == True, "Legal text is not displaying in global footer. It should be " \
#                                              "displayed in footer. "
#     assert home_page.verify_contact_us() == True, "Contact-us is not displaying in global footer. It should be " \
#                                                   "displayed in footer. "
#     my_comment = 'Youtube icon is not displaying in global footer. It should be displayed in footer. '
#     assert home_page.verify_youtubeIcon() == True, "Youtube icon is not displaying in global footer. It should be " \
#                                                    "displayed in footer. "
#     assert home_page.verify_fbIcon() == True, "Facebook icon is not displaying in global footer. It should be " \
#                                               "displayed in footer. "
#     assert home_page.verify_twitterIcon() == True, "Twitter icon is not displaying in global footer. It should be " \
#                                                    "displayed in footer. "
#     assert home_page.verify_instaIcon() == True, "Instagram icon is not displaying in global footer. It should be " \
#                                                  "displayed in footer. "
#     assert home_page.verify_copyright() == True, "Copyright is not displaying in global footer. It should be " \
#                                                  "displayed in footer. "
#     my_comment = 'Connect is not displaying in global footer. It should be displayed in footer. '
#     assert home_page.verify_connect() == True, "Connect is not displaying in global footer. It should be " \
#                                                "displayed in footer. "
#     my_comment = '''Cart Details page should have the following elements:
# 1. Global Header
# 2. Cart name and edit button
# 3. Total assets count
# 4. delete button
# 5. Download cart button
# 6. Sorting Filter
# 7 Assets in Tabular form
# 8. Global Footer'''
#
#
# #@allure.title('TC_484: Verify cart name is correct ')
# def test_verify_cart_name_correct(browser):
#     my_cart_obj = MyCartsPage(browser)
#     global test, my_comment
#     test = test_case_ids[480]  # 1294 #611
#     my_comment = 'cart name is not present / Cart name is not correct '
#     title_name = my_cart_obj.verify_cart_title_name_text()
#     assert 'testElements' in title_name, 'cart name is not present / Cart name is not correct '
#     my_comment = 'User should able to see correct cart name'
#
#
# #@allure.title('TC_486: Verify total assets count is correct ')
# def test_verify_cart_name_correct_count(browser):
#     my_cart_obj = MyCartsPage(browser)
#     global test, my_comment
#     test = test_case_ids[482]  # 1296 #613
#     my_comment = 'Assets Count is not correct in Cart detail page'
#     assets_count = my_cart_obj.verify_assets_count_cart_detail_page()
#     assert  assets_count == '4', 'Assets Count is not correct in Cart detail page'
#     my_comment = 'Total assets counts is correct'
#
#
# #@allure.title('TC_487: Verify delete button is clickable ')
# def test_verify_cart_detail_delete_button(browser):
#     my_cart_obj = MyCartsPage(browser)
#     global test, my_comment
#     test = test_case_ids[483]  # 1297 #614
#     my_comment = 'Delete button is not present in Cart Detail page'
#     my_cart_obj.click_delete_button_test_elements_cart()
#     my_comment = 'Delete popup is not present / Delete button is not clickable'
#     delete_cart = my_cart_obj.verify_delete_popup_delete_cart_button()
#     assert delete_cart == True, 'Delete popup is not present / Delete button is not clickable'
#     my_comment = 'On click delete button a popup should be opened'
#
#
# #@allure.title('TC_488: Verify delete popup elements')
# def test_verify_delete_cart_popup_elements_cart_detail_page(browser):
#     my_cart_obj = MyCartsPage(browser)
#     global test, my_comment
#     test = test_case_ids[484]  # 1298 #615
#     my_comment = 'Delete cart popup is not present / cart delete button is not present'
#     delete_cart = my_cart_obj.verify_delete_popup_delete_cart_button()
#     assert delete_cart == True, 'cart Delete button is not present'
#     cancel_button = my_cart_obj.verify_delete_popup_cancel_button()
#     assert cancel_button == True, 'Cancel button is not present in delete popup'
#     my_comment = 'Close button is not present in delete popup'
#     close_button = my_cart_obj.verify_delete_popup_close_button()
#     assert close_button == True, 'Close button is not present in delete popup'
#     my_comment = 'Static Text is not present in delete popup'
#     static_text = my_cart_obj.verify_delete_popup_static_text()
#     assert static_text == True, 'Static Text is not present in delete popup'
#     my_comment = '''Delete popup have following elements:-
#
# 1.Close button
# 2. static text
# 3. Cart name
# 4. Delete button
# 5. Cancel button'''
#
#
# #@allure.title('TC_489: Verify close button is clickable')
# def test_click_close_button_cart_popup_cart_detail_page(browser):
#     my_cart_obj = MyCartsPage(browser)
#     global test, my_comment
#     test = test_case_ids[485]  # 1299 #616
#     my_comment = 'Delete cart popup is not present / close button is not clickable in delete cart popup'
#     close_button = my_cart_obj.click_close_button_delete_popup()
#     assert close_button == True, 'close button is not clickable in delete cart popup'
#     my_comment = 'On click close button popup should be closed'
#
#
# #@allure.title('TC_491: Verify cancel button is clickable')
# def test_click_cancel_button_cart_detail_page_popup(browser):
#     my_cart_obj = MyCartsPage(browser)
#     global test, my_comment
#     test = test_case_ids[487]  # 1301 #618
#     my_comment = 'Delete popup is not present '
#     # my_cart_obj.click_test_elements_cart()
#     my_cart_obj.click_delete_button_test_elements_cart()
#     my_comment = 'Delete popup is not present / Delete button is not clickable'
#     delete_cart = my_cart_obj.verify_delete_popup_delete_cart_button()
#     assert delete_cart == True, 'Delete popup is not present / Delete button is not clickable'
#     my_comment = 'cancel button is not clickable in delete cart popup'
#     cancel_button = my_cart_obj.click_cancel_button_delete_popup()
#     assert cancel_button == True, 'cancel button is not clickable in delete cart popup'
#     my_comment = 'on Click cancel button popup should be closed'
#
#
# #@allure.title('TC_492: Verify Download cart popup Elements:-')
# def test_verify_download_cart_popup_elements_cart_details_page(browser):
#     my_cart_obj = MyCartsPage(browser)
#     global test, my_comment
#     test = test_case_ids[488]  # 1303 #619
#     my_comment = 'Download popup is not present'
#     # my_cart_obj.click_test_elements_cart()
#     my_cart_obj.click_download_cart_detail_page()
#     my_comment = 'Start Download button is not present in Download cart popup'
#     start_download = my_cart_obj.verify_start_download_Button_cart_detail_page()
#     assert start_download == True, 'Start Download button is not present in Download cart popup '
#     my_comment = 'Close button is not present in delete popup'
#     close_button = my_cart_obj.verify_delete_popup_close_button()
#     assert close_button == True, 'Close button is not present in delete popup'
#     cancel_button = my_cart_obj.verify_delete_popup_cancel_button()
#     assert cancel_button == True, 'Cancel button is not present in delete popup'
#     static_text = my_cart_obj.verify_delete_popup_static_text()
#     assert static_text == True, 'Static Text is not present in delete popup'
#     my_comment = '''Download cart have following elements:-
#
# 1.Close button
# 2. Static text
# 3. Start download button
# 4. Cancel button'''
#
# #
# #@allure.title('TC_493: Verify close button is clickable ')
# def test_click_close_button_download_popup_cart_detail_page(browser):
#     my_cart_obj = MyCartsPage(browser)
#     global test, my_comment
#     test = test_case_ids[489]  # 1304 #620
#     my_comment = 'Download cart popup is not present / close button is not clickable in download cart popup'
#     close_button = my_cart_obj.click_close_button_delete_popup()
#     assert close_button == True, 'close button is not clickable in delete cart popup'
#     my_comment = 'On click close button popup should be closed'
#
#
# #@allure.title('TC_494: Verify count of selected items is correct')
# def test_verify_static_text_download_cart_popup_(browser):
#     my_cart_obj = MyCartsPage(browser)
#     global test, my_comment
#     test = test_case_ids[490]  # 1305 #621
#     my_comment = 'Download popup is not present'
#     my_cart_obj.click_download_cart_detail_page()
#     my_comment = 'Count of selected item is not correct in Cart detail page'
#     static_text = my_cart_obj.verify_download_popup_static_text()
#     assert '4' in static_text, 'Count of selected item is not correct in Cart detail page'
#     my_comment = 'Count of selected assets should be correct'
#
#
# #@allure.title('TC_496: Verify cancel button is clickable')
# def test_click_cancel_button_download_cart_popup(browser):
#     my_cart_obj = MyCartsPage(browser)
#     global test, my_comment
#     test = test_case_ids[492]  # 1307 #623
#     my_comment = 'cancel button is not clickable in delete cart popup'
#     cancel_button = my_cart_obj.click_cancel_button_delete_popup()
#     assert cancel_button == True, 'cancel button is not clickable in delete cart popup'
#     my_comment = 'on Click cancel button popup should be closed'
#
#
# #@allure.title('TC_495: Verify user is able to download asset')
# def test_click_start_download_button_download_cart_popup(browser):
#     my_cart_obj = MyCartsPage(browser)
#     global test, my_comment
#     test = test_case_ids[491]  # 1306 #622
#     my_comment = 'Downloading is not started after click on start download button'
#     my_cart_obj.click_download_cart_detail_page()
#     download_start = my_cart_obj.click_start_download_Button_cart_detail_page()
#     assert 'Download in progress' in download_start, 'Downloading is not started after click on start download button'
#     time.sleep(10)
#     my_comment = 'On click start download button downloading should be start'
#
#
# #@allure.title('TC_497: Verify the options of Sorting and their functionality')
# def test_verify_sorting_functionality_cart_detail_page(browser):
#     my_cart_obj = MyCartsPage(browser)
#     global test, my_comment
#     test = test_case_ids[493]  # 1308 #624
#     my_comment = 'Sorting button is not clickable in Cart detail page'
#     my_cart_obj.click_list_tabular_row_button()
#     my_cart_obj.click_cart_page_sorting_button()
#     my_comment = 'sorting by higher to lower file size functionality is not working '
#     first_file, second_file = my_cart_obj.click_file_down_size_sorting_button()
#     assert first_file > second_file, 'sorting by higher to lower file size functionality is not working '
#     my_comment = 'sorting by lower to higher file size functionality is not working '
#     my_cart_obj.click_cart_page_sorting_button()
#     first_file, second_file = my_cart_obj.click_file_up_size_sorting_button()
#     assert first_file < second_file, 'sorting by lower to higher file size functionality is not working '
#     my_cart_obj.click_cart_page_sorting_button()
#     my_comment = 'sorting A to Z functionality is not working '
#     file_name, last_name = my_cart_obj.verify_sorting_a_to_z()
#     assert (file_name == '1') & (last_name == 'R'), 'sorting A to Z functionality is not working '
#     my_comment = 'sorting Z to A functionality is not working '
#     my_cart_obj.click_cart_page_sorting_button()
#     file_name, last_name = my_cart_obj.verify_sorting_z_to_a()
#     assert (file_name == 'R') & (last_name == '1'), 'sorting Z to A functionality is not working '
#     my_comment = '''Sorting drop down should have the following options with mentioned behaviour
# 1. File size (Low to high)  -- Titles should be ordered in Increasing order
# 2. File size (highTo low)  -- Titles should be ordered in Decreasing corder
# 3. Sort A-Z  -- Assets should be ordered in Ascending order of Alphabets
# 4. Sort Z-A -- Assets should be ordered in Descending order of Alphabets
# '''
#
#
# #@allure.title('TC_498: Verify assets in tabular form')
# def test_verify_cart_details_page_tabular(browser):
#     my_cart_obj = MyCartsPage(browser)
#     global test, my_comment
#     test = test_case_ids[494] #1309 #625
#     my_comment = 'Asset Cart detail page is not is Tabular form'
#     title_column = my_cart_obj.verify_title_name_column()
#     assert title_column >= 4, 'Title column is not present'
#     file_name = my_cart_obj.verify_file_name_column()
#     assert file_name >= 4, 'File Name Column is not present'
#     file_size = my_cart_obj.verify_file_size_column()
#     assert file_size >= 4, 'File Size Column is not present'
#     asset_type = my_cart_obj.verify_asset_type_column()
#     assert asset_type >= 4, 'Asset type Column is not present'
#     my_comment = '''1. Title name
# 2. File name
# 3. File Size
# 4. Asset Type
# 5. Delete button'''
#
#
# #@allure.title('TC_499: Verify user is able to delete particular asset ')
# def test_verify_cart_elements(browser):
#     my_cart_obj = MyCartsPage(browser)
#     global test, my_comment
#     test = test_case_ids[495]# 1310 #626
#     home = homepage(browser)
#     my_comment = 'My Carts title is not clickable /  Your Cart text is not present in My-cart page'
#     home.gotohomepage(_url_)
#     cart_page = my_cart_obj.click_my_carts_header_title()
#     assert cart_page == True, 'My Carts title is not clickable /  Your Cart text is not present in My-cart page'
#     my_cart_obj.click_testing_first_cart()
#     my_cart_obj.click_list_tabular_row_button()
#     first_file_name = my_cart_obj.verify_first_asset_file_name()
#     my_cart_obj.click_delete_remove_asset_button()
#     my_cart_obj.click_remove_asset_button()
#     my_comment = 'user is not able to remove a particular asset'
#     after_remove_first_file_name = my_cart_obj.verify_first_asset_file_name()
#     assert (first_file_name != after_remove_first_file_name), 'user is not able to remove a particular asset'
#     my_comment = 'user should be able to delete any asset from carts by clicking on delete button'
#
#
# #@allure.title('TC_490: Verify user is able to delete the cart')
# def test_verify_cart_detail_delete_cart_button(browser):
#     my_cart_obj = MyCartsPage(browser)
#     home = homepage(browser)
#     global test, my_comment
#     test = test_case_ids[486]  # 1300 #617
#     my_comment = 'Delete button is not present in Cart Detail page'
#     time.sleep(8)
#     my_cart_obj.click_delete_button_test_elements_cart()
#     my_comment = 'Delete popup is not present / Delete button is not clickable'
#     delete_cart = my_cart_obj.verify_delete_popup_delete_cart_button()
#     assert delete_cart == True, 'Delete cart popup is not present'
#     my_comment = 'user is not able to delete any cart'
#     click_delete_cart = my_cart_obj.verify_click_delete_cart_button_delete_popup()
#     assert click_delete_cart == True, 'user is not able to delete any cart'
#     home.gotohomepage(_url_)
#     cart_page = my_cart_obj.click_my_carts_header_title()
#     assert cart_page == True, 'My Carts title is not clickable /  Your Cart text is not present in My-cart page'
#     testing_cart = my_cart_obj.verify_first_testing_first_cart_not_present()
#     assert testing_cart == False,'user is not able to delete any cart'
#     my_comment = 'On click delete cart button cart is deleted successfully'
#
#
# #@allure.title('TC_Raw: logout after all process')
# def test_raw_logout_button_my_cart(browser):
#     home = homepage(browser)
#     home.gotohomepage(_url_)
#     verify = home.ClickLogoutButton()
#     assert verify == True, "User is not logged out"










