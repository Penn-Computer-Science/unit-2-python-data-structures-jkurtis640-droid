##1. Tuples
color = ("red", "orange", "yellow", "green", "blue")
print("red")
print("blue")
for i in range(2):
    print(color)
color = ("purple", "orange", "yellow", "green", "blue")
print(color)
##2. Lists
number = ["1","2","3","4","5","6","7","8","9","10"]
print(number[0])
print(number[4])
print(number[9])
number.append("11")
print(number)
number[2] = 99
print(number)
print(number[1])
print(number[3])
print(number[5])
print(number[7])
print(number[9])
##3. Dictionaries
countries = {
   "America": "Washington DC",
    "Canada": "Ottawa",
    "Mexico": "Mexico City",
    "Honduras": "Tegucigalpa",
    "Belize": "Belmopan",
}
print("Belmopan")
print("Tegucigalpa")
countries["Nicaragua"] = "Managua"
print(countries)
print(countries)
##4. Sets
favorite_fruit = {"apple", "banana", "grape", "raspberries", "blueberries", "blackberries"}
print(favorite_fruit)
favorite_fruit.add("dragonfruit")
favorite_fruit.remove("apple")
print(favorite_fruit)
