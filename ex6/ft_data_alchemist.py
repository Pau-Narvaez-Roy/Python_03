#!/usr/bin/env python3


if __name__ == "__main__":
    print("=== Game Data Alchemist ===\n")
    total_players: list = ['Alice', 'bob', 'Charlie', 'dylan', 'Emma',
                           'Gregory', 'john', 'kevin', 'Liam']
    print(f"Initial list of players: {total_players}")

    capitalized: list = []
    for player in total_players:
        capitalized.append(player.capitalize())
    print(f"New list with all names capitalized: {capitalized}")

    capitalized_only: list = [n for n in total_players if n.istitle()]
    print(f"New list with all names capitalized: {capitalized_only}\n")

    scores: dict = {'Alice': 263, 'Bob': 666, 'Charlie': 907,
                    'Dylan': 170, 'Emma': 568, 'Gregory': 446,
                    'John': 90, 'Kevin': 527, 'Liam': 54}
    print(f"Score dict: {scores}")
    avrg = round(sum(scores.values()) / len(scores.values()), 2)
    print(f"Score average is {avrg}")
    top: dict[str, int] = dict()
    for player, score in scores.items():
        if score > avrg:
            top.update({player: score})
    print(f"High scores: {top}")
