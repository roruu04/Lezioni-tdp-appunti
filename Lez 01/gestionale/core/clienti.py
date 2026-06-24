from dataclasses import dataclass

categorie_valide = {"Gold", "Silver", "Bronze"}


class Cliente:
    def __init__(self, name: str, email: str, categoria: str):
        self.name = name
        self.email = email
        self._categoria = None  # presuppone getter e setter
        self.categoria = categoria

    @property
    def categoria(self):
        return self._categoria

    @categoria.setter
    def categoria(self, value):
        if value not in categorie_valide:
            raise ValueError("Categoria non valida")
        self._categoria = value

    def descrizione(self):
        return f"Cliente {self.name} {self._categoria}- Email: {self.email}"


@dataclass
class ClienteRecord:
    name: str
    email: str
    categoria: str


def _test_modulo():
    print("Sto testando il modulo clienti.py")
    c1 = Cliente(name="Mario Bianchi", email="mario.bianchi@polito.it", categoria="Gold")
    # c2 = Cliente(name="Carlo Masone", email="carlo.masone@polito.it", categoria="Platinum") #lancio un'eccezione perchè la categoria non è valida
    print(
        c1.descrizione())  # metodo dell'istanza lo chiamiamo come nome.metodo() metre il metodo di classe lo chiamiamo come nome_classe.metodo() e il metodo statico lo chiamiamo come nome_classe.metodo()


if __name__ == "__main__":
    _test_modulo()