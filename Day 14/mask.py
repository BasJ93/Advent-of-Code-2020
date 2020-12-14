import copy
from itertools import product

class Mask():
    def __init__(self, mask: str):
        self.mask = mask
        self.mutations = [str]
        self.floatingBits = [int]

    def mutate(self):
        """
        Generate all possible masks using the floating rule
        Floating bits take all possible values, therefore generating multiple masks
        """
        self.mutations = []
        self.floatingBits = [x[0] for x in enumerate(self.mask) if x[1] == "X"]
        mutations = self.mask.count("X")
        patterns = ["".join(seq) for seq in product("01", repeat=mutations)]
        for pattern in patterns:
            _mask = copy.copy(self.mask)
            for bit in enumerate([x for x in enumerate(self.mask) if x[1] == "X"]):
                _mask = _mask[:bit[1][0]] + pattern[bit[0]] + _mask[bit[1][0] + 1:]
            self.mutations.append(_mask)

    def apply(self, address, value) -> {int, str}:
        """
        For all the masks available,
        bitwise or the address and set all those addresses to the value
        floats count as an AND operation
        """
        mem = {}
        addressBin = str(bin(address))[2:].rjust(len(self.mask), "0")

        for _mask in self.mutations:
            _address = copy.copy(addressBin)
            for bit in enumerate(_mask):
                if bit[1] == "1" or bit[0] in self.floatingBits:
                    _address = _address[:bit[0]] + bit[1] + _address[bit[0] + 1:]
            mem[int(_address, 2)] = value

        return mem

    def __repr__(self):
        return f"{self.mask}"
