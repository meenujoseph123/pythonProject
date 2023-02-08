import json
import requests
import re
import time
from selenium import webdriver
from selenium.webdriver.chrome import options


def insertRecords():
    url = "http://localhost:8080/swagger-ui.html#/calculator-controller/insertPersonUsingPOST"
    file = open('..\\OppenheimerProject\\oppenheimer.json', 'r')
    json_input = file.read()
    request_json = json.loads(json_input)
    response = requests.post(url, request_json)
    print(response.content)
    if response.status_code == 201:
        return 1
    else:
        return 0

#This method is for uploading using Upload button in the UI.
def uploadCSVfromUI():
    driver = webdriver.Chrome(executable_path="C:\Windows\chromedriver.exe")
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

#upload csv file using API call is as below.
def uploadLargeFileForInsertionToDatabaseUsingAPI():
    url = "http://localhost:8080/swagger-ui.html#/calculator-controller/uploadFileUsingPOST"
    files = dict(
        kpi=open('path/filename.csv', 'rb'),
        environment=(None, 'environment name'),
        status=(None, 10))
    requests.post(url, files=files, headers={
        'x-access-token': "<api_token>"})
