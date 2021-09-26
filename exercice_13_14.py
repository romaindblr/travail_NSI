# exercice 13
# print(b)
# 5

# Exercice 14
def Mention(note):
    if note <= 10:
        mention = "None"
        return mention
    elif note > 10 and note <= 12:
        mention = "P"
        return mention
    elif note > 12 and note <= 15:
        mention = "AB"
        return mention
    elif note > 15 and note <= 18:
        mention = "B"
        return mention
    elif note < 18 and note <= 20:
        mention = "TB"
        return mention
    else:
        mention = "Cette note n'est pas correcte"
        return mention
Note = float(input("Quelle est ta note : "))
print("Ta mention est :", Mention(Note))