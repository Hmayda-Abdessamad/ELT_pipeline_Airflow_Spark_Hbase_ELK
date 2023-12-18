import yfinance as yf
import pandas as pd

tickers = ["aapl", "goog", "amzn", "msft", "BA"]


# for one year
def HistoricalData():
    # get historical data for all of this tickers at once
    data = yf.download("AMZN AAPL GOOG MSFT BA", period="1y", interval="1d")
    return data
print(HistoricalData())










def get_actions(tickers=tickers):

    all_actions = pd.DataFrame()
    for ticker in tickers:
        stock = yf.Ticker(ticker)
        actions = stock.actions
        actions['Ticker'] = ticker.upper()  # Adding a column for ticker symbol
        all_actions = pd.concat([all_actions, actions])

    return all_actions

def get_balance_sheets(tickers=tickers):
    all_balance_sheets = pd.DataFrame()
    for ticker in tickers:
        stock = yf.Ticker(ticker)
        balance_sheets = stock.balancesheet
        balance_sheets['Ticker'] = ticker.upper()
        all_balance_sheets = pd.concat([all_balance_sheets, balance_sheets])
    all_balance_sheets.to_csv("all_balance_sheets.csv", index=False)  # Replace "all_balance_sheets.csv" with your desired filename
    return all_balance_sheets

def get_quarterly_income_statements(tickers=tickers):
    all_income_statements = pd.DataFrame()  # Initialize an empty DataFrame
    for ticker in tickers:
        stock = yf.Ticker(ticker)
        income_statements = stock.quarterly_income_stmt
        income_statements['Ticker'] = ticker.upper()  # Adding a column for ticker symbol
        all_income_statements = pd.concat([all_income_statements, income_statements])
    return all_income_statements

def get_info(dataframe) :
    stock_info = pd.DataFrame({
                    'Datatype' : dataframe.dtypes, # Data types of columns
                    'Total_Element': dataframe.count(), # Total elements in columns
                    'Null_Count': dataframe.isnull().sum(), # Total null values in columns
                    'Null_Percentage': dataframe.isnull().sum()/len(dataframe) * 100 # Percentage of null values
                       })
    return stock_info

def FundamentalsData():

    tickers_data = {}  # empty dictionary
    combined_data=pd.DataFrame()
    for ticker in tickers:
        ticker_object = yf.Ticker(ticker)
        # convert info() output from dictionary to dataframe
        temp = pd.DataFrame.from_dict(ticker_object.info, orient="index")
        temp.reset_index(inplace=True)
        temp.columns = ["Attribute", "Recent"]

        # add (ticker, dataframe) to main dictionary
        tickers_data[ticker] = temp
        combined_data = pd.concat(tickers_data)
        combined_data = combined_data.reset_index()
        del combined_data["level_1"]  # clean up unnecessary column
        combined_data.columns = ["Ticker", "Attribute", "Recent"]  # update column names
    return  combined_data





