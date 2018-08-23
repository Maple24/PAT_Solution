def func(a, b):
  c = str(int(a)+int(b))
  list = []
  count = 0
  for i in range(0,len(c))[::-1]:
    if count!= 0 and count%3 == 0 and c[i] is not '-':
      list.append(",")
    list.append(c[i])
    count = count + 1
    
  result = ""
  list.reverse()
  for v in list:
    result = result + v
  
  return result

if __name__ == '__main__':
    a = input('a:')
    b = input('b:')
    print(func(a,b))
