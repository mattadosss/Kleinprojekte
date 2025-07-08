import random
import string
import time
import requests


def random_letter():
    return random.choice(string.ascii_uppercase)


def check_place_exists(place, type_filter):
    if not place.strip():
        return False

    url = "https://nominatim.openstreetmap.org/search"
    params = {
        'q': place,
        'format': 'json',
        'limit': 1,
        'addressdetails': 1
    }

    headers = {
        'User-Agent': 'CityCountryRiverGame/1.0'
    }

    try:
        response = requests.get(url, params=params, headers=headers, timeout=5)
        response.raise_for_status()
        data = response.json()
        if not data:
            return False

        address = data[0].get('address', {})
        if type_filter == "city":
            return 'city' in address or 'town' in address
        elif type_filter == "country":
            return 'country' in address
        elif type_filter == "river":
            return 'river' in address or 'waterway' in address or 'natural' in address
        else:
            return False
    except:
        return False


def score_entry(entry, letter, type_filter):
    if not entry.upper().startswith(letter):
        return 0
    return 10 if check_place_exists(entry, type_filter) else 0


def play_round():
    letter = random_letter()
    print(f"\nYour letter is: {letter}")
    print("You have 30 seconds to enter a City, Country, and River!")

    start_time = time.time()

    city = input("City: ")
    country = input("Country: ")
    river = input("River: ")

    end_time = time.time()
    if end_time - start_time > 30:
        print("Time's up! No points this round.")
        return 0

    score = 0
    city_score = score_entry(city, letter, "city")
    country_score = score_entry(country, letter, "country")
    river_score = score_entry(river, letter, "river")

    score += city_score + country_score + river_score

    print("\n--- Scoring ---")
    print(f"City: {city} ({city_score} points)")
    print(f"Country: {country} ({country_score} points)")
    print(f"River: {river} ({river_score} points)")
    print(f"Total this round: {score}")

    return score


def start_game():
    print("🎮 Welcome to City, Country, River with Online Validation!")
    total = 0
    while True:
        total += play_round()
        again = input("\nPlay another round? (y/n): ").lower()
        if again != 'y':
            break
    print(f"\nGame over. Final score: {total}")


if __name__ == "__main__":
    start_game()
