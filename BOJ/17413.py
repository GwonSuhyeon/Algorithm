S = input()

tag = False

stack = []

for i in S:
    if i == '<':
        while len(stack):
            print(stack.pop(), end='')
        
        tag = True
    
    if tag == True:
        print(i, end='')
    
    elif tag == False and i == ' ':
        while len(stack):
            print(stack.pop(), end='')
        
        print(i, end='')
    
    else:
        stack.append(i)
    
    if i == '>':
        tag = False

while len(stack):
    print(stack.pop(), end='')