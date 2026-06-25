import copy
from collections import deque
from email.policy import default
from typing import Counter

from gestionale.core.clienti import ClienteRecord
from gestionale.core.prodotti import ProdottoRecord
from gestionale.vendite.ordini import Ordine, RigaOrdine

p1 = ProdottoRecord("Laptop", 1200.0)
p2 = ProdottoRecord("Mouse", 20.0)
p3 = ProdottoRecord("Auricolari", 250.0)

carrello = [p1, p2, p3, ProdottoRecord("Tablet", 700.0)]
print("Prodotti nel carrello")
for i, p in  enumerate(carrello):
    print(f"{i+1}) {p.name} - {p.prezzo_unitario}")

#aggiungere a una lista
carrello.append(ProdottoRecord("Monitor", 150.0))
carrello.sort(key=lambda x: x.prezzo_unitario)

print("Prodotti nel carrello")
for i, p in enumerate(carrello):
    print(f"{i+1}) {p.name} - {p.prezzo_unitario}")

tot = sum(p.prezzo_unitario for p in carrello)
print(f"Totale del carrello: {tot}")

#aggiungere
carrello.append(ProdottoRecord("Propdo", 100.0))
carrello.extend([ProdottoRecord("aaa", 100.0)])
#carrello.insert(2, ProdottoRecord("ccc", 100.0))

#rimuovere
#carrello.pop() #rimuove l'ultimo elemento
#carrello.pop(2) #rimuove in posizione 2
carrello.remove(p1) #rimuove alla prima occorrenza di p1
#carrello.clear() #rimuove tutti gli elementi

#sorting
#carrello.sort() #ordina seguendo ordinamento naturale -- non funziona se gli oggetti contenuti non definiscono un ordinamento naturale
#carrello.sort(reverse=True) #ordina al contrario
#carrello.sort(key = function)
#carrello_ordinato = sorted(carrello)

#copio
#carrello.reverse() #inverte l'ordine degli elementi
#carrello_copia = carrello.copy() #shallow copy gli oggetti sono gli stessi identici, se apporto modifiche si modificano entrambi
#carrello_copia2 = copy.deepcopy(carrello) #deep copy, copio anche il contenuto degli oggetti, quindi gli oggetti saranno diversi

#Tuple
sede_principale = (45, 8) #latitudine, longitudine
sede_milano = (45, 9) #lat e long della sede Milano

print(f"Sede principale lat: {sede_principale[0]}, long: {sede_principale[1]}")

#tupla di tuple
AliquoteIVA = (
    ("Standard", 0.22),
    ("Ridotta", 0.10),
    ("Alimentari", 0.04),
    ("Esente", 0.0)
)

for descr, valore in AliquoteIVA:
    print(f"{descr}: {valore*100}%")

    if descr == "Esente":
        break

def calcola_statistiche_carrello(carrello):
    """Restituisce prezzo totale, prezzo medio, massimo e minimo"""
    prezzi = [p.prezzo_unitario for p in carrello]
    return sum(prezzi), sum(prezzi) / len(prezzi), max(prezzi), min(prezzi)

tot, media, max, min = calcola_statistiche_carrello(carrello)
#tot, *altri_campi = calcola_statistiche_carrello(carrello)
print(tot)

#SET
categorie = {"Gold", "Silver", "Bronze", "Gold"}
print(categorie) #non vengono stampati i duplicati
print(len(categorie)) #3
categorie2 = {"Platinum", "Elite", "Gold"}
#categorie_all = categorie.union(categorie2) #unione di due set
categorie_all = categorie | categorie2 #unione di due set (uguale a quello sopra)
print(categorie_all)

categorie_comuni = categorie & categorie2 #intersezione di due set
print(categorie_comuni)

categorie_esclusive = categorie - categorie2 #elementi presenti in un set ma non nell'altro
print(categorie_esclusive)
categorie_esclusive_simmetriche = categorie ^ categorie2 #elementi presenti in un set o nell'altro, ma non in entrambi
print(categorie_esclusive_simmetriche)

prodotti_ordine_A = {ProdottoRecord("Laptop", 1200.0),
                    ProdottoRecord("Mouse", 20.0),
                    ProdottoRecord("Tablet", 700.0)}

prodotti_ordine_B = {ProdottoRecord("Laptop2", 1200.0),
                    ProdottoRecord("Mouse2", 20.0),
                    ProdottoRecord("Tablet2", 700.0)}

