import json,os,urllib.request
q=lambda t:[ord(c)-100 for c in t]
V=os.environ.get("MAKEFUN_ENV_URL")
# node budget per search depth: bigger is stronger but slower
H=130000
n={'P':100,'N':320,'B':330,'R':500,'Q':900,'K':0}
W=lambda b,m:(n.get(b[m[1]].upper(),0)*10-n[b[m[0]].upper()],)
t=lambda b,m:b[m[1]]!='.' and b[m[1]].upper()=='K'
I=33,31,18,14,-33,-31,-18,-14
C=17,16,15,1,-17,-16,-15,-1
J=17,15,-17,-15
K=16,1,-16,-1
L={0:'Q',7:'K',4:'KQ',112:'q',119:'k',116:'kq'}
X=q('ddddddddinnPPnnii_ZddZ_idddxxdddiin}}niinnx\x82\x82xnn\x96\x96\x96\x96\x96\x96\x96\x96dddddddd')
Y=q('2<FFFF<2<PdiidP<FinssniFFdsxxsdFFisxxsiFFdnssndF<PddddP<2<FFFF<2')
M=q('PZZZZZZPZiddddiZZnnnnnnZZdnnnndZZiinniiZZdinnidZZddddddZPZZZZZZP')
N=q('ddiidddd_dddddd__dddddd__dddddd__dddddd__dddddd_innnnnnidddddddd')
Z=q('x\x82nddn\x82xxxddddxxZPPPPPPZPFF<<FFPF<<22<<FF<<22<<FF<<22<<FF<<22<<F')
aa=q('2FFFFFF2FFddddFFFZx\x82\x82xZFFZ\x82\x8c\x8c\x82ZFFZ\x82\x8c\x8c\x82ZFFZx\x82\x82xZFFPZddZPF2<FPPF<2')
j=0
def O(fen):
 b=['.']*128
 parts=fen.split()
 rows=parts[0].split('/')
 for r,row in enumerate(rows):
  f=0
  rank=7-r
  for c in row:
   if c.isdigit():
    f+=int(c)
   else:
    b[rank*16+f]=c
    f+=1
 s=1 if parts[1]=='w' else-1
 ep=None
 if parts[3]!='-':
  ep=(int(parts[3][1])-1)*16+"abcdefgh".index(parts[3][0])
 cr=parts[2].replace('-','')
 return b,s,ep,cr
def l(b,sq,s):
 for p,ds in(('Pp'[s<0],(15,17)if s<0 else(-15,-17)),('Nn'[s<0],I),('Kk'[s<0],C)):
  for d in ds:
   t=sq+d
   if not t&0x88 and b[t]==p:
    return True
 bq=('B','Q')if s==1 else('b','q')
 rq=('R','Q')if s==1 else('r','q')
 for ds,pcs in((J,bq),(K,rq)):
  for d in ds:
   t=sq+d
   while not t&0x88:
    if b[t]!='.':
     if b[t]in pcs:
      return True
     break
    t+=d
 return False
def y(b,s,ep,cr,caps=False):
 ms=[]
 pm=lambda f,t:ms.append((f,t,'q')if(t>>4)in(0,7)else(f,t,None))
 for i in range(128):
  if i&0x88:
   continue
  p=b[i]
  if p=='.' or(p.isupper()!=(s==1)):
   continue
  u=p.upper()
  if u=='P':
   fwd=16*s
   t=i+fwd
   if not caps and not t&0x88 and b[t]=='.':
    pm(i,t)
    if(i>>4)==(1 if s==1 else 6)and b[t+fwd]=='.':
     ms.append((i,t+fwd,None))
   for d in(fwd-1,fwd+1):
    t=i+d
    if not t&0x88:
     if b[t]!='.' and b[t].isupper()!=(s==1):
      pm(i,t)
     elif t==ep:
      ms.append((i,t,None))
  elif u in 'NK':
   for d in(I if u=='N' else C):
    t=i+d
    if not t&0x88 and(b[t]=='.' or b[t].isupper()!=(s==1)):
     if not caps or b[t]!='.':
      ms.append((i,t,None))
   if not caps and u=='K':
    ks=(0 if s==1 else 7)*16+4
    if i==ks:
     e='Kk'[s<0]
     q='Q' if s==1 else 'q'
     o='R' if s==1 else 'r'
     if e in cr and b[ks+1]==b[ks+2]=='.' and b[ks+3]==o and not l(b,ks,-s)and not l(b,ks+1,-s):
      ms.append((ks,ks+2,None))
     if q in cr and b[ks-1]==b[ks-2]==b[ks-3]=='.' and b[ks-4]==o and not l(b,ks,-s)and not l(b,ks-1,-s):
      ms.append((ks,ks-2,None))
  else:
   dirs=J if u=='B' else K if u=='R' else C
   for d in dirs:
    t=i+d
    while not t&0x88:
     if b[t]=='.':
      if not caps:
       ms.append((i,t,None))
     else:
      if b[t].isupper()!=(s==1):
       ms.append((i,t,None))
      break
     t+=d
 return ms
