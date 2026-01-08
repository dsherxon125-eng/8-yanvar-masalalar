import os
os.system("cls")

login = {
    "jeymsBond": "agent007",
    "tony_stark": "ironman101",
    "piterParker": "spider.12.12",
    "sherlok": "sher.l04"
}

foydalanuvchi = input("Username kiriting: ")
ism = input("Parol kiriting: ")

if foydalanuvchi in login:
    if login[foydalanuvchi] == ism:
        print("Hisobga kirdingiz")
    else:
        print("Parol noto‘g‘ri")
else:
    print("Bunday foydalanuvchi mavjud emas")
