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
# Kosinus
    elif auswahl == 2 :
        print ('''
                    Kosinus soll berechnet werden

                    Kosinus folgt dem Schema 
                    
                    Ankathete / Hypotenuse (b/c)

                    Bitte geben sie sie die Werte ein

                ''')
        auswahl2A = float(raw_input("Geben sie die lange der Ankathete des Winkels an ~> "))
        auswahl2H = float(raw_input("Jetzt die lange der Hypotenuse ~> "))
        
        # Rechnet den Sinus des Winkela
        KosinusWinkel = auswahl2A / auswahl2H

        print "\n Der Kosinus des Winkels ist %s " % KosinusWinkel

#Tangens
    elif auswahl == 3:
        

        print ('''
                    Tangens soll berechnet werden

                    Tangens folgt dem Schema 
                    
                    Gegenkathete / Ankathete (a/b)

                    Bitte geben sie sie die Werte ein

                ''')
        auswahl3G = float(raw_input("Geben sie die lange der Gegenkathete  des Winkels an ~> "))
        auswahl3A = float(raw_input("Jetzt die lange der Ankathete ~> "))
        
        # Rechnet den Sinus des Winkela
        TangensWinkel = auswahl3G / auswahl3A

        print "\n Der Tangens des Winkels ist %s " % TangensWinkel


usage()
use()
