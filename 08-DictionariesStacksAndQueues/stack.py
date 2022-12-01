stack = []

def push(value):
    stack.append(value)
    
   
def pop():
    if not empty():
        return stack.pop()
    else:
        return None

def empty():
    return len(stack) == 0


def display():
    for i in range(len(stack)-1,-1,-1):
        print(stack[i])
    print()