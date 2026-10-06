#!/usr/bin/env python3
import sys


def inventory_printing(data: dict) -> None:
    print(f"Got inventory: {data}")
    print(f"Item list: {list(data.keys())}")
    print(f"Total quantity of the {len(data.keys())} items:",
          f"{sum(data.values())}")
    for i in data:
        res = (data[i] / sum(data.values())) * 100
        print(f"Item {i} represents {round(res, 1)}%")
    max = 0
    for i in data:
        if data[i] > max:
            max = data[i]
            key = i
    print(f"Item most abundant: {key} with quantity {max}")
    min = sum(data.values())
    for i in data:
        if data[i] < min:
            min = data[i]
            key = i
    print(f"Item least abundant: {key} with quantity {min}")
    data.update({"magic_item": 1})
    print(f"Updated inventory: {data}")


if __name__ == "__main__":
    print("=== Inventory System Analysis ===")
    data: dict[str, int] = dict()
    if len(sys.argv) > 1:
        for i in range(1, len(sys.argv)):
            try:
                key = str(sys.argv[i].split(':')[0])
                value = int(sys.argv[i].split(':')[1])
                if value <= 0:
                    raise ValueError("Value can't be negative")
                if key not in data:
                    data.update({key: value})
                else:
                    print(f"Redundant item '{key}' - discarding")
            except IndexError:
                print(f"Error - invalid parameter '{sys.argv[i]}'")
            except ValueError as e:
                print(f"Quantity error for '{key}': {e}")
        inventory_printing(data)
    else:
        print("Empty inventory.")
