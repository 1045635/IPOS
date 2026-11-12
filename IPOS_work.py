state_populations= {}

with open('populations.txt', 'r') as file:
    for line in file:
        line = line.strip()
        if not line:
            continue
        state, population = line.split(",")
        state_populations[state] = int(population)
New_York = state_populations["New York"]
California = state_populations["California"]
Texas = state_populations["Texas"]
Florida = state_populations["Florida"]









