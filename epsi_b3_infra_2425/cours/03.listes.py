# eleves = ["Camille", "Lisa", "Elise", "Thomas", "Luc", "Michel"]
# notes = [12, 14.5, 8.5, 14.5, 18, 0]

# for i, eleve in enumerate(eleves):
#     print(f"Eleve {eleve}: {notes[i]}/20")

# print(len(notes))

# print(eleves[0])
# print(eleves[5])

# print(eleves[-1])
# print(eleves[-6])

# jours = ["lun", "mar", "mer", "jeu", "ven", "sam", "dim"]
# print(jours[-1])

# # slicing
#     # liste[debut:fin+1]
# week_end = jours[-3:]
# print(week_end)
# print(jours[:5])

# phrase = "Bonjour, Geoffroy Ladrat"
# print(phrase[9:])

# log = ""
# with open("C:\\Users\\Geoffroy\\Documents\\exercices\\2024-2025\\epsi_b3_infra_2425\\cours\\log.csv", "r") as file:
#     log = file.read()

# print(log)
# jour = log.split(";")[1][:2]
# url = log.split(";")[3].split("/")
# print(jour)
# print(url)

# serie
jours = ["lun", "mar", "mer", "jeu", "ven", "sam", "dim"]

jours_fr_en = [
    ["lun", "mar", "mer", "jeu", "ven", "sam", "dim"],
    ["mon", "tue", "wed", "thu", "fri", "sat", "sun"]
]

# matrice
print(jours_fr_en[0][-2:])