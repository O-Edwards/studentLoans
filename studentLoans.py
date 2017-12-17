import pandas as pd
import datetime

def addLoan(df):
    name = input("What is the name of the Loan: ")
    ifSub = input("Is the loan subsidized or unsubsidized: ")
    amount = int(input("What is the amount of the Loan: "))
    interest = float(input("What is the interest rate on the Loan: "))
    year= int(input("Enter the Year of the Loan:"))
    month= int(input("Enter the month(1-12) of the Loan:"))
    day= int(input("Enter the day of the Loan:"))
    date = datetime.date(year,month,day)
    loan = [{'Loan Name':name,'Subsidized or Unsubsidized':ifSub,'Amount':amount,'Interest Rate':interest,'Start Date':date}]
    newDF=pd.DataFrame(loan)
    df = pd.concat([df,newDF],ignore_index=True)
    return df

    
def deleteLoan(df):
    print(df)
    index = int(input("Please enter the index of the loan you would like to remove: "))
    df.drop(df.index(index))
    return df

def madePayment(df):
    print(df)
    index = int(input("Please enter the amount of the payment  "))
    ##To do how much was made towards principal and how much was made to interest


dataFrame = pd.DataFrame(columns=['Loan Name','Subsidized or Unsubsidized','Amount','Interest Rate','Start Date'])


run = True
while run:
    print('''Enter a number to choose from the following options:
    1: Add A Loan
    2: Remove A Loan
    3: Log a made payment
    4: View Accumulated Interest
    5: Export to Csv File
    6. Import from Csv file 
    7: Print
    8: Exit
    ''')
    choice = int(input())

    if choice == 1:
        dataFrame=addLoan(dataFrame)
    if choice == 2:
        dataFrame=deleteLoan(dataFrame)
    if choice ==3 or choice == 4:
        print("Coming Soon")
    if choice == 5:
        dataFrame.to_csv('studentLoans.csv')
    if choice == 6:
        dataFrame = dataFrame.from_csv('studentLoans.csv')
    if choice ==7:
        print(dataFrame)
    if choice ==8:
        run = False

