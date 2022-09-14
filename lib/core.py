import os
import time
from robot.api.logger import trace
from robot.libraries.BuiltIn import BuiltIn
from selenium import webdriver
from selenium.common.exceptions import StaleElementReferenceException
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from lib.locator_types import LocatorTypes

from lib.logger import Logger


class UIAutomationCore:
    def __init__(self):
        self.logger = Logger().get_logger()
        self.explicit_wait = 30

        try:
            desired_caps = DesiredCapabilities.CHROME
            desired_caps['loggingPrefs'] = {'browser': 'ALL'}
            chrome_options = Options()
            chrome_options.add_argument('--allow-running-insecure-content')
            chrome_options.add_argument('--ignore-certificate-errors')
            chrome_options.add_argument('--no-sandbox')

            try:
                # chrome_options.headless = eval(BuiltIn().get_variable_value("${md.headless}"))
                chrome_options.headless = True
            except Exception:
                self.logger.debug("Config not found/read. Setting headless to True")
                chrome_options.headless = True

            current_path = os.getcwd()
            beyondhr_dir = os.path.join(current_path[:current_path.find('beyondhr')], 'beyondhr')
            download_dir = os.path.join(BuiltIn().get_variable_value("${OUTPUT DIR}"), 'Downloads')
            download_path = {"download.default_directory": f"{download_dir}", "safebrowsing.enabled": "false"}
            chrome_options.add_experimental_option("prefs", download_path)
            self.driver = webdriver.Chrome(f'{beyondhr_dir}/chromedriver', options=chrome_options)

        except Exception as e:
            self.logger.error(f'Unable to initialize Chrome driver. Error: {e}')

    def open_url(self, url):
        try:
            self.driver.get(url)
        except Exception as e:
            trace(e)
            self.logger.error(f'Unable to open URL: {url}')

    def get_elements(self, locator, locator_type='xpath'):
        try:
            self.logger.debug(f'Getting element: {locator}')
            elements = WebDriverWait(self.driver, self.explicit_wait).until(
                EC.presence_of_all_elements_located((LocatorTypes[locator_type], locator)))
            self.logger.debug(f'Total elements found :  {len(elements)}')
            return elements

        except StaleElementReferenceException as e:
            self.logger.error(
                f'Stale element reference exception. Waiting until element not attach to the DOM. Error: {e}')
            element = WebDriverWait(self.driver, self.explicit_wait).until(
                EC.presence_of_all_elements_located((LocatorTypes[locator_type], locator)))
            WebDriverWait(self.driver, self.explicit_wait).until(EC.staleness_of(element))
            return element

        except Exception as e:
            self.logger.error(f'Element {locator} not found. Error: {e}')

    def element_present(self, locator, locator_type='xpath'):
        try:
            self.logger.debug(f'Checking if element is present: {locator}')
            element = WebDriverWait(self.driver, self.explicit_wait).until(
                EC.presence_of_element_located((LocatorTypes[locator_type], locator)))
            return element.is_displayed()

        except StaleElementReferenceException as e:
            self.logger.error(
                f'Stale element reference exception. Waiting until element not attach to the DOM. Error: {e}')
            element = WebDriverWait(self.driver, self.explicit_wait).until(
                EC.presence_of_element_located((locator_type, locator)))
            WebDriverWait(self.driver, self.explicit_wait).until(EC.staleness_of(element))
            return element.is_displayed()

        except Exception as e:
            self.logger.error(f'Element {locator} not found. Error: {e}')

    def element_enabled(self, locator, locator_type='xpath'):
        try:
            self.logger.debug(f'Checking if element is enabled: {locator}')
            element = WebDriverWait(self.driver, self.explicit_wait).until(
                EC.presence_of_element_located((LocatorTypes[locator_type], locator)))
            return element.is_enabled()

        except StaleElementReferenceException as e:
            self.logger.error(
                f'Stale element reference exception. Waiting until element not attach to the DOM. Error: {e}')
            element = WebDriverWait(self.driver, self.explicit_wait).until(
                EC.presence_of_element_located((locator_type, locator)))
            WebDriverWait(self.driver, self.explicit_wait).until(EC.staleness_of(element))
            return element.is_enabled()

        except Exception as e:
            self.logger.error(f'Element {locator} not found. Error: {e}')

    def execute_script(self, script):
        try:
            self.logger.debug(f'Executing script: {script}')
            return self.driver.execute_script(script)

        except Exception as e:
            self.logger.error(f'Error while executing script. Error: {e}')

    def get_text(self, locator_type, locator):
        try:
            self.logger.debug(f'Getting text from element: {locator}')
            element = WebDriverWait(self.driver, self.explicit_wait).until(
                EC.presence_of_element_located((locator_type, locator)))
            self.logger.debug(f'Found text is: {element.text}')
            return element.text

        except StaleElementReferenceException as e:
            self.logger.error(
                f'Stale element reference exception. Waiting until element not attach to the DOM. Error: {e}')
            element = WebDriverWait(self.driver, self.explicit_wait).until(
                EC.presence_of_element_located((locator_type, locator)))
            WebDriverWait(self.driver, self.explicit_wait).until(EC.staleness_of(element))
            return element.text

        except Exception as e:
            self.logger.error(f'Element {locator} not found. Error: {e}')

    def title_matches(self, title):
        try:
            self.logger.debug(f'Checking if title matches: {title}')
            WebDriverWait(self.driver, self.explicit_wait).until(EC.title_is(title))

        except Exception as e:
            self.logger.error(f'Error while checking title. Error: {e}')

    def refresh(self):
        try:
            self.logger.debug(f'Refreshing page')
            self.driver.refresh()
            time.sleep(5)

        except Exception as e:
            self.logger.error(f'Error while refreshing page. Error: {e}')

    def scroll_to(self, locator, locator_type=By.XPATH):
        try:
            self.logger.debug(f'Scrolling to element: {locator}')
            element = WebDriverWait(self.driver, self.explicit_wait).until(
                EC.presence_of_all_elements_located((locator_type, locator)))
            self.driver.execute_script("arguments[0].scrollIntoView();", element)

        except Exception as e:
            self.logger.error(f'Element {locator} not found. Error: {e}')

    def scroll_to_top(self):
        self.logger.debug(f'Scrolling to top of page')
        self.driver.execute_script("window.scrollTo(0, -document.body.scrollHeight);")
        time.sleep(3)

    def scroll_to_bottom(self):
        self.logger.debug(f'Scrolling to bottom of page')
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(3)

    def mouse_hover(self, locator, locator_type=By.XPATH):
        try:
            self.logger.debug(f'Mouse hovering to element: {locator}')
            element = WebDriverWait(self.driver, self.explicit_wait).until(
                EC.presence_of_element_located((locator_type, locator)))
            hover = ActionChains(self.driver).move_to_element(element)
            hover.click().perform()
        except Exception as e:
            self.logger.error(f'Element {locator} not found. Error: {e}')