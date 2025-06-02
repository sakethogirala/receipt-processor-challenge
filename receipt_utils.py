import math 
from datetime import datetime

def calculate_points(receipt: dict) -> int:
    """
    Rules include:
    - +1 point for each alphanumeric character in the retailer name
    - +50 points if the total is a whole dollar amount
    - +25 points if the total is a multiple of 0.25
    - +5 points for every two items on the receipt
    - For each item, if the trimmed short description length is divisible by 3,
      add ceil(price * 0.2) points
    - +6 points if the day of the purchase date is odd
    - +10 points if the purchase time is between 2:00 and 4:00

    Args:
        receipt (dict): A dictionary representing the receipt data.

    Returns:
        int: The total calculated points for the receipt.
    """

    # total points
    points = 0

    # retailer
    retailer = receipt.get("retailer", "")
    points += sum(char.isalnum() for char in retailer)

    # price calculations
    dollars = receipt.get("total", "0")
    try:
        # whole dollar
        dollars = float(dollars)
        if dollars.is_integer():
            points += 50
        
        # 0.25 multiple
        if dollars % 0.25 == 0:
            points += 25
    except:
        pass

    # number of items
    items = receipt.get("items", [])
    points += 5 * (len(items)//2)

    for item in items:
        short_description = item.get("shortDescription", "").strip()
        if len(short_description) % 3 == 0:
            try:
                price = float(item.get("price", "0"))
                price = math.ceil(price*0.2)
                points += price
            except:
                pass
    
    # purchase data 
    purchase_data = receipt.get("purchaseDate", "")
    try:
        day =int(purchase_data.split("-")[2])
        if day % 2 == 1:
            points += 6
    except:
        pass

    # purchase time
    purchase_time = receipt.get("purchaseTime", "")
    try:
        time = datetime.strptime(purchase_time, "%H:%M").time()
        if time >= datetime.strptime("14:00", "%H:%M").time() and time < datetime.strptime("16:00", "%H:%M").time():
            points += 10
    except:
        pass

    return points

