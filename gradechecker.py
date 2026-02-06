while True:
    marks=int(input("\nEnter student's marks:"))

    if marks >= 90:
        print("Grade: A")
    elif marks >=80:
        print("Grade: B")
    elif marks >=70:
        print("Grade: C")
    elif marks >= 60:
        print("Grade: D")
    elif marks >= 40:
        print("Grade: E")
    else:
        print("Grade: Fail")

    
    choice=input("Do you want to check another student? (y/n): ")
    if choice.lower() != 'y':
        print("\nProgram ended. Have a grate day!!")
        break