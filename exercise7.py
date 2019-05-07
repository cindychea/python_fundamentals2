# Re-usable / Extracted functionality
def speed_calc(distance, time_mins):
    return float(distance) / float(time_mins) * 60

# 1: Gathering Data (faked out input functions)
test_racers = [
    {
        "name": "Larry",
        "distance": 5000,
        "time": 25
    },
    {
        "name": "Moe",
        "distance": 5000,
        "time": 35
    },
    {
        "name": "Curly",
        "distance": 5000,
        "time": 40
    }
]

# 2: Performing Work
for racer in test_racers:
    racer['speed'] = speed_calc(racer['distance'], racer['time'])

# 3: Rendering Results
# Sort our 'results' array of dictionaries by key
sorted_results = sorted(test_racers, key=lambda result: result['speed'])
for result in sorted_results:
    print(result)
# Announce Race Winner
winner = sorted_results[-1]
print("The winner of the race is {} at a speed of {} m/s!".format(winner['name'], winner['speed']))