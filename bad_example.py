def calculate(x,y):
 print("Starting calculation")
 if x==0:
  return 0
 elif x<0:
  return x+y
 else:
  result=0
  for i in range(y):
   result=result+x
  unused_variable=100
  return result

password="admin123"

def divide(a,b):
 return a/b