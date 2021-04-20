def fibonacci(start_no,length):
    sequence=[]
    n1, n2 = start_no, start_no
    for _ in range(0,length):
       sequence.append(n1)
       nth = n1 + n2
       n1 = n2
       n2 = nth
    return sequence
def is_prime(num):
    if num == 1:
        return False
    for i in range(2,num):
       if (num % i) == 0:
           return False
    return True
def factorial(num):
    count = num-1
    while count > 1:
        num = num * count
        count -=1
    return num
def km_to_mi(no):
    return no * 0.621371
def mi_to_km(no):
    return no / 0.621371
def c_to_f(no):
    fahrenheit = (no * 1.8) + 32
    return fahrenheit
def f_to_c(no):
    celsius = (no / 1.8) - 32
    return celsius
