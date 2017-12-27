BOYS_MAX, GIRLS_MAX= 3,2
boys = [1]*BOYS_MAX
girls = [0]*GIRLS_MAX
import copy
global cnt
cnt=0


def stand_in_line(q, cnt=[0]):

    if q.count(1)==BOYS_MAX and q.count(0)==GIRLS_MAX:
        cnt[0]+=1
        return

    if len(q) > BOYS_MAX+GIRLS_MAX:
        cnt[0]+=0
        return

    for i in [0,1]:
        # person = copy.copy(i)
        q.append(i)
        stand_in_line(q,cnt)

    return cnt

if __name__ == '__main__':
    q=[]
    cnt=[0]
    stand_in_line(q,cnt)
    print(cnt)