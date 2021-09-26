# exercice 13
# print(b)
# 5

# Exercice 14
class mention:
    def __init__(self):
        self.note = float(input("Quelle est ta note : "))
        self.Note(self.note, 0, 10, "None")
        self.Note(self.note, 10, 12, "P")
        self.Note(self.note, 12, 14, "AB")
        self.Note(self.note, 14, 16, "B")
        self.Note(self.note, 16, 20, "TB")

    def Note(self, note, note_min, note_max, mention):
        if float(note) >= int(note_min) and note < int(note_max):
            print("Ta mention est :", mention)
            exit()
        else:
            return
mention()
