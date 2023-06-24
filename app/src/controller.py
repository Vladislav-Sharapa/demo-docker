import pandas as pd
import matplotlib.pyplot as plt
from db.connection import *
from db.queries import *
 

def output_bar() -> None:
    df = get_data(SALES).groupby("car")['price'].sum()
    df = df.to_dict()
    
    plt.bar(df.keys(), df.values(), color ='maroon',
            width = 0.4)
    
    plt.xlabel("Car name")
    plt.ylabel("Sales $")
    plt.title("Sales for different cars")
    plt.show()

def output_hist() -> None:
    df = get_data(SALES)
    # group cars 
    df=df["car"]

    plt.hist(df, bins=3)
    plt.xlabel('cars')
    plt.ylabel('Number of sold cars')
    plt.show()

def output_pie() -> None:
    df = get_data(SALES) 
    df=df["car"]
    values = df.value_counts()
    keys = values.keys()

    fig = plt.figure()
    ax = fig.add_axes([0,0,1,1]) 
    ax.axis('equal')   
    plt.title("General information of sold cars")   

    ax.pie(values, labels=keys,autopct='%1.2f%%') 
    plt.show()
    
def export_to_excel():
    '''Export tables in excel'''
    sales = get_data(SALES)
    cars = get_data(CARS)
    suppliers = get_data(SUPPLIERS)

    sheets = {'Sales': sales, 'Cars': cars, 'Suppliers': suppliers}
    writer = pd.ExcelWriter('./file.xlsx', engine='xlsxwriter')

    for sheet_name in sheets.keys():
        sheets[sheet_name].to_excel(writer, sheet_name=sheet_name, index=False)
    
    writer.close()