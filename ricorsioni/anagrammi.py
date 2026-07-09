import copy
from functools import lru_cache


def anagrammi(parola):
    soluzioni=[]
    ricorsione([], parola, soluzioni)
    return soluzioni

def ricorsione(parziale:list,rimanenti:str, soluzioni:list)->list:
    #caso terminale
    if len(rimanenti)==0:
        soluzioni.append(copy.deepcopy(parziale))

    #caso ricorsivo
    else:
        for i in range(len(rimanenti)):
            parziale.append(rimanenti[i])
            nuovi_rimanenti = rimanenti[:i]+rimanenti[i+1:]
            ricorsione(parziale, nuovi_rimanenti, soluzioni)
            parziale.pop()

#con il set non ho ripetizioni
def anagrammi_str(parola):
    soluzioni=set()
    ricorsione_str('', parola, soluzioni)
    return soluzioni

#@lru_cache(maxsize=None) non si può perchè set non è hashable
def ricorsione_str(parziale:str,rimanenti:str, soluzioni:set):
    #caso terminale
    if len(rimanenti)==0:
        soluzioni.add(copy.deepcopy(parziale))

    #caso ricorsivo
    else:
        for i in range(len(rimanenti)):
            nuovi_rimanenti = rimanenti[:i]+rimanenti[i+1:]
            ricorsione_str(parziale+rimanenti[i], nuovi_rimanenti, soluzioni)

#non le salvo, le stampo
def anagrammi_str2(parola):
    ricorsione_str2('', parola)

@lru_cache(maxsize=None)#con la cache stampa una copia, senza stampa tutto senza tenere conto se siano doppioni
def ricorsione_str2(parziale:str,rimanenti:str):
    #caso terminale
    if len(rimanenti)==0:
        print(parziale)

    #caso ricorsivo
    else:
        for i in range(len(rimanenti)):
            nuovi_rimanenti = rimanenti[:i]+rimanenti[i+1:]
            ricorsione_str2(parziale+rimanenti[i], nuovi_rimanenti)


if __name__=="__main__":
    #print(anagrammi('casa'))
    #print(anagrammi_str('casa'))
    print(anagrammi_str2('aaaa'))