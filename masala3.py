import os
os.system("cls")

ids = ['S001', 'S002', 'S003', 'S004']
ismlar = ['Adina Park', 'Leyton Marsh', 'Duncan Boyle', 'Saim Richards']
hisob = [85, 98, 89, 92]

nested_dict = [
    {ids[i]: {ismlar[i]: hisob[i]}}
    for i in range(len(ids))
]

print(nested_dict)
