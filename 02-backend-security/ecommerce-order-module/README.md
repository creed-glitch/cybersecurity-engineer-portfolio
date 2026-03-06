# E-Commerce Order Processing Module

Author: Cha'Tara Reed

## Overview

This project contains the **Order History backend module** for a Python-based e-commerce bookstore application.

The system was developed as part of a **3-person team project**. My responsibility was designing and implementing the order processing and order history functionality using SQLite.

The module manages order creation, order tracking, and the transfer of cart items into finalized orders.

---

# Responsibiliities

As the backend developer responsible for the order system, I implemented:

- Order creation and order tracking
- Unique order ID generation
- Rretrieval of user order history
- Detailed order inspection
- Cart-to-order item transfer logic
- Database interaction using parameterized SQL queries
- Validation to ensure users can only view their own orders

---

# Responsibilities 

As the backend developer responsible for the order system, I implemented:

- Order creation and order tracking
- Unique order ID generation
- Rretrieval of user order history
- Detailed order inspection
- Cart-to-oreder item transfer logic
- Database interaction using parameterized SQL queries 
- Validation to ensure users can only view their own orders

---

# Technologies

Python
SQLite
SQL
CLI Application Devleopment
Database Integration

---

# Skills Demonstrated

- Backend system design
- Database-driven application development
- SQL JOIN queries
- Transaction handling
- Defensive programming
- Secure database querying practices

---

# System Architecture

the orderHistory module interacts with several databse tables to process and retrieve order information.

'''mermaid
flowchart TD

User[User Application CLI]

Cart[(Cart Table)]
Orders[(Orders Table)]
OrderItems[(OrderItems Table)]
Inventory[(Inventory Table)]

CreateOrder[createOrder()]
AddItems[addOrderItems()]
ViewHistory[viewHistory()]
ViewOrder[viewOrder()]

User --> Cart
Cart --> CreateOrder
CreateOrder --> Orders
Orders --> AddItems
AddItems --> OrderItems
OrderItems --> ViewOrder
Inventory --> ViewOrder
Orders --> ViewHistory
ViewHistory --> User
ViewOrder --> User

