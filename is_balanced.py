# -*- coding: utf-8 -*-

def is_balanced(input_str):
    close_for_open = { '(': ')', '[': ']', '{': '}' }

    stack = []
    for c in input_str:
        if c in '({[':
            stack.append(c)
        elif c in ')}]':
            if len(stack) == 0:
                return False

            o = stack.pop()
            if close_for_open[o] != c:
                return False
    return len(stack) == 0

print(is_balanced("((()))"))
print(is_balanced("(()(()()))"))
print(is_balanced("((()"))
