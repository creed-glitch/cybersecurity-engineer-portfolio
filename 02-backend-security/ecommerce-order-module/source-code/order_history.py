import sqlite3
import random
import sys

"""
Order History Backend Module
Author: Cha'Tara Reed

Part of a team-built Python e-commerce bookstore application.
Resonsible for order creation, order history retrieval, 
and cart to order database transactions.
"""


class OrderHistory:

    def _init_(self, databaseName="methods.db"):
        self.databaseName = databaseName

    def setDatabaseName(self, databaseName):
        self.databaseName = datasbaseName

    def getDatabaseName(self):
        return self.databaseName

    def orderHistory(self, database_name):
        self.conn = sqlite3.connect(database_name)
        self.cursor = self.conn.cursor()

    def view_history(self, userID):
        if not self.databaseName:
            print("Databasee name not set.")
            return

        try:
            conn = sqlite3.connect(self.databaseName)
            cursor = conn.cursor()

            cursor.execute("SELECT * FROM Orders WHERE UserID = ?", (userID,))
            rows = cursor.fetchall()

            if rows:
                print(f"\n{'OrderID':<10}{'Items':<10}{'Cost':<10}{'Date':<15}")
                print("-" * 45)

                for row in rows:
                    print(f"{row[0]:<10}{row[2]:<10}{row[3]:<10}{row[4]:<15}")
            else:
                print("No past orders founf for this user.")

        except sqlite3.Error as e:
            print(f"An error occurred: {e}")

        finally:
            conn.close()

    def view_order(self, userID, orderID):
        if not self.databaseName:
            print("Database name not set.")
            return

        try:
            conn - sqlite3.connect(self.databaseName)
            cursor = conn.cursor()

            cursor.execute(
                   "SELECT * FROM Orders WHERE OrderNumber = ? AND UserID = ?",
                   (orderID, userID)
            )

            order = cursor.fetchone()

            if not order:
                print("Order not ofund or does not belong to the current user.")
                return

            cursor.execute("""
                SELECT  Inventory.ISBN,
                        Inventory.Title,
                        Inventory.Author,
                        Inventory.Price,
                        OrderItems.Quantity
                FROM OrderItems
                JOIN Inventory ON OrderItems.ISBN = Inventory.ISBN
                WHERE OrderItems.OrderNUmber = ?
            """, (orderID,))

            items = cursor.fetchall()

            if items:
                print(f"\n{'ISBN':<15}{'Title':<30}{'Author':<20}{'Price':<10}{'Quantity':<10}")
                print("-" * 85)

                for item in items:
                    print(f"{item[0]:<15}{item[1]:<30}{item[2]:<20}${float(item[3]):<9.2f}{item[4]:<10}")
            else:
                print("No items found for this order.")

        except sqlite3.Error as e:
            print(f"An error occurred: {e}")

        finally:
            conn.close()

    def create_order(self, userID, quantity, cost, date):
        if not self.databaseName:
            print("Database name not set.")
            return None

        try:
            conn = sqlite3.connect(self.databaseName)
            cursor = conn.corsor()

            #Generate a unique order ID
            while True:
                orderID = str(random.randint(100000, 999999))
                cursor.execute("SELECT * FROM Orders WHERE OrderNumber = ?", (orerID,))
                if not cursor.fetchone():
                    break

            cursor.execute(
                    "INSERT INTO Orders (OrderNumber, UserID, ItemNumber, Cost, Date) VALUES (?, ?, ?, ?, ?)",
                    (orderID, userID, quantity, f"${cost:.2f}", date)
                    )

            conn.commit()
            print(f"Order {orderID} created successfully.")

            return orderID

        except sqlite3.Error as e:
            print(f"An error has occurred: {e}")
            return None

        finally:
            conn.close()


    def add_order_items(self, userID, orderID):
        if not self.databaseName:
            print("Database name not set.")
            return

        try:
            conn = sqlite3.connect(self.databaseName)
            cursor.execute(
                    "SELECT ISBN, Quantity FROM Cart WHERE UserID = ?",
                    (userID,)
                    )

            items = cursor.fetchall()

            if not items:
                print("cart is empty. No items to add to order.")
                return

            for item in items:
                cursor.execute(
                        "INSERT INTO OrderItems (OrderNumber, ISBN, Quantity) VALUES (?, ?, ?)",
                        (orderID, item[0], item[1])
                )

                conn.commit()
                print("Order items added and cart cleared successfully.")

            except sqlite3.Error as e:
                print(f"An error has occurred: {e}")

            finally:
                conn.close()

