def chiefHopper(arr):
    start_energy = 0
    while True:
        energy = start_energy
        for item in arr:
            energy = energy * 2 - item
            if energy < 0:
                break
        if energy >= 0:
            return start_energy
        start_energy += 1

