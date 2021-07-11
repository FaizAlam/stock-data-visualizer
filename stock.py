#description : This is a stock web app

import streamlit as st
import pandas as pd
from PIL import Image

#Add a title and image
st.write("""
    Stock Web Application
    **visually** show data of a stock
""")
image = Image.open('/Users/home/Desktop/python/stock web app/stock1.jpeg')
st.image(image, use_column_width=True)

st.sidebar.header("User Input")

#create a function to get user input
def get_input():
    start_date = st.sidebar.text_input("start date","2020-07-13")
    end_date = st.sidebar.text_input("End date","2021-07-09")
    stock_symbol = st.sidebar.text_input("stock symbol","AMZN")
    return start_date,end_date,stock_symbol

#create a function to get the company name
def get_company_name(symbol):
    if symbol == "AMZN":
        return 'Amazon'
    elif symbol == "GOOG":
        return 'Google'
    elif symbol == "MSFT":
        return 'Microsoft'
    else:
        return 'None'
    
#create a function to get proper company data and timeframe
def get_data(symbol,start,end):

    #Load Data
    if symbol.upper()=='AMZN':
        df = pd.read_csv('/Users/home/Desktop/python/stock web app/data/AMZN.csv')
        
    elif symbol.upper() == 'GOOG':
        df = pd.read_csv('/Users/home/Desktop/python/stock web app/data/GOOG.csv')
   
    elif symbol.upper() == 'MSFT':
        df = pd.read_csv('/Users/home/Desktop/python/stock web app/data/MSFT.csv')
    
    else:
        df = pd.DataFrame(columns=['Date','Close','Open','Volumne','Adj Close','High','Low'])
        

    #get the date range
    start = pd.to_datetime(start)
    end = pd.to_datetime(end)

    # set the start and end index
    start_row = 0
    end_row = 0

    #start the date from top of the dataset and go down to see if user start date <= date in dataset
    for i in range(0,len(df)):
        if start <= pd.to_datetime(df['Date'][i]):
            start_row = i
            break

    #start from the bottom of the data set and go up to see if users end date is greater than or equal to date inn data set
    for i in range(0,len(df)):
        if end >= pd.to_datetime(df['Date'][len(df-1)]):
            end_row = len(df)-1-j
            break
    
    #set the index to be the date
    df = df.set_index(pd.DatetimeIndex(df['Date'].values))

    return df.iloc[start_row:end_row+1, :]

#get the user input
start,end,symbol = input()
#get the data
df = get_data(symbol,start,end)
#get the company name
company_name = get_company_name(symbol.upper())

#display the class price
st.header(company_name+" Close Price\n")
st.line_chart(df['Close'])

#display the volume
st.header(company_name+" Volume\n")
st.line_chart(df['Volume'])

#Get statistics on the data
st.header("Data Statistics")
st.write(df.describe())

