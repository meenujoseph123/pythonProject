# import the webdriver
import re
import self
from selenium import webdriver
from robot.libraries.BuiltIn import BuiltIn
from webdriver_manager import driver


class verifyNatIdMasked(object):
    def __init__(self):
        self.selenium_lib = None
        i = 0

    def run_my_code(self):
        self.selenium_lib = BuiltIn().get_library_instance('ExtendedSelenium2Library')
        driver = webdriver.Chrome(executable_path="C:\\chromedriver.exe")
        # get method to launch the URL

        driver.get("http://localhost:8080/")
        # to identify the table column below is the sample table element
        l = driver.find_elements_by_xpath("//*[@class= 'spTable']/tbody/tr/td[3]")
        # to traverse through the list of cell data of column 0(natid)
        for i in l:
            print("natid-" + i + ":" + i.text)
            natid = i.text
            # find the index where $ starts from
            print("The '$' symbol is displaying from index " + natid.index("$") + 1)
            # to close the browser
        driver.close()
