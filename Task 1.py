stack=[]
stack.append(7)
stack.append(99)
stack.append(11)
print("Stack:", stack)
print("Popped:", stack.pop())
print("Stack after pop:", stack)
print("Top element:", stack[-1])
if len(stack)==0:
    print("Empty")
else:
    print("Not empty")
