import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


class TestReportScreenshot:
    def __init__(self, url, image_path):
        self.url = url
        self.image_path = image_path

    def save_image(self):
        options = webdriver.ChromeOptions()
        options.add_argument('headless')
        driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)

        time.sleep(3)
        driver.get(self.url)
        print(driver.title)
        driver.save_screenshot(self.image_path)
        print("Report screenshot taken")
        driver.quit()

    def take_full_page_screenshot(self):
        options = webdriver.ChromeOptions()
        # options.add_argument('headless')
        options.add_argument('window-size=1920x1080')
        driver = webdriver.Chrome(options=options)
        time.sleep(3)
        driver.get(self.url)
        print(driver.title)
        el = driver.find_element(By.TAG_NAME, 'body')
        el.screenshot(self.image_path)
        driver.quit()
