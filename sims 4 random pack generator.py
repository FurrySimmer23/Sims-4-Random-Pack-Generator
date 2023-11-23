import random


all_packs = [
    "Base Game",
    "Get To Work",
    "Get Together",
    "City Living",
    "Cats and Dogs",
    "Seasons",
    "Get Famous",
    "Island Living",
    "Discover University",
    "Eco Lifestyle",
    "Snowy Escape",
    "Cottage Living",
    "High School Years",
    "Growing Together",
    "Horse Ranch",
    "For Rent",
    "Outdoor Retreat",
    "Spa Day",
    "Dine Out",
    "Vampire",
    "Parenthood",
    "Jungle Adventure",
    "StrangerVille",
    "Realm Of Magic",
    "Star Wars Journey To Batuu",
    "Dream Home Decorator",
    "My Wedding Stories",
    "Werewolves",
    "Holiday Celebration Pack",
    "Luxury Party Stuff",
    "Perfect Patio Stuff",
    "Game Pack 2",
    "Game Pack 2",
    "Game Pack 2",
    
    # Add more packs as needed
]

def generate_random_pack():
    return random.choice(all_packs)

def main():
    # Generate a random pack
    random_pack = generate_random_pack()

    # Write the random pack to a text file
    with open("random_pack.txt", "w") as file:
        file.write(random_pack)

    print(f"Random pack generated: {random_pack}")
    print("Check random_pack.txt for the result.")

if __name__ == "__main__":
    main()