#Metodi utili per i set
s = set() #crea un set vuoto
s1 = set()

s.add(ProdottoRecord("aaa", 20.0)) #aggiunge un elemento al set
s.update([ProdottoRecord("aaa", 20.0), ProdottoRecord("bbb", 20.0)]) #aggiunge più elementi al set
s.remove(ProdottoRecord("aaa", 20.0)) #rimuove un elemento dal set, se non esiste solleva un errore KeyError (lo stesso errore del dizionario)
s.discard(ProdottoRecord("aaa", 20.0)) #rimuove un elemento dal set, se non esiste non solleva errori
s.pop() #rimuove un elemento a caso dal set e lo restituisce, se il set è vuoto solleva un errore KeyError
s.clear() #rimuove tutti gli elementi dal set

#operazioni insiemistiche
s.union(s1) #s|s1 genera un set che unisce i due set di partenza
s.intersection(s1) #s&s1 genera un set con gli elementi comuni ai due set di partenza
s.difference(s1) #s-s1 genera un set con gli elementi presenti in s ma non in s1
s.symmetric_difference(s1) #s^s1 genera un set con gli elementi presenti in s o in s1 ma non in entrambi

s1.issubset(s) #s1 <= s restituisce True se s1 è un sottoinsieme di s
s1.issuperset(s) #s1 >= s restituisce True se s1 è un soprainsieme di s
s1.isdisjoint(s) #s1.isdisjoint(s) restituisce True se s1 e s non hanno elementi in comune

#Dictionary
catalogo = {
    "LAP001 ": ProdottoRecord("Laptop", 1200.0),
    "LAP002": ProdottoRecord("Laptop Pro", 2300.0),
    "MAU001": ProdottoRecord("Mouse", 20.0),
    "AUR001": ProdottoRecord("Auricolari", 250.0)
}

cod = "LAP002"
prod =catalogo[cod] #accedo al prodotto con chiave cod
print(f"Il prodotto con codice {cod} è {prod.name} al prezzo di {prod.prezzo_unitario}")
#print(f"Cerco un altro oggetto: {catalogo["Non esiste"]}") #solleva un errore KeyError
prod1 = catalogo.get("Non esiste") #restituisce None se la chiave non esiste
if prod1 is None:
    print("Prodotto non trovato")
prod2 = catalogo.get("NonEsiste2", ProdottoRecord("Sconosciuto", 0.0)) #restituisce un prodotto di default se la chiave non esiste
print(prod2)
keys = catalogo.keys() #restituisce una vista delle chiavi del dizionario
values = catalogo.values() #restituisce una vista dei valori del dizionario
keys = list(catalogo.keys()) #restituisce una lista delle chiavi del dizionario
values = list(catalogo.values()) #restituisce una lista dei valori del dizionario

for k in keys:
    print(k)
for v in values:
    print(v)

for key, value in catalogo.items(): #restituisce una vista di coppie chiave-valore del dizionario
    print(f"Chiave: {key}, Valore: {value}")

rimosso = catalogo.pop("LAP002") #rimuove l'elemento con chiave "LAP001" e lo restituisce, se la chiave non esiste solleva un errore KeyError
print(f"Rimosso: {rimosso}")

#deep comprehesion
prezzi={codice: prod.prezzo_unitario for codice, prod in catalogo.items()} #dizionario con chiave codice prodotto e valore prezzo unitario

#v = d[keys] #leggere
#d[keys] = v #scrivere
#v = d.get(keys, default) #legge senza rischiare un errore se la chiave non esiste, restituisce default
#d.pop() #rimuove e restituisce un elemento a caso del dizionario, se il dizionario è vuoto solleva un errore KeyError
#d.clear() #rimuove tutti gli elementi del dizionario
#d.keys() #restituisce una vista delle chiavi del dizionario
#d.values() #restituisce una vista dei valori del dizionario
#d.items() #restituisce una vista di coppie chiave-valore del dizionario
#key in d #restituisce True se la chiave è presente nel dizionario, False altrimenti

"""Esercizio live
Per ciascuno dei seguenti casi, decidere quale struttura usare: """

