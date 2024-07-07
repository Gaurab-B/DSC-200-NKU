#Gaurab Baral ->DSC 200-001 -->Lab 1

#this is the main function that is being called first. It then calls other functions.
#this function declares all the variables/lists/dictionaries, inputs the data using GetScripting and GetMath functions and calls the OUTPUT function at the end.
def GetData(NoOfDays,StudentsNumber):
    StudentScript = []
    StudentMath = []
    StudentSubject = {}
    for y in range(1,StudentsNumber+1):
        StudentMath = []
        StudentScript = []
        for x in range(1,NoOfDays+1):
            ScriptNumber = GetScripting(x,y)
            MathNumber = GetMath(x,y)
            StudentScript.append(ScriptNumber)
            StudentMath.append(MathNumber)
        StudentSubject[y] = [StudentScript,StudentMath]

    Output(StudentSubject,StudentScript,StudentMath,StudentsNumber)
#This function inputs and validates the data for scripting
def GetScripting(i,j):
    while True:
        try:
            data = float(input(f"For student {j}, For day {i}, enter the number of hours you spend for scripting: "))
            if (data >=0 and data <=9):
                return data
            print("Please enter a valid positive number and you cannot exceed 9 hours.")
        except:
            print("Re-enter with an integer value")

#This function inputs and validates the data for math
def GetMath(i,j):
    while True:
        try:
            data = float(input(f"For student {j}, For day {i}, enter the number of hours you spend for math: "))
            if (data >= 0 and data <= 9):
                return data
            print("Please enter a valid positive number and you cannot exceed 9 hours.")
        except:
            print("Re-enter with an integer value")

#this function is used in displaying the output where it checks if the user had scripted more or practised math more.
def CheckSubject(ScptTime,MathTime):
    if (ScptTime > MathTime):
        Most_Time_Spent = "Scripting"
    elif (ScptTime < MathTime):
        Most_Time_Spent = "Math"
    elif (ScptTime == MathTime):
        Most_Time_Spent = "Same"
    return Most_Time_Spent

#this function displays the output in the screen with proper Formatting.
def Output(StudentSubject,StudentScript,StudentMath,StudentsNumber):
    print("------------------------------------------------------------------------------------------------------------------------")
    print()
    print("Student #\t\tAvg Scripting Time\t\tAvg. Math Time\t\tMost Time Spent Subject")
    print("----------\t\t---------------\t\t\t----------\t\t\t----------")
    totalScpt = 0;
    totalMath = 0;
    maxScpt = 0;
    maxMath = 0;
    for i in range(1,StudentsNumber+1):
        ScptTime = StudentSubject[i][0]
        MathTime  = StudentSubject[i][1]
        for a in range(0,len(ScptTime)):
            totalScpt += ScptTime[a]
            maxScpt +=ScptTime[a]
        for b in range(0, len(MathTime)):
            totalMath += MathTime[b]
            maxMath += MathTime[b]
        AvgScpt = totalScpt / len(ScptTime)
        AvgMath = totalMath / len(MathTime)
        Most_Time_Spent = CheckSubject(AvgScpt,AvgMath)
        print(f"{i}\t\t\t\t{AvgScpt:.2f}\t\t\t\t\t{AvgMath:.2f}\t\t\t\t{Most_Time_Spent}")
        totalScpt = 0;
        totalMath = 0;

    MaxScptAvg = maxScpt/StudentsNumber / len(ScptTime)
    MaxMathAvg = maxMath/StudentsNumber / len(MathTime)
    Most_Time_Spent2 = CheckSubject(MaxScptAvg,MaxMathAvg)
    print()
    print("------------\t---------------\t\t\t----------\t\t\t----------")
    print(f"Overall Avg.\t{MaxScptAvg:.2f}\t\t\t\t\t{MaxMathAvg:.2f}\t\t\t\t{Most_Time_Spent2}")



#This is the part where the user inputs the data and then the first function:GetData is called.
while True:
    try:
        StudentsNumber = int(input("Enter the number of students in the class: "))
        if(StudentsNumber<=0):
            print("Re-enter with positive value of the number of students")
            continue
        break
    except:
        print("Enter an integer value")


while True:
    try:
        NoOfDays = int(input("Enter the number of hours in the long week: "))
        if(NoOfDays<=0   or NoOfDays >7):
            print("Re-enter with positive value of the number of days")
            continue
        break
    except:
        print("Enter an integer value")
GetData(NoOfDays,StudentsNumber)


#Output

#Student #		Avg Scripting Time		Avg. Math Time		Most Time Spent Subject
#----------		---------------			----------			----------
#1				2.00					3.00				Math
#2				8.50					6.50				Scripting

#------------	---------------			----------			----------
#Overall Avg.	5.25					4.75				Scripting

#Process finished with exit code 0