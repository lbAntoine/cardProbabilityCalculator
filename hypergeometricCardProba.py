from scipy.stats import hypergeom


def test_prob():
    deck_size = int(input(f'Deck size : '))
    numb_draw = int(input(f'Number of cards in draw hand : '))
    numb_copy = int(input(f'Number of target : '))

    x = min_success = 1
    M = deck_size
    n = numb_copy
    N = numb_draw

    for min_success in range(numb_draw):
        pval = hypergeom.sf(x-1, M, n, N)

        print(f'For {min_success+1} copy(ies) in starting hand : {round(pval*100, 2)}%')

        x = x+1
        numb_copy = numb_copy-1
        deck_size = deck_size-1
        numb_draw = numb_draw-1
        if numb_copy == 0: break
        if numb_draw == 0: break
        if deck_size == 0: break

test_prob()