import random
from typing import List, Dict
from enum import Enum

class PrizeWeight(Enum):
    COMMON = 1
    UNCOMMON = 2
    RARE = 3
    EPIC = 4
    LEGENDARY = 5

class Treasure:
    def __init__(self, business: str, prize_description: str, type_prize: PrizeWeight):
        self.business = business
        self.prize_description = prize_description
        self.type_prize = type_prize

    def __str__(self):
        return f"{self.prize_description} ({self.business})"

class Business:
    def __init__(self, name: str):
        self.name = name
        self.prizes: Dict[PrizeWeight, List[Treasure]] = {prize: [] for prize in PrizeWeight}

    def add_prize(self, treasure: Treasure):
        self.prizes[treasure.type_prize].append(treasure)

    def get_prizes(self, type_prize: PrizeWeight) -> List[Treasure]:
        return self.prizes[type_prize]

class TreasureManager:
    def __init__(self):
        self.businesses: Dict[str, Business] = {}

    def add_business(self, business: Business):
        self.businesses[business.name] = business

    def add_prize(self, business_name: str, treasure: Treasure):
        if business_name in self.businesses:
            self.businesses[business_name].add_prize(treasure)
        else:
            raise ValueError(f"Business '{business_name}' not found")

# Prize data
treasure = {
    "common":  ["1% off a drink", "3% off a book", "3% off an appetizer", "4% off a haircut", "No prize", "3% off a bouquet", "1% off a color service", "2% off a book"],
    "uncommon": ["5% off a book", "8% off a book", "5% off a drink", "8% off a drink", "5% off a bouquet", "8% off a bouquet", "Spin again", "5% off a haircut", "8% off a haircut", "5% off a meal", "8% off a meal"],
    "rare": ["3 free roses", "Free drink", "50% off appetizer", "10% off a book", "15% off a book", "15% off a drink", "10% off a drink", "15% off a bouquet", "10% off a bouquet", "15% off a haircut", "10% off a haircut", "15% off a meal", "10% off a meal"],
    "epic": ["25% off haircut", "25% off a book", "25% off a bouquet", "25% off a coffee", "25% off a meal"],
    "legendary": ["50% off haircut", "50% off a book", "50% off a bouquet", "50% off a coffee", "50% off a meal"]
}

# Weight distribution for the prizes
prize_weight = {
    "common": 0.45,
    "uncommon": 0.25,
    "rare": 0.15,
    "epic": 0.10,
    "legendary": 0.05
}

def open_prizes():
    # Select rarity based on weighted probability
    rarity = random.choices(list(prize_weight.keys()), weights=prize_weight.values(), k=1)[0]

    # Select a random prize from that rarity level
    if treasure[rarity]:
        item = random.choice(treasure[rarity])
        return f"You found a {rarity} item: {item}"
    else:
        return f"You found a {rarity} prize, but it was empty!"

# Run the function to test
print(open_prizes())
