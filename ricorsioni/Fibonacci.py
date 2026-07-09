from functools import lru_cache


class Fibonacci:
    def __init__(self):
        self.cache = {0: 0, 1: 1}
        self.ricorsioni = 0
        self.ricorsioni_cache = 0

    # MEMOIZATION
    @lru_cache(maxsize=None)
    def calcola_elemento_cache_lru(self, n):
        # se ho già la soluzione per questo n la prendo da cache non la ricalcolo
        if self.cache.get(n) is not None:
            return self.cache[n]
        # altrimenti devo andare avanti con la ricorsione
        else:
            self.ricorsioni_cache += 1
            self.cache[n] = (self.calcola_elemento_cache_lru(n - 1) + self.calcola_elemento_cache_lru(n - 2))
            return self.cache[n]

    def calcola_elemento(self, n):  # ci mette meno trovandolo nella cache in termini di tempo è meglio
        # terminale
        if n == 0:
            return 0
        elif n == 1:
            return 1
        # non terminale
        else:
            self.ricorsioni += 1
            return self.calcola_elemento(n - 1) + self.calcola_elemento(n - 2)


if __name__ == '__main__':
    N = 10
    fib = Fibonacci()
    print(fib.calcola_elemento(N))
    print(fib.ricorsioni)
    print(fib.calcola_elemento_cache_lru(N))
    print(fib.ricorsioni_cache)