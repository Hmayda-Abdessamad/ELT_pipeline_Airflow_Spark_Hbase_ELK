import yfinance as yf 
import Yahoo
tickers = ["aapl", "goog", "amzn", "msft", "BA"]
    


    # get common cols
columns=Yahoo.get_income_statements_common_columns()

print(columns[1])

result=[]
    # get data for each ticker 
for ticker in tickers:
    stock = yf.Ticker(ticker)
    income_statements = stock.income_stmt
    income_statements = income_statements.transpose()
    income_statements.reset_index(inplace=True)
    income_statements.rename(columns={'index': 'Date'}, inplace=True)
    income_statements["Ticker"] = ticker
        # Sélectionner uniquement les colonnes présentes dans la liste 'columns'
    income_statements_filtered = income_statements.loc[:,columns]
    print(income_statements_filtered.columns[1])