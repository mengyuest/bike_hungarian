
def draw(lx,ly,dist_mat):
    print("   "+" ".join(["%2d"%(y) for y in ly]))
    print("-"*20)
    for x,line in enumerate(dist_mat):
        print("%2d|"%(lx[x])+" ".join(["%2d"%(xy) for xy in line]))

# input: [X, Y]
# output: [dist, matching case]
def solve(pos_dist_mat, people, bikes):

    minus_dist_mat = list(pos_dist_mat)
    for i,line in enumerate(pos_dist_mat):
        for j,dist in enumerate(line):
            minus_dist_mat[i][j]=-1*dist


    maxx=65535
    m=len(minus_dist_mat)
    n=len(minus_dist_mat[0])

    # initial_labelling
    lx=[max(x) for x in minus_dist_mat]
    ly=[0]* n

    link_x=[-1]*m
    link_y=[-1]*n

    # # initial matching
    # link_x[0]=0
    # link_y[0]=0
    # num_matched=1

    num_matched=0

    # step 2,3,4
    S=[]
    T=[]
    goto=2
    while num_matched<m:
        #print("matched:",num_matched)
        #print("lx:",lx)
        #print("ly:",ly)
        #print("link_x:",link_x)
        #print("link_y:",link_y)
        #print("S:", S)
        #print("T", T)
        if goto==2:
            # step2: pick free vertex u \in X
            for u,y in enumerate(link_x):
                if y==-1:
                    #print("step2: pick free u=",u)
                    # set S={u}, T={empty}
                    S=[u]
                    T=[]
                    
                    # update NLS: find in the equality graph
                    NLS=[]
                    for iter_y in range(n):
                        if lx[u]+ly[iter_y]==minus_dist_mat[u][iter_y] and iter_y not in NLS:
                            NLS.append(iter_y)
                    #draw(lx,ly,minus_dist_mat)
                    #print("update NLS to:", NLS)
                    goto=3
                    break

        # step 3 update labels
        if goto==3:
            #print("step3 :NLS=",NLS,"and T=",T)
            if set(NLS) == set(T):
                al=maxx
                for x in S:
                    for y in range(n):
                        if y not in T:
                            al=min(al,lx[x]+ly[y]-minus_dist_mat[x][y])
                for y in T:
                    ly[y]=ly[y]+al
                for x in S:
                    lx[x]=lx[x]-al
                    # update NLS: find in the equality graph
                    for iter_y in range(n):
                        if lx[x]+ly[iter_y]==minus_dist_mat[x][iter_y] and iter_y not in NLS:
                            NLS.append(iter_y)
                
                #print("find al=",al)
                #print("modified lx=",lx)
                #print("modified ly=",ly)

                #draw(lx,ly,minus_dist_mat)
                #print("update NLS to:", NLS)

                goto=3

            # step 4 find augment path
            else:
                #pick one y in NLS-T
                for y in set(NLS)-set(T):
                    # if y free, link u and y: we found a new match~
                    if link_y[y]==-1:
                        #print("step4:",y,"is free")
                        link_x[S[0]]=y
                        link_y[y]=S[0]
                        num_matched+=1                  
                        goto=2


                    # if y matched
                    else:
                        #print("step 4:",y,"is matched")
                        ### append S and T
                        z=link_y[y]
                        #print("find z=",z)
                        S.append(z)
                        T.append(y)
                        
                        #update NLS
                        for iter_y in range(n):
                            if lx[z]+ly[iter_y]==minus_dist_mat[z][iter_y] and iter_y not in NLS:
                                NLS.append(iter_y)
                        #print("updated NLS=",NLS)
                        goto=3
                    
                    break

    dist_sum=0
    dist_pair=[(x,link_x[x]) for x in range(m)]
    for pair in dist_pair:
        dist_sum+=minus_dist_mat[pair[0]][pair[1]]
    return [dist_sum*-1, dist_pair]
