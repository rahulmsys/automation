from behave import *
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from locators.login_page_locators import *
from locators.home_page_locators import *
from config.conf_vars import *
from selenium.webdriver.support import expected_conditions as EC
from features.helper.logger import Logger

log_file = 'test.log'
log = Logger(log_file)


@given('Open web browser')
def open_web_browser(context):
    context.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    context.driver.get(base_url)
    log.info("Web browser opened")
    context.driver.maximize_window()
    log.info("Web browser maximized")
    context.driver.wait = WebDriverWait(context.driver, 30)


@when('I am on the OrangeHRM login page')
def login_page(context):
    assert context.driver.wait.until(EC.title_is(login_page_title)) is True
    log.info("Login page opened")


@then('I enter "{uname}" as username and "{pwd}" as password')
def enter_username_and_password(context, uname, pwd):
    context.driver.wait.until(EC.presence_of_element_located((By.XPATH, LoginPageLocators.USERNAME_FIELD))).send_keys(
        uname)
    context.driver.wait.until(EC.presence_of_element_located((By.XPATH, LoginPageLocators.PASSWORD_FIELD))).send_keys(
        pwd)


@then('I click on login button')
def click_on_login_button(context):
    context.driver.wait.until(EC.element_to_be_clickable((By.XPATH, LoginPageLocators.LOGIN_BTN))).click()


@then('I should see the OrangeHRM home page')
def verify_home_page(context):
    try:
        context.driver.wait.until(EC.presence_of_element_located((By.XPATH, HomePageLocators.DASHBOARD_LOGO))) is True
    except Exception as e:
        print(e)
        context.driver.quit()
        assert False, "Test failed"


@then('Close the web browser')
def close_web_browser(context):
    context.driver.quit()
    assert True, "Test passed"
