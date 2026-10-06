#!/usr/bin/env python3
import random as rnd
from typing import Generator


def consume_event(lst: list) -> Generator[int, None, None]:
    while len(lst) > 0:
        random = rnd.randrange(0, len(lst))
        event = lst[random]
        print(f"Got event from list: {event}")
        lst.remove(event)
        yield len(lst)


def gen_event() -> Generator[tuple[str, str], None, None]:
    players = ["bob", "alice", "dylan", "charlie"]
    actions = ["run", "eat", "sleep", "grab",
               "move", "climb", "swim", "release"]
    while True:
        player = players[rnd.randrange(0, 4)]
        action = actions[rnd.randrange(0, 8)]
        yield (player, action)


if __name__ == "__main__":
    print("=== Game Data Stream Processor ===")
    gen = gen_event()
    for i in range(1000):
        event = next(gen)
        print(f"Event {i}: Player {event[0]} did action {event[1]}")
    lst: list[tuple[str, str]] = [next(gen_event()) for _ in range(10)]
    print(F"Built list of 10 events: {lst}")
    for i in consume_event(lst):
        print(f"Remains in list {lst}")
