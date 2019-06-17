import datetime
S=input()
form=datetime.datetime.strptime(S,"%Y/%m/%d")

if form>datetime.datetime.strptime('2019/04/30',"%Y/%m/%d"):
    print('TBD')
else:
    print('Heisei')