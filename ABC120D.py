import sys

sys.setrecursionlimit(1000000)
N, M = map(int, input().split())
datas = [[int(u) for u in input().split()] for _ in range(M)]
dellist = lambda items, indexes: [item for index, item in enumerate(items) if index not in indexes]


def dfs(finlist, nowpoint, _datas):
    childs = []
    kicker = []
    finlist.append(nowpoint)
    print("nowpoint {}".format(nowpoint))
    print("finlist {}".format(finlist))
    for data in range(len(_datas)):
        if _datas[data][0] == nowpoint:
            if _datas[data][1] not in finlist:
                childs.append(_datas[data][1])
                kicker.append(data)
        elif _datas[data][1] == nowpoint:
            if _datas[data][0] not in finlist:
                childs.append(_datas[data][0])
                kicker.append(data)
    print("childs {}".format(childs))
    if not kicker:
        return finlist
    _datas = dellist(_datas, kicker)
    if childs:
        for child in childs:
            if child not in finlist:
                finlist.append(child)
                finlist = dfs(finlist, child, datas)
    return finlist


while datas:
    datas.pop(0)
    anss = [dfs([], i, datas) for i in range(1,N+1)]
    print(anss)
