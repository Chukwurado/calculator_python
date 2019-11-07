import re

def calculate(exp):
    exp_arr = exp.strip().split(' ')
    post_exp = infix_to_postfix(exp_arr)
    result = calc_postfix(post_exp)
    return result
    
def infix_to_postfix(arr):
    operators = {
            '^': 4,
            '*': 3, 
            '/': 3,
            '+': 2,
            '-': 2,
            '(': 1,
            ')': 1
        }
    postfix = []
    oper_stack = []
    for o in arr:
        if not operators.get(o):
            postfix.append(float(o))
        else:
            if len(oper_stack) == 0:
                oper_stack.append(o)
            else:
                if o == "(":
                    oper_stack.append(o)
                elif o == ")":
                    while oper_stack[len(oper_stack)-1] != '(':
                        postfix.append(oper_stack.pop())
                    oper_stack.pop()
                else:
                    top = oper_stack[len(oper_stack)-1]
                    while len(oper_stack) > 0 and operators[o] <= operators[top]:
                        postfix.append(oper_stack.pop())
                        if len(oper_stack) > 0:
                            top = oper_stack[len(oper_stack)-1]
                    oper_stack.append(o)
    while len(oper_stack) > 0:
        postfix.append(oper_stack.pop())
    return postfix

def calc_postfix(arr):
    calc = []
    for o in arr:
        if o == '^':
            a = calc.pop()
            b = calc.pop()
            calc.append(b**a)
        elif o == '*':
            a = calc.pop()
            b = calc.pop()
            calc.append(b*a)
        elif o == '/':
            a = calc.pop()
            b = calc.pop()
            calc.append(b/a)
        elif o == '+':
            a = calc.pop()
            b = calc.pop()
            calc.append(b+a)
        elif o == '-':
            a = calc.pop()
            b = calc.pop()
            calc.append(b-a)
        else:
            calc.append(o)
    return calc.pop()


# calculate("( 42.3 / 3 ) - 34 ")
# calculate("1 + 2 * 4.2")
# # 6 -7 * 7 + 5 -> 677*-5+
calculate('( 2 + 1 ) ^ 3')