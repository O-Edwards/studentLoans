import pandas as pd

# df = pd.DataFrame(index= [:10],columns=['Loan Names','Subsidized or Unsubsidized','Amount','Interest','Start Date'])


def addLoan(name,ifSub,amount,interest,date,pandasDF):
    loan = {'Loan Name':name,'Subsidized or Unsubsidized':ifSub,'Amount':amount,'Interest Rate':interest,'Start Date':date}
    df.from_dict(loan)
    print(df)

addLoan("Tosin","Subsidized",10000,1.89,"June 25, 1993",df)
# while True:
#     print('''Enter a number to choose from the following options:
#     1: Add A Loan
#     2: Remove A Loan
#     3: Log a made payment
#     4: View Accumulated Interest
#     5: Export to Text File
#     ''')
#     choice = int(input())

#     if choice == 1:

        