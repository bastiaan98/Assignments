#Hier worden de opties van de gebruiker geprint en gevraagd welke optie de gebruiker wilt kiezen.

print('1.Ik wil weten hoeveel kluizen er nog vrij zijn.\n2.Ik wil een nieuw kluis.\n3.Ik wil even iets uit mijn kluis halen.')
optie = eval(input("Kies een optie:"))

# als de gebruiker een optie invoert die geen 1,2 of 3 is, word er geprint dat de invoer ongeldig is

if optie <1 or optie >3:
    print('Foutmelding:ongeldige optie')

#functie voor optie 1 die laat zien hoeveel kluizen er nog vrij zijn

if optie == 1:
    def toon_aantal_kluizen_vrij():
        infile = open('kluizen.txt','r')
        aantalRegels = infile.readlines()
        return 12-len(aantalRegels)
    print('Er zijn ',toon_aantal_kluizen_vrij(), 'kluizen vrij.')

#

if optie == 2:
    def nieuwe_kluis():

        lijst1 = []
        lijst2 = []

        #lijst met alle kluis nummers
        kluisnummer = [1,2,3,4,5,6,7,8,9,10,11,12]
        #opent het bestand waar de kluizen met codes in staan
        infile = open('kluizen.txt', 'r')
        #read is een lijst met alle regels uit bestand kluizen.txt
        read = infile.readlines()
        #in deze for loop word elk item in een nieuwe lijst gezet, met alleen het getal voor het symbool ';'
        for kluis in read:
            if kluis != '\n':
                lijst1.append(kluis.strip().split(';'))

        for kluis in lijst1:
            lijst2.append(int(kluis[0]))

        # elk item in de nieuwe lijst met alle kluizen die bezet zijn, haalt nu alle gebruikte kluizen uit de lijst
        # met alle kluizen die er zijn.
        vrijeKluizen = []
        for kluis in kluisnummer:
            if kluis not in lijst2:
                vrijeKluizen.append(kluis)
        #als de lengte van de lijst vrijeKluizen 0 is, wat dus betekent dat er geen vrije kluizen meer over zijn, word
        #er geprint dat er geen kluizen meer over zijn
        if len(vrijeKluizen) == 0:
            print('Er zijn geen kluizen meer over.')
            return 0
        return vrijeKluizen
        infile.close()



    vrijeKluizen = nieuwe_kluis()
    if len(vrijeKluizen) > 0:
            print('De kluizen', str(vrijeKluizen).strip('[').strip(']') , 'zijn bezet')
            WW = input('Voer een code in voor je nieuwe kluis:')
            print('Je hebt kluisnummer' , str(vrijeKluizen[0]), 'gekregen', 'met code:', str(WW))
            infile = open('kluizen.txt', 'a')
            infile.write('\n')
            infile.write(str(vrijeKluizen[0]))
            infile.write(';')
            infile.write(str(WW))
            infile.close()
if optie == 3:
    def kluis_openen():
        newList = []
        kluisnummer = input("Wat is je kluisnummer?")
        wachtwoord = input('Wat is je wachtwoord?')

        infile = open('kluizen.txt')
        alle_Kluizen = infile.readlines()
        infile.close()
        combinatie = kluisnummer +';' +wachtwoord
        for x in alle_Kluizen:
            newList.append(x.strip())

        if combinatie in newList:
            return print('Correcte combinatie, kluis word geopend')
        if combinatie not in newList:
            return print('Foute combinatie')
    kluis_openen()
