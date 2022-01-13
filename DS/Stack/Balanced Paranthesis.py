class Stack:
    def __init__(self):
        self.s=[]
        self.size=0
        
    '<----Push Operation---->'    
    def push(self,x):
        self.s.append(x)
        self.size+=1
        return self.s
    
    '<----pop operation---->'
    def pop(self):
        if self.size>0:
            self.s.pop(-1)
            self.size-=1
            return self.s
        return 'Stack is Empty!'

    '<----peek operation---->'
    def peek(self):
        if self.size>0:
            return self.s[-1]
        return 'Stack is Empty'
    
    '<----isEmpty Operation---->'
    def isEmpty(self):
        if self.size==0:
            return True
        return False

    '<----Size of Stack---->'
    def Size(self):
        return self.size

def Balanced(s):
    stack=[]
    
    for i in s:
        if i=='[' or i=='(' or i=='{':
            stack.append(i)
            
        else:
            if len(stack)==0:    # this is for a case where the function will get closing paranthesis at very starting of string EX-')({]}}'
                return False
            elif i==']' and stack[-1]=='[':
                stack.pop()
                
            elif i==')' and stack[-1]=='(':
                stack.pop()
                
            elif i=='}' and stack[-1]=='{':
                stack.pop()
                
    if len(stack)==0:
        return True
    else:
        return False

print(Balanced('(((abcd)))'))
print(Balanced("{[(abc)]}"))
print(Balanced('{[}]'))
print(Balanced('(abc){[bcc]}'))
print(Balanced(')(())'))