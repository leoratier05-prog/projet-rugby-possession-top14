import pandas as pd


d = pd.read_csv("donnees_top14_1.csv")

#calcule de la moyenne de tous les matchs et de toutes les équipes 
moyenne = d.groupby("victoire")["possession"].mean()
print(moyenne)

#Calcule la corrélation entre possession et victoire 
correlation = d["possession"].corr(d["victoire"])
print(correlation)

import matplotlib.pyplot as plt

d.boxplot(column="possession", by="victoire")
plt.title("Possession selon le résultat du match")
plt.suptitle("") #pour enlever le titre automatique 
plt.xlabel("Victoire (0=défaite, 1 = victoire)")
plt.ylabel("Possession")
plt.show()

#Même procedure pour l'occupations de toutes les équipes 
moyenne_occup = d.groupby("victoire")["occupation"].mean()
print(f"Moyenne occupation : {moyenne_occup}")

correlation_occup = d["occupation"].corr(d["victoire"])
print(f"Corrélation occupation/victoire : {correlation_occup}")

import matplotlib.pyplot as plt 

d.boxplot(column="occupation", by="victoire")
plt.title("Occupation selon le résultat du match")
plt.suptitle("")  # enlève le titre automatique 
plt.xlabel("Victoire (0 = défaite, 1 = victoire)")
plt.ylabel("Occupation")
plt.show()

import matplotlib.pyplot as plt

fig, axes = plt.subplots(1, 2, figsize=(10, 5))

d.boxplot(column="possession", by="victoire", ax=axes[0])
axes[0].set_title("Possession selon le résultat")
axes[0].set_xlabel("Victoire (0 = défaite, 1 = victoire)")

d.boxplot(column="occupation", by="victoire", ax=axes[1])
axes[1].set_title("Occupation selon le résultat")
axes[1].set_xlabel("Victoire (0 = défaite, 1 = victoire)")

plt.suptitle("")
plt.tight_layout()
plt.show()

#Analyse uniquement sur l'équipe de Toulouse 

toulouse = d[d["equipe"] == "Stade Toulousain"]
moyenne_tls = round(toulouse["possession"].mean(), 2)
print(moyenne_tls)

correlation_tls = round(toulouse["possession"].corr(d["victoire"]), 2)
print(correlation_tls)
