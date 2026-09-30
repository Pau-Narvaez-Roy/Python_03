#!/usr/bin/env python3
import sys


def calculate(lst: list) -> None:
    print(f"Total players: {len(lst)}")
    print(f"Total score: {sum(lst)}")
    print(f"Average score: {sum(lst) / len(lst)}")
    print(f"Hight score: {max(lst)}")
    print(f"Low score: {min(lst)}")
    print(f"Score range: {max(lst) - min(lst)}")


if __name__ == "__main__":
    print("=== Player Score Analytics ===")
    lst = []
    if len(sys.argv) > 1:
        for i in range(1, len(sys.argv)):
            try:
                lst.append(int(sys.argv[i]))
            except ValueError:
                print(f"Invalid parameter: '{sys.argv[i]}'")
        if len(lst) > 0:
            calculate(lst)
    if len(sys.argv) <= 1 or len(lst) == 0:
        print(
            "No scores provided.",
            "Usage: python3 ft_score_analytics.py <score1> <score2> ..."
        )
