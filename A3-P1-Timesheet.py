#Program 1 – Timesheet
#Description:   Design and write a program that accepts the number of hours worked on 
#               each of five work days from the user, then displays different 
#               information calculated about those entries as output. 

#Student #: W0457754   
#Student Name: William Wilson

def workCalculator():
    #Create containers for user inputs
    workDays = [1, 2, 3, 4, 5]
    hrsWorked = []
    maxHrs = []
    minHrs = []

    #Gather the hours worked on certain days from the user to store in lists
    for i in range(len(workDays)):
        hrsWorked.append(int(input(f"Please enter the hours work for Day # {i+1}: ")))

    for i in range(len(hrsWorked)):
        if hrsWorked[i] == max(hrsWorked):
            maxHrs.append(hrsWorked[i])

    print("---------------------------------------------------------------------------")
    
    #Find the busiest day
    for i in range(len(maxHrs)):
        print(f"Your busiest day was on: \nDay {workDays[i]+1} you worked {max(hrsWorked)} hours")

    print("---------------------------------------------------------------------------")

    #Calculate the total hours worked and the average
    totalHrs = sum(hrsWorked)
    print(f"Total hours worked in the week is {totalHrs}")

    average = totalHrs / len(workDays)
    print(f"The average amount of hours worked in the week was: {average}")

    print("---------------------------------------------------------------------------")

    #Calculate shift length to figure out slow days
    minWorkHrs = int(input("Please input the minimum amount of hours in a day:  "))
    if minWorkHrs < 0:
        print("You can not work less than 0 hours. Please input hours above 0.")
        minWorkHrs = int(input("Please input the minimum amount of hours in a day:  "))
    else:
        print(f"These are your slowest days (Less than {minWorkHrs} hours worked):")

    #Create an output for slow days
    for i in range(len(workDays)):
        if hrsWorked[i] < minWorkHrs:
            minHrs.append(hrsWorked[i])
            print(f"Day # {workDays[i]}: {hrsWorked[i]} hours")

def main():
    # YOUR CODE STARTS HERE, each line must be indented (one tab)
    
    #Print welcome message
    print("Welcome to the work day database.")
    #Call function
    workCalculator()

    # YOUR CODE ENDS HERE

main()