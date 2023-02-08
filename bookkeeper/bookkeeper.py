# import the webdriver
import re
from datetime import time
from webbrowser import Chrome

import self
from selenium import webdriver
from robot.libraries.BuiltIn import BuiltIn
from webdriver_manager import driver

from datetime import date


def loadApplication():
    driver = webdriver.Chrome(options=Chrome, executable_path="C:\Windows\chromedriver.exe")
    time.sleep(25)
    driver.maximize_window()
    driver.get("http://localhost:8080")
    time.sleep(25)
    return driver


def natIdMasked():
    try:
        self.selenium_lib = BuiltIn().get_library_instance('ExtendedSelenium2Library')
        driver1 = loadApplication()
        l = driver1.find_elements_by_xpath("//*[@class= 'spTable']/tbody/tr/td[0]")
        # to traverse through the list of cell data of column 0(natid)
        i = 0
        for i in l:
            print("natid-" + i + ":" + i.text)
            natId = i.text                     #"G3333$$$$"
            # find the index where $ starts from
            print("The '$' symbol is displaying from index " + natId.index("$$$") + 1)
            if natId.index("$") == 4:
                return 1
            else:
                return 0
            # to close the browser
        driver1.close()
    except:
        print("Table is not available in the UI")


# we can use panda to get data from csv.here I used direct entry details from user since upload feature was not working.
def calculate(variable, bonus, salary, taxPaid):
    return ((salary - taxPaid) * variable) + bonus


def calculate_income_tax(age, gender, salary, taxPaid):
    if gender == "M" and age <= 18:
        return calculate(1, 0, salary, taxPaid)
    elif gender == "M" and age <= 35:
        return calculate(0.8, 0, salary, taxPaid)
    elif gender == "M" and age <= 50:
        return calculate(0.5, 0, salary, taxPaid)
    elif gender == "M" and age <= 75:
        return calculate(0.367, 0, salary, taxPaid)
    elif gender == "M" and age <= 76:
        return calculate(0.05, 0, salary, taxPaid)
    elif gender == "F" and age <= 18:
        return calculate(1, 500, salary, taxPaid)
    elif gender == "F" and age <= 35:
        return calculate(0.8, 500, salary, taxPaid)
    elif gender == "F" and age <= 50:
        return calculate(0.5, 500, salary, taxPaid)
    elif gender == "F" and age <= 75:
        return calculate(0.367, 500, salary, taxPaid)
    elif gender == "F" and age <= 76:
        return calculate(0.05, 500, salary, taxPaid)


# we can use this below function to calculate age from birthday in the table.
def age(birthdate):
    today = date.today()
    l = driver.find_elements_by_xpath("//*[@class= 'spTable']/tbody/tr/td[3]")  # birthday column cell
    # to traverse through the list of cell data of column 0(natid)
    i = 0
    for i in l:
        print("birthday-" + i + ":" + i.text)
        birthday = i.text
        day = birthday[0:1]
        month = birthday[2:3]
        year = birthday[3:6]
        age = today.year - year - ((today.month, today.day) < (month, day))
        return age


# we can calculate age from birthday from csv that we upload,I am directly getting from user since the table is not available.
def calculateTaxRelief():
    age1: int = int(input("What's your age?"))
    gender1: str = str(input("What's your gender? Male enter 'M' for Female enter 'F'"))
    salary1: float = float(input("What's your salary?"))
    taxPaid1: float = float(input("What's your tax paid?"))
    txr1 = calculate_income_tax(age1, gender1, salary1, taxPaid1)
    print(f"Total tax relief applicable is $" + str(txr1))
    return txr1


def calculateTaxReliefAfterNormalRounding():
    tax = calculateTaxRelief()
    print(tax)
    # normal rounding is applied to tax we calculated
    rounded = round(tax)
    print(f"Total tax relief applicable after normal rounding is ${rounded}")
    return rounded


def calculateTaxReliefForLessThanFifty():
    taxR = 0
    tax = calculateTaxRelief()
    # normal rounding is applied to tax we calculated
    rounded = round(tax)
    print(f"Total tax relief applicable after normal rounding is ${rounded}")
    # condition check
    if 0.00 <= rounded <= 50.00:
        taxR = 50.00
        print(f"Total tax relief applicable is $" + str(taxR))
        return taxR
    elif 0.00 > rounded > 50.00:
        print(f"Total tax relief applicable after rounded is ${rounded}")
        return rounded


def calculateTaxReliefAfterRemovingDecimal():
    tax = calculateTaxRelief()
    # value with more than 2 decimal point truncated at second decimal point.
    taxFormat = format(tax, '.2f')
    print(f"Total tax relief applicable is ₹{taxFormat}")
    # normal rounding is applied to tax we calculated
    roundedFinally = round(taxFormat)
    print(f"Total tax relief applicable after normal rounding is ${roundedFinally}")
    return roundedFinally


if __name__ == '__main__':
    calculateTaxRelief()
