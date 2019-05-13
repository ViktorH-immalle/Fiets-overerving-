class Voertuig:
    def __init__(self, aantalWielen, kleur):
        self.aantalWielen = aantalWielen
        self.kleur = kleur
        self.rijdend = False
    

    def ride(self):
        if self.rijdend == False:
            self.rijdend = True
            print('Gas op die lolly!')
        else:
            print('Je voertuig is al aan het rijden.')

    def stop(self):
        if self.rijdend == True:
            self.rijdend = False
            print('De bestuurder smijd alles dicht!')
        else:
            print('Je staat stil, remmen heeft niet veel nut')
    
    def paint(self, kleur):
        self.kleur = kleur
        


class Auto(Voertuig):
    def __init__(self):
        Voertuig.__init__(self, 4, 'geel')    



class Fiets(Voertuig):
    def __init__(self):
        Voertuig.__init__(self, 2, 'zilver')

    def stop(self):
        if self.rijdend == False:
            self.rijdend = True
            print('Trappen trappen!')
        else:
            print('Je staat stil!')


if __name__ == "__main__":
    auto1 = Auto()

    print(auto1.kleur)
    auto1.ride()

    fiets1 = Fiets()
    fiets1.ride()
    fiets1.stop()
    fiets1.stop()
    