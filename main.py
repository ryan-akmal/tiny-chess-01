import os
from json import*
from urllib.request import*
E=os.getenv("MAKEFUN_ENV_URL")
V=[0,100,320,330,500,900,0];I='abcdefgh'
n=[-33,-31,-18,-14,14,18,31,33];g=[-17,-16,-15,-1,1,15,16,17];h=[-17,-15,15,17];j=[-16,-1,1,16]
B=[0]*128;T={};U=[]
class X(Exception):pass
def rq(p,y):
 try:return load(urlopen(E+p,dumps(y).encode()))
 except:exit(1)
def P(t,s,c):
 f=s&7;r=s>>4
 if c<0:r=7-r
 q=min(f,7-f)+min(r,7-r)
 return ord('0048>HX0'[r])-48+10*(f in(3,4))if t==1 else 6*q-20 if t==2 else 15*(r==6)+5*(r==0 and f in(3,4))if t==4 else(ord('DI:00:ID'[f])-48 if r==0 else max(-50,-15*r))if t==6 else 0
def ev():return(S+P(6,W,1)-P(6,Z,-1))*D
def A(s,c):
 for O,t in(((-15*c,-17*c),1),(n,2),(g,6)):
  for o in O:
   x=s+o
   if not x&136 and B[x]==t*c:return 1
 for O,t in((h,(3,5)),(j,(4,5))):
  for e in O:
   x=s+e
   while not x&136:
    p=B[x]
    if p:
     if p//c in t:return 1
     break
    x+=e
 return 0
def il(c):return A(W if c>0 else Z,-c)
def G(p):
 m=[]
 for s,q in enumerate(B):
  if s&136 or q*D<=0:continue
  t=q*D
  if t==1:
   e=16*D;r=s>>4;R=(6,1)[D>0];v=r==7-R
   for o in(s+e,s+15*D,s+17*D):
    if o&136:continue
    w=B[o]
    if o==s+e:
     if w:continue
     if not p and r==R and B[o+e]==0:m.append((s,o+e,0))
    elif w*D>=0:continue
    if v:m.append((s,o,5))
    elif not p or w:m.append((s,o,0))
  elif t==2 or t==6:
   for o in(n if t==2 else g):
    x=s+o
    if not x&136 and B[x]*D<=0 and(not p or B[x]):m.append((s,x,0))
  else:
   for e in(h if t==3 else j if t==4 else h+j):
    x=s+e
    while not x&136 and not B[x]:
     if not p:m.append((s,x,0))
     x+=e
    if not x&136 and B[x]*D<0:m.append((s,x,0))
 if not p:
  for k,t,r,o,q in(((4,6,7,-1,(5,6)),(4,2,0,-1,(1,2,3)))if D>0 else((116,118,119,1,(117,118)),(116,114,112,1,(113,114,115)))):
   if B[k]==-6*o and B[r]==-4*o and all(B[x]==0 for x in q)and not(A(k,o)or A(q[-2],o)or A(q[-1],o)):m.append((k,t,0))
 return m
def mk(m):
 global S,W,Z,D
 f,t,q=m;p=B[f];c=D;e=p*c;v=B[t]
 U.append((f,t,q,v,c,S,W,Z))
 S-=c*(V[e]+P(e,f,c));k=q or e;S+=c*(V[k]+P(k,t,c))
 if v:S+=c*(V[-v*c]+P(-v*c,t,-c))
 B[f]=0;B[t]=c*k
 if e==6:
  if c>0:W=t
  else:Z=t
  if t-f==2:B[f+3]=0;B[f+1]=c*4
  elif f-t==2:B[f-4]=0;B[f-1]=c*4;S+=5*c
 D=-c
def um():
 global S,W,Z,D
 f,t,q,v,c,S,W,Z=U.pop()
 B[f]=c if q else B[t];B[t]=0
 if v:B[t]=v
 if not q and abs(t-f)==2 and abs(B[f])==6:
  if t>f:B[f+3]=B[f+1];B[f+1]=0
  else:B[f-4]=B[f-1];B[f-1]=0
 D=c
def od(m,z):
 s=[]
 for x in m:
  w=0
  if x==z:w=10**7
  else:
   f,t,q=x;v=B[t]
   if v:w=10**6+10*abs(v)-abs(B[f])
   if q:w+=10**6+V[q]
  s.append((-w,x))
 s.sort()
 return[x for _,x in s]
def qs(a,b,y):
 global N
 N+=1
 if N>=L:raise X
 if y>100:return ev()
 c=D;v=A(W if c>0 else Z,-c);o=-10**9
 if not v:
  o=ev()
  if o>=b:return b
  if o>a:a=o
 for m in od(G(0 if v else 1),0):
  mk(m)
  if il(c):um();continue
  s=-qs(-b,-a,y+1);um()
  if s>o:o=s
  if s>a:a=s
  if a>=b:break
 return o if v else a
def sc(d,a,b,y):
 global N,Q
 N+=1
 if N>=L:raise X
 if d<=0:return qs(a,b,y)
 k=(tuple(B),D);z=T.get(k,0)
 c=D;o=-10**9;w=0
 for m in od(G(0),z):
  mk(m)
  if il(-D):um();continue
  s=-sc(d-1,-b,-a,y+1);um()
  if s>o:o=s;w=m
  if s>a:a=s
  if a>=b:break
 if o==-10**9:return-100000+y if A(W if D>0 else Z,-D) else 0
 T[k]=w
 if y==0:Q=w
 return o
def su(o):
 global S,W,Z,D,N
 B[:]=[0]*128;S=W=Z=0;N=0;U.clear();T.clear()
 w=o.split();s=112
 for ch in w[0]:
  if ch=='/':s-=24
  elif ch.isdigit():s+=int(ch)
  else:
   c=1 if ch.isupper() else -1;t='pnbrqk'.index(ch.lower())+1;B[s]=c*t
   if t==6:W,Z=(s,Z)if c>0 else(W,s)
   else:S+=c*(V[t]+P(t,s,c))
   s+=1
 D=2*(w[1]=='w')-1
def uc(m):
 f,t,q=m
 return I[f&7]+str((f>>4)+1)+I[t&7]+str((t>>4)+1)+(''if not q else'nbrq'[q-2])
def be(o,y,z):
 global L
 su(o);L=40000+50000*(z<100)
 for d_ in range(1,10):
  try:r=sc(d_,-100001,100001,0)
  except X:break
  if r>90000:break
 u=uc(Q)
 return u if u in y else y[0]
while(z:=rq('/game',{}))['status']!='done':
 while z['status']=='your_move':
  y=z['legal_moves']
  try:u=be(z['fen'],y,z['plies'])
  except:u=y[0]
  z=rq('/move',{'game':z['game'],'move':u})
