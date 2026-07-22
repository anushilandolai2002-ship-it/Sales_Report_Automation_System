from sqlalchemy import create_engine,text
import pandas as pd
import logging
import openpyxl
logging.basicConfig(filename="app.log",
                    level=logging.INFO,
                    format="%(asctime)s-%(levelname)s-%(message)s")
engine=create_engine("sqlite:///sales.db")
logging.info("create engine successfully.")
try:
    df=pd.read_excel("sales.xlsx")
    logging.info("read excel file successfully.")
    df.to_sql("sales",con=engine,if_exists="append",index=False)
    logging.info("successfully import the file into the database.")
    print("show the 5 data to show the data import successfully.")
    df_db=pd.read_sql("sales",con=engine)
    print(df_db.head())
    logging.info("read top five data for confermation.")
except Exception as e:
    logging.error(e)