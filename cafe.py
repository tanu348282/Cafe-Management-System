Menu = {
    "Appetizers": {
        'ALMOND & PISTACHIO CHICKEN STRIPS': 2590,
        'DYNAMITE CHICKEN': 1495,
        'PRAWN BASKET': 1395,
        'CLASSIC HUMMUS WITH SHREDDED BEEF': 2195,
        'CHIMICHURI BITES': 1795,
        'CHICKEN CROQUETTES': 1695
    },
    "Soup": {
        'CHICKEN BROTH': 900,
        'SUN-DRIED TOMATO SOUP': 1150,
        'MUSHROOM SOUP': 800,
        'SEAFOOD CHOWDER SOUP': 1000,
        'CREAM OF CHICKEN': 700
    },
    "Pastas": {
        'ALFREDO PASTA': 1795,
        'AGLIO OLIO PASTA': 1895,
        'CREAMY MEATY LINGUINE': 1695,
        'LEMON & RICOTTA PASTA': 1795,
        'SUNRIED & SHIITAKE MUSHROOM PASTA': 1895
    },
    "Pizza": {
        'SPINACH AND FETA CHEESE': 2000,
        'CHIMICHURI PIZZA': 1695,
        'HAWAIIAN PIZZA': 1495,
        'NEW YORK PIZZA': 1895,
        'PARMESAN PIZZA': 1595
    },
    "Seafood": {
        'DARK ASIAN FISH': 2695,
        'PARMESAN CRUSTED RED SNAPPER': 3695,
        'GRILLED FISH WITH DILL CREAM SAUCE': 3000,
        'TIGER PRAWNS': 4400,
        'GRILLED FISH WITH LEMON BUTTER SAUCE': 3400
    },
    "Sweet Treats": {
        'ALMOND CHOCOLATE TABULAR': 2000,
        'MOLTEN LAVA CAKE': 1400,
        'LINDT CHOCOLATE TART': 1900,
        'BASQUE BURNT CHEESECAKE': 1600,
        'COOKIE SKILLET': 1300
    },
    "Drinks": {
        'Berry Blast': 890,
        'Misty Ocean': 750,
        'Pink Lady': 950,
        'Green Apple Mountain': 1000,
        'Hazelnut': 800
    }
}
 # Welcome Message
print("🍽️ Welcome to Python Cafe 🍽️\n") #Displays a welcome message when the program starts.

#Variables for Billing
total_bill = 0 #stores the final total amount
order_list = []    # stores ordered items

while True:

    # Display Categories
    print("\nMenu Categories:") 
    categories = list(Menu.keys())  #gets all category names
    for i, category in enumerate(categories, start=1):   #enumerate() adds numbers (1, 2, 3…)
        print(f"{i}. {category}")   #Displays menu categories

    # Category Selection
    category_choice = int(input("Select category number: ")) - 1  #User selects category number
    selected_category = categories[category_choice]  #Stores selected category name

    # Display Items
    print(f"\n--- {selected_category} Menu ---")
    items = list(Menu[selected_category].items())  #Fetches items of selected category
    for i, (item, price) in enumerate(items, start=1):
        print(f"{i}. {item} - Rs.{price}")    #Displays food name with price

    # Item Selection
    item_choice = int(input("Select item number: ")) - 1 #User selects item
    quantity = int(input("Enter quantity: "))  #User enters quantity


    # Cost Calculation
    item_name, item_price = items[item_choice]  #Retrieves item name & price
    cost = item_price * quantity  #Calculates cost = price × quantity

# Update Bill & Order List
    total_bill += cost  #Adds cost to total bill
    order_list.append((item_name, quantity, cost)) #Saves order details for receipt

    print(f"Added {item_name} x {quantity} (Rs.{cost})")

    # Continue or Stop Ordering?
    more = input("Order more? (yes/no): ").lower()
    if more != "yes":
        break
    
# Display FINAL BILL
print("\n FINAL BILL")
for item, quantity, price in order_list:
    print(f"{item} x {quantity} = Rs.{price}")
print(f"\nTotal Amount: Rs.{total_bill}")
print("Thank you for visiting Python Cafe ❤️")


# SAVE RECEIPT
with open("receipt.txt", "w") as file:
    file.write("PYTHON CAFE RECEIPT\n")
    file.write("--------------------------------\n")
    for item, quantity, price in order_list:
        file.write(f"{item} x {quantity} = Rs.{price}\n")
    file.write("--------------------------------\n")
    file.write(f"Total Amount: Rs.{total_bill}\n")
    file.write("Thank you for visiting Python Cafe \n")

print("Receipt saved successfully!")

