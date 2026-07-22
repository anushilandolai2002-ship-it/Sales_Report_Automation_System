from sqlalchemy import create_engine,text
import logging
logging.basicConfig(filename="app.log",
                    level=logging.INFO,
                    format="%(asctime)s-%(levelname)s-%(message)s")
engine=create_engine("sqlite:///sales.db")
logging.info("connect database successfully.")
def add_sale(params):
    try:
        with engine.begin() as conn:
            result=conn.execute(text("""INSERT INTO sales (sale_id,order_date,customer_name,product,category,quantity,price,city,sales_person)
        VALUES (:sale_id,:order_date,:customer_name,:product,:category,:quantity,:price,:city,:sales_person)"""),params)
        logging.info("add sales successfully.")
        return result.rowcount
    except Exception :
        logging.exception("Failed to add data")

def update_price(params):
    try:
        with engine.begin() as conn:
            row=conn.execute(text("""UPDATE sales
                              SET price=:price
                              WHERE sale_id=:id"""),params)
        logging.info("create update price function successfully.")
        return row.rowcount
    except Exception as e:
        logging.exception("Fail update price")
def delete_sale(params):
    try:
        with engine.begin() as conn:
            row=conn.execute(text("""DELETE sales
                                  where sale_id:id"""),params)
        logging.info("create delete sale  function successfully.")
        return row.rowcount
    except Exception as e:
        logging.error(e)
def search_sale(params):
    try:
        with engine.begin() as conn:
            row=conn.execute(text("""SELECT * 
                                  FROM sales
                                    WHERE sale_id=:id"""),params)
        logging.info("create search sale function successfully.")
        return row.rowcount
    except Exception as e:
        logging.error(e)
    