def w(b,s,ep,cr,m):
 f,t,pr=m
 nb=b[:]
 p=nb[f]
 nb[f]='.'
 nep=None
 if p in 'Pp':
  if t==ep and nb[t]=='.':
   nb[t-16*s]='.'
  if(t>>4)in(0,7):
   p=pr.upper()if s==1 else pr
  elif abs(t-f)==32:
   nep=f+16*s
 elif p in 'Kk':
  if t-f==2:
   nb[f+1]=nb[f+3]
   nb[f+3]='.'
  elif f-t==2:
   nb[f-1]=nb[f-4]
   nb[f-4]='.'
 nb[t]=p
 ncr=''.join(c for c in cr if c not in L.get(f,'')and c not in L.get(t,''))
 return nb,nep,ncr
def D(b):
 sc=0
 phase=0
 wk=bk=-1
 wb=bb=0
 for i,p in enumerate(b):
  if p=='.':
   continue
  s=1 if p.isupper()else-1
  u=p.upper()
  r=i>>4
  f=i&15
  r2=r if s==1 else 7-r
  v=n[u]
  if u=='N':
   v+=Y[r2*8+f]
   phase+=1
  elif u=='B':
   v+=M[r2*8+f]
   phase+=1
  elif u=='R':
   v+=N[r2*8+f]
   phase+=2
  elif u=='Q':
   v+=(N[r2*8+f]+M[r2*8+f])//2
   phase+=4
  elif u=='P':
   v+=X[r2*8+f]
  else:
   if s==1:
    wk=(r,f)
   else:
    bk=(r,f)
  sc+=s*v
 wb+=p=='B'
 bb+=p=='b'
 if wk==-1:
  return-90000
 if bk==-1:
  return 90000
 if wb>1:sc+=30
 if bb>1:sc-=30
 e=min(phase,24)
 km=lambda r,f:(Z[r*8+f]*e+aa[r*8+f]*(24-e))//24
 sc+=km(wk[0],wk[1])-km(7-bk[0],bk[1])
 return sc
h=90000
class E(Exception):
 pass
def P(b,s,ep,a,bt,ply,d=0):
 global j
 j+=1
 if j>H:
  raise E
 if 'Kk'[s<0]not in b:
  return s*90000
 stand=s*D(b)
 ks=b.index('Kk'[s<0])
 chk=l(b,ks,-s)
 if not chk:
  if stand>=bt:
   return stand
  if stand>a:
   a=stand
  ms=y(b,s,ep,'',caps=True)
 else:
  ms=y(b,s,ep,'')
  if not ms:
   return-h+ply
 ms.sort(key=lambda m:n.get(b[m[1]].upper(),0)*10-n[b[m[0]].upper()],reverse=True)
 evs=chk
 anyev=False
 for m in ms:
  if t(b,m):
   return h-ply
  v0=n.get(b[m[1]].upper(),0)
  if not chk and a-stand>v0+200 and b[m[1]]!='.':
   continue
  nb,nep,ncr=w(b,s,ep,'',m)
  if evs and l(nb,nb.index('Kk'[s<0]),-s):
   continue
  anyev=True
  v=-P(nb,-s,nep,-bt,-a,ply+1,d+1)
  if v>=bt:
   return v
  if v>a:
   a=v
 if evs and not anyev:
  return-h+ply
 return a
