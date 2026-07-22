from sqlalchemy import create_engine,text
import logging
logging.basicConfig(filename="app.log",
                    level=logging.INFO,
                    format="%(asctime)s-%(levelname)s-%(message)s")
engine=create_engine("sqlite:///sales.db")
logging.info("create engine successfully.")
try:
    with engine.begin() as conn:
        conn.execute(text("""CREATE TABLE IF NOT EXISTS sales(
                         sale_id INTEGER PRIMARY KEY,
                          order_date TEXT,
                          customer_name TEXT,
                          product TEXT,
                          category TEXT,
                          quantity INTEGER,
                          price REAL,
                          city TEXT,
                          sales_person  TEXT ) """))
    logging.info("create table successfully.")
except Exception as e:
    logging.error(e)