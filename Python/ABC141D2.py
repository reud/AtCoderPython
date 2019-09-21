import bisect


def main():
    N, M = map(int, input().split())
    As = [0]
    As.extend([int(i) for i in input().split()])

    As.sort()
    checkt_used = 0
    used = [0]
    while checkt_used < M:
        checkt_used += 1
        if not (N == 1 and used == [0]):
            if As:
                takai = As[-1]
                if used:
                    takakatta = used[-1]
                    if takai > takakatta:
                        takai = As.pop()
                    else:
                        takai = used.pop()
                else:
                    takai = As.pop()
                takai //= 2
                b_takai = max(As[-1],used[-1])
                while checkt_used < M and b_takai < takai:
                   takai //= 2
                   checkt_used += 1

                bisect.insort_left(used, takai)
            else:
                takai = used.pop()
                takai //= 2
                b_takai = max(As[-1],used[-1])
                while checkt_used < M and b_takai < takai:
                    takai //= 2
                    checkt_used += 1
                bisect.insort_left(used, takai)
        else:
            As[1] //= 2
        # print(used)

    print(sum(As) + sum(used))

if __name__ == '__main__':
    main()
