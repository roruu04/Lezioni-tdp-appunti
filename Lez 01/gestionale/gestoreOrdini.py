from collections import deque, Counter, defaultdict

from gestionale.core.clienti import Cliente, ClienteRecord
from gestionale.core.prodotti import ProdottoRecord
from gestionale.vendite.ordini import Ordine, RigaOrdine


class GestoreOrdini:
    def __init__(self):
        self._ordini_da_processare = deque()
        self._ordini_processati = []
        self._statistiche_prodotti = Counter()
        self._ordini_per_categoria = defaultdict(list)

    #aggiungere nuovo ordine da elementi da gestire
    def add_ordine(self, ordine:Ordine):
        self._ordini_da_processare.append(ordine)
        print(f"Ricevuto nuovo ordine da parte di {ordine.cliente}")
        print(f"Ordini ancora da evadere {len(self._ordini_da_processare)}")

    def processa_prossimo(self):
        print("\n" + "-" * 60)
        print("\n" + "-" * 60)
        #assicuriamoci ordine da processare esista
        if not self._ordini_da_processare:
            print("Non ci sono ordini in coda")
            return False
        ordine=self._ordini_da_processare.popleft() #fifo
        print(ordine.riepilogo())

        #aggiornare statistiche sui prodotti venduti
        for riga in ordine.righe:
            self._statistiche_prodotti[riga.prodotto.name] += riga.quantita

        #raggruppare per categoria
        self._ordini_per_categoria[ordine.cliente.categoria].append(ordine)

        #archivio
        self._ordini_processati.append(ordine)
        print("Ordine correttamente processato.")
        return True

    def processa_tutti_gli_ordini(self):
        print("\n" + "-" * 60)
        print(f"Processando {len(self._ordini_da_processare)} ordini")
        while self._ordini_da_processare:
            self.processa_prossimo()
        print("Tutti gli ordini sono stati processati.")

    def get_statistiche_prodotti(self, top_n=5):
        #restituisce info sui 5 prodotti + venduti
        valori=[]
        for prodotto, quantita in self._statistiche_prodotti.most_common(top_n):
            valori.append((prodotto, quantita))
        # potrei return(self._statistiche_prodotti.most_common(top_n)) ma è meglio di no perchè ho messo il _ a posta per non toccarla quindi nonla rendo in uscita
        return valori

    def get_distribuzione_categoria(self):
        #restituisce info sul totale fatturato per categoria
        valori = []
        for cat in self._ordini_per_categoria.keys():
            ordini =self._ordini_per_categoria[cat]
            totale_Fatturato = sum([o.totale_lordo(0.22) for o in ordini])
            valori.append((cat, totale_Fatturato))
        return valori

    def stampa_riepilogo(self):
        #stampa info di massiam
        print("Stato attuale del business")
        print(f"ordini correttamente gestiti: {len(self._ordini_processati)}")
        print(f"Ordini in coda {len(self._ordini_da_processare)}")

        print("Prodotti più venduti")
        for prod, quantita in self.get_statistiche_prodotti():
            print(f"{prod}: {quantita}")

        print("Fatturato per categoria")
        for cat, fatturato in self.get_distribuzione_categoria():
            print(f"{cat}: {fatturato}")


def test_modulo():
    sistema = GestoreOrdini()
    ordini=[
        Ordine([RigaOrdine(ProdottoRecord("Laptop", 1200.0), 1),
                RigaOrdine(ProdottoRecord("Mouse", 10.0), 3)],
               ClienteRecord("Mario Rossi", "mario@mail.it", "Gold")),
        Ordine([RigaOrdine(ProdottoRecord("Laptop", 1200.0), 1),
                RigaOrdine(ProdottoRecord("Mouse", 10.0), 2),
                RigaOrdine(ProdottoRecord("Tablet", 500.0), 1),
                RigaOrdine(ProdottoRecord("Cuffie", 250.0), 3)],
               ClienteRecord("Fulvio Bianchi", "bianchi@gmail.it", "Gold")),
        Ordine([RigaOrdine(ProdottoRecord("Laptop", 1200.0), 2),
                RigaOrdine(ProdottoRecord("Mouse", 10.0), 2)],
               ClienteRecord("Giuseppe Averta", "giuseppe.averta@polito.it", "Silver")),
        Ordine([RigaOrdine(ProdottoRecord("Tablet", 500.0), 1),
                RigaOrdine(ProdottoRecord("Cuffie", 250.0), 3)],
               ClienteRecord("Carlo Masone", "carlo@mail.it", "Gold")),
        Ordine([RigaOrdine(ProdottoRecord("Laptop", 1200.0), 1),
                RigaOrdine(ProdottoRecord("Mouse", 10.0), 3)],
               ClienteRecord("Francesca Pistilli", "francesca@gmail.it", "Gold"))
    ]
    for o in ordini:
        sistema.add_ordine(o)
    sistema.processa_tutti_gli_ordini()
    sistema.stampa_riepilogo()

if __name__ == "__main__":
    test_modulo()
