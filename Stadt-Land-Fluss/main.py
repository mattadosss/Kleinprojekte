import random
import string
import time


def random_letter():
    return random.choice(string.ascii_uppercase)


def score_entry(entry, letter):
    if entry.strip() == "":
        return 0
    return 10 if entry.upper().startswith(letter) else 0


def play_round():
    letter = random_letter()
    print(f"\nYour letter is: {letter}")
    print("You have 30 seconds to enter a City, Country, and River!")

    start_time = time.time()

    city = input("City: ")
    country = input("Country: ")
    river = input("River: ")

    end_time = time.time()
    time_taken = end_time - start_time

    if time_taken > 30:
        print("Time is up.")
        return 0

    total_score = 0
    total_score += score_entry(city, letter)
    total_score += score_entry(country, letter)
    total_score += score_entry(river, letter)

    print("\n--- Scoring ---")
    print(f"City: {city} ({score_entry(city, letter)} points)")
    print(f"Country: {country} ({score_entry(country, letter)} points)")
    print(f"River: {river} ({score_entry(river, letter)} points)")
    print(f"Total points this round: {total_score}")

    return total_score


def start_game():
    print("Welcome to City, Country, River!")
    total_points = 0

    while True:
        total_points += play_round()
        again = input("\nDo you want to play another round? (y/n): ").lower()
        if again != 'y':
            break

    print(f"\nGame Over. Your total score: {total_points} points.")


if __name__ == "__main__":
    start_game()
