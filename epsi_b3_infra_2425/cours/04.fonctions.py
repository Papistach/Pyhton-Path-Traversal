# # b3_dev = ["Geoffroy", "Lisa", "Luc"]
# # b3_asrbd = ["Geoffroy", "Lisa", "Luc"]
# # b3_ia = ["Geoffroy", "Lisa", "Luc"]

# # def envoyer_email(une_classe):
# #     for el in une_classe:
# #         print(f"""Bonjour, {el}

# #         Je t'informe que l'examen...
                
# #         Geoffroy Ladrat""")

# # envoyer_email(b3_dev)
# # envoyer_email(b3_asrbd)
# # envoyer_email(b3_ia)

import datetime


# def afficher_date():
#     print(datetime.datetime.now().strftime("%d/%m/%y, %H:%M:%S"))

# def recuperer_date():
#     return datetime.datetime.now().strftime("%d/%m/%y, %H:%M:%S")


# # afficher_date()
# # afficher_date()
# # afficher_date()
# # afficher_date()


# def dire_bonjour():
#     print("bonjour")

# # def generer_bonjour():
# #     return "bonjour"

# dire_bonjour()
# print(dire_bonjour())
# print(dire_bonjour)


# print("Bonjour")

import datetime
print2 = print
def print(element):
    print2(datetime.datetime.now().strftime("%d/%m/%y, %H:%M:%S"), "-", element)
    with open("./log.log", "a") as file:
        file.write(datetime.datetime.now().strftime("%d/%m/%y, %H:%M:%S") + " - " + element + "\n")


print("COUCOU")