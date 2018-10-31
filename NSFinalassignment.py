def standaardprijs(afstandKM):
    afstandKM2 = afstandKM * 0.8
    if afstandKM > 50:
        afstandKM2 = (afstandKM * 0.6) +15
    if afstandKM <1:
        afstandKM2 = 0
    return afstandKM2

def ritprijs(leeftijd,weekendrit,afstandKM):
    ''
    afstandKM2 = standaardprijs(afstandKM)
    if leeftijd >= 65 or leeftijd < 12:
        if weekendrit == True:
            return standaardprijs(afstandKM) * 0.65
        else:
            return standaardprijs(afstandKM) * 0.70
    else:
        if weekendrit == True:
            return standaardprijs(afstandKM) * 0.60
    return standaardprijs(afstandKM)


print(ritprijs(11,False,55))