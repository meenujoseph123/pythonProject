
*** Settings ***
Library  RequestsLibrary
Library  Collections
Library  os
Library  Collections
Library  JSONLibrary
*** Variables ***
${base_url}=    http://localhost:8080/swagger-ui.html#/calculator-controller

*** Test Cases ***
TC_AC1:
    create session  mysession   ${base_url}
    ${response}=   get on session  mysession   ${base_url}/dispenseUsingGET

    log to console  ${response.status_code}
    log to console  ${response.content}

    #validation
    ${status_code}=    convert to string  ${response.status_code}
    #should be equal as strings  ${response.status_code} 200
    ${res_body}=    convert to string   ${response.content}
    should contain  ${res_body}  200
    #should contain  ${res_body}     Operation completed successfully



