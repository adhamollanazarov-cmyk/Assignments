def find_item_index(item_names, item_name):
    for i in range(len(item_names)):
        if item_names[i] == item_name:
            return i
    else:
        return -1

def process_inventory_events(initial_items, initial_quantities, events):
    items = initial_items[:]
    quantities = initial_quantities[:]
    for event in events:
        events_command = event[0]
        if events_command == "PICKUP":
            item_name= event[1]
            quantity = event[2]
            item_index = find_item_index(items, item_name)
            if item_index != -1:
                quantities[item_index] += quantity
            else:
                items.append(item_name)
                quantities.append(quantity)
        elif events_command == "USE":
            item_name= event[1]
            quantity = event[2]
            item_index = find_item_index(items, item_name)
            if item_index != -1:
                quantities[item_index] -= quantity
                if quantities[item_index] <=0:
                    items.pop(item_index)
                    quantities.pop(item_index)
            else:
                continue
        elif events_command == "DROP":
            item_name= event[1]
            item_index = find_item_index(items, item_name)
            if item_index != -1:
                items.pop(item_index)
                quantities.pop(item_index)    
            else:
                continue       
    return items , quantities




items = ["Sword", "Health Potion", "Gold Coin"]
quantities = [1, 5, 100]
game_events = [
    ["PICKUP", "Gold Coin", 50],
    ["USE", "Health Potion", 2],
    ["DROP", "Sword"],
    ["PICKUP", "Magic Scroll", 1],
    ["USE", "Health Potion", 3]  
]

final_items, final_quantities = process_inventory_events(items, quantities, game_events)
print("Final Inventory:")
print(f"final_items: {final_items}")
print(f"final_quantities: {final_quantities}")

# # Test Case 1
# items = ["Sword", "Health Potion", "Gold Coin"]
# quantities = [1, 5, 100]
# game_events = [
#     ["PICKUP", "Gold Coin", 50],
#     ["USE", "Health Potion", 2],
#     ["DROP", "Sword"],
#     ["PICKUP", "Magic Scroll", 1],
#     ["USE", "Health Potion", 3]  # This will cause the item to be removed
# ]

# # When you call your function:
# final_items, final_quantities = process_inventory_events(items, quantities, game_events)

# Expected Output:

# Final Inventory:
# final_items: ['Gold Coin', 'Magic Scroll']
# final_quantities: [150, 1]

