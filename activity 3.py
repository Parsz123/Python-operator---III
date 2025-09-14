print("Please enter marks obtained:")
Markone = int(input("Enter Mark one:"))
Marktwo = int(input("Enter Mark two:"))
Markthree = int(input("Enter Mark three:"))
Markfour = int(input("Enter Mark four:"))
Markfive = int(input("Enter Mark five:"))

tot = Markone + Marktwo + Markthree + Markfour + Markfive
average = tot / 5

if 91 <= average <= 100:
    print("Your grade is A1")
elif 81 <= average <= 90:
    print("Your grade is A2")
elif 71 <= average <= 80:
    print("Your grade is B1")
elif 61 <= average <= 70:
    print("Your grade is B2")
elif 51 <= average <= 60:
    print("Your grade is C1")
elif 41 <= average <= 50:
    print("Your grade is C2")
elif 31 <= average <= 40:
    print("Your grade is D1")
elif 21 <= average <= 30:
    print("Your grade is D2")
elif 0 <= average <= 20:
    print("Your grade is F")
else:
    print("Invalid average!")
