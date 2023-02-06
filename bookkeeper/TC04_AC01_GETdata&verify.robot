
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
    ${response}=   get request  mysession   /getTaxReliefUsingGET

    log to console  ${response.status_code}
    log to console  ${response.content}

    #validation
    ${status_code}=    convert to string  ${response.status_code}
    should be equal  ${status_code} 200
    ${res_body}=    convert to string   ${response.content}
    should contain  ${res_body}  OPERATION_SUCCESS
    should contain  ${res_body}     Operation completed successfully



