def get_grade(score):
    if score >= 90 :
        return "A"
    elif score >= 80 :
        return "B"
    elif score >= 70 :
        return "C"
    elif score >= 60 :
        return "D"
    else :
        return "F"
name = str(input("Enter your name"))
score = int(input("Enter your score: "))

score = get_grade(score)
print (f"{name} your grade is {score}")


def calculate(num1, operator, num2):
    if operator == "+" :
        return num1 + num2
    elif operator == "-" :
        return num1 - num2
    elif operator == "*" :
        return num1 * num2
    elif operator == "/" :
        return num1 / num2
num1 = int(input("Enter number: "))
operator = input("Enter operator: ")
num2 = int(input("Enter second number: "))
result = calculate(num1, operator, num2)
print(result)
