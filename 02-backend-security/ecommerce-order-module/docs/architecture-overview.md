# Order History Module - Architecture Overview

## Overview

The **OrderHistory module** is responsible for managing order creation, order tracking, and order history retrieval within a Python-based e-commerce bookstore application.

This module interacts with multiple database table to maintain order data and ensure that user purschase information is stored and retrieved correctly.

The class design follows the projct specification provided for the system and focuses on handling order-related database operations.

---

# Class Structure

The 'OrderHistory' class contains several functions responsible for interacting with the database and managing order data.

## Constructors

### 'OrderHistory()'
A zero-parameter constructor that allows the class to be initialized without immediately connecting to a database.
This enables the classe methods to be accessed before setting a database name.

### 'Orderhistory(string databaseName)'
Initialies the class with the name of the database that will be used for all database operations. 
The database name is stored and referenced by other functions when establishing connections. 

---

# Core Functions

## 'viewOrder(string userID, string ovcerderID)'

Displays detailed information for a specific order.

**Security Validation**

Before displaying order details, the system confirms that:

- The requested 'orderID' belongs to the currently logged-in 'userID'

If the order does not belong to the user, an error message is displayed/

**Database Interaction**

This function interacts with multiple tables:

- **Orders table** - verifies order ownership
- **OrderItems table** -retrieves items included in the order
- **Inventory table** - retrieves product information such as title, author, and price

This allows the system to display full details of each book included in the selected order.

---

## 'createOrder(string userID, int quantity, float cost, string date)'

Creates a new order record for the user.

**Order ID Generation**

A random number generator is used to produce a unique 'orderID'.
The system repeatedly generates IDs until one if found that does not already exist in the **Orders table**.

**Database Interaction**

Once a unique ID is generated, a new row is inserted into the **Orders table** containing:

- OrderNumber
- User ID
- Quantity
- Cost
- Date

The function returns the generated 'orderID' so it can be used in subsequent order processing steps.

---

## 'addOrderItems(string userID, string orderID)'
Transfers item from a user's shopping cart into a finalized order.

**Database Interaction**

This function coordinates between two tables:

- **Cart table** - stores items the user has selected but not yet purchased
- **OrderItems table**  - stores items associated with a completed order

**Process**

1. Retrieve all cart items belonging to the current user
2. Copy the relevant item data into the **OrderItems table** 
3. Associate each item with the generated 'orderID'
4. Remove the items from the **Cart table** after the transfer is complete

The database schema was designed so that **Cart and OrderItems share similar fieldds**, which allows the rows to be transferred directly during the order creation procress.

---

# Data Flow Summary

The order processing workflow follows these steps:

1. User adds items to the **Cart**
2. 'createOrder()' generates a new order record
3. 'addOrderItems()' transfers cart items to the **OrderItems table**
4. Cart entries are removed after the order is finalized
5. 'viewHistory()' allows users to view past orders
6. 'viewOrder()' displays the details of a specific order

---

# Security Considerations

The module includes several safegaurds:

- **Parameterized SQL queires** are used to prevent SQL injection
- **Order ownership validation** ensures users cannot view order belonging to other users
- **Unique order ID generation** prevents collisions between order records
- **Controlled database connections** reduce the risk of data corruption

---

## System Architecture Diagram

'''mermaid
flowchart TD 


User[User Application CLI]

Cart[(cart Table)]
Orders[(Orders table)]
OrderItems[(OrderItems Table)]
Inventory[(Inventory Table)]

CreatOrder[createOrder()]
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
