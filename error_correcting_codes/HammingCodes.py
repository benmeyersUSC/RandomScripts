import random

green_print = lambda x: f"\033[30;42m{x}\033[0m"
red_print = lambda x: f"\033[30;41m{x}\033[0m"
yellow_print = lambda x: f"\033[30;43m{x}\033[0m"
blue_print = lambda x: f"\033[30;44m{x}\033[0m"


def int_to_bin_list(x: int):
    if x == 0:
        return [0]

    res = []
    while x > 0:
        res.append(x % 2)
        x //= 2

    return res[::-1]


def get_poss(bits):
    print(f"\nPossible messages:")
    posss = []
    for i in range(2 ** bits)[11:12]:
        b = int_to_bin_list(i)
        while len(b) < bits:
            b.insert(0, 0)
        posss.append(b)
        print(f"{i:0{len(str(2 ** bits))}d}: {green_print("".join([str(x) for x in b]))}")
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
        pars[f"P{j}"] = {"indices": get_nums_with_one_at(j, numStuff)}

    return pars


def stuff_poss(possibilities, pars):
    parity_count = pars["count"]
    print(f"\nParity bits added:")
    j = 0
    for poss in possibilities:
        for i in range(parity_count):
            ordn = 2 ** i - 1
            pname = f"P{i + 1}"
            pars[pname]["ordn"] = ordn
            poss.insert(ordn, pname)
        print(f"{j:0{len(str(len(possibilities)))}d}: {print_hamming_code(poss)}")
        j += 1


def print_hamming_code(c):
    lc = [x for x in c]
    for i in range(len(lc)):
        if sum(int_to_bin_list(i + 1)) == 1:
            lc[i] = red_print(lc[i])
        else:
            lc[i] = green_print(lc[i])
    return "".join(lc)


def print_bit_flip(c):
    lc = [x for x in c]
    for i in range(len(lc)):
        if "y" in str(lc[i]).lower():
            lc[i] = red_print("*")
        else:
            lc[i] = green_print(" ")
    return "".join(lc)


def fill_parities(possibilities, pars):
    print(f"\nParity bits assigned:")
    pks = list(pars.keys())
    pks.remove("count")
    i = 0
    for poss in possibilities:
        for k in pks:
            # get sum
            sm = 0
            for x in pars[k]["indices"]:
                if "P" not in str(poss[x - 1]):
                    sm += poss[x - 1]
            # now change digit according
            knp = 2 ** (int(k[1:]) - 1) - 1
            if sm % 2 == 1:
                poss[knp] = 1
            else:
                poss[knp] = 0
        print(f"{i:0{len(str(len(possibilities)))}d}: {print_hamming_code(poss)}")
        i += 1


def show_random_error_correction(msgs, pars):
    msg = random.choice(msgs)
    print("\n\n-------------------------------------------------------------------------------------------")
    print(
        f"INTENDED MESSAGE: \n{green_print("".join([str(msg[a]) for a in range(len(msg)) if not ((a + 1) > 0 and ((a + 1) & a) == 0)]))}")
    print(f"\nENCODED TRANSMISSION: \n{print_hamming_code(msg)}")
    rind = random.randint(0, len(msg) - 1)
    msg[rind] = msg[rind] ^ 1
    flip_show = [str(x) for x in msg]
    flip_show[rind] += "y"

    print(f"{rind + 1}-th most significant bit ({msg[rind] ^ 1}) was flipped in transit !")
    print(f"{print_bit_flip(flip_show)}")
    print(f"{print_hamming_code(msg)}")
    print(f"{print_bit_flip(flip_show)}\n")

    pkeys = list(pars.keys())
    pkeys.remove("count")

    parity_bits_failed = []
    elmt = 0
    elmt_str = []
    for k in pkeys:
        indices = pars[k]["indices"]
        print(f"{k} bits{indices} => sum: ", end="")
        sm = 0
        for j in indices:
            sm += msg[j - 1]
        if sm % 2 != 0:
            print(red_print(sm))
            parity_bits_failed.append(k)
            ordn = int(k[1:]) - 1
            elmt += 2 ** ordn
            bnlist = [str(z) for z in int_to_bin_list(2 ** ordn)]
            elmt_str.append(f"(2**{ordn} = {green_print(2 ** ordn)} = {blue_print("".join(bnlist))})")
        else:
            print(green_print(sm))

    print(f"\nParity checks failed: \n{parity_bits_failed}")
    print(
        f"\nFLIPPED BIT: {" + ".join(elmt_str)} = {green_print(elmt)} = {blue_print("".join([str(g) for g in int_to_bin_list(elmt)]))}")

    msg[elmt - 1] = msg[elmt - 1] ^ 1
    print(f"\nCORRECTED TRANSMISSION:\n{print_hamming_code(msg)}")
    print(
        f"\nDECODED MESSAGE: \n{green_print("".join([str(msg[a]) for a in range(len(msg)) if not ((a + 1) > 0 and ((a + 1) & a) == 0)]))}")


def run_one_example(length):
    ls = [random.randint(0, 1) for _ in range(length)]
    print(f"Randomly Generated Message:\n{green_print("".join([str(x) for x in ls]))}")
    msgs = [ls]

    parities = get_pars(length)
    stuff_poss(msgs, parities)

    # properly encode Hamming Parity Bits
    fill_parities(msgs, parities)

    # now take a random possibility, mess with it, and show how to error-correct
    show_random_error_correction(msgs, parities)


def exhaustive_n_bit_hamming(n):
    possibilities = get_poss(n)
    parities = get_pars(n)
    stuff_poss(possibilities, parities)

    # properly encode Hamming Parity Bits
    fill_parities(possibilities, parities)

    # now take a random possibility, mess with it, and show how to error-correct
    show_random_error_correction(possibilities, parities)


if __name__ == "__main__":
    # exhaustive_n_bit_hamming(4)

    run_one_example(54)
