x1=0
code=[]
def code(x,y):
  x1=x1+1
  code.append(x1 + f"{x}\n{y}")
code("条","簡単")
for i in code:
  print(i)
