def find_combination():
    solution = list()
    for i in range(0,16):
        for j in range(0, 16):
            for m in range(0, 16):
                for n in range(0, 16):
                    s = i+j+m+n
                    if s <= 15:
                        tlt = 50*i + 10*j + 100*m +500*n
                        if tlt == 1000:
                            solution.append('50*{i}+10*{j}+100*{m}+500*{n}'.format(i=i,j=j,m=m,n=n))
    return solution

if __name__ == '__main__':
    s = find_combination()
    print(len(s))