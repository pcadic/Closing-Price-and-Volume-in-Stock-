import datetime
import pandas as pd
import pandas_datareader as pdr


# Show all columns of the data frame.
def getColumnPosition(df, columnName):
    columnList = list(df.keys())

    # Show all columns of the data frame in a list.
    #print(columnList)
    columnPosition = 0
    for i in range(0, len(columnList)):
        if(columnList[i]==columnName):
            columnPosition = i
            break # Exit the loop.
    return columnPosition


#menuChoice : "1" to continue, "2" to quit
menuChoice = "1"

while menuChoice == "1":
    # Display Menu Choice Header
    print("-------------------------------------------------")
    print("Stock Report Menu Options")
    print("-------------------------------------------------")
    print("1. Report changes for a stock")
    print("2. Quit")
    menuChoice = input()

    #if menuChoice == "2", quit and exit the loop
    if menuChoice == "2":
        break

    #Enter the stock symbol
    print("Please enter the stock symbol: ")
    stockSymbol = input()

    #Ask for nb of days of analysis, convert into integer, and negative (ex: -5),
    #Then compute today date and date analysis beginning
    print("Please enter the number of days for the analysis: ")
    daysAnalysis = input()
    daysAnalysis = int(daysAnalysis)
    daysAnalysis = daysAnalysis * (-1)
    todayDate = datetime.date.today()
    pastDate = todayDate + datetime.timedelta(daysAnalysis)

    #Report building Title
    print("************************************************************")
    print("Daily Percent Changes - " + str(pastDate) + " to " + str(todayDate) + " * " + stockSymbol.upper() + " * ")
    print("************************************************************")

    #Get back initial dataframe : Call Yahoo finance to get stock data for the stock provided.
    df = pdr.get_data_yahoo(stockSymbol,
         start= datetime.datetime(pastDate.year, pastDate.month, pastDate.day),
         end  = datetime.datetime(todayDate.year, todayDate.month, todayDate.day))

    # Allow the full width of the data frame to show.
    #pd.set_option('display.max_columns', None)
    #pd.set_option('display.width', 1000)

    #Add 'Volume % Change' and 'Close % Change' columns, Save their index position
    df['Volume % Change'] = 0.0
    df['Close % Change'] = 0.0
    tempColumnPositionVPC = getColumnPosition(df, "Volume % Change")
    tempColumnPositionCPC = getColumnPosition(df, "Close % Change")
    #Dataset Loop
    for i in range(0, len(df)):
        #If first item, no previous value => 0
        if i == 0:
            closePctChange = 0
            volumePctChange = 0
        #Otherwise, use formula using the current value and the previous one
        else:
            closePctChange = (df.iloc[i]['Close'] - df.iloc[i-1]['Close']) / df.iloc[i-1]['Close']
            volumePctChange = (df.iloc[i]['Volume'] - df.iloc[i-1]['Volume']) / df.iloc[i-1]['Volume']
        #Rounding Percentage Change to 3 numbers after .
        closePctChange = round(closePctChange, 3)
        volumePctChange = round(volumePctChange, 3)
        # Store float values in cell.
        df.iat[i, tempColumnPositionVPC] = volumePctChange
        df.iat[i, tempColumnPositionCPC] = closePctChange


    # Remove the 'High', 'Low', 'Open' and 'Adj Close' columns
    # i.e. Keep 'Close' and 'Volume' columns only.
    newColumnList = ['Close', 'Volume', 'Volume % Change', 'Close % Change']
    df = df[newColumnList]

    #Report building : New Data Set
    print(df)

    #Report building : Ending part
    print("------------------------------------------------------------")
    print("Summary of Cumulative Changes for "+ stockSymbol)
    print("------------------------------------------------------------")
    print(str(pastDate) + " to " + str(todayDate))

    #Computation of the change from the Period start close price and the Period end close price
    #Rounding and display
    numRows = len(df)
    closePctChange = ( df.iloc[numRows - 1]['Close'] - df.iloc[0]['Close']) / df.iloc[0]['Close']
    volumePctChange = ( df.iloc[numRows - 1]['Volume'] - df.iloc[0]['Volume']) / df.iloc[0]['Volume']
    closePctChange = round(closePctChange, 3)
    volumePctChange = round(volumePctChange, 3)
    print("% Volume Change:      " + str(volumePctChange))
    print("% Close Price Change: " + str(closePctChange))
