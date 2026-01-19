# customer_analysis.py
# E-Commerce Customer Order Analysis

orders = [
    {"customer": "Alice", "product": "Laptop", "category": "Electronics", "price": 1200},
    {"customer": "Bob", "product": "T-Shirt", "category": "Clothing", "price": 25},
    {"customer": "Alice", "product": "Headphones", "category": "Electronics", "price": 150},
    {"customer": "Charlie", "product": "Shoes", "category": "Clothing", "price": 80},
    {"customer": "Bob", "product": "Monitor", "category": "Electronics", "price": 300},
]

# Total revenue
total_revenue = sum(order["price"] for order in orders)
print("Total Revenue:", total_revenue)

# Revenue per category
category_revenue = {}
for order in orders:
    category = order["category"]
    category_revenue[category] = category_revenue.get(category, 0) + order["price"]

print("\nRevenue by Category:")
for cat, rev in category_revenue.items():
    print(f"{cat}: {rev}")

# Customer spending
customer_spending = {}
for order in orders:
    customer = order["customer"]
    customer_spending[customer] = customer_spending.get(customer, 0) + order["price"]

print("\nCustomer Spending:")
for cust, amt in customer_spending.items():
    print(f"{cust}: {amt}")

# Top customer
top_customer = max(customer_spending, key=customer_spending.get)
print(f"\nTop Customer: {top_customer}")