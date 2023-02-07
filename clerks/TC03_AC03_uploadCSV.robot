*** Settings ***
Library     ExtendedSelenium2Library
Library     clerks.py


*** Test Cases ***
Test
    #Method 1
    uploadCSVfromUI
    #Method 2
    uploadLargeFileForInsertionToDatabaseUsingAPI