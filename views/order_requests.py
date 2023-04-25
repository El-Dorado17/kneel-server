import sqlite3
from models import Order



ORDERS = [
        {
            "id": 1,
            "metalId": 3,
            "sizeId": 2,
            "styleId": 3,
            "timestamp": 1614659931693
        }
    ]

def get_all_orders():
    """this function returns all Orders from SQL"""
    with sqlite3.connect("./kneeldiamonds.sqlite3") as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        db_cursor.execute("""
        SELECT
            o.id,
            o.metal_id,
            o.size_id,
            o.style_id,
            o.timestamp
        FROM Orders o
        """)

        orders = []

        dataset = db_cursor.fetchall()

        for row in dataset:
            order = Order(row['id'], row['metal_id'], row['size_id'],
                        row['style_id'], row['timestamp'])

            orders.append(order.__dict__)

    return orders

def get_single_order(id):
    """gets single order from SQL db"""
    with sqlite3.connect("./kneeldiamonds.sqlite3") as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        db_cursor.execute("""
        SELECT
            o.id,
            o.metal_id,
            o.size_id,
            o.style_id,
            o.timestamp
        FROM Orders o
        WHERE o.id = ?
        """, ( id, ))

        data = db_cursor.fetchone()


        order = Order(data['id'], data['metal_id'], data['size_id'],
                            data['style_id'], data['timestamp'])

    return order.__dict__

def create_order(new_order):
    """This function is in charge of adding a new order w SQL!"""
    with sqlite3.connect("./kennel.sqlite3") as conn:
        db_cursor = conn.cursor()
#!Terminal says no such table Orders...? line 74
        db_cursor.execute("""
        INSERT INTO Orders
            ( metal_id, size_id, style_id, timestamp )
        VALUES
            ( ?, ?, ?, ?);
        """, (new_order['metal_id'], new_order['size_id'],
            new_order['style_id'], new_order['timestamp'], ))

        id = db_cursor.lastrowid

        new_order['id'] = id

    return new_order

def delete_order(id):
    """This function deletes orders obvi"""
    order_index = -1
    for index, order in enumerate(ORDERS):
        if order["id"] == id:
            order_index = index
    if order_index >= 0:
        ORDERS.pop(order_index)

def update_order(id, new_order):
    """PUT/replace things!"""
    for index, order in enumerate(ORDERS):
        if order["id"] == id:
            ORDERS[index] = new_order
            break
