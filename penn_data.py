import pandas as pd
import random

fNames =  ["Mac", "Jerome ","John ","Ben ","Hugh ","James ","Mohammed","Mary ","Carman ","Jessica ","Joe","Robert","David","William","Richard","Thomas","Christopher"]
lNames =  ["Seeman","Anderson","Smith","Dover","Janus","Dirkas", "Alakas","Tarken","Emma","Kurtis"]
years = ["Freshman","Sophmore","Junior","Senior"]
pathways = ["Early College","Engineering","Computer Science","Buisness","Marketing", "Early childhood Education","culinary","criminal justice","Math","Bio med","Athletics", "Music","Pervert","Pedophile"]
names = []
for i in range(20000):
    names.append(f"{random.choice(fNames)},{random.choice(lNames)}")
print(names)

data = {
    "Name": names,
    "Age":  [random.randint(14,19) for _ in names],
    "GPA":  [round(random.uniform(0.0,4.5),2) for _ in names],
    "Credits Completed":  [random.randint(0, 60) for _ in names],
    "Year": [random.choice(years) for _ in names],
    "Pathway": [random.choice(pathways) for _ in names]
}

pennData = pd.DataFrame(data)
pennData.to_csv("pennData.csv", index=False)
print(pennData)