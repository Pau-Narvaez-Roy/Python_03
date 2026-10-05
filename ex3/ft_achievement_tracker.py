#!/usr/bin/env python3
import random as rnd


def gen_player_achievements() -> set:
    achievements = ['Crafting Genius', 'Strategist', 'World Savior',
                    'Speed Runner', 'Survivor', 'Master Explorer',
                    'Treasure Hunter', 'Unstoppable', 'First Steps',
                    'Collector Supreme', 'Untouchable', 'Sharp Mind',
                    'Boss Slayer']
    total = rnd.randrange(1, 14)
    player = []
    for i in range(0, total):
        achievement = achievements[rnd.randrange(0, 13 - i)]
        player.append(achievement)
        achievements.remove(achievement)
    return set(player)


if __name__ == "__main__":
    print("=== Achievement Tracker System ===\n")
    achievements = {'Crafting Genius', 'Strategist', 'World Savior',
                    'Speed Runner', 'Survivor', 'Master Explorer',
                    'Treasure Hunter', 'Unstoppable', 'First Steps',
                    'Collector Supreme', 'Untouchable', 'Sharp Mind',
                    'Boss Slayer'}
    alice = gen_player_achievements()
    print(f"Player Alice: {alice}")
    bob = gen_player_achievements()
    print(f"Player Bob: {bob}")
    charlie = gen_player_achievements()
    print(f"Player Charlie: {charlie}")
    dylan = gen_player_achievements()
    print(f"Player Dylan: {dylan}")
    print()
    print(f"All distinct achievements: {achievements}")
    print()
    print("Common achievements:",
          set.intersection(alice, bob, charlie, dylan))
    print()
    print("Only Alice has:",
          alice.difference(bob, charlie, dylan))
    print("Only Bob has:",
          bob.difference(alice, charlie, dylan))
    print("Only Charlie has:",
          charlie.difference(bob, alice, dylan))
    print("Only Dylan has:",
          dylan.difference(bob, charlie, alice))
    print()
    print("Alice is missing:",
          achievements.difference(alice))
    print("Bob is missing:",
          bob.difference(alice))
    print("Charlie is missing:",
          charlie.difference(alice))
    print("Dylan is missing:",
          dylan.difference(alice))
