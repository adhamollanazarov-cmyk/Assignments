print("=== Pizza Shop Order System ===")
print("Enter pizza size: personal, medium, or family")
print("Type 'done' when finished ordering")
total = 0.0
while True:
    print()
    user_input = input("Enter pizza size: ")
    if user_input == "personal":
        total += 7.00
        print("Price: $7.00")
        print(f"Current total: ${total:.2f}")
    elif user_input == "medium":
        total += 12.00
        print("Price: $12.00")
        print(f"Current total: ${total:.2f}")
    elif user_input == "family":
        total += 18.00
        print("Price: $18.00")
        print(f"Current total: ${total:.2f}")
    elif user_input == "done":
        break
    else:
        print("Other category. Try again")
    print()
if total >= 40.00:
    discount = 5.00
else:
    discount = 0.00
final_total = total - discount
print("=== Order Summary ===")
print(f"Subtotal: ${total:.2f}")
print(f"Party Order Discount: -${discount} ")
print(f"Final Total: ${final_total:2f}")
print("Thank you for your order!")
