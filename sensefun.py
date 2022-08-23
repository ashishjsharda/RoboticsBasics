p=[0.2,0.2,0.2,0.2,0.2]
world=['green','red','red','green','green']
Z='red'
p_Hit=0.6
p_Miss=0.2

def sense(p,Z):
    q=[]
    for i in range(len(p)):
        hit=Z==world[i]
        q.append(p[i]*(hit*p_Hit+(1-hit)*p_Miss))
    s=sum(q)
    for i in range(len(q)):
        q[i]=q[i]/s
    return q
print(sense(p,Z))

