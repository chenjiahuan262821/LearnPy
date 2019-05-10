import random
counter = 0
gambler = 0
maker = 0
rounds = 100000

while counter < rounds:
    counter += 1
    x = random.randint(1, 6)
    y = random.randint(1, 6)
    sum0 = x + y
    if (sum0 == 7) | (sum0 == 11):
        gambler += 1  #The gambler wins the game
    elif (sum0 == 2) | (sum0 == 3) | (sum0 == 12):
        maker += 1  #The maker wins the game
    else:
        while True:
            x = random.randint(1, 6)
            y = random.randint(1, 6)
            new_sum = x + y
            if new_sum == sum0:
                gambler += 1  #The gambler wins the game
                break
            elif new_sum == 7:
                maker += 1  #The maker wins the game
                break
            else:
                continue
print('In %d rounds, the gambler wins %d while the maker wins %d.' % (rounds, gambler, maker))
if maker != 0:
    odds = gambler/maker
    print('The odd-ratio is %.4f' % odds)
else:
    print('This time the odd-ratio is infinite')