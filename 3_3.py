def thesaurus(*args):
    names = {}
    for i in sorted(args):
        letter = i[0]
        if letter in names:
            names[letter] += [i]
        else:
            names[letter] = [i]
    return names

print(thesaurus('Eugene', 'Mark', 'Mary', 'Victor', 'Michael', 'Johnny'))
