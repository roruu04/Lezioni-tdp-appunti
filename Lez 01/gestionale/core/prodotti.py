from dataclasses import dataclass


class Prodotto:
    aliquota_iva = 0.22  # variabile di classe, è condivisa da tutte le istanze della classe Prodotto, non è necessario specificarla per ogni istanza, è sufficiente specificarla una volta sola a livello di classe

    def __init__(self, name: str, price: float, quantity: int, supplier=None):
        self.name = name
        self._price = None
        self.price = price
        self.quantity = quantity
        self.supplier = supplier  # se non specifico il supplier, di default è None

    def valore(self):
        return self._price * self.quantity

    def valore_lordo(self):
        netto = self.price * self.quantity
        lordo = netto * (
                    1 + Prodotto.aliquota_iva)  # posso accedere alla variabile di classe anche attraverso il nome della classe, non è necessario specificare l'istanza
        return lordo  # posso accedere alla variabile di classe anche attraverso il nome della classe, non è necessario specificare l'istanza

    # costruttore alternativo, è un metodo di classe che permette di creare un'istanza della classe in modo diverso rispetto al costruttore standard, in questo caso permette di creare un'istanza della classe Prodotto con una quantità di 1, senza dover specificare la quantità come parametro
    @classmethod  # decoratore che indica che il metodo è un metodo di classe, non è necessario specificare l'istanza come primo parametro, ma è necessario specificare la classe come primo parametro
    def costruttore_con_quantita_uno(cls, name: str, price: float,
                                     supplier: str):  # il primo parametro è la classe, non è necessario specificare l'istanza come primo parametro, ma è necessario specificare la classe come primo parametro
        return cls(name, price, 1,
                   supplier)  # posso accedere alla variabile di classe anche attraverso il nome della classe, non è necessario specificare l'istanza

    # metodo statico, è un metodo che non ha accesso alla classe o all'istanza, è un metodo che può essere chiamato senza dover creare un'istanza della classe, è un metodo che può essere chiamato direttamente sulla classe, non è necessario specificare l'istanza come primo parametro, ma è necessario specificare la classe come primo parametro
    @staticmethod  # decoratore che indica che il metodo è un metodo statico, non è necessario specificare l'istanza come primo parametro, ma è necessario specificare la classe come primo parametro
    def applica_sconto(prezzo: float,
                       sconto: float):  # essendo un metodo statico non devo passare cls o self come primo parametro, ma è necessario specificare la classe come primo parametro
        return prezzo * (
                    1 - sconto)  # posso accedere alla variabile di classe anche attraverso il nome della classe, non è necessario specificare l'istanza

    # tutto ciò ha senso se voglio fare dei controlli
    @property
    def price(self):  # getter
        return self._price

    @price.setter  # SOLO SE HO GIà DEFINITO UN GETTER POSSO FARE IL SETTER
    def price(self, value):
        if value < 0:
            raise ValueError("Il prezzo non può essere negativo")
        self._price = value

    def __str__(self):
        return f"{self.name} - disponibili {self.quantity} pezzi a {self.price}$"

    def __repr__(self):
        return f"PRodotto(name={self.name}, prize = {self.price}, quantity={self.quantity}, supplier={self.supplier})"

    def __eq__(self, other: object):
        if not isinstance(other, Prodotto):
            return NotImplemented
        return (self.name == other.name
                and self.price == other.price
                and self.quantity == other.quantity
                and self.supplier == other.supplier)

    def __lt__(self, other: "Prodotto") -> bool:
        return self.price < other.price

    def prezzo_finale(self) -> float:
        return self.price * (1 + self.aliquota_iva)


class ProdottoScontato(Prodotto):
    def __init__(self, name: str, price: float, quantity: int, supplier: str, sconto_percento: float):
        super().__init__(name, price, quantity, supplier)
        self.sconto_percento = sconto_percento

    def prezzo_finale(self) -> float:
        return self.valore_lordo() * (1 - self.sconto_percento / 100)


class Servizio(Prodotto):
    def __init__(self, name: str, tariffa_oraria: float, ore: int):
        super().__init__(name=name, price=tariffa_oraria, quantity=1, supplier=None)
        self.ore = ore

    def prezzo_finale(self) -> float:
        return self.price * self.ore


class Abbonamento:
    def __init__(self, nome: str, prezzo_mensile: float, mesi: int):
        self.name = nome
        self.prezzo_mensile = prezzo_mensile
        self.mesi = mesi

    def prezzo_finale(self) -> float:
        return (self.prezzo_mensile * self.mesi)


@dataclass
class ProdottoRecord:
    name: str
    prezzo_unitario: float


MAX_QUANTITA = 1000


def crea_prodotto_standard(nome: str, prezzo: float):
    return Prodotto(nome, prezzo, quantity=1, supplier=None)


def _test_modulo():
    print("Sto testando il modulo prodotti.py")
    myproduct1 = Prodotto(name="Laptop", price=1200.0, quantity=12,
                          supplier="ABC")  # se non specifichiamo la categoria dobbiamo ricordarci l'ordine dei parametri, altrimenti dobbiamo specificare i nomi dei parametri
    print(f"Nome prodotto:{myproduct1.name} - Prezzo prodotto:{myproduct1.price}")
    print(f"Il totale lordo di myproduct1 è {myproduct1.valore_lordo()}")
    p3 = Prodotto.costruttore_con_quantita_uno(name="Auricolari", price=200.0,
                                               supplier="ABC")  # posso chiamare il metodo di classe direttamente sulla classe, non è necessario creare un'istanza della classe
    print(
        f"Prezzo scontato di myproduct1 {Prodotto.applica_sconto(myproduct1.price, 0.15)}")  # posso chiamare il metodo statico direttamente sulla classe, non è necessario creare un'istanza della classe
    myproduct2 = Prodotto(name="Mouse", price=10.0, quantity=25, supplier="CDE")
    print(f"Nome prodotto:{myproduct2.name} - prezzo: {myproduct2.price}")

    print(f"Valore lordo di myproduct1: {myproduct1.valore_lordo()}")
    Prodotto.aliquota_iva = 0.24  # non ho modificato l'istanza ma il parametro della classe, si riperquote su tutte le istanze
    print(f"Valore lordo di myproduct1: {myproduct1.valore_lordo()}")
    # come le proteggo quindi?
    # mettendo un _ davanti al nome della variabile la rendo privata
    # mettendo __ davanti al nome della variabile la rendo privata e non accessibile dall'esterno della classe
    # ---> l'opzione migliore è mettere un solo _ e poi usare come "getter e setter" di java che in py sono costrutti di property

    print(myproduct1)

    p_a = Prodotto(name="Laptop", price=1200.0, quantity=12, supplier="ABC")
    p_b = Prodotto(name="Mouse", price=10, quantity=14, supplier="CDE")

    print("myproduct1 == p_a?", myproduct1 == p_a)
    print("p_a == p_b?", p_a == p_b)

    mylist = [p_a, p_b, myproduct1]
    mylist.sort()

    print("lista prodotti ordinata")
    for p in mylist:
        print(f"-{p}")


if __name__ == "__main__":
    _test_modulo()
