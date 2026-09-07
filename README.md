📊 Sales & Profit Analysis using MySQL

📌 Project Overview

Sales & Profit Analysis using MySQL is a database project created to analyze sales data and understand overall business performance. The project converts raw sales data into structured tables and uses SQL queries to generate useful business insights.

The analysis focuses on sales, profit, quantity, customers, products, categories, regions, discounts, and loss-making transactions.

🎯 Objectives

Analyze total sales and total profit

Find top-performing products

Analyze product categories and sub-categories

Compare sales and profit across regions

Analyze customer and customer-segment performance

Understand the impact of discounts on profit

Identify loss-making products and orders

Perform basic data-quality checks

Calculate important business KPIs


🛠️ Tools & Technologies

MySQL

MySQL Workbench

Excel – Used as the source/raw dataset

GitHub – Project documentation and version control


🗂️ Database Structure

The project contains the following main tables:

1. Customers

Stores customer-related information such as:

Customer ID

Customer Name

Segment


2. Products

Stores product-related information such as:

Product ID

Product Name

Category

Sub-Category


3. Orders

Stores order-related information such as:

Order ID

Order Date

Ship Date

Ship Mode

Customer ID

Country

City

State

Region


4. Order_Details

Stores transaction-level information such as:

Order ID

Product ID

Sales

Quantity

Discount

Profit


5. Sales_Data

This table contains the original/raw imported sales data and is used as the staging source.

🔍 SQL Concepts Used

The project uses several important SQL concepts:

SELECT

SUM()

COUNT()

AVG()

GROUP BY

ORDER BY

WHERE

HAVING

JOIN

CASE

CTE

RANK()

Aggregate Functions

Data Quality Checks


📈 Analysis Performed

The SQL analysis includes:

Total Sales

Total Profit

Total Quantity

Total Orders

Average Order Value

Category-wise Sales & Profit

Region-wise Sales & Profit

Segment-wise Performance

Top 10 Products by Sales

Top 10 Products by Profit

Monthly Sales & Profit

Loss-making Products

Top Customers

Sub-category Performance

Profit Margin

Discount vs Profit Analysis

Top 3 Products within Each Category

Customer Ranking

Highest Sales Orders

Negative Profit Orders

Data Quality Analysis


📊 Key KPIs

The final analysis calculates:

KPI	Description

Total Orders	Total number of unique orders
Total Customers	Total number of unique customers
Total Sales	Overall sales generated
Total Quantity	Total units sold
Total Profit	Overall profit generated
Profit Margin	Profit as a percentage of sales


🔄 Project Workflow

Raw Excel Data
      ↓
Import into MySQL
      ↓
Create Database
      ↓
Create Tables
      ↓
Insert & Organize Data
      ↓
Run SQL Queries
      ↓
Analyze Sales & Profit
      ↓
Generate Business Insights

💡 Conclusion

This project demonstrates how MySQL and SQL queries can be used to transform raw sales data into meaningful business information. It provides insights into product, customer, category, regional, and profitability performance and helps understand how databases can support business decision-making.


📁 Suggested GitHub Files

GitHub repository mein tum ye files rakh sakti ho:

Sales-Profit-Analysis-MySQL/
│
├── README.md
├── database_creation.sql
├── table_creation.sql
├── analysis_queries.sql
├── dataset/
│   └── sales_data.csv
│
└── screenshots/
    ├── database.png
    ├── tables.png
    └── query_results.png

Ye README directly GitHub ke README.md mein paste kar sakti ho.
