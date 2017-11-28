class Thing:
    pass

example = Thing()

print(type(example))
print(type(Thing))


class Thing2:
    letters = "abc"

print(Thing2.letters)


class Thing3:
    Thing2.letters = "xyz"

print(Thing2.letters)