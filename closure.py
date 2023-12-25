

def parent_func(person):
    coins = 3

    def play_game():
        nonlocal coins
        coins -= 1

        if coins > 1:
            print("\n" + person + " has " + str(coins) + " coins left.")
        elif coins == 1:
            print("\n" + person + ' has ' + str(coins) + ' coins left.')
        else:
            print("\n" + person + " is out of coins.")
    return play_game


mucu = parent_func('Mucu')
alice = parent_func('Alice')

mucu()
mucu()
mucu()
alice()
