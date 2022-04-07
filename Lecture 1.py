# Schreibe eine rekursive Funktion fac_rec(num), die die Zahlen von 1 bis num multipliziert.

def fac_rec(num):
    if num == 1:
        return 1
    else:
        return num * fac_rec(num - 1)


print(fac_rec(3))


# Schreibe eine rekursive Funktion fib_rec(n), die die nte Fibonacci-Zahl.berechnet.

def fib_rec(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib_rec(n-1) + fib_rec(n-2)


print(fib_rec(5))

# Schreibe eine Funktion compound_interest(base_interest, run_time) die den Zinseszins berechnet
def compound_interest(base_interest, run_time):
    zinsfaktor = (1 + base_interest / 100)
    return (zinsfaktor ** run_time)


anfangskapital = 37
zinssatz = 3.5
laufzeit = 10

kapital  = anfangskapital * compound_interest(zinssatz, laufzeit)
print(kapital) # 52.19215414298148


