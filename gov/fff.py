from selenium import webdriver
try:
    driver = webdriver.Chrome(executable_path="C:\Windows\chromedriver.exe")
    #driver.get("https://www.python.org")
    driver.get("http://localhost:8080")
except:
    print("error...")