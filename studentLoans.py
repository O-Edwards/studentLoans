import pandas as pd
import datetime

df = pd.DataFrame(columns=['Loan Name','Subsidized or Unsubsidized','Amount','Interest Rate','Start Date'])

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
    df = df.append(newDF)

while True:
    print('''Enter a number to choose from the following options:
    1: Add A Loan
    2: Remove A Loan
    3: Log a made payment
    4: View Accumulated Interest
    5: Export to Text File
    ''')
    choice = int(input())

    if choice == 1:
        addLoan(df)
    elif choice ==2:

        