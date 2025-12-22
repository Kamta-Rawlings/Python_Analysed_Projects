'''
QUESTION
Full Question (Anagram Checker)
Two strings w₁ and w₂ are anagrams
if one can obtain w₂ from w₁ by rearranging the letters in w₂.
Only lowercase letters are considered.
All other characters —
such as spaces and uppercase letters — must be ignored.

Examples of anagrams:

“mary” and “army”

“elvis” and “lives”

“tom marvolo riddle” and “i am lord voldemort”
Examples that are not anagrams:

“Flat broke” and “Table fork” → number of f and t letters differ
(uppercase F and T are ignored)
'''

letters = "abcdefghijklmnopqrstuvwxyz"
# count letters in the first string
store_s1 = []
# count = 0
s1 = input("Enter the string you want to count lower letters: ")
for i in letters:
    count1 = 0
    for j in s1:
        if i == j:
            count1 += 1
    # print(f'{i}: {count}')
    store_s1.append(count1)

# count letters in the second string
store_s2 = []
s2 = input("Enter the second string you want to count lower letters: ")
for i in letters:
    count2 = 0
    for j in s2:
        if i == j:
            count2 += 1
    store_s2.append(count2)

if store_s1 == store_s2:
    print(f'{s1} and {s2} are anagrams')
else:
    print(f'{s1} and {s2} are not anagrams')
'''
i would refer you to the exercise on "iteration_countletter"
simply compare a string with the letter of the alphabet, save the lowercase
letters and then do same for the second string.
Then you later compare the arrays which
the number of counts of the letter were been stored.
'''
