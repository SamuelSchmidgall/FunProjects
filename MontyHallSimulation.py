import random


def simulation(switch, doors=3, iterations=1000):
    outcomes = list()
    for itr in range(iterations):
        door_items = [0 for _ in range(doors)]
        door_items[random.choice(range(doors))] = 1
        initial_door = random.choice(range(doors))
        if switch:
            if door_items[initial_door] == 1:
                outcomes.append(0)
            else:
                outcomes.append(1)
        else:
            outcomes.append(door_items[initial_door])
    return sum(outcomes)/iterations

print(simulation(switch=False, doors=3))


