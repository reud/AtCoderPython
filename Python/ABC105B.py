N=int(input())


def boughter(num):

    if num<-5:

        return
    elif num==0:
        print('Yes')
        exit(0)
    boughter(num-4)
    boughter(num-7)
    return

boughter(N)
print ( 'No' )
