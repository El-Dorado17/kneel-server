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
    """this function returns a list all orders and their properties"""
    return ORDERS

def get_single_order(id):
    """gets single order"""
    requested_order = None
    for order in ORDERS:
        if order["id"] == id:
            requested_order = order
    return requested_order

def create_order(order):
    """This function is in charge of adding a new order to the list!"""
    # Get the id value of the last order in the list
    max_id = ORDERS[-1]["id"]
    new_id = max_id + 1
    order["id"] = new_id
    ORDERS.append(order)
    return order

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
