def wizards(N,start,duels):
    owner=start
    num_owners=1
    for i in range(N):
        if duels[i][1] == owner:
            num_owners=1
            print(duels[i][1])    
            owner=duels[i][0]
            num_owners+=1
    print(owner,num_owners)

wizards(3,"A",["BA","CB","DA"])