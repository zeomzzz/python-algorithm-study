import sys

while True :
  str_lst = list(sys.stdin.readline().rstrip())
  if str_lst == ["."] : 
    break

  stack = []
  balanced = True

  for i in str_lst :
    if i not in ["(", ")", "[", "]"] :
      continue
    elif i in ["(", "["] :
      stack.append(i)
    elif i in [")", "]"] :
      if len(stack) > 0 :
        if stack[-1] == "(" and i == ")" :
          stack.pop()
        elif stack[-1] == "[" and i == "]" :
          stack.pop()
        else :
          balanced = False
          break
      else :
        balanced = False
        break

  if balanced == True and len(stack) == 0 :
    print("yes")
  else :
    print("no")
