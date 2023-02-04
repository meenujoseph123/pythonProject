import re
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium import webdriver
try:
    driver = webdriver.Chrome(options=crome,executable_path="C:\Windows\chromedriver.exe")
    time.sleep(25)
    driver.maximize_window()
    driver.get("http://localhost:8080")
    time.sleep(25)
    #method 1
    buttonColor = driver.findElement(By.css("#contents > a.btn.btn-danger.btn-block")).getCssValue("color")
    print("Button color: " + buttonColor)
    #Method 2
    button = driver.find_elements_by_css_selector("#contents > a.btn.btn-danger.btn-block")
    color = button.value_of_css_property("backgroundColor")
    print(color)
    if color == "rgba(255, 0, 0, 0)":
        print("Button with Red color detected")

    # clicking on the button
    button.click()
    time.sleep(5)
    src = driver.page_source
    text_found = re.search(r'Cash Dispensed', src)
    # self.assertNotEqual(text_found, None)
    print("Text 'Cash Dispersed' detected")
except:
    print("python-BaseException")