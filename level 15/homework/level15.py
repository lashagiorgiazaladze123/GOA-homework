# GPA და ოჯახის შემოსავლის შეყვანა
gpa = float(input("შეიყვანეთ თქვენი GPA (საშუალო ქულა): "))
family_income = float(input("შეიყვანეთ ოჯახის შემოსავალი: "))

# დარწმუნდით, რომ GPA და ოჯახის შემოსავალი არის დადებითი
if gpa < 0 or family_income < 0:
    print("GPA და ოჯახის შემოსავალი უნდა იყოს დადებითი რიცხვები.")
else:
    # სტიპენდიის წესები
    if gpa >= 3.5:
        print("თქვენ გაქვთ სტიპენდიის მიღების უფლება.")
        print("სტიპენდიის ოდენობა: მაღალი სტიპენდია")
    elif gpa >= 3.0 and family_income < 50000:
        print("თქვენ გაქვთ სტიპენდიის მიღების უფლება.")
        print("სტიპენდიის ოდენობა: უმაღლესი სტიპენდია")
    elif gpa >= 3.0:
        print("თქვენ გაქვთ სტიპენდიის მიღების უფლება.")
        print("სტიპენდიის ოდენობა: სტანდარტული სტიპენდია")
    else:
        print("თქვენ არ გაქვთ სტიპენდიის მიღების უფლება.")
