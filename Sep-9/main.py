import mysql.connector
import pandas as pd
import matplotlib.pyplot as plt


# ==========================================
# 1. Connect to MySQL
# ==========================================

connection = mysql.connector.connect(
    host="localhost",
    user="root",
    port="3307",
    password="root",
    database="sales_db"
)

print("Connected to MySQL successfully!")


# ==========================================
# 2. SQL Query
# ==========================================

query = """
SELECT
    DATE_FORMAT(order_date, '%Y-%m') AS month,
    category,
    SUM(quantity * price) AS revenue,
    SUM(quantity) AS units_sold
FROM sales
GROUP BY
    DATE_FORMAT(order_date, '%Y-%m'),
    category
ORDER BY month, category
"""


# ==========================================
# 3. Execute SQL and load into Pandas
# ==========================================

df = pd.read_sql(query, connection)


# ==========================================
# 4. Close MySQL connection
# ==========================================

connection.close()


# ==========================================
# 5. Display SQL result
# ==========================================

print("\nSales Analysis")
print("=" * 50)

print(df)


# ==========================================
# 6. Total Revenue
# ==========================================

total_revenue = df["revenue"].sum()

print("\nTotal Revenue:")
print(total_revenue)


# ==========================================
# 7. Revenue by Category
# ==========================================

category_revenue = (
    df.groupby("category")["revenue"]
    .sum()
    .sort_values(ascending=False)
)

print("\nRevenue by Category:")
print(category_revenue)


# ==========================================
# 8. Units Sold by Category
# ==========================================

category_units = (
    df.groupby("category")["units_sold"]
    .sum()
    .sort_values(ascending=False)
)

print("\nUnits Sold by Category:")
print(category_units)


# ==========================================
# 9. Monthly Revenue
# ==========================================

monthly_revenue = (
    df.groupby("month")["revenue"]
    .sum()
)

print("\nMonthly Revenue:")
print(monthly_revenue)


# ==========================================
# 10. Monthly Revenue Chart
# ==========================================

plt.figure(figsize=(8, 5))

plt.bar(
    monthly_revenue.index.astype(str),
    monthly_revenue.values,
    color="steelblue"
)

plt.title("Monthly Revenue")
plt.xlabel("Month")
plt.ylabel("Revenue")

plt.xticks(rotation=45)

plt.tight_layout()

plt.show()
