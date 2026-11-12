state_populations= []

with open('state_populations_random.csv', 'r') as file:
    for line in file:
        line = line.strip()
        if not line:
            continue
        parts = line.split(",")
        state = parts[0].strip()
        population = int(parts[1].strip())
        state_populations.append((state, population))

print(state_populations)







