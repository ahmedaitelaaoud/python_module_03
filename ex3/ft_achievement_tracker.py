def main():
    data_set = {
        'alice': ['first_blood', 'pixel_perfect', 'speed_runner',
                  'first_blood', 'first_blood'],
        'bob': ['level_master', 'boss_hunter', 'treasure_seeker',
                'level_master', 'level_master', 'first_blood'],
        'charlie': ['treasure_seeker', 'boss_hunter', 'combo_king',
                    'first_blood', 'boss_hunter', 'first_blood',
                    'boss_hunter', 'first_blood'],
        'diana': ['first_blood', 'combo_king', 'level_master',
                  'treasure_seeker', 'speed_runner', 'combo_king',
                  'combo_king', 'level_master'],
        'eve': ['level_master', 'treasure_seeker', 'first_blood',
                'treasure_seeker', 'first_blood', 'treasure_seeker'],
        'frank': ['explorer', 'boss_hunter', 'first_blood', 'explorer',
                  'first_blood', 'boss_hunter']
    }

    print("=== Achievement Tracker System ===")

    alice = set(data_set['alice'])
    bob = set(data_set['bob'])
    charlie = set(data_set['charlie'])
    diana = set(data_set['diana'])
    eve = set(data_set['eve'])
    frank = set(data_set['frank'])

    print(f"Player alice achievements: {alice}")
    print(f"Player bob achievements: {bob}")
    print(f"Player charlie achievements: {charlie}")
    print(f"Player diana achievements: {diana}")
    print(f"Player eve achievements: {eve}")
    print(f"Player frank achievements: {frank}")

    print("\n=== Achievement Analytics ===")

    all_achievements = alice.union(bob, charlie, diana, eve, frank)

    print(f"All unique achievements: {all_achievements}")
    print(f"Total unique achievements: {len(all_achievements)}")

    common_achievements = alice.intersection(bob, charlie, diana, eve, frank)

    print(f"Common to all players: {common_achievements}")


    rare_alice = alice.difference(bob, charlie, diana, eve, frank)
    rare_bob = bob.difference(alice, charlie, diana, eve, frank)
    rare_charlie = charlie.difference(alice, bob, diana, eve, frank)
    rare_diana = diana.difference(alice, bob, charlie, eve, frank)
    rare_eve = eve.difference(alice, bob, charlie, diana, frank)
    rare_frank = frank.difference(alice, bob, charlie, diana, eve)

    rare_achievements = rare_alice.union(rare_bob, rare_charlie, rare_diana, rare_eve, rare_frank)

    print(f"Rare achievements (1 player): {rare_achievements}")

    print("\n=== Specific Comparison (Alice vs Bob) ===")

    print(f"Alice vs Bob common: {alice.intersection(bob)}")
    print(f"Alice unique: {alice.difference(bob)}")
    print(f"Bob unique: {bob.difference(alice)}")


main()
