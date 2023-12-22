import yfinance as yf
import pandas as pd

tickers = ["aapl", "goog", "amzn", "msft", "BA"]


# for one year
def HistoricalData():
    # get historical data for all of this tickers at once
    data = yf.download("AMZN AAPL GOOG MSFT BA", period="1y", interval="1d")
    return data


def get_shares_full(tickers=tickers):
    all_shares=pd.DataFrame()
    for item in tickers:
        ticker = yf.Ticker(item)
        shares_count = ticker.get_shares_full()
        # Transpose DataFrame to make the timestamp index as a column
        shares_count = shares_count.T.reset_index()
        # Assign columns names
        shares_count.columns = ['Date', 'Value']
        shares_count['Ticker'] = item.upper()
        all_shares = pd.concat([all_shares, shares_count])
     
    return all_shares
def get_income_statements_common_columns(tickers=tickers):
    common_columns = None

    for ticker in tickers:
        stock = yf.Ticker(ticker)
        income_statements = stock.income_stmt
        income_statements = income_statements.transpose()
        income_statements.reset_index(inplace=True)
        income_statements.rename(columns={'index': 'Date'}, inplace=True)
        income_statements["Ticker"] = ticker

        # Si c'est la première itération, définir les colonnes communes
        if common_columns is None:
            common_columns = set(income_statements.columns)
        else:
            # Trouver les colonnes communes avec les itérations précédentes
            common_columns &= set(income_statements.columns)

   

    return list(common_columns)
        

  
    

    

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





