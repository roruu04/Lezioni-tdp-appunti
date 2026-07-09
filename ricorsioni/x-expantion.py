import copy


class XExpantion:
    def __init__(self):
        self.soluzioni = []
        self.soluzioni_list = []

    def calcola_list(self, input):
        self.soluzioni_list=[] #azzerare la lista per ripetere
        self._ricorsione_list([],input)
    #parziale è la soluzione parziale
    #rimanenti sono il resto dei caratteri da esaminare

    def _ricorsione_list(self, parziale:list, rimanenti:str):
        #caso terminale
        if len(rimanenti)==0:
            self.soluzioni_list.append(copy.deepcopy(parziale)) #altra lista, sennò il pop lo elimina da entrambe e perdiamo pezzi
        #caso ricorsivo
        else:
            if rimanenti[0]=="X":
                #cicliamo sugli step possibili
                for c in ['0', '1']:
                    parziale.append(c)
                    self._ricorsione_list(parziale, rimanenti[1:])
                    parziale.pop()
                # parziale.append('0')
                # self._ricorsione_list(parziale, rimanenti[1:])
                # parziale.pop()
                # parziale.append('1')
                # self._ricorsione_list(parziale, rimanenti[1:])
                # parziale.pop()
            else:
                parziale.append(rimanenti[0])
                self._ricorsione_list(parziale, rimanenti[1:])




    def calcola(self, input):
        self.soluzioni=[] #azzerare la lista per ripetere
        self._ricorsione('',input)
    #parziale è la soluzione parziale
    #rimanenti sono il resto dei caratteri da esaminare

    def _ricorsione(self, parziale:str, rimanenti:str):
        #caso terminale
        if len(rimanenti)==0:
            self.soluzioni.append(parziale)
        #caso ricorsivo
        else:
            if rimanenti[0]=="X":
                self._ricorsione(parziale+'0', rimanenti[1:])
                self._ricorsione(parziale+'1', rimanenti[1:])
            else:
                self._ricorsione(parziale+rimanenti[0], rimanenti[1:])

#==============================OPPURE=======================================#
def x_expantion2(input):
    soluzioni = []

    def ricorsione(parziale:str, rimanenti:str):
        #caso terminale
        if len(rimanenti)==0:
            soluzioni.append(parziale)
        #caso ricorsivo
        else:
            if rimanenti[0]=="X":
                ricorsione(parziale + "0", rimanenti[1:])
                ricorsione(parziale + "1", rimanenti[1:])
            else:
                ricorsione(parziale + rimanenti[0], rimanenti[1:])
    ricorsione("",input)
    return soluzioni


if __name__ == '__main__':
   sequenza = "01X0X"
   x_exp = XExpantion()

   # metodo con soluzioni parziali in stringhe
   x_exp.calcola(sequenza)
   print(x_exp.soluzioni)

   #metodo con soluzioni parziali in liste
   x_exp.calcola_list(sequenza)
   print(x_exp.soluzioni_list)


