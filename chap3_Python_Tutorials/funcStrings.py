# def substring(s, frm, ln):
#     result = ""
#     i = frm
#     count = 0

#     while i < len(s) and count < ln:
#         result += s[i]   # manually building the substring
#         i += 1
#         count += 1

#     return result


def substring(s, frm, ln):
    result = ""

    # loop from frm up to frm + ln
    # (but do not go past len(s))
    for i in range(frm, frm + ln):
        if i < len(s):
            result += s[i]

    return result


def find_pos(term, corpus):
    term_len = len(term)
    text_len = len(corpus)

    for i in range(text_len - term_len + 1):
        # Take a piece of corpus the same length as term
        part = substring(corpus, i, term_len)

        if part == term:
            return i

    return None


# print(find_pos("with", "a sentence with words"))

# def find_pos(term, corpus):
#     i = term[0]
#     count = 0
#     result = 0
#     for j in range(len(corpus)):
#         if i == corpus[j]:
#             result += j
#         else:
#             count += 1


# find_pos("with", "a sentence with words")
