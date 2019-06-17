o=input()
vowel=['a','A','e','E','i','I','o','O','u','U']
Consonant=['b','B','c','C','d','D','f','F','j','J','k','K','l','L','m','M','n','N','p','P','q','Q','r','R','s','S','t','T','v','V','w','W','x','X','y','Y','z','Z']
if o in vowel:
    print("Vowel")
elif o in Consonant:
    print("Consonant")
else:
    print("invalid")
