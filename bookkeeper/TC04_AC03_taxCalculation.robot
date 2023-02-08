*** Settings ***
Library     ExtendedSelenium2Library
Library     bookkeeper.py


*** Test Cases ***
Please enter Age[enter]Gender[Enter]Salary[Enter]TaxPaid[Enter]|TaxRelief amount will be calculated.
    ${taxrelief}=   calculateTaxRelief
    log to console  ============================================
    log to console  Final amount of tax relief is ${taxrelief} $
    LOG TO CONSOLE  ============================================