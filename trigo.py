import math
version = "v0.1"
def usage():
    print '''

            Trigonometrie Rechner %s

            1. Sinus berechnen 
            2. Kosinus berechnen
            3. Tangens berechnen


            ''' % version


def use():
    auswahl = int(raw_input("Was mochtest du berechnen ? ~> "))

    if auswahl == 1 :
        print ('''
                    Sinus soll berechnet werden

                    Sinus folgt dem Schema 
                    
                    Gegenkathete / Hypotenuse (a/c)

                    Bitte geben sie sie die Werte ein

                ''')
        auswahl1G = float(raw_input("Geben sie die lange der Gegenkathete des Winkels an ~> "))
        auswahl1H = float(raw_input("Jetzt die lange der Hypotenuse ~> "))
        
        # Rechnet den Sinus des Winkela
        SinusWinkel = auswahl1G / auswahl1H

        print "\n Der Sinus des Winkels ist %s " % SinusWinkel



use()
