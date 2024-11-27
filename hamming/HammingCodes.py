"""
4-Data bit messages with Hamming codes

Parity bits at powers of 2 (1, 2, 4), so only 3 needed for a 4 bit message
"""

green_print = lambda x: f"\033[30;42m{x}\033[0m"
red_print = lambda x: f"\033[30;41m{x}\033[0m"


def int_to_bin_list(x: int):
    if x == 0:
        return [0]

    res = []
    while x > 0:
        # res = str(x % 2) + res
        res.append(x % 2)
        x //= 2

    return res[::-1]


def get_poss(bits):
    posss = []
    for i in range(2 ** bits):
        b = int_to_bin_list(i)
        while len(b) < bits:
            b.insert(0, 0)
        posss.append(b)
    return posss


def get_nums_with_one_at(i, rng):
    r = []
    for j in range(i, rng + 1):
        bn = int_to_bin_list(j)
        lbn = len(bn)
        if i <= lbn:
            if bn[lbn - i] == 1:
                r.append(j)

    return r


def get_pars(bits):
    i = 0
    numStuff = bits

    while 2 ** i <= numStuff:
        i += 1
        numStuff += 1

    pars = {"count": i}

    for j in range(1, i + 1):
        pars[f"P{j}"] = get_nums_with_one_at(j, numStuff)

    return pars


def stuff_poss(possibilities, parity_count):
    for poss in possibilities:
        for i in range(parity_count):
            poss.insert(2 ** i - 1, f"P{i + 1}")
        print_hamming_code(poss)
    # return possibilities


def print_hamming_code(c):
    lc = [x for x in c]
    for i in range(len(lc)):
        if sum(int_to_bin_list(i + 1)) == 1:
            lc[i] = red_print(lc[i])
        else:
            lc[i] = green_print(lc[i])
    print("".join(lc))


def fill_parities(possibilities, pars):
    pks = list(pars.keys())
    pks.remove("count")
    for poss in possibilities:
        for k in pks:
            # get sum
            sm = 0
            for x in pars[k]:
                if "P" not in str(poss[x - 1]):
                    sm += poss[x - 1]
            # now change digit according
            knp = 2 ** (int(k[1:]) - 1) - 1
            if sm % 2 == 1:
                poss[knp] = 1
            else:
                poss[knp] = 0
        print_hamming_code(poss)


def NbitHamming(n):
    possibilities = get_poss(n)
    parities = get_pars(n)
    stuff_poss(possibilities, parities["count"])

    fill_parities(possibilities, parities)


if __name__ == "__main__":
    NbitHamming(8)

