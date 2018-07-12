def test( n ):
    n=n.lower()
    if (n>='a' and n<='z'):
        return "Alphabet"
    else:
        return "No"
n=input()
print(test(n))
