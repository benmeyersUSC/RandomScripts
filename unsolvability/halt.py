

def HALT(P, i):
    """
    Basic halting function to determine whether P halts on i
    :param P: some program's source code
    :param i: some input to a program
    :return: if P(i) halts, return True, else, return False
    """
    return P(i) halts

def G(P):
    """
    Pathological function to highlight the contradiction HALT creates
    :param P: some program's source code
    :return: whatever HALT(P, P) says, do the opposite

    Suppose HALT(P, P) is True
        then P halts on P and G will thus run forever
    Suppose HALT(P, P) is False
        then P runs forever on P and G will thus halt

    what about G(G)...?

    if HALT(G, G)
        then G (of G !) runs forever, contradicting what HALT just said about G(G)
    if not HALT(G, G)
        then G (of G !) must halt, contradicting what HALT just said about G(G)

    HALT inevitably invites contradiction
    """
    if HALT(P, P):
        time.sleep(infinity)
    return

def T(P):
    """
    Totality halting function to determine behavior for all inputs
    :param P: some program's source code
    :return: if P halts on all inputs, return True, but if at least one runs forever, return False

    this function can also be disproven by showing how it allows us to construct the impossible HALT
    """
    return P(i) halts for i in range(infinity)

def newHALT(P, i):
    """
    HALT which we can build if T(P) is possible
    :param P: some program's source code
    :param i: some input to a program
    :return: if P(i) halts, return True, else, return False

    how does this work?

    we want to know if P(i) halts, but all we have is the ability to talk about ALL inputs
        it would not suffice to say if T(P) is true, then HALT(P, i) is True (well that does, but....)
        if T(P) is not true, we have no way to know if i was the input that runs forever

    so we make a new function...
    if x is not i, then we halt immediately (this gets us close to reducing our problem...)
    if x is i, then we let P run on i

    thus, T(new function) will only return False if P(i) runs forever!

    new function de-totalizes the problem by cancelling out all inputs but i
    """
    def fn(x):
        if x == i:
            return P(i)
        return
    return T(fn)



"""
ASSUME HALT(P, i) exists,
    contradiction (the function G(G), which is enabled by HALT(P, i), is undecidable)
        walk back assumption
        
ASSUME T(P) exists, 
    contradiction (ability to construct impossible HALT(P, i))
        walk back assumption
"""