from sqlalchemy import create_engine,text
import logging
logging.basicConfig(filename="app.log",
                    level=logging.INFO,
                    format="%(asctime)s-%(levelname)s-%(message)s")
engine=create_engine("sqlite:///sales.db")
logging.info("Connect with database successfully.")
try:
    with engine.begin() as conn:
        result=conn.execute(text("""SELECT SUM(quantity*price) as total_sales,
                            count(*) as total_order,
                            avg(quantity*price) as average_order_value,
                            max(quantity*price) as highest_order_value,
                            min(quantity*price) as lowest_order_value
                            from sales"""))
        logging.info("Analysis  data successfully.")
        row=result.fetchone()
        print(f"Total sales {row.total_sales}")
        print(f"Total order {row.total_order}")
        print(f"Total sales {row.average_order_value}")
        print(f"Total sales {row.highest_order_value}")
        print(f"Total sales {row.lowest_order_value}")
        logging.info("display the data successfully.")
    
        
except Exception as e:
    logging.error(e)
try:
    with engine.begin() as conn:
        city=conn.execute(text("""SELECT city,SUM(quantity*price) as total_sales
                                from sales
                                group by city"""))
        logging.info("find sales by city successfully")
        print("Total sales by city")
        for row in city:
            print(row)
except Exception as e:
    logging.error(e)
try:
    with engine.begin() as conn:
        category=conn.execute(text("""SELECT category, SUM(quantity*price) as total_sales 
                                   from sales
                                   group by category
                                    """))
        logging.info("find sales by category successfully")
        print("******Sales by Category******")
        for row in category:
            print(row)
except Exception as e:
    logging.error(e)
try:
    with engine.begin() as conn:
        salesman=conn.execute(text("""SELECT sales_person, SUM(quantity*price) as total_sales 
                                   from sales
                                   group by sales_person
                                   order by total_sales desc
                                    """))
        logging.info("find the top sales person successfully.")
        print("******Top salesperson******")
        for row in salesman:
            print(row)
except Exception as e:
    logging.error(e)
