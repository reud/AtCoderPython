import bisect
N = int(input())
Cs = [int(input()) for _ in range(N)]
dp = [1] * N

def insertion_sort(tl):
    for i in range(1,len(tl)):
        if tl[i-1]<tl[i]:
            tmp = tl[i-1]
            tl[i-1] = tl[i]
            tl[i] = tmp
            return

sch_cs = [Cs[0]]
sch_dp = [dp[0]]
# (val, dp)
for i in range(1, N):
    ind = bisect.bisect_left(sch_dp,dp[i])
    # print(ind)
    # dp値 降順
    for j in range(i):
        if sch_cs[j]<Cs[i]:
            dp[i]=sch_dp[j]+1
            break
    sch_cs.insert(ind,Cs[i])
    sch_dp.insert(ind,dp[i])
# print(dp)
print(N-max(dp))

