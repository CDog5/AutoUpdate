# generator object that splits a sentence into words
def sentence_to_words(words):
    punctuation = [".",",","?","!","-"," ",":",";"]
    for punc in punctuation:
        words = words.replace(punc," ")
    words = words.split()
    yield from words
# generator object that splits a string into certain chars
def string_to_chars(string,mode="all"):
    chars=[]
    if "all" in mode.lower():
        for char in string:
            chars.append(char)
    elif "alpha" in mode.lower():
        alphabet = "abcdefghijklmnopqrstuvwxyz"
        for char in string:
            if char.lower() in alphabet:
                chars.append(char)
    elif "numeric" in mode.lower():
        numbers = "0123456789"
        for char in string:
            if char in numbers:
                chars.append(char)
    elif "special" in mode.lower():
        specials = r"!£$%^&*()_+{}[]#~/*-¬`@\|"
        for char in string:
            if char in specials:
                chars.append(char)
    yield from chars

s = string_to_chars("Hello people, I am Bob!","alpha")
print([c for c in s])
