N, M = map ( int, input ( ).split ( ) )# N,Mを取得
#初期化
lists = [ ]
#listに要素を追加　後で並び変えるため並び替える前の順番を示すキーを第三要素に挿入しておく
for i in range ( M ):
    lists.append ( list ( map ( int, input ( ).split ( ) ) ) + [ i ] )
#第一要素に昇順で並び替えた後、第二要素で昇順に並び替える
lists.sort ( key=lambda x: x[ 0 ] )
lists.sort ( key=lambda x: x[ 1 ] )
# befは前回の第一要素　stateは第一要素での順位
bef = 0
state = 0
retstr = ''
triple = [ ]#第四要素に識別番号を追加したリストの初期化
for i in lists:
    if (i[ 0 ] != bef):
        bef = i[ 0 ]
        state = 1
        triple.append ( [ i[ 0 ], i[ 1 ], i[ 2 ], str ( i[ 0 ] ).rjust ( 6, '0' ) + str ( state ).rjust ( 6, '0' ) ] )
    else:
        state += 1
        triple.append ( [ i[ 0 ], i[ 1 ], i[ 2 ], str ( i[ 0 ] ).rjust ( 6, '0' ) + str ( state ).rjust ( 6, '0' ) ] )

triple.sort ( key=lambda x: x[ 2 ] )#第三要素で並び替えて、元の入力に対応した式ベンツ番号の順番に戻す
for i in triple:
    print ( i[ 3 ] )#識別番号の出力

