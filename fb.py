def fizzbuzz(number):
    #return str() #vrací prázdný string
    ret = ""
    if number % 3 == 0:
        ret+= 'fizz'
    if number % 5 == 0:
        ret+= 'buzz'
    return ret or str(number)


""" alternativní řešení:
    if number % 15 == 0: #záleží na pořadí
        return 'fizzbuzz'
    if number % 3 == 0: #funguje i s elif
        return 'fizz'
    if number % 5 == 0:
        return 'buzz'

    else:
        return str(number)
"""



def fizzbuzz(number):
    #return str() #vrací prázdný string
    if number % 15 == 0: #záleží na pořadí
        return 'haha'
    if number % 3 == 0: #funguje i s elif
        return 'haha'
    if number % 5 == 0:
        return 'haha'

    else:
        return str(number)
