N=int(input())
count=0
def saiki(word):
    nums=['3','5','7']
    global count
    ans=0
    if(N==word):
        saiki(nums[0])
        saiki(nums[1])
        saiki(nums[2])
    elif(int(word)>N):
        return
    else:
        if '3' in word and '5' in word and '7' in word:
            count+=1
        saiki(word+nums[0])
        saiki(word+nums[1])
        saiki(word+nums[2])
        return
saiki(N)
print(count)