F={}
A={}
G={}
def Q(b,s,ep,cr,d,a,bt,ply,rep):
 global j
 j+=1
 if j>H:
  raise E
 key=(tuple(b),s,ep,cr)
 if ply and key in rep:
  return 0
 e=F.get(key)
 tm=None
 if e is not None:
  if e[0]>=d:
   v,f=e[1],e[2]
   if v>h-1000:
    v-=ply
   elif v<-h+1000:
    v+=ply
   if f==0 or(f==1 and v>=bt)or(f==2 and v<=a):
    return v
  tm=e[3]
 rep.add(key)
 try:
  oa=a
  if d<=0:
   return P(b,s,ep,a,bt,ply)
  if d>=3 and ply and not l(b,b.index('Kk'[s<0]),-s)and s*D(b)>-300:
   v=-Q(b,-s,ep,cr,d-3,-bt,-bt+1,ply+1,rep)
   if v>=bt:
    rep.discard(key)
    return v
  ms=y(b,s,ep,cr)
  if not ms:
   rep.discard(key)
   if l(b,b.index('Kk'[s<0]),-s):
    return-h+ply
   return 0
  kls=G.get(ply)
  ms.sort(key=lambda m:(t(b,m),W(b,m),m==tm,m==kls,A.get((b[m[0]],m[1]),0)),reverse=True)
  best=-2*h
  bm=None
  cut=None
  chk=d>2 and l(b,b.index('Kk'[s<0]),-s)
  red=d>2 and not chk
  anyred=False
  for mi,m in enumerate(ms):
   if t(b,m):
    rep.discard(key)
    return h-ply
   nb,nep,ncr=w(b,s,ep,cr,m)
   rm=red and mi>2 and b[m[1]]=='.' and m[2]is None
   if rm:
    anyred=True
   for dd in((d-2,d-1)if rm else(d-1,)):
    v=-Q(nb,-s,nep,ncr,dd,-bt,-a,ply+1,rep)
    if v>a and dd<d-1:
     continue
    break
   if v>best:
    best=v
    bm=m
    if v>a:
     a=v
     if a>=bt:
      cut=m
      break
  if cut is not None and b[cut[1]]=='.':
   G[ply]=cut
   hk=(b[cut[0]],cut[1])
   A[hk]=A.get(hk,0)+d*d
  f=1 if best>=bt else 0 if best>oa else 2
  sv=best
  if sv>h-1000:
   sv+=ply
  elif sv<-h+1000:
   sv-=ply
  if not anyred:
   F[key]=(d,f,sv,bm)
  if f==1:
   return best
 finally:
  rep.discard(key)
 return best
def ab(b,s,ep,cr):
 for m in y(b,s,ep,cr):
  nb,nep,ncr=w(b,s,ep,cr,m)
  if not l(nb,nb.index('Kk'[s<0]),-s):
   return True
 return False
def ac(fen,legal,moves,start_fen):
 global j,z
 u=B.get(' '.join(fen.split()[:2]))
 if u in legal:return u
 b,s,ep,cr=O(fen)
 hb,hs,hep,hcr=O(start_fen)
 hist=[(tuple(hb),hs,hep,hcr)]
 for u in moves:
  hb,hep,hcr=w(hb,hs,hep,hcr,R(u))
  hs=-hs
  hist.append((tuple(hb),hs,hep,hcr))
 lms=[R(m)for m in legal]
 F.clear()
 A.clear()
 G.clear()
 best=lms[0]
 rep0=set(hist)
 for d in range(1,40):
  j=0
  scores=[]
  rep=set(rep0)
  a=-2*h
  try:
   lms.sort(key=lambda m:m!=best)
   for m in lms:
    nb,nep,ncr=w(b,s,ep,cr,m)
    k=(tuple(nb),-s,nep,ncr)
    v=-Q(nb,-s,nep,ncr,d-1,-2*h,-a,1,rep)if k not in rep else 0
    scores.append((v,m))
    if v>a:
     a=v
  except E:
   break
  scores.sort(key=lambda x:-x[0])
  best=scores[0][1]
  if s*D(b)>60 or a>h-1000:
   for v,m in scores:
    nb,nep,ncr=w(b,s,ep,cr,m)
    if 'Kk'[s>0]not in nb:
     continue
    if ab(nb,-s,nep,ncr)or l(nb,nb.index('Kk'[s>0]),s):
     best=m
     break
  if a>h-1000 and(best==scores[0][1]or s*D(b)<=60):
   break
 return ad(best)
def R(u):
 f=S(u[:2])
 t=S(u[2:4])
 pr=u[4]if len(u)>4 else None
 return(f,t,pr)
def S(s):
 return(int(s[1])-1)*16+"abcdefgh".index(s[0])
def T(i):
 return "abcdefgh"[i&15]+str((i>>4)+1)
def ad(m):
 return T(m[0])+T(m[1])+(m[2]or '')
