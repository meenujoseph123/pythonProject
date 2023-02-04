import pandas as pd
data= pd.read_csv("sample.csv")
data
data.columns
data.Salary

def calculate(variable, bonus):
    salary=1000
    taxpaid=200
    return ((salary-taxpaid)*variable)+bonus
#salary, taxpaid get from csv file
def calculate_income_tax(age,gender):
    if gender == "M" and age <= 18:
        return calculate(1, 0)
    elif gender == "M" and age <= 35:
        return calculate(0.8, 0)
    elif gender == "M" and age <= 50:
        return calculate(0.5, 0)
    elif gender == "M" and age <= 75:
        return calculate(0.367, 0)
    elif gender == "M" and age <= 76:
        return calculate(0.05, 0)
    elif gender == "F" and age <= 18:
        return calculate(1, 500)
    elif gender == "F" and age <= 35:
        return calculate(0.8, 500)
    elif gender == "F" and age <= 50:
        return calculate(0.5, 500)
    elif gender == "F" and age <= 75:
        return calculate(0.367, 500)
    elif gender == "F" and age <= 76:
        return calculate(0.05, 500)

if __name__ == '__main__':
    age = int(input("What's your age?"))
    gender = str(input("What's your gender? Male enter 'M' for Female enter 'F'"))
    tax = calculate_income_tax(age,gender)
    print(f"Total tax applicable is ${tax}")

    print(f"Total tax applicable after rounded is ${tax}")
        if tax => 0.00 and tax <= 50.00 :
         print(f"Total tax applicable is $50.00")
    elif tax<0.00 and tax>50.00 :
      print(f"Total tax applicable after rounded is ${tax}")

    format(tax, '.2f')
    print(f"Total tax applicable is ₹{tax}")
