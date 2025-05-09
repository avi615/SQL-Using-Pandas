# -*- coding: utf-8 -*-
"""sales_data.db.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1_X7HGerRBTFFn2ewQCnWpltEdfunlV0f
"""

import sqlite3

# Connect to SQLite database (or create it if it doesn't exist)
conn = sqlite3.connect("sales_data.db")
cursor = conn.cursor()

# Step 1: Create the table
cursor.execute("""
CREATE TABLE IF NOT EXISTS sales (
    order_id INTEGER PRIMARY KEY,
    order_date TEXT,
    category TEXT,
    region TEXT,
    sales REAL,
    profit REAL
)
""")

# Step 2: Insert sample records
sample_data = [
    (101, '2023-01-01', 'Furniture', 'West', 250.75, 40.25),
    (102, '2023-01-03', 'Technology', 'East', 980.50, 120.10),
    (103, '2023-01-05', 'Office Supplies', 'South', 150.00, 20.50),
    (104, '2023-01-07', 'Furniture', 'Central', 330.25, -15.00),
    (105, '2023-01-09', 'Technology', 'West', 870.10, 90.00)
]

cursor.executemany("INSERT INTO sales VALUES (?, ?, ?, ?, ?, ?)", sample_data)

# Commit changes and verify
conn.commit()

# Step 3: Query to check the data
for row in cursor.execute("SELECT * FROM sales"):
    print(row)

# Close connection when done
conn.close()

import sqlite3
import pandas as pd

# Creating the database sales data
conn = sqlite3.connect("sales_data.db")
c = conn.cursor()

# Step 1: Create the table
cursor.execute("""
CREATE TABLE IF NOT EXISTS sales (
    order_id INTEGER PRIMARY KEY,
    order_date TEXT,
    category TEXT,
    region TEXT,
    sales REAL,
    profit REAL
)
""")

# Step 2: Insert sample records
sample_data = [
    (101, '2023-01-01', 'Furniture', 'West', 250.75, 40.25),
    (102, '2023-01-03', 'Technology', 'East', 980.50, 120.10),
    (103, '2023-01-05', 'Office Supplies', 'South', 150.00, 20.50),
    (104, '2023-01-07', 'Furniture', 'Central', 330.25, -15.00),
    (105, '2023-01-09', 'Technology', 'West', 870.10, 90.00)
]

cursor.executemany("INSERT INTO sales VALUES (?, ?, ?, ?, ?, ?)", sample_data)

# Commit changes and verify
conn.commit()

c.execute('select * from sales')
c.fetchall()

df=pd.read_sql_query('select * from sales',conn)
df

# max salary
pd.read_sql_query('select max(sales) from sales',conn)

#Total profit
pd.read_sql_query('select sum(profit) as total_profit from sales',conn)

# each sales group by category
 pd.read_sql_query('select category,sum(sales) as Total_sales from sales group by category ',conn)

pd.read_sql_query('select region,sum(sales) as Total_sales from sales group by region ',conn)

# Group and plot
import matplotlib.pyplot as plt
plt.figure(figsize=(4, 4))
category_sales = df.groupby("category")["sales"].sum()

category_sales.plot(kind="bar", color="skyblue")
plt.title("Total Sales by Category")
plt.xlabel("Category")
plt.ylabel("Sales")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# Scatter Plot: Sales vs Profit
plt.figure(figsize=(4, 4))
plt.scatter(df["sales"], df["profit"], color="purple")
plt.title("Sales vs Profit")
plt.xlabel("Sales")
plt.ylabel("Profit")
plt.grid(True)
plt.tight_layout()
plt.show()

#Bar Plot: Profit by Region
plt.figure(figsize=(4, 4))
region_profit = df.groupby("region")["profit"].sum()

region_profit.plot(kind="bar", color="salmon")
plt.title("Total Profit by Region")
plt.xlabel("Region")
plt.ylabel("Profit")
plt.xticks(rotation=0)
plt.tight_layout()
plt.show()

