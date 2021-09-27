def prix(articles_distincts,nombre_exemplaire,prix_unit):
    prix_total = prix_unit*nombre_exemplaire
    if nombre_exemplaire >= 5:
        prix_total= prix_total*95/100
        return prix_total
    else:
        return prix_total