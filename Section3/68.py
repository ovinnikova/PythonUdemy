# Question: Create an English to Portuguese translation program.
#
# The program takes a word from the user as input and translates it using
# the following dictionary as a vocabulary source. In addition, return the
# message "We couldn't find that word!" when the user enters a word that is
# not in the dictionary. Also, make the program non case-sensitive meaning
# that for example, both earth and Earth should return the translation
# correctly for that word.

d = dict(weather="clima", earth="terra", rain="chuva")

# Expected output:
#
# Enter word: hello
# We couldn't find that word!


def translate(inp):
    inp = inp.lower()
    dict_value = d.get(inp)
    if dict_value is None:
        dict_value = "We couldn't find that word!"
    return dict_value


inp = input("Enter word: ")

print(translate(inp))
