"""Practice with disctionaries."""

ice_cream: dict[str, int] = {'chocolate' : 1, 'mint chocolare, cjop' : 25, 'dtasrweberry' : 5}  # dict() when empty
print(ice_cream)

ice_cream["mint"] = 3  # adding mint yo lisr
print("add mint:")
print(ice_cream)

ice_cream.pop("mint")  # removing mint
print("remoive mint:")
print(ice_cream)

# acess onlt chocloate
print(ice_cream["chocolate"])
# f strings use single quotes
print(f"Use single quotes for access num of choc {ice_cream['chocolate']}")

# updating a value
ice_cream["chocolate"] += 1
print("After updating value")
print(ice_cream)

# finding length
len(ice_cream)
print("length:")
print(len(ice_cream))

# checking if in dictionary
print("checking for mint:")
print("mint" in ice_cream)
print("checking for chocolate:")
print("chocolate" in ice_cream)

# you CANNOT have the same key names example chocolate twice
# however you can have two of the same values example 12 for choc and 12 for vanilla