(lambda n:
    (lambda mmap=[0]*(n*n),
            show=list('   a   b   c \n1    |   |   \n  ---|---|---\n2    |   |   \n  ---|---|---\n3    |   |   '),
            step=lambda r,turn,mmap,sh,st,
                        interaction=lambda tr,mp,sh,st,it,
                                           temp=[],ins=lambda pt
                                                          :{'a1':0,'a2':3,'a3':6,
                                                            'b1':1,'b2':4,'b3':7,
                                                            'c1':2,'c2':5,'c3':8}.get(input(pt))
                                       :temp.clear() or 1
                                       and (tr==1 and (temp.append(ins("\nX's turn: ")) or 1)
                                       or tr==0 and (temp.append(ins("\nO's turn: ")) or 1))
                                       and ((temp[0]==None and (lambda lg:print(''.join([chr(l) for l in lg])+'\n') or 1)
                                       ([32,32,32,97,32,32,32,98,32,32,32,99,32,10,
                                         49,32,32,78,32,124,32,111,32,124,32,69,32,10,
                                         32,32,45,45,45,124,45,45,45,124,45,45,45,10,
                                         50,32,32,86,32,124,32,97,32,124,32,32,32,10,
                                         32,32,45,45,45,124,45,45,45,124,45,45,45,10,
                                         51,32,32,97,32,124,32,32,32,124,32,32,32])
                                             or mp[temp[0]]!=0) and (st(1,tr,mp,sh,st) or 1)
                                           or (mp.pop(temp[0]) or 1) and (mp.insert(temp[0],tr*2-1) or 1)
                                              and (sh.pop([17,21,25,45,49,53,73,77,81][temp[0]]) or 1)
                                              and (sh.insert([17,21,25,45,49,53,73,77,81][temp[0]],chr(111+9*tr)) or 1)
                                              and st((lambda m
                                                        :(lambda stat:
                                                               -3 in stat and 2
                                                               or 3 in stat and 3
                                                               or 0
                                                           )(set([m[i*3]+m[i*3+1]+m[i*3+2] for i in range(3)]
                                                             +[m[i]+m[3+i]+m[6+i] for i in range(3)]
                                                             +[m[0]+m[4]+m[8],m[2]+m[4]+m[6]]))
                                                          or 0 in set(m) and 1
                                                          or 4
                                                     )(mp),1-tr,mp,sh,st)
                                           )
                    :(print(''.join(sh)) or 1) and 
                    (r==1 and (interaction(turn,mmap,sh,st,interaction) or 1)
                    or r==2 and print('O win'))
                    or r==3 and print('X win')
                    or r==4 and print('A draw')
        :step(1,1,mmap,show,step)
    )()
)(3)


