"""
This module contains shared fixtures for web UI tests.
For now, only Chrome browser is supported.
"""
import datetime
import json
import time

import pytest
import allure
import os
import chromedriver_autoinstaller
from appium import webdriver
from allure_commons.types import AttachmentType
from selenium.webdriver.chrome.options import Options


from tests import test_mgm_roar
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver import Firefox
# from webdriver_manager.firefox import GeckoDriverManager

from selenium.webdriver import Chrome

CONFIG_PATH = 'resources/config.json'
Browser_path = "Scripts/chromedriver.exe"
DEFAULT_WAIT_TIME = 10
SUPPORTED_BROWSERS = ['chrome']
# SUPPORTED_BROWSERS = ['firefox']
SUPPORTED_EXECUTORS = ['mobile', 'desktop']


@allure.step('Reading config from json file')
@pytest.fixture(scope='session')
def config():
    # Read the JSON config file and returns it as a parsed dict
    with open(CONFIG_PATH) as config_file:
        data = json.load(config_file)
    return data


@allure.step('Configuring browser')
@pytest.fixture(scope='session')
def config_browser(config):
    # Validate and return the browser choice from the config data
    # To extend the browser support in future
    if 'browser' not in config:
        raise Exception('The config file does not contain "browser"')
    elif config['browser'] not in SUPPORTED_BROWSERS:
        raise Exception(f'"{config["browser"]}" is not a supported browser')
    return config['browser']


@allure.step('Configuring executor')
@pytest.fixture(scope='session')
def config_executor(config):
    # Validate and return the browser choice from the config data
    # To extend the browser support in future
    if 'executor' not in config:
        raise Exception('The config file does not contain "executor"')
    elif config['executor'] not in SUPPORTED_EXECUTORS:
        raise Exception(f'"{config["executor"]}" is not a supported executor')
    return config['executor']


@allure.step('Configuring the wait time for browser')
@pytest.fixture(scope='session')
def config_wait_time(config):
    # Validate and return the wait time from the config data
    return config['wait_time'] if 'wait_time' in config else DEFAULT_WAIT_TIME

def pytest_addoption(parser):
    parser.addoption("--set_url", action="store", default="https://roar.dev.mgm.com/login")

# def create_run_id(run_id):
#     run_ids = str(run_id)


@allure.step('Initializing the configured browser')
@pytest.fixture(scope='session')
def browser(config_browser, config_wait_time, config_executor, request):
    # Initialize WebDriver
    global driver
    if config_browser == 'chrome':
    #if config_browser == 'firefox':
        if config_executor == "mobile":
            desired_caps = {}
            desired_caps['platformName'] = 'Android'
            desired_caps['platformVersion'] = '10'
            desired_caps['deviceName'] = 'myphone'
            desired_caps['browserName'] = 'Chrome'
            driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
        elif config_executor == "desktop":
            # chromedriver_autoinstaller.install()

            options = Options()
            # options.headless = True
            options.add_argument('log-level=3') 
            options.add_argument("--window-size=1920,1080")
            options.add_argument("--disable-extensions")
            options.add_argument("--proxy-server='direct://'")
            options.add_argument("--proxy-bypass-list=*")
            options.add_argument("--start-maximized")
            options.add_argument('--disable-gpu')
            options.add_argument('--disable-dev-shm-usage')
            options.add_argument('--no-sandbox')
            options.add_argument("disable-infobars")
            options.add_argument("--ignore-certificate-errors")
            driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)

            # driver = Chrome(options=options)
            # driver = Firefox(options=options)
            # driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)
            # driver = webdriver.Chrome(ChromeDriverManager().install())
            # driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
        else:
            raise Exception(f'"{config_executor}" is not a supported executor')
    else:
        raise Exception(f'"{config_browser}" is not a supported browser')

    # Wait implicitly for elements to be ready before attempting interactions
    driver.implicitly_wait(config_wait_time)
    driver.maximize_window()

    # Return the driver object at the end of setup
    yield driver



    # For cleanup, quit the driver


# driver.quit()


# @pytest.fixture(scope="function")
# def listener(request):
#     if request.node.rep_call.failed:
#         # Make the screen-shot if test failed:
#         try:
#             b.execute_script("document.body.bgColor = 'white';")
#
#             allure.attach(b.get_screenshot_as_png(),
#                           name=request.function.__name__,
#                           attachment_type=allure.attachment_type.PNG)
#         except:
#             pass # just ignore
#
@pytest.hookimpl(tryfirst=False, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    # print("function is up ")
    pytest_html = item.config.pluginmanager.getplugin("html")
    rep = outcome.get_result()
    extra = getattr(rep, "extra", [])
    extra.append(pytest_html.extras.url("https://mgmstudios.testrail.io/index.php?/projects/overview/1"))
    # print(rep)
    if rep.when == 'call' and rep.outcome == 'passed':
        # print(rep)
        #     print("I am in")
        #     mode = 'a' if os.path.exists('failures') else 'w'
        try:
            # print("in try")
            if test_mgm_roar.update_testrail == True:
                # test_mgm_roar.case_fields()
                test_mgm_roar.pass_update()

        except:
            pass

    if rep.when == 'call' and rep.failed:
        mode = 'a' if os.path.exists('failures') else 'w'
        # file_name = rep.nodeid.replace("::", "_") + ".png"
        # _capture_screenshot(file_name)
        # allure.attach(driver.get_screenshot_as_png(), name="Screenshot", attachment_type=AttachmentType.PNG)
        # print(rep)
        #     print("I am in")
        #     mode = 'a' if os.path.exists('failures') else 'w'
        # extra.append(pytest_html.extra.image('file.png'))
        # rep.extra = extra

        report_directory = os.path.dirname(item.config.option.htmlpath)
        # file_name = rep.nodeid.replace("::", "_") + ".png"
        file_name = str(int(round(time.time() * 1000))) + ".png"
        destinationFile = os.path.join(report_directory, file_name)
        driver.save_screenshot(destinationFile)
        # extra.append(pytest_html.extras.url("https://practicallogix.testrail.io/index.php?/projects/overview/1"))
        if file_name:
            html = '<div><img src="%s" alt="screenshot" style="width:300px;height=200px"' \
                   'onclick="window.open(this.src)" align="right"/></div>' %file_name
            extra.append(pytest_html.extras.html(html))
        rep.extra = extra
        try:
            # print("in try")
            if test_mgm_roar.update_testrail == True:
                # test_mgm_roar.case_fields()
                test_mgm_roar.fail_update()
        except Exception as e:
            print('Fail to take screen-shot: {}'.format(e))
            # with open('failures', e) as f:
            #     if 'browser' in item.fixturenames:  # assume this is fixture with webdriver
            #         web_driver = item.funcargs['browser']
            #     else:
            #         print('Fail to take screen-shot')
            #     return
            # allure.attach(
            #     web_driver.get_screenshot_as_png(),
            #     name='screenshot',
            #     attachment_type=allure.attachment_type.PNG
            # )

def pytest_html_report_title(report):
    report.title = "MGM ROAR"



# def _capture_screenshot(name):
#     # driver.get_screenshot_as_file('screenshot/' + name + "")
#     driver.save_screenshot(name)

# @pytest.fixture(scope='module', autouse=True)
# def teardown_module():
#     yield
#     test_mgm_roar.teardwn()
