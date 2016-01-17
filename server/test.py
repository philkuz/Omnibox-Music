def passive():
    pass
def aggressive():
    return 0
def neutral():
    nonlocal passive, aggressive
    passive = lambda : print("litmas is early")
    aggressive = lambda : print("camel is a snitch")
neutral()
