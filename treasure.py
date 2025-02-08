"""
grab 5 common,4 uncommon,3 rare, 2 epic, and 1 legendary 
grab from mutiple businesses 

treasure = [
    common: "bobs burger","mary's salon, "la fruteria", "siri", "flower shop", 
    uncommon: "", 
    rare:"",
    epic:"",
    legendary: "",
]
append randomly to treasure, 

Map 

"""
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

    def __init__(self,business: str,prize_description: str, type_prize: PrizeWeight):
        self.business = business
        self.prize_description = prize_description
        self.type_prize = type_prize
    def __str__(self):
        return f"{self.name} ({self.prize_description.business} - {self.value.business})"
class Business:

    def __init(self,name:str):
        self.name = name
        self.prizes: Dict[PrizeWeight,List[Treasure]] = {type_prize: [] for type_prize in PrizeWeight}

    def add_prize(self, treasure: Treasure):
        self.treasure[treasure.type_prize].append(treasure)
    def get_prizes(self, type_prize: PrizeWeight ) -> List[Treasure]:
        return self.treasure[type_prize]
    
class TreasureManager:
    def __init__(self):
        self.businesses: Dict[str,Business] = {}

    def add_business(self, business:Business):
        self.businesses[business.name] = business

    def add_prize(self,business_name:str,treasure:Treasure):
        if business_name in self.businesses:
            self.busniesses[business_name].add_prize(treasure)
        else: 
            raise ValueError(f"Business '{business_name}' not found")


treasure = {
    "common": ["bobs burger- 25","mary's salon", "la fruteria", "siri", "flower shop"], 
    "uncommon": ["burger","tea","weed","help"], 
    "rare":["bi","bello","kellog"],
    "epic":["cats","hello"],
    "legendary": ["dogs"],
}
prize_weight = {
    "common" : 0.45,
    "uncommon": 0.25,
    "rare": 0.15,
    "epic": 0.10,
    "legendary": 0.05,
}
def data_creation():
    manager = TreasureManager()

    
def open_prizes():
    rarity = random.choice(list(prize_weight.keys()), weights=prize_weight.values(),k=1)[0]
    if treasure[rarity]:
        item = random.choice(treasure[prize_weight])
        return f"You found a {rarity} item: {item}"
    else:
        return f"You found a {rarity} prize, but it was empty!"
print(open_prizes())