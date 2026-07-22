from sqlalchemy import create_engine,text
import pandas as pd
import logging
import openpyxl
logging.basicConfig(filename="app.log",
                    level=logging.INFO,
                    format="%(asctime)s-%(levelname)s-%(message)s")
engine=create_engine("sqlite:///sales.db")
try:
    df=pd.read_sql_table("sales",con=engine)
    logging.info("read sales table successfully.")
    df["total_amount"]=df["quantity"]*df["price"]
    logging.info("create total amount column successfully.")
    df["tax"]=df["total_amount"]*(18/100)
    logging.info("add tax column successfully.")
    df["final_amount"]=df["total_amount"]+df["tax"]
    logging.info("add final amount column successfully.")
    def sales_category(value):
        if value<1000:
            return "Low"
        elif value>1000 and value<5000:
            return "Medium"
        else:
            return "High"
    logging.info("create sales_category function successfully.")
    df["sales_category"]=df["total_amount"].apply(sales_category)
    logging.info("create sales category column successfully.")
    




        


