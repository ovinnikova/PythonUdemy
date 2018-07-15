# Question: Create an English to Portuguese translation program.
#
# The program takes a word from the user as input and translates it using the
# following dictionary as a vocabulary source.
#
d = dict(weather="clima", earth="terra", rain="chuva")
#
# Expected output:
#
# Enter word: earth
# terra


def translate(inp):
    dict_value = d.get(inp)
    return dict_value


inp = input("Enter word: ")

print(translate(inp))
