*** Settings ***
Library     ExtendedSelenium2Library
Library     bookkeeper.py


*** Test Cases ***
Please enter Age[enter]Gender[Enter]Salary[Enter]TaxPaid[Enter]|TaxRelief amount will be calculated.
    ${taxrelief}=   calculateTaxReliefAfterRemovingDecimal
    log to console  ${taxrelief}

