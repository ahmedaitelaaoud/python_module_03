#!/usr/bin/env python3
"""
Exercise 4: Inventory Master
Demonstrates dictionary usage for managing game inventories
with nested data structures and complex relationships.
"""


def get_data_set():
    """Create and return the game data set."""
    data_set = {
        'players': {
            'alice': {
                'items': {
                    'pixel_sword': 1,
                    'code_bow': 1,
                    'health_byte': 1,
                    'quantum_ring': 3
                },
                'total_value': 1875,
                'item_count': 6
            },
            'bob': {
                'items': {
                    'code_bow': 3,
                    'pixel_sword': 2
                },
                'total_value': 900,
                'item_count': 5
            },
            'charlie': {
                'items': {
                    'pixel_sword': 1,
                    'code_bow': 1
                },
                'total_value': 350,
                'item_count': 2
            },
            'diana': {
                'items': {
                    'code_bow': 3,
                    'pixel_sword': 3,
                    'health_byte': 3,
                    'data_crystal': 3
                },
                'total_value': 4125,
                'item_count': 12
            }
        },
        'catalog': {
            'pixel_sword': {
                'type': 'weapon',
                'value': 150,
                'rarity': 'common'
            },
            'quantum_ring': {
                'type': 'accessory',
                'value': 500,
                'rarity': 'rare'
            },
            'health_byte': {
                'type': 'consumable',
                'value': 25,
                'rarity': 'common'
            },
            'data_crystal': {
                'type': 'material',
                'value': 1000,
                'rarity': 'legendary'
            },
            'code_bow': {
                'type': 'weapon',
                'value': 200,
                'rarity': 'uncommon'
            }
        }
    }
    return data_set


def player_inventory(data_set, player_name):
    """Display a player's inventory with all details."""
    catalog = data_set.get('catalog')
    players = data_set.get('players')
    player_data = players.get(player_name)

    if not player_data:
        print(f"Error: Player '{player_name}' not found.")
        return

    player_items = player_data.get('items')

    print(f"=== {player_name.capitalize()}'s Inventory ===")

    total_value = 0
    total_count = 0
    categories = {}

    for item_key, quantity in player_items.items():
        details = catalog.get(item_key)

        if details:
            i_type = details.get('type')
            i_val = details.get('value')
            i_rarity = details.get('rarity')

            item_total_val = i_val * quantity
            total_value += item_total_val
            total_count += quantity

            current_cat_qty = categories.get(i_type, 0)
            categories.update({i_type: current_cat_qty + quantity})
            print(f"{item_key} ({i_type}, {i_rarity}): "
                  f"{quantity}x @ {i_val} gold each = {item_total_val} gold")

    print(f"Inventory value: {total_value} gold")
    print(f"Item count: {total_count} items")

    cat_string = ""
    for cat, count in categories.items():
        if len(cat_string) > 0:
            cat_string += ", "
        cat_string += f"{cat}({count})"
    print(f"Categories: {cat_string}\n")


def transfer_item(data_set, from_player, to_player, item_name, quantity):
    """Transfer items between players dynamically."""
    print(f"=== Transaction: {from_player} gives {to_player} {quantity} {item_name} ===")
    players = data_set.get('players')

    # Check if both players exist
    if from_player not in players:
        print(f"Error: Player '{from_player}' not found.")
        return False

    if to_player not in players:
        print(f"Error: Player '{to_player}' not found.")
        return False

    source_items = players[from_player]['items']

    # Check if source player has the item
    if item_name not in source_items:
        print(f"Error: {from_player} doesn't have {item_name}")
        return False

    # Check if enough quantity
    if source_items[item_name] < quantity:
        print(f"Error: {from_player} only has {source_items[item_name]} "
              f"{item_name}(s)")
        return False

    # Get item value from catalog for updating totals
    catalog = data_set.get('catalog')
    item_value = catalog[item_name]['value']
    transfer_value = item_value * quantity

    # Remove from source
    source_items[item_name] -= quantity
    players[from_player]['total_value'] -= transfer_value
    players[from_player]['item_count'] -= quantity

    # If quantity reaches 0, remove the item
    if source_items[item_name] == 0:
        del source_items[item_name]

    # Add to destination
    dest_items = players[to_player]['items']
    if item_name in dest_items:
        dest_items[item_name] += quantity
    else:
        dest_items[item_name] = quantity

    players[to_player]['total_value'] += transfer_value
    players[to_player]['item_count'] += quantity

    return True


def find_most_valuable_player(data_set):
    """Find the player with the highest inventory value."""
    players = data_set.get('players')
    max_value = 0
    richest_player = None

    for player_name, player_data in players.items():
        value = player_data.get('total_value', 0)
        if value > max_value:
            max_value = value
            richest_player = player_name

    return richest_player, max_value


def find_player_with_most_items(data_set):
    """Find the player with the most items."""
    players = data_set.get('players')
    max_items = 0
    player_with_most = None

    for player_name, player_data in players.items():
        item_count = player_data.get('item_count', 0)
        if item_count > max_items:
            max_items = item_count
            player_with_most = player_name

    return player_with_most, max_items


def find_rarest_items(data_set):
    """Find all items of a specific rarity across all players."""
    catalog = data_set.get('catalog')
    players = data_set.get('players')

    rare_items = set()

    for player_data in players.values():
        for item_name in player_data['items'].keys():
            if catalog[item_name]['rarity'] == 'rare':
                rare_items.add(item_name)

    return rare_items


def get_player_item_count(data_set, player_name, item_name):
    """Get the quantity of a specific item for a player."""
    players = data_set.get('players')
    if player_name in players:
        return players[player_name]['items'].get(item_name, 0)
    return 0


def main():
    """Main function demonstrating inventory system."""
    print("=== Player Inventory System ===\n")

    # Get the data set
    data_set = get_data_set()

    # Display Alice's inventory
    player_inventory(data_set, 'diana')


    # Note: Alice only has 1 code_bow, so let's transfer that
    if transfer_item(data_set, 'charlie', 'alice', 'code_bow', 1):
        print("Transaction successful!\n")

    # Display updated inventories
    print("=== Updated Inventories ===")
    alice_bows = get_player_item_count(data_set, 'alice', 'code_bow')
    bob_bows = get_player_item_count(data_set, 'bob', 'code_bow')
    print(f"Alice code_bow: {alice_bows}")
    print(f"Bob code_bow: {bob_bows}\n")

    # Analytics
    print("=== Inventory Analytics ===")

    # Most valuable player
    richest, value = find_most_valuable_player(data_set)
    print(f"Most valuable player: {richest.capitalize()} ({value} gold)")

    # Player with most items
    most_items_player, item_count = find_player_with_most_items(data_set)
    print(f"Most items: {most_items_player.capitalize()} "
          f"({item_count} items)")

    # Rarest items
    rare_items = find_rarest_items(data_set)
    if rare_items:
        rare_items_str = ", ".join(sorted(rare_items))
        print(f"Rarest items: {rare_items_str}")


main()
