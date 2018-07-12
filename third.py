def vowels(n):
    n=n.lower()
    if(n=='a' or n=='e' or n=='i' or n=='o' or n=='u' ):
        return "Vowel"
    else:
        return "Consonant"
n=input()
print(vowels(n))
