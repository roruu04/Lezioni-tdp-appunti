from gestionale.core.prodotti import Prodotto, \
    crea_prodotto_standard  # oppure crea_prodotto_standard as cps oppure import prodotti (as p) e accedo col punto
from gestionale.core.clienti import Cliente
from gestionale.core.clienti import ClienteRecord
from gestionale.core.prodotti import ProdottoRecord
from gestionale.vendite.ordini import RigaOrdine, Ordine, OrdineConSconto

print("=============================================")
p1 = Prodotto("Ebook Reader", 120.0, 1, "AAA")
p2 = crea_prodotto_standard(nome="Tablet", prezzo=750.0)
print(p1)
print(p2)
print("=============================================")
c1 = Cliente("Mario Rossi", "mail@mail.com", "Gold")

print("-----------------------Dataclass---------------------------------------")

Cliente1 = ClienteRecord("Mario Rossi", "mariorossi@example.com", "Gold")
p1 = ProdottoRecord("Laptop", 1200.0)
p2 = ProdottoRecord("Mouse", 20.0)

ordine = Ordine([RigaOrdine(p1, 2), RigaOrdine(p2, 10)], Cliente1)
ordine_scontato = OrdineConSconto([RigaOrdine(p1, 2), RigaOrdine(p2, 10)], Cliente1, 0.1)

print(ordine)  # mi scrive già un repr
print("Numero di righe nell'ordine: ", ordine.numero_righe())
print("Totale netto: ", ordine.totale_netto())
print("Totale lordo (IVA 22%): ", ordine.totale_lordo(0.22))

print(ordine_scontato)
print("Totale netto sconto:", ordine_scontato.totale_netto())
print("Totale lordo sconto (IVA 22%): ", ordine_scontato.totale_lordo(0.22))
print("--------------------------------------------------------------")

