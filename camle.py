def camelCase(st):
  output = ''.join(x for x in st.title() if x.isalpha())
  return output[0].upper() + output[1:]
i=str(input("enter the str:"))
l=camelCase(i)
print(l)
