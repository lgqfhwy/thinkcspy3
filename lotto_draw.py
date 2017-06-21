import random

def lotto_draw(num = 6, lower_bound = 1, upper_bound = 49):
    rng = random.Random()
    result = []
    for i in range(num):
        result.append(rng.randrange(lower_bound, upper_bound))
    return result


def lotto_match(draw, ticket):
    num = 0
    for i in draw:
        if i in ticket:
            num += 1
    return num

#print(lotto_match([42, 4, 7, 11, 1, 13], [2, 5, 7, 11, 13, 17]))


def lotto_matches(draw, my_tickets):
    result = []
    for ticket in my_tickets:
        num = lotto_match(draw, ticket)
        result.append(num)
    return result


my_tickets = [[7, 17, 37, 19, 23, 43],
              [7, 2, 13, 41, 31, 43],
              [2, 5, 7, 11, 13, 17],
              [13, 17, 37, 19, 23, 43]]

#print(lotto_matches([42, 4, 7, 11, 1, 13], my_tickets))


def Is_prime(integer):
    num = int(integer ** 0.5 + 1)
    if integer == 1:
        return False
    for i in range(2, num):
        if integer % i == 0:
            return False
    return True


def primes_in(integers):
    num = 0
    for i in integers:
        if Is_prime(i):
            num += 1
    return num


def prime_misses(my_tickets):
    primes = []
    for i in range(2, 50):
        if Is_prime(i):
            primes.append(i)
    missprime = []
    for i in primes:
        misses = True
        for j in my_tickets:
            if i in j:
                misses = False
                break
        if misses:
            missprime.append(i)
    return missprime

#print(prime_misses(my_tickets))

def repeatedly_at_least_n_correct_picks(n, my_tickets):
    correct_picks = 0
    tries = 0
    while True:
        draw = lotto_draw()
        tries += 1
        result = lotto_matches(draw, my_tickets)
        for i in result:
            if i >= n:
                return tries

def average_number_draw_needed(n, my_tickets, times = 20):
    sum = 0
    for i in range(times):
        tries = repeatedly_at_least_n_correct_picks(n, my_tickets)
        sum += tries
    average = sum // tries
    return average

#print(average_number_draw_needed(3, my_tickets))
print(average_number_draw_needed(5, my_tickets))



































