from typing import List, Set, Optional, Tuple

street: str = "Ologuneru"

locations: List[str] = ["Apata", "Ologuneru", "Ajegunle"]

age: int = 3

Vector = List[List[int]]

def add_up(num: Vector):
    return num[0][1] + num[1][1]


number = [[21, 45, 67], [12, 13, 14], [67, 78, 67]]

names: Set[str] = {"Olamide", "Ayokunle", "Bolaji"}

uuid: Tuple[int, int, int] = (13432, 20098, 324644)


view: Optional[Vector | None]



# print(add_up(number))
