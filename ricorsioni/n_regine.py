import copy
class NRegine():
    def __init__(self):
        self.nchiamate = 0
        self.nsoluzioni = 0
        self.soluzioni = []

    #==============================Approccio 2================================
    #rappresentiamo soluzione con un vettore di N regine ognuno rappresentante una regina come riga e colonna
    def solve2(self, N):
        self.nchiamate = 0
        self.nsoluzioni = 0
        self.soluzioni = []
        self._ricorsione2([], N)


    #parziale è un vettore di coppie (riga e colonna)
    def _ricorsione2(self, parziale, N):
        self.nchiamate += 1
        #caso terminale
        if len(parziale)==N:
            # if self._is_soluzione(parziale): ridondante
            #     self.nsoluzioni += 1
            #     print(parziale)
            if self._is_nuova_soluzione(parziale):
                self.nsoluzioni += 1
                self.soluzioni.append(copy.deepcopy(parziale))
                print(parziale)

        #caso ricorsivo
        else:
            for riga in range(N):
                for colonna in range(N):
                    nuova_regina=[riga, colonna]
                    if self._stepIsValid(nuova_regina, parziale):
                        #aggiungo
                        parziale.append(nuova_regina)
                        #continuo ricorsione
                        self._ricorsione2(parziale, N)
                        #backtracking
                        parziale.pop()

    #funzione che controlla se la nuova reg da inserire sia ammissibile rispetto la soluz parziale costruita fin'ora
    def _stepIsValid(self, nuova_regina, parziale)->bool:
        for regina in parziale:
            if not self._is_pair_admissible(nuova_regina, regina):
                return False
        return True



    #funzione che prende due regine e restituisce True se non si possono attaccare, altrimenti False
    def _is_pair_admissible(self, regina1, regina2):
        #1: verifico la riga
        if regina1[0]==regina2[0]:
            return False
        #2: verifico la colonna
        if regina1[1]==regina2[1]:
            return False
        #3: verifico la prima diagonale
        if regina1[0]-regina1[1] == regina2[0]-regina2[1]:
            #colonna di r1 - riga di r1 ==
            #colonna di r2 - riga di r2 = stessa diagonale
            return False
        #4: verifico la seconda diagonale
        if regina1[0]+regina1[1] == regina2[0]+regina2[1]:
            # colonna di r1 + riga di r1 ==
            # colonna di r2 + riga di r2 = stessa diagonale
            return False
        #5: passati tutti i controlli return true
        else:
            return True

    #Data una possibile soluzione verifica se sia ammissibile
    def _is_soluzione(self, soluzione_possibile)->bool:
        for i in range(len(soluzione_possibile)-1):#-1 per ottimizzare e non confrontare coppie già confrontate prima
            for j in range(i+1, len(soluzione_possibile)): #i+1 per ottimizzare e non confrontare coppie già confrontate prima
                if self._is_pair_admissible(soluzione_possibile[i], soluzione_possibile[j]):
                    return False

        return True

    #confrontiamo soluzione potenziale con tutte quelle trovate se è diversa True
    def _is_nuova_soluzione(self, soluzione_potenziale)->bool:
        N = len(soluzione_potenziale)
        for soluzione in self.soluzioni:
            counter = 0
            for regina in soluzione_potenziale:
                if regina in soluzione:
                    counter += 1
            if counter == N:
                return False
        return True




if __name__ == "__main__":
    nreg = NRegine()
    nreg.solve2(4)
    print(f"Ho trovato {nreg.nsoluzioni} soluzioni.")
    print(f"Chiamate effettuate: {nreg.nchiamate}.")
    print(nreg.soluzioni)