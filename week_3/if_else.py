# simple if_else
# Date 26/02/2024
# Name : Johnson

age = 6
if age > 18.1 :
    print("you are allowed to drive")

if age < 18 :
    print("u aren't allowed top drive")

salary = 45000
if salary > 30000 and salary < 50000 :
    salary = salary * 0.1 + salary 
    print(salary)

home_county = "Nyeri"

if home_county == "Nyeri" or home_county == "Kisii":
    print("u get bursary")

grade = 70

if grade >= 84 and grade <= 90 :
    print("u win a free a calculator")
elif grade >= 50 and grade <= 83 :
    print("u win a mathematical set")
else :
    print ("u get nothing ! ")         