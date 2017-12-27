euro_roulette = [0,32,15,19,4,21,2,25,17,34,6,27,13,36,11,30,8,23,10,5,
                24,16,33,1,20,14,31,9,22,18,29,7,28,12,35,3,26]

us_roulette = [0,28,9,26,30,11,7,20,32,17,5,22,34,15,3,24,36,13,1,0,27,
               10,25,29,12,8,19,31,18,6,21,33,16,4,23,35,14,2]


def find_max_of_n(n, roulette):
    s = 0
    for i in range(len(roulette)):
        start = i
        end = start+n
        # start_num = roulette[start]
        if end > len(roulette):
            e1 = slice(0, end-len(roulette))
            s2 = sum(roulette[start:None]) + sum(roulette[e1])
            # ls = roulette[start:None] + roulette[e1]
        else:
            s2=sum(roulette[start:end])
            # ls = roulette[start:end]
        s=max(s,s2)
    return s

if __name__ == '__main__':
    cnt =0
    for i in range(2,37):
        euro_mx = find_max_of_n(i, euro_roulette)
        us_max = find_max_of_n(i, us_roulette)

        if euro_mx < us_max:
          cnt+=1
    print(cnt)