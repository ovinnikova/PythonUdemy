# Question: Complete the script so that it removes duplicate items from list a .
#
a = ["1", 1, "1", 2]
# Expected output:
#
#  ['1', 2, 1]

a = list(set(a))
print(a)
