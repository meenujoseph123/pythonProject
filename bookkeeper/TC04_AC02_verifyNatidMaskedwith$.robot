*** Settings ***
Library     ExtendedSelenium2Library
Library     bookkeeper.py


*** Variables ***

*** Test Cases ***
Testcase
    ${natidcheck}=   natIdMasked
    #should be equal as integers  ${natid}    1
    log to console  ${natidcheck}
    run keyword if  ${natidcheck}  should be equal as integers  1
         log to console  ============================================
        log to console  Nat id is masked from 5th charecter onwards
        LOG TO CONSOLE  ============================================
    run keyword unless
        log to console  ============================================
        log to console  Nat id is not masked.
        LOG TO CONSOLE  ============================================


