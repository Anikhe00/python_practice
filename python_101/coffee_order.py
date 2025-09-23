# ☕ Coffee Order Queue Challenge

# 1. Set up two variables: one for total price, one for drink count
total_price = 0
drink_count = 0

# 2. Start a while True loop
while True:
    # 3. Ask for the customer's name
    name = input("Enter your name: ")
    
    # 4. If the name is "done", break the loop
    if name.lower() == "done":
        break
        
    # 5. Ask for their drink order
    drink_order = input("Enter drink order(latte, americano, espresso, etc): ")
    
    # 6. If it's "latte", add 3.50 to total and +1 to drink count
    if drink_order.lower() == "latte":
        total_price += 3.50
        drink_count += 1
    
    # 7. If it's "americano", add 3.00 to total and +1 to drink count
    elif drink_order.lower() == "americano":
        total_price += 3.00
        drink_count += 1

    # 8. If it's "espresso", add 2.50 to total and +1 to drink count
    elif drink_order.lower() == "espresso":
        total_price += 2.50
        drink_count += 1
    
    # 9. If it's not one of those drinks, print a warning and continue
    else:
        print(f"We don't have {drink_order} on the menu.")
        continue
        
# 10. After the loop, print total number of drinks and total price
print(f"\nTotal drinks: {drink_count}")
print(f"Total price: ${total_price:.2f}")
        