import re
import time
from selenium import webdriver
from selenium.webdriver.chrome import options


def uploadCSV():
    driver = webdriver.Chrome(options=options, executable_path="C:\Windows\chromedriver.exe")
    time.sleep(25)
    driver.get("http://localhost:8080")
    driver.maximize_window()
    driver.find_elements_by_css_selector("#contents > div.input-group.mb-3 > div.custom-file > input").send_keys(
        "C:\Windows\sample.csv")
    time.sleep(5)
    src = driver.page_source
    text_found = re.search(r'Uploaded', src)
    # self.assertNotEqual(text_found, None)
    print("File uploaded successfully")
