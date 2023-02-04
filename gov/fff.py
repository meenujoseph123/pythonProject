from selenium import webdriver
#driver = webdriver.Chrome(executable_path="C:\Windows\chromedriver.exe")
#driver.get("https://www.python.org")
options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=options, executable_path="C:\Windows\chromedriver.exe")
driver.get("http://localhost:8080")

