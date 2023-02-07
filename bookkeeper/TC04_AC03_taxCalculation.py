# we can use panda to get data from csv.here I used direct entry details from user since upload feature was not working.
from self import self

def calculate(variable, bonus, salary, taxPaid):
    return ((salary - taxPaid) * variable) + bonus


def calculate_income_tax(age, gender, salary, taxPaid):
    if gender == "M" and age <= 18:
        return calculate(1, 0,salary, taxPaid)
    elif gender == "M" and age <= 35:
        return calculate(0.8, 0,salary, taxPaid)
    elif gender == "M" and age <= 50:
        return calculate(0.5, 0,salary, taxPaid)
    elif gender == "M" and age <= 75:
        return calculate(0.367, 0,salary, taxPaid)
    elif gender == "M" and age <= 76:
        return calculate(0.05, 0,salary, taxPaid)
    elif gender == "F" and age <= 18:
        return calculate(1, 500,salary, taxPaid)
    elif gender == "F" and age <= 35:
        return calculate(0.8, 500,salary, taxPaid)
    elif gender == "F" and age <= 50:
        return calculate(0.5, 500,salary, taxPaid)
    elif gender == "F" and age <= 75:
        return calculate(0.367, 500,salary, taxPaid)
    elif gender == "F" and age <= 76:
        return calculate(0.05, 500,salary, taxPaid)


def calculateTaxRelief():
    age: int = int(input("What's your age?"))
    gender: str = str(input("What's your gender? Male enter 'M' for Female enter 'F'"))
    salary: float = float(input("What's your salary?"))
    taxPaid: float = float(input("What's your tax paid?"))
    tax = calculate_income_tax(age, gender, salary, taxPaid)
    print(f"Total tax relief applicable is $"+str(tax))


if __name__ == '__main__':
    calculateTaxRelief()
