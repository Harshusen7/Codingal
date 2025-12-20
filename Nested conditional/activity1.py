#Take input for the student that he can attend the exam or not
medical_cause=input("did you have a medical cause y or n: ")
#Take input of the attendence
atten = int(input("enter the attendence of the student: "))

#checking the user input predicting output accordingly
if medical_cause == 'y' : #checking the condition 1
    print (" you are allowed")
else:
    if atten>=75: #checking the condition 2 
        print("allowed")
    else:
        print("not allowed")