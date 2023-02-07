import json
import requests


def insertRecords():
    url = "http://localhost:8080/swagger-ui.html#/calculator-controller/insertPersonUsingPOST"
    file = open('..\\OppenheimerProject\\oppenheimer.json', 'r')
    json_input = file.read()
    request_json = json.loads(json_input)
    response = requests.post(url, request_json)
    print(response.content)
    assert response.status_code == 201
