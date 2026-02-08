def sInterest(p, t, r):
    return (p * t * r) / 100


def cInterest(p, t, r):
    return p * (((1 + r / 100) ** t) - 1)


if __name__ == "__main__":
    p = float(input("P?"))
    t = float(input("T?"))
    r = float(input("R?"))
    print(f"simple interest is {sInterest(p, t, r)}")
    print(f"conpound interest is {cInterest(p, t, r)}")
