from operator import add, sub, mul, floordiv as div
import copy

operators = {'+': add,
             '-': sub,
             '*': mul,
             '/': div,
             'n': lambda x,y:int('%s%s'%(x,y))
             }


def rpn(n):
    nc = copy.copy(list(n))
    if n.count('n') == 3:
        return False

    for i in range(len(n)):
        if n[i] == 'n':
            nc[i-1] = nc[i-1]+nc[i+1]
            nc[i],nc[i+1]='',''

    for i in range(len(n)):

        if n[i] in ('+','-'):
            nc.append(n[i])
            nc[i] =''

        if n[i] in ('*','/'):
            nc[i],nc[i+1] = nc[i+1],nc[i]

    cval = list()
    for i in range(len(nc)):
        if nc[i] !='':
            cval.append(nc[i])

    return cval


def cal_num(num_lst):

    operand_stack = list()
    for i in range(len(num_lst)):
        if num_lst[i].isdigit():
            operand_stack.append(int(num_lst[i]))
        else:
            try:
                operand1= int(operand_stack.pop())
                operand2= int(operand_stack.pop())
                operator = operators.get(num_lst[i])
                try:
                    result = operator(operand2, operand1)
                    operand_stack.append(result)
                except:
                    pass
            except:
                pass
    if len(operand_stack):
        val = operand_stack.pop()
        return val


def reslove(nums):
    ops = ['+', '-', '*', '/', 'n']
    solutions = dict()
    for curr_num in nums:
        ns = str(curr_num)

        for i in range(5):
            for j in range(5):
                for m in range(5):
                    val = ns[0]+ops[i]+ns[1]+ops[j]+\
                    ns[2]+ops[m]+ns[3]
                    n_rpn = rpn(val)
                    if not n_rpn:
                        continue
                    result = cal_num(n_rpn)
                    if str(result)[::-1] ==  ns:
                        print("Find the number!!")
                        print(ns)
                        solutions[ns]=val
    return solutions

if __name__ == '__main__':
    ns = range(1000,10000)
    s = reslove(ns)
    print(s)