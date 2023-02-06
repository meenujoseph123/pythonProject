# import the webdriver
import re
from selenium import webdriver
# import the Keys class
from selenium.webdriver.common import keys

driver = webdriver.Chrome(executable_path="C:\\chromedriver.exe")
# get method to launch the URL
driver.get("http://localhost:8080/")
# to identify the table column below is the sample table element
l = driver.find_elements_by_xpath("//*[@class= 'spTable']/tbody/tr/td[3]")
# to traverse through the list of cell data of column 0(natid)
i = 0
for i in l:
    print("natid-" + i + ":" + i.text)
    natid = i.text
    # find the index where $ starts from
    print("The '$' symbol is displaying from index " + natid.index("$") + 1)
# to close the browser
driver.close()