"""1) Memorizzare un elenco di ordini che dovranno poi essere processati in ordine di arrivo."""
ordini_da_processare = [] #lista
o1 = Ordine([], ClienteRecord("Mario Rossi", "mario@polito.it", "Gold"))
o2 = Ordine([], ClienteRecord("Mario Bianchi", "bianchi@polito.it", "Silver"))
o3 = Ordine([], ClienteRecord("Fulvio Rossi", "fulvio@polito.it", "Bronze"))
o4 = Ordine([], ClienteRecord("Carlo Masone", "carlo@polito.it", "Gold"))

ordini_da_processare.append((o1, 0))
ordini_da_processare.append((o2, 10))
ordini_da_processare.append((o3, 3))
ordini_da_processare.append((o4, 45))

"""2) Memorizzare i CF dei clienti (univoco)"""
cf_clienti = {"yhrbgtf55435", "yhrbgtf55436", "yhrbgtf55437", "yhrbgtf55435"} #set
print(cf_clienti) #non vengono stampati i duplicati

"""3) Creare un database di prodotti che possa cercare con un codice univoco"""
listino_prodotti = {
    "LAP001 ": ProdottoRecord("Laptop", 1200.0),
    "KEY001": ProdottoRecord("Keyboard", 20.0),
} #dizionario

"""4) Memorizzare le coordinate gps della nuova sede di Roma"""
magazzino_roma = (45, 6) #tupla

"""5) Tenere traccia delle categorie di clienti che hanno fatto un ordine in un certo range temporale"""
#ha più senso sia un set perchè le categorie sono univoche, ma va bene anche la lista
categorie_periodo = set()
categorie_periodo.add("Gold")
categorie_periodo.add("Bronze")

print("==========================================================================")


#counter
lista_clienti = [
    ClienteRecord("Mario Rossi", "mario@polito.it", "Gold"),
    ClienteRecord("Mario Bianchi", "bianchi@polito.it", "Silver"),
    ClienteRecord("Fulvio Rossi", "fulvio@polito.it", "Bronze"),
    ClienteRecord("Carlo Masone", "carlo@polito.it", "Gold"),
    ClienteRecord("Mario Bianchi", "mario@polito.it", "Gold"),
    ClienteRecord("Giuseppe Averta", "bianchi@polito.it", "Silver"),
    ClienteRecord("Francesca Pistilli", "fulvio@polito.it", "Bronze"),
    ClienteRecord("Carlo Masone", "carlo@polito.it", "Gold"),
    ClienteRecord("Fulvio Corno", "carlo@polito.it", "Silver")
]

categorie = [c.categoria for c in lista_clienti]
categorie_counter = Counter(categorie)
print(f"Distribuzione categorie clienti: {categorie_counter}") #fa tutto da solo Counter top
print(f"Categoria più frequente: {categorie_counter.most_common(2)}") #il numero serve a dire quante deve prenderne
print(f"Totale: {categorie_counter.total()}")

vendite_gennaio = Counter(
    {"Laptop": 13, "Tablet": 15}
)

vendite_febbraio = Counter(
    {"Laptop": 3, "Stampante": 1}
)
vendite_bimestre = vendite_gennaio + vendite_febbraio #aggregare info

print(f"Vendite gennaio: {vendite_gennaio}")
print(f"Vendite febbraio: {vendite_febbraio}")
print(f"Vendite bimestre: {vendite_bimestre}")

print(f"Differenza di vendite: {vendite_gennaio - vendite_febbraio}")

#modificare un counter in the fly
vendite_gennaio["Laptop"] += 4
print(f"Vendite gennaio aggiornate: {vendite_gennaio}")
#DA RICORDARE
#c.most_common(n) #restituisce gli n elementi più comuni del counter, restituisce una lista di tuple (elemento, conteggio)
#c.total() #restituisce il totale dei conteggi del counter

#Deque
print("=================DEQUE================")
coda_ordini = deque()

for i in range(1, 10):
    cliente = ClienteRecord(f"Cliente {i}", f"cliente{i}@polito.it", "Gold")
    prodotto = ProdottoRecord(f"Prodotto{i}", 100.0*i)
    ordine = Ordine([RigaOrdine(prodotto, 1)], cliente)
    coda_ordini.append(ordine)
print(f"Ordini in coda: {len(coda_ordini)}")

while coda_ordini:
    ordine_corrente = coda_ordini.popleft()
    print(f"Sto gestendo l'ordine del cliente: {ordine_corrente.cliente}")
print("Ho processato tutti gli ordini!")

