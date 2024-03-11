"""Demonstartes range in a for loop."""

names: list[str] = ["Alyssa", "Michi", "Tay"]

for index in range(0, len(names)):
    print(f"{index}:{names[index]}")