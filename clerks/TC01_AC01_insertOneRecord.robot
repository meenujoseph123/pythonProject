
*** Settings ***
Library  RequestsLibrary
Library  Collections

*** Variables ***
${base_url}=    http://localhost:8080/swagger-ui.html#/calculator-controller/insertPersonUsingPOST_1

*** Test Cases ***
Post_one_record
    create session  mysession   http://localhost:8080/swagger-ui.html#/calculator-controller
    ${body}=    create dictionary   birthday=07041989   gender=female   name=meenu   natid=g5424555    salary=7000    tax=400
    ${header}=  create dictionary   Content-Type=application/json
    ${response}=    POST On Session  mysession   ${base_url}    data=${body}    headers=${header}

    log to console  ${response.status_code}
    log to console  ${response.content}

    #validation
    ${status_code}=    convert to string  ${response.status_code}
    should be equal  ${status_code} 201
    ${res_body}=    convert to string   ${response.content}
    should contain  ${res_body}  OPERATION_SUCCESS
    should contain  ${res_body}     Operation completed successfully
