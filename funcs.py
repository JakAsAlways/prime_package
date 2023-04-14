def is_prime(num):
    if num==2:
        return True
    for i in range(2,num):
        if num%i==0:
            return False
    return True

def prime_range(num):
    for i in range(2,num+1):
        if is_prime(i):
            yield i


def prime_factors(num):
    lst = []
    i = 2
    while num>1:
        if num%i:
            i+=1
        else:
            num//=i
            lst.append(i)
    return lst