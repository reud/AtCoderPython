N = int(input())
A=[-1]
A.extend([int(a) for a in input().split()])

ans = {}
ret = []

def get_xor(frm):
    global ans
    i = frm *2
    re = 0
    while i < len(A):
        re = re ^ ans[i]
        i += frm
    return re

for i in range(1,len(A)):
    ri = len(A) - i
    if 2 * ri < len(A):
        # recursive search
        ans[ri] = A[ri] ^ get_xor(ri)
        if ans[ri]==1:
            ret.append(str(ri))
        pass
    else:  # only one
        ans[ri] = A[ri]
        if ans[ri]==1:
            ret.append(str(ri))
print(len(ret))
s = " ".join(ret)
if s:
    print(s)