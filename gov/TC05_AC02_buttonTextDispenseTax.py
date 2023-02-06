import re
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium import webdriver
from selenium_chrome import Chrome

try:
    driver = webdriver.Chrome(options=Chrome,executable_path="C:\Windows\chromedriver.exe")
    time.sleep(25)
    driver.maximize_window()
    driver.get("http://localhost:8080")
    time.sleep(25)
    # method 1
    buttonText = driver.findElement(By.css("#contents > a.btn.btn-danger.btn-block")).getText()
    print("Button color: " + buttonText)
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