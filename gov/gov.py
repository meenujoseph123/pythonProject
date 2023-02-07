import re
import time
from webbrowser import Chrome

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium import webdriver
#from seleniumrequests import Chrome


#from selenium_chrome import Chrome


def loadApplication():
    driver = webdriver.Chrome(options=Chrome, executable_path="C:\Windows\chromedriver.exe")
    time.sleep(25)
    driver.maximize_window()
    driver.get("http://localhost:8080")
    time.sleep(25)
    return driver


def buttonColor():
    try:
        driver = loadApplication()
        # method 1
        Color = driver.findElement(By.css("#contents > a.btn.btn-danger.btn-block")).getCssValue("color")
        print("Button color: " + Color)
        # Method 2
        button = driver.find_elements_by_css_selector("#contents > a.btn.btn-danger.btn-block")
        color = button.value_of_css_property("backgroundColor")
        print(color)
        if color == "rgba(255, 0, 0, 0)":
            print("Button with Red color detected")

    except:
        print("python-BaseException")


def buttonText():
    try:
        driver = loadApplication()
        # method 1
        Text = driver.findElement(By.css("#contents > a.btn.btn-danger.btn-block")).getText()
        print("Button color: " + Text)
        # Method 2
        button = driver.find_elements_by_css_selector("#contents > a.btn.btn-danger.btn-block")
        text = button.value_of_css_property("text")
        print(text)
        if text == "Dispense Now":
            print("Button with text 'Dispense Now' detected")
        else:
            print("Button with text 'Dispensed Now' is not detected")
    except:
        print("python-BaseException")


def clickButton():
    try:
        driver = loadApplication()
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
