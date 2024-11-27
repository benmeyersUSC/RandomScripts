

N = 243000000
F = "(-Ez) ( P( z,Q( y,ssss,,,,,,,,,sssss0,y ) ) )"
# F = "(Ex) (x = sss0 * y)"


def nth_prime(n):
    def is_prime(num):
        if num < 2:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True

    count = 0
    num = 2
    while count < n:
        if is_prime(num):
            count += 1
        if count == n:
            return num
        num += 1


def godelize(formula: str) -> int:

    mapping_dict = {
        "-": 1, "|": 2, "@": 3, "E": 4, "=": 5, "0": 6, "s": 7, "(": 8, ")": 9, ",": 10, "+": 11, "*": 12,
        "x": 13, "y": 17, "z": 19, "p": 367, "q": 373, "r": 379, "P": 383, "Q": 389, "R": 397
    }

    godel_number = 1
    for i in range(len(formula)):
        if formula[i] == ' ':
            i += 1
        else:
            godel_number *= nth_prime(i + 1) ** mapping_dict[formula[i]]
    # print(f"GODEL NUM: {godel_number}")
    return godel_number


def formulize(godel_number: int) -> str:

    reversed_mapping_dict = {
        1: "-", 2: "|", 3: "@", 4: "E", 5: "=", 6: "0", 7: "s", 8: "(", 9: ")", 10: ",", 11: "+", 12: "*",
        13: "x", 17: "y", 19: "z", 367: "p", 373: "q", 379: "r", 383: "P", 389: "Q", 397: "R"
    }

    formula = ""
    prime_i = 1

    while godel_number > 1:
        prime = nth_prime(prime_i)
        exponent = 0

        while godel_number % prime == 0:
            godel_number //= prime
            exponent += 1

        if exponent > 0:
            formula += reversed_mapping_dict[exponent]

        prime_i += 1

    return formula


# Test the functions
print(f"Formula: {F}")
encoded = godelize(F)
print(f"Encoded: {encoded}")
decoded = formulize(encoded)
print(f"Decoded: {decoded}")

theorems = ["0Es",
"-(0=s0)",
"(x)(y)(sx=sy@x=y)",
"(x)-(sx=0)",
"(P)((P0@(x)(Px@Psx))@(x)Px)",
"(x)(y)(x=y@y=x)",
"(x)(y)(z)((x=y@y=z)@x=z)",
"(x)(y)(x=y@sx=sy)",
"(x)(y)(x=y@(Px@Py))",
"(x)(x+0=x)",
"(x)(y)(x+sy=s(x+y))",
"(x)(y)(x+y=y+x)",
"(x)(y)(z)((x+y)+z=x+(y+z))",
"(x)(x*0=0)",
"(x)(y)(x*sy=(x*y)+x)",
"(x)(y)(x*y=y*x)",
"(x)(y)(z)((x*y)*z=x*(y*z))",
"(x)(y)(z)(x*(y+z)=(x*y)+(x*z))",
"(x)(y)(Ex)(x=sy|y=sx)",
"(x)(y)(z)((x+z=y+z)@x=y)",
"(x)(y)(z)((x*z=y*z@-(z=0))@x=y)",
"(x)(y)(z)((x|y@x|z)@x|(y+z))",
"(x)(y)(z)((x|y@x|z)@x|(y*z))",
"(x)(y)((x|y@y|x)@x=y)",
"(x)(Ex)(y)(x=y*y)",
"(x)(y)((x|y@y|x)@(x=y|x=-y))",
"(P)(Ex)(Px@(y)(Py@x=y))",
"(x)(y)(z)((x=y+z)@(z=x-y))",
"(x)(y)(z)(((x=y@y=z)|x=z)@x=z)",
"(x)(y)(x+y=0@(x=0@y=0))",
"(x)(y)(x*y=0@(x=0|y=0))",
"(x)(y)(z)((x+y=x+z)@y=z)",
"(x)(y)(z)((x*y=x*z@-(x=0))@y=z)",
"(x)(y)(z)(x*(y+z)=(x*y)+(x*z))",
"(x)(y)(z)((x+y)*z=(x*z)+(y*z))",
"(x)(y)((x+y)*(x-y)=(x*x)-(y*y))",
"(x)(y)(z)((x*x)+(y*y)=(z*z)@(Ex)(Ey)(Ez)(x*x)+(y*y)=(z*z))"]

for x in theorems:
    G = godelize(x)
    G = str(G)[0] + ''.join([str(G)[i] if (i % 81 != 0) else (str(G)[i]+"\n") for i in range(1, len(str(G)))])
    print(f"Formula: {x}:\n{G}\n")