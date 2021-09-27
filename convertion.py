# crée par Romain Doublier-Villette
# convertisseur des nombres en décimal, binaire et hexadécimal

class convertion:

    def __init__(self):
        print("Bonjours !!")
        print("Bienvenue sur mon programme de Convertion")
        self.start()

    def start(self):
        # savoir ce qu'elle est son unité de départ
        print("qu'elle est ton unité de départ :")
        print("1 = décimal")
        print("2 = binaire")
        print("3 = hexadécimal")
        self.choix = int(input("Fait ton choix : "))
        self.choix_verif()

    def start_convertion(self):
        # demande le chiffre qu'il veut convertire
        self.chiffre_start = input("Qu'elle chiffre veut-tu convertir ? ")
        self.converte()
        self.decimal()
        self.binaire()
        self.hexadecimal()
        self.print()
        self.Continue()

    def choix_verif(self):
        # vérifie si son choix est correcte
        if self.choix == 1 or self.choix == 2 or self.choix == 3:
            #choix correcte
            self.start_convertion()
        else:
            # choix pas correcte
            print("aie tu t'est tromper !!")
            self.start()

    def decimal(self):
        # convertire en décimal
        self.resultat_decimal = int(self.chiffre_convert)
        return

    def binaire(self):
        # convertire en binaire
        self.resultat_binaire = bin(self.chiffre_convert)
        self.resultat_binaire = self.resultat_binaire[2::]
        return

    def hexadecimal(self):
        # convertire en hexadécimal
        self.resultat_hexa = hex(self.chiffre_convert)
        self.resultat_hexa = self.resultat_hexa[2::]
        return

    def converte(self):
        # verifi si le chiffre qu'il a mis correspond a l'unité qu'il a choisi
        if self.choix == 1:
            try:
                self.chiffre_convert = int(self.chiffre_start)
                return
            except:
                print("aie ceci n'est pas du décimal")
                self.start_convertion()
        elif self.choix == 2:
            try:
                self.chiffre_convert = int(self.chiffre_start, 2)
                return
            except:
                print("aie ceci n'est pas du binaire")
                self.start_convertion()
        elif self.choix == 3:
            try:
                self.chiffre_convert = int(self.chiffre_start, 16)
                return
            except:
                print("aie ceci n'est pas de l'hexadecimal")
                self.start_convertion()

    def Continue(self):
        # savoir si il veut convertire d'autre chiffre
        try :
            self.cont = int(input("Veut-tu continuer a convertire des nombres ? 1 = oui ; 2 = non : "))
        except:
            print("ceci n'est pas un chiffre")
            self.Continue()
        if self.cont == 1:
            self.start()
        elif self.cont == 2:
            print("au revoir !!")
            exit()
        else:
            print("aie tu t'est tromper !!")
            self.Continue()

    def print(self):
        # affiche dans la console les résultat
        print("décimal :", self.resultat_decimal)
        print("binaire :", self.resultat_binaire)
        print("hexadécimal :", self.resultat_hexa)

convertion()