*** Settings ***
Library     ExtendedSelenium2Library
Library     clerks.py

*** Variables ***

${checkInsert}
*** Test Cases ***
Testcase
${checkInsert} = insertRecords
log to console  ${checkInsert}
    run keyword if  ${checkInsert}  should be equal as integers  1
         log to console  =======================================================================================
        log to console  Multiple records are inserted to DB.(POST request is successful.Returned status code 201)
        LOG TO CONSOLE  ========================================================================================
    run keyword unless
        log to console  ============================================
        log to console  POST Request is failed.
        LOG TO CONSOLE  ============================================
