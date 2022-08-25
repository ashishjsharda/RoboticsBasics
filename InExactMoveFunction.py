p=[0,1,0,0,0]
world=['green','red','red','green','green']
measurements=['red','green']
p_Hit=0.6
p_Miss=0.2
p_Exact=0.8
p_Overshoot=0.1
p_Undershoot=0.1

def sense(p,Z):
    q=[]
    for i in range(len(p)):
        hit= (Z==world[i])
        q.append(p[i]*(hit*p_Hit+(1-hit)*p_Miss))
    s=sum(q)
    for i in range(len(p)):
        q[i]=q[i]/s
    return q

def move(p,U):
    q=[]
    for i in range(len(p)):
        s=p_Exact*p[(i-U)%len(p)]
        s=s+p_Overshoot*p[(i-U-1)%len(p)]
        s=s+p_Undershoot*p[(i-U+1)%len(p)]
        q.append(s)
    return q

print(move(p,1))

