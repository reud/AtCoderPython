N, K = map(int, input().split())
As = [int(i) for i in input().split()]
sumAs = sum(As)
back_sum =[]
for i in range(N):
    back_sum.append(sumAs)
    sumAs-=As[i]
score=0
skipper=-1
for main_pointer in range(N):
    if main_pointer<=skipper:
        print(f'{main_pointer} {skipper} skipping')
        continue
    if back_sum[main_pointer]<K:
        print(score)
        exit(0)
    # print(f'{main_pointer} -> score {score}')
    val= As[main_pointer]
    if val >= K:
        score += 1
    if main_pointer == N-1:
        break
    skipper=-1
    for sub_pointer in range(main_pointer+1,N):
        if val+back_sum[sub_pointer]<K:
            print(score)
            exit(0)
        val+=As[sub_pointer]
        if val >= K:
            cval=val
            cmain_pointer=main_pointer
            kakeru=1
            skipper=main_pointer-1
            cval-=As[cmain_pointer]
            while cval>=K and cmain_pointer<N:
                print(f'ok skipping! {cval} {K} {cmain_pointer} {sub_pointer}')
                kakeru+=1
                skipper+=1
                cval-=As[cmain_pointer]
                cmain_pointer+=1
            score+=kakeru
            print(f'{main_pointer} {sub_pointer} -> score {score}')
            if sub_pointer!=N-1:
                exist = (N - (sub_pointer+1))*kakeru
                score+=exist
                print(f'sp {exist} -> {score}')
            break

print(score)
