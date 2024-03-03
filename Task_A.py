print("Welcome to Marks entry system!")
while(True):
    k=str(input("Enter 1 q to stop:- "))
    if(k=='q' or k=='Q'):
        print("Thank You!") 
        break
    name=str(input("Enter Name of Student:-"))
    try:
        roll=int(input("Enter the roll number:-"))
    except:
        roll=int(input("Enter the roll number:-"))
    try:
        maths=int(input("Enter the marks of Maths:-"))
    except:
        maths=int(input("Enter the marks of Maths:-"))
    try:
        phy=int(input("Enter the marks of Physics:-"))
    except:
         phy=int(input("Enter the marks of Physics:-"))
    try:
         chem=int(input("Enter the marks of chem:-"))
    except:
        chem=int(input("Enter the marks of chem:-"))
    print("--------------------------------------")
    print("Student Name:",name)
    print("Roll Number:",roll)
    over=(maths+phy+chem)//3
    if(maths>=90):
        print("Grade in Maths: A")
    elif(maths<=89 and maths>=80):
         print("Grade in Maths: B")
    elif(maths<=79 and maths>=70):
         print("Grade in Maths: C")
    elif(maths<=69 and maths>=60):
         print("Grade in Maths: D")
    else:
         print("Grade in Maths: E")
    if(phy>=90):
         print("Grade in Physics: A")
    elif(phy<=89 and phy>=80):
          print("Grade in Physics: B")
    elif(phy<=79 and phy>=70):
        print("Grade in Physics: C")
    elif(phy<=69 and phy>=60):
         print("Grade in Physics: D")
    else:
         print("Grade in Physics: E")
    if(chem>=90):
        print("GGrade in Chemistry A")
    elif(chem<=89 and chem>=80):
         print("Grade in Chemistry: B")
    elif(chem<=79 and chem>=70):
         print("Grade in Chemistry: C")
    elif(chem<=69 and chem>=60):
        print("Grade in Chemistry: D")
    else:
        print("Grade in Chemistry: E")
    if(over>=90):
         print("Overall Grade: A")
    elif(over<=89 and over>=80):
         print("Overall Grade: B")
    elif(over<=79 and over>=70):
        print("Overall Grade C")
    elif(over<=69 and over>=60):
        print("Overall Grade: D")
    else:
        print("Overall Grade: E")
        print("--------------------------------------")