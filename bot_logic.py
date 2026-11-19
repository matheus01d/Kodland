mport random
def flip_coin():
    flip = random.randint(0, 1)
    if flip == 0:
        return "cara"
    else:
        return "coroa"
