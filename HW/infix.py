def solution(expr):
    def precedence(op):
        if op=="^":
            return 3
        if op=="*" or op=="/":
            return 2
        if op=="+" or op=="-":
            return 1
        else:            
            return 0
        
    stack=[]
    postfix=""
    for char in expr:
        if char.isalnum():
            postfix+=char
        elif char=="(":
            stack.append(char)
        elif char==")":
            while stack and stack[-1]!="(":
                postfix+=stack.pop()
            stack.pop() 
        else:
            while stack and precedence(stack[-1])>=precedence(char):
                postfix+=stack.pop()
            stack.append(char)
    while stack:
        postfix+=stack.pop()
    return postfix

# Taking user input
expr = input("Enter infix expression: ")    

result = solution(expr)
print("Postfix Expression:", result)

