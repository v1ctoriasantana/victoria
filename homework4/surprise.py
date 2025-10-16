# File: surprise.py

# Below is a dictionary of targets you want to observe.

# If you are an observational astronomer or instrumentalist, picking the correct targets
# to point the telescope at is very important. Let's practice below.

targets = {
    "Vega": {
        "RA": "18h 36m 56.3s",
        "Dec": "+38° 47′ 01″",
        "Magnitude": 0.03,
        "Spectral Type": "A0Va"
    },
    "Betelgeuse": {
        "RA": "05h 55m 10.3s",
        "Dec": "+07° 24′ 25″",
        "Magnitude": 0.42,
        "Spectral Type": "M1-M2 Ia-Ib"
    },
    "Sirius": {
        "RA": "06h 45m 08.9s",
        "Dec": "−16° 42′ 58″",
        "Magnitude": -1.46,
        "Spectral Type": "A1V"
    },
    "Rigel": {
        "RA": "05h 14m 32.3s",
        "Dec": "−08° 12′ 06″",
        "Magnitude": 0.12,
        "Spectral Type": "B8Ia"
    },
    "Polaris": {
        "RA": "02h 31m 49.1s",
        "Dec": "+89° 15′ 51″",
        "Magnitude": 1.97,
        "Spectral Type": "F7Ib"
    }
}

# --- Questions ---
# 1) Write a function that uses a loop to print the name of each star.

def print_star_names(targets_dict):
    print("Star Names:")
    for name in targets_dict:
        print(name)
# Got a syntax error, i forgot to add the colon at the end of the for loop, i changed for name in targets to for name in targets:
# 2) Write a function that uses a loop to print the name of each star with its spectral type.

def print_star_types(targets_dict):
    print("Star Names with Spectral Types:")
    for name, data in targets_dict.items():
        print(f"{name}: {data['Spectral Type']}")
# 3) Write a function that uses a conditional to find stars with magnitudes greater than 0.1 mag.

def stars_magnitude_above(threshold=0.1):
    print(f"Stars with magnitude > {threshold}:")
    for name, data in targets.items():
        if data['Magnitude'] > threshold:
            print(f"{name}: {data['Magnitude']}")

#syntax error, i accidentally used => instead of >= when comparing magnitudes. I changed if data["Magnitude"] => 0.1 to id data["Magnitude"] >= 0.1
# 4) Look up another target, add all the necessary information to the targets list. 

targets["Altair"] = {
    "RA": "19h 50m 47.0s",
    "Dec": "+08° 52′ 06″",
    "Magnitude": 0.77,
    "Spectral Type": "A7V"
}
# 5) Write a function that finds the brightest star whose Declination is closest to 20°.

import re

def parse_dec(dec_str):
    """Convert a Dec string like '+08° 52′ 06″' to decimal degrees."""
    match = re.match(r"([+\-−])(\d+)°\s*(\d+)′\s*(\d+)″", dec_str)
    if not match:
        return None
    sign, deg, min_, sec = match.groups()
    deg, min_, sec = int(deg), int(min_), int(sec)
    decimal = deg + min_ / 60 + sec / 3600
    if sign in ('−', '-'):
        decimal *= -1
    return decimal

def brightest_near_dec(targets_dict, target_dec=20.0):
    closest_star = None
    closest_diff = float('inf')
    for name, data in targets_dict.items():
        dec = parse_dec(data["Dec"])
        if dec is None:
            continue
        diff = abs(dec - target_dec)
        if diff < closest_diff:
            closest_diff = diff
            closest_star = name
    return closest_star
#type error, i tried to compare the declination string directly to an integer like this: if data["Dec"] < 20. I realized that dec is a string and cant be compared to a number without converting. I removed the comparison and just printed the Dec valies.
 # 6) What is your favorite constellation?

favorite_constellation = "Orion"

if __name__ == "__main__":
    print_star_names(targets)
    print()
    print_star_types(targets)
    print()
    stars_magnitude_above()
    print()
    print("Added target: Altair")
    print()
    star = brightest_near_dec(targets)
    print("Brightest star closest to +20° Dec:", star)
    print()
    print("My favorite constellation is:", favorite_constellation)