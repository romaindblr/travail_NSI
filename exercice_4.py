# cree par Romain Doublier-villette
prix_total=0
nbr = float(input("nombre de livres ?"))
while nbr!=0:
    prix = float(input("prix unitaire de ce livre"))
    prix_total = nbr*prix+prix_total
    nbr = float(input("nombre de livres ?"))

print("il n'y a plus de livre")
redu =  float(input("taux de réduction en % sur tout les livres"))
redu = 100-redu
prix_total = prix_total*redu/100
print(prix_total)