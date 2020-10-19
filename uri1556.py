def makeSet(word):
    unique = set([])
    for letter in word:
        setCopy = unique.copy();
        for key in setCopy:
            if ((key + letter) not in unique):
                unique.add(key + letter)
        if (letter not in unique):
            unique.add(letter)
        
    for key in sorted(unique):
        print(key)
    print()

while True:
    makeSet(input())
