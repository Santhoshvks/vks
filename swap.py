s=str(input("enter the string:"))
l=''.join([c[1] + c[0] for c in zip(s[::2], s[1::2])])
print(l)
