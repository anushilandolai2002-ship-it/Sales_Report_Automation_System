# Sales_Report_Automation_System
Automated sales reporting system using Python, SQLAlchemy, SQLite, Pandas, and Excel automation.


## About This Project

I built this project to automate a common sales reporting process using Python.

In many companies, sales data is stored in Excel files and employees manually calculate totals, compare sales performance, and prepare reports. This project automates that process by importing sales data into a SQLite database, analyzing the data using SQL and Pandas, and generating a final Excel report automatically.

This project helped me practice how Python can be used to connect databases, analyze business data, and automate repetitive reporting tasks.

---

## What This Project Does

The workflow is:

Excel File → SQLite Database → SQL Analysis → Pandas Analysis → Excel Report

The project can:

- Import sales data from an Excel file
- Store the data in a SQLite database
- Add, update, delete, and search sales records
- Generate sales reports using SQL
- Calculate total sales and other business metrics
- Analyze sales by city, category, product, and salesperson
- Use Pandas to create calculated columns
- Categorize sales into Low, Medium, and High
- Export the final analysis into a multi-sheet Excel report
- Create logs to track the program and errors

---

## Technologies I Used

- Python
- SQL
- SQLite
- SQLAlchemy
- Pandas
- OpenPyXL
- Logging

---

## Database Columns

The sales table contains:

- `sale_id`
- `order_date`
- `customer_name`
- `product`
- `category`
- `quantity`
- `price`
- `city`
- `sales_person`

---

## Analysis Performed

### Overall Sales Analysis

The project calculates:

- Total sales
- Total number of orders
- Average order value
- Highest order value
- Lowest order value

### Business Reports

I also created reports for:

- Sales by city
- Sales by product
- Sales by category
- Sales by salesperson
- Average price by product
- Top 5 highest sales
- Top 5 lowest sales

---

## Pandas Analysis

After loading the data, I used Pandas to create additional business metrics.

### Total Amount

```text
quantity × price
