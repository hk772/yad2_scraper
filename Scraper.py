from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time

from selenium.webdriver.common.by import By


class Scraper:
    def __init__(self, driver_path='chromedriver.exe'):
        self.driver = None
        self.service = None
        self.driver_path = driver_path

    def start(self):
        self.service = Service(executable_path=self.driver_path)
        self.driver = webdriver.Chrome(service=self.service)

    def open_page(self, url, sleep_time=10):
        self.driver.get(url)
        time.sleep(sleep_time)

    def get_html_content(self):
        return self.driver.page_source

    def quit_page(self):
        self.driver.quit()

    def next_page(self):
        next_button = self.driver.find_element(By.XPATH, '/html/body/div[2]/div[2]/div/main/div/div[4]/div[5]/div['
                                                         '2]/div[6]/a[2]')
        next_button.click()
        time.sleep(20)

    def get_htmls_for_pages(self, url, num_of_pages):
        self.open_page(url, 20)
        html_content = {}
        for i in range(num_of_pages):
            html_content[i] = self.get_html_content()
            self.next_page()

        self.driver.quit()
        return html_content

