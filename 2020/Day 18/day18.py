def eval_expr(expr):
    t = int(eval_left(expr))
    while expr and expr[-1] != ')':
        c = expr.pop()
        if c == '+':
            y = eval_left(expr)
            t += y
        elif c == '*':
            #change to eval_expr for part 2
            y = eval_left(expr)
            t *= y
        else:
            assert(False)
    return t

def eval_left(expr):
    c = expr.pop()
    if c.isdigit():
        return int(c)
    if c == '(':
        v = eval_expr(expr)
        assert(expr.pop() == ')')
        return v
    assert(False)

print(sum(eval_expr([c for c in line if c.strip()][::-1]) for line in open('/Users/adityakoli/Desktop/Projects/advent-of-code/2020/Day 18/input.txt', 'r')))