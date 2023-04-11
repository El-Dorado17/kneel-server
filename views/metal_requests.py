METALS = [
        { "id": 1, "metal": "Sterling Silver", "price": 12.42 },
        { "id": 2, "metal": "14K Gold", "price": 736.4 },
        { "id": 3, "metal": "24K Gold", "price": 1258.9 },
        { "id": 4, "metal": "Platinum", "price": 795.45 },
        { "id": 5, "metal": "Palladium", "price": 1241.0 }
    ]


def get_all_metals():
    """this function returns a list all metals and their properties"""
    return METALS

# Function with a single parameter
def get_single_metal(id):
    """gets single metal"""
    # Variable to hold the found metal, if it exists
    requested_metal = None

    # Iterate the METALS list above. Very similar to the
    # for..of loops you used in JavaScript.
    for metal in METALS:
        # Dictionaries in Python use [] notation to find a key
        # instead of the dot notation that JavaScript used.
        if metal["id"] == id:
            requested_metal = metal

    return requested_metal

def create_metal(metal):
    """This function is in charge of adding a new metal to the list!"""
    # Get the id value of the last metal in the list
    max_id = METALS[-1]["id"]
    new_id = max_id + 1
    metal["id"] = new_id
    METALS.append(metal)
    return metal

def delete_metal(id):
    """This function deletes metals obvi"""
    metal_index = -1
    for index, metal in enumerate(METALS):
        if metal["id"] == id:
            metal_index = index
    if metal_index >= 0:
        METALS.pop(metal_index)

def update_metal(id, new_metal):
    """PUT/replace things!"""
    for index, metal in enumerate(METALS):
        if metal["id"] == id:
            METALS[index] = new_metal
            break
