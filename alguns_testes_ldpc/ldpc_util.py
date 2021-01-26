import numpy as np
from bitstring import BitArray, Bits


def convert_list_to_bitarray(rw):
    w = BitArray()
    for b in rw:
        w.append(Bits(uint=b, length=1))
    return w

def random_bits(K):
    import numpy as np
    rw = np.random.randint(2, size=K)
    return convert_list_to_bitarray(rw)

def add_noise(x, E):
    """
    Aplica E rasuras a x em posições aleatórias

    :param x: um BitArray de tamanho N
    :param E: o número de bits (<= N) que devem ser rasurados
    :return: um par (y, q) em que y e q são ambos BitArrays de tamanho N, com a seguinte propriedade:
    q é um BitArray aleatório com exactamente E 1's (cada 1 dá a posição de uma rasura "?")
    y é um BitArray que é igual a x nas posições em que q é 0, e é igual a 0 nas posições aonde q é 1
    """
    assert E <= len(x)

    q = [1]*E + [0] * (len(x) - E)
    np.random.shuffle(q)
    q = BitArray(q)
    y = BitArray(x)
    for i in range(len(q)):
        if q[i]:
            y[i] = False
    return (y, q)


def strnoise(K, y, q,highlight=()):
    assert len(y) == len(q)
    s = ""
    for i in range(len(y)):
        if i == 0:
            s += "\u001b[32m"
        elif i == K:
            s += "\u001b[0m|"
        if i in highlight:
            s += "\u001b[31m"
        if q[i]:
            s += "?"
        elif y[i]:
            s += "1"
        else:
            s += "0"
        if i in highlight:
            if i >= K:
                s += "\u001b[0m"
            else:
                s += "\u001b[32m"
    return s