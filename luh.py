def even_nth_numbers(n):
    numbers = []
    for i in n:
        if i%2==0:
            numbers.append(i)
    return numbers


def odd_nth_numbers(n):
    numbers = []
    for i in n:
        if i%2!=0:
            numbers.append(i)
    return numbers