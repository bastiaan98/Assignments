#lijst van alle stations
stations = ['Schagen', 'Heerhugowaard', 'Alkmaar', 'Castricum', 'Zaandam', 'Amsterdam Sloterdijk',
                'Amsterdam Centraal',
                'Amsterdam Amstel', 'Utrecht Centraal', '\'s-Hertogenbosch', 'Eindhoven', 'Weert', 'Roermond',
                'Sittard', 'Maastricht']
#Functie vraagt de gebruiker om het begin station, als deze niet in de lijst staat word er ongeldige invoer geprint, en
#  vervolgens de vraag opnieuw gesteld met een while loop. als een goeie invoer is ingevoerd stopt de loop.
def inlezen_beginstation(stations):
    while True:
        begin = input('Wat is je begin station?')
        if begin in stations:
            return begin
        if begin not in stations:
            print('Ongeldige invoer')
#vraagt de gebruiker om het eindstation, checkt of deze in de lijst staat en of deze hoger staat dan het begin station
# zo niet word er een foutmelding weergegeven,  de while loop zorgt ervoor dat er naar het station word gevraagd
#  totdat er een correct antwoord is gegeven
def inlezen_eindstation(stations, beginstation):
    while True:
        eind = input('Wat is je eindbestemming?')
        if eind in stations:
            if stations.index(eind) > stations.index(beginstation):
                return eind
            else:
                print('Dat station komt niet na het beginstation.')
        else:
            print('Ongeldige invoer.')
def omroepen_reis(stations, beginstation, eindstation):
    print('Het begin station',beginstation,'is het',stations.index(beginstation),'e station in het traject')
    print('Het eind station',eindstation, 'is het', stations.index(eindstation), 'e station in het traject')
    afstand = stations.index(eindstation)-stations.index(beginstation)
    print('De afstand bedraagt',afstand,'station(s)')
    prijs = afstand * 5
    print('De ritprijs is',prijs,'euro')
    print('\n')
    print('Je stapt in op:',beginstation)
    for x in range(1, stations.index(eindstation) - stations.index(beginstation)):
        print('- ' + stations[x], sep='-\n')
    print('Je stapt uit op',eindstation)






beginstation = inlezen_beginstation(stations)
eindstation  = inlezen_eindstation(stations, beginstation)
omroepen_reis(stations, beginstation, eindstation)
