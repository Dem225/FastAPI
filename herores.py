from typing import List
from classe import Hero
import csv
HEROES: List[Hero] = [
    Hero(
        id=1,
        nik_name="Zebi",
        full_name="wilsonne",
        occupation=["Mizard", "adventurer", "Deity"],
        power=["Magical prowess", "Charisma"],
        hobby=["studying magic", "cooking"],
        type="wizard",
        rank=54
    ),

]

#CREATE A CSV FILLE FROM THE ABOVE
def format_array(py_list):
    return '{' + ' , '.join(f'"{item}"' for item in py_list) + '}'


with open("heroes.csv", "w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)

    # Header
    writer.writerow([
        "nik_name",
        "full_name",
        "occupation",
        "power",
        "hobby",
        "type",
        "rank"
    ])

    # Data
    for hero in HEROES:
        
        writer.writerow([
            hero.nik_name,
            hero.full_name,
            format_array(hero.occupation),
            hero.power,
            format_array(hero.hobby),
            hero.type,
            hero.rank
        ])


