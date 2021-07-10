This application allows users to examine daily and cumulative changes to closing price and volume for stocks in the stock market.  The application prompts the user to either examine a stock or terminate the application.

If a user chooses to examine a stock they are prompted to enter a stock symbols and total days back for the analysis. The results of the analysis are printed and the cycle is repeated until the user chooses to exit the application.

The loop is set up so the user can run the program successfully from the start to completion without termination as many times as the use wants. The application terminates properly when the user wants.

All day and stock inputs are read from the user and handled correctly and dynamically.

All statistics in one summary data frame are generated correctly for both stocks. 

The formula for daily percent change = (Current day close price - Previous day close price) / Previous day close price

The formula for the overall percentage change = (Period end close price - Period start close price) / Period start close price

Error handling is not implemented.

pandas_datareader package is required.

Sample Output
-------------------------------------------------
Stock Report Menu Options
-------------------------------------------------
1. Report changes for a stock
2. Quit
1
Please enter the stock symbol: 
msft
Please enter the number of days for the analysis: 
6
************************************************************
Daily Percent Changes - 2021-01-15 to 2021-01-20 * MSFT * 
************************************************************
                 Close    Volume  Volume % Change  Close % Change
Date                                                             
2021-01-15  212.649994  31691500           0.0000          0.0000
2021-01-19  216.440002  30480900          -0.0382          0.0178
2021-01-20  224.339996  37777260           0.2394          0.0365
------------------------------------------------------------
Summary of Cumulative Changes for msft
------------------------------------------------------------
2021-01-15 to 2021-01-20
% Volume Change:      0.192
% Close Price Change: 0.055