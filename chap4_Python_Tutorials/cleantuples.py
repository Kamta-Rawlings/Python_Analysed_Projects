'''
Write a function clean_tuple(tpl) that takes a tuple as
input and returns a tuple in which all duplicates are
removed. In particular, only the first occurrence of each
value should be kept in the returned tuple. Notice that the
tuple can contain anything (integers, strings, …).
Example:
>>> clean_tuple(("John", "Niels", "Brecht", "Niels", "Erik"))
("John", "Niels", "Brecht", "Erik")
'''


def clean_tuple(tpl):
    clean = []

    for item in tpl:
        if item not in clean:
            clean.append(item)

    return tuple(clean)
    # return clean


'''
if you use "return clean" without
the tuple it will return an array
'''
