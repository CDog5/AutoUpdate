def fizzbuzz_v1(start,stop):
    for i in range(start,stop+1): 
        output=""
        if i % 3 == 0:
            output += "Fizz"
        if i % 5 == 0:
            output += "Buzz"
        if output == "":
            output = i
        print(output)
mlts={3:"Fizz",5:"Buzz"}
# far superior method, using dictionaries and generators
def fizzbuzz_v2(multiples,start,stop):
    for i in range(start,stop+1):
        out = ""
        for mlt,prnt in multiples.items():
            if i % mlt == 0:
                out += prnt
        yield (i,out)


f =  fizzbuzz_v2(multiples=mlts,start=0,stop=100)

for x in f:
    print(x)