B={}
# Indent by ply: incoming move, reply.
p=[O('rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w - -')[0]]
for r in '''. e2e4
 e2e4 e7e5
  e7e5 g1f3
   g1f3 b8c6
    b8c6 f1b5
     f1b5 a7a6
      a7a6 b5a4
       b5a4 g8f6
        g8f6 e1g1
     f1c4 f8c5
      f8c5 c2c3
       c2c3 g8f6
        g8f6 d2d4
      g8f6 d2d3
     d2d4 e5d4
      e5d4 f3d4
       f3d4 g8f6
        g8f6 b1c3
    g8f6 f3e5
    d7d6 d2d4
    f7f5 f3e5
   f1c4 g8f6
    g8f6 d2d3
    f8c5 g1f3
    b8c6 g1f3
   b1c3 g8f6
    g8f6 f2f4
   f2f4 e5f4
    e5f4 g1f3
    f8c5 g1f3
   d2d4 e5d4
    e5d4 d1d4
   d1h5 b8c6
  c7c5 g1f3
   g1f3 d7d6
    d7d6 d2d4
    b8c6 d2d4
    e7e6 d2d4
    a7a6 c2c3
   c2c3 g8f6
    g8f6 e4e5
    d7d5 e4d5
   b1c3 b8c6
    b8c6 g1f3
   d2d4 c5d4
    c5d4 c2c3
   f2f4 d7d5
  e7e6 d2d4
   d2d4 d7d5
    d7d5 b1c3
   g1f3 d7d5
  c7c6 d2d4
   d2d4 d7d5
    d7d5 e4e5
   b1c3 d7d5
  d7d5 e4d5
   e4d5 d8d5
    d8d5 b1c3
    g8f6 d2d4
  g8f6 e4e5
   e4e5 f6d5
    f6d5 d2d4
  d7d6 d2d4
   d2d4 g8f6
    g8f6 b1c3
    g7g6 b1c3
  g7g6 d2d4
   d2d4 f8g7
    f8g7 b1c3
  b8c6 g1f3
   g1f3 e7e5
 d2d4 d7d5
  d7d5 c2c4
   c2c4 e7e6
    e7e6 b1c3
     b1c3 g8f6
      g8f6 c1g5
       g1f3 c7c6
        c7c6 e2e3
    c7c6 g1f3
     g1f3 g8f6
      g8f6 b1c3
       b1c3 d5c4
        d5c4 a2a4
    d5c4 e2e3
    e7e5 d4e5
   g1f3 g8f6
    g8f6 c2c4
   c1f4 g8f6
    g8f6 e2e3
    c7c5 e2e3
  g8f6 c2c4
   c2c4 e7e6
    e7e6 b1c3
    g7g6 b1c3
    c7c5 d4d5
   g1f3 d7d5
    e7e6 c2c4
    g7g6 c2c4
   c1g5 f6e4
    f6e4 g5f4
   c1f4 d7d5
  e7e6 c2c4
   c2c4 d7d5
  f7f5 g2g3
   g2g3 g8f6
    g8f6 f1g2
  c7c5 d4d5
   d4d5 g8f6
    g8f6 b1c3
 c2c4 e7e5
  e7e5 b1c3
   b1c3 g8f6
    g8f6 g1f3
  c7c5 g1f3
   g1f3 g8f6
  g8f6 b1c3
   b1c3 e7e5
 g1f3 d7d5
  d7d5 d2d4
  g8f6 d2d4
 g2g3 d7d5
 f2f4 d7d5
 b1c3 d7d5'''.splitlines():
 u,m=r.split()
 d=r.index(u)
 if d:p[d:]=[w(p[d-1],(-1)**(d-1),None,'',R(u))[0]]
 k='/'.join(''.join(p[d][i:i+8])for i in range(112,-1,-16))
 for i in range(8,0,-1):k=k.replace('.'*i,str(i))
 B[k+' '+'wb'[d%2]]=m
def U(path,body):
 rq=urllib.request.Request(V+path,data=json.dumps(body).encode(),headers={"content-type":"application/json"})
 return json.load(urllib.request.urlopen(rq))
def ae():
 while True:
  g=U("/game",{})
  if g["status"]=="done":
   break
  while g["status"]=="your_move":
   u=ac(g["fen"],g["legal_moves"],g["moves"],g["start_fen"])
   g=U("/move",{"game":g["game"],"move":u})
ae()
