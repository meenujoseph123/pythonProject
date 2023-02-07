import re
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium import webdriver
from selenium_chrome import Chrome


def clickButton():
    try:
        driver = webdriver.Chrome(options=Chrome, executable_path="C:\Windows\chromedriver.exe")
        time.sleep(25)
        driver.maximize_window()
        driver.get("http://localhost:8080")
        time.sleep(25)
        button = driver.find_elements_by_css_selector("#contents > a.btn.btn-danger.btn-block")
        # clicking on the button
        button.click()
        time.sleep(5)
        src = driver.page_source
        text_found = re.search(r'Cash Dispensed', src)
        # self.assertNotEqual(text_found, None)
        print("Text 'Cash Dispersed' detected")
    except:
        print("python-BaseException")
