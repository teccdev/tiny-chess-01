import json,os,urllib.request as u,zlib,base64
E=os.environ["MAKEFUN_ENV_URL"]
def R(p,d={}):
 try:return json.load(u.urlopen(u.Request(E+p,json.dumps(d).encode())))
 except:return R(p,d)
S={x+str(r):ord(x)-97+8*r-8 for x in"abcdefgh"for r in range(1,9)}
V=dict(p=100,n=320,b=330,r=500,q=900,k=10000)
X=zlib.decompress(base64.b85decode('c-qB~Ef&Nu2!wA~9gRkhsTqSA6N9PAA@+m|X)9OnCqkIVJbuWVkldw+6C}<kDYNy^b(JjTS}A=V9vhEg#W;pnDScRIPK6m~=A>D4?7Vea)fGNopJU^QJq4f*zzzhub(G!{M&)-~ygvS!Tq3n{AFECV-@t3RTG8u0j{g0KUuRCaD*'))
P={k:[z-128 for z in X[i*64:i*64+64]] for i,k in enumerate("pnbrqk")}
ky=lambda m:-V.get(b[m>>6&63].lower(),0)
Y={v:k for k,v in S.items()}
N=[(1,2),(2,1),(2,-1),(1,-2),(-1,-2),(-2,-1),(-2,1),(-1,2)]
K=[(1,0),(1,1),(0,1),(-1,1),(-1,0),(-1,-1),(0,-1),(1,-1)]
G=[(1,1),(1,-1),(-1,1),(-1,-1)]
D=[(1,0),(-1,0),(0,1),(0,-1)]
T="nbrq";Q=range(64)
b=[];w=1;e=-1;h=[];n=0;Z=400000;RP={};M=1
def ld(F):
 global b,w,e
 g=F.split();b=["."]*64;i=56
 for x in g[0]:
  if x=="/":i-=16
  elif x.isdigit():i+=int(x)
  else:b[i]=x;i+=1
 w=g[1]=="w";e=S.get(g[3],-1)
def C():
 global w
 w=1-w;z=[x>>6&63 for x in g()];w=1-w
 k="K"if w else"k"
 return k in b and b.index(k)in z
def g():
 ms=[];W=w
 for s in Q:
  p=b[s]
  if p=="."or p.isupper()!=W:continue
  l=p.lower();f=s&7;r=s>>3
  if l=="p":
   d=8-16*(1-W);t=s+d
   if t in Q and b[t]==".":
    if t>55 or t<8:
     for k in 1,2,3,4:ms.append(s|t<<6|k<<12)
    else:
     ms.append(s|t<<6)
     if r in(1,6)and b[t+d]==".":ms.append(s|(t+d)<<6)
   for j in(-1,1):
    t=s+d+j
    if 0<=f+j<8 and t in Q:
     q=b[t]
     if q!="."and q.isupper()!=W:
      if t>55 or t<8:
       for k in 1,2,3,4:ms.append(s|t<<6|k<<12)
      else:ms.append(s|t<<6)
     elif t==e:ms.append(s|t<<6)
  elif l in"nk":
   for x,y in(N if l=="n"else K):
    if 0<=f+x<8 and 0<=r+y<8:
     t=f+x+8*r+8*y;q=b[t]
     if q=="."or q.isupper()!=W:ms.append(s|t<<6)
  else:
   for x,y in(G+D if l=="q"else G if l=="b"else D):
    X=f+x;Y=r+y
    while 0<=X<8 and 0<=Y<8:
     t=X+8*Y;q=b[t]
     if q==".":ms.append(s|t<<6)
     else:
      if q.isupper()!=W:ms.append(s|t<<6)
      break
     X+=x;Y+=y
 return ms
def mk(m):
 global e,w
 f=m&63;t=m>>6&63;p=m>>12;q=b[f];h.append((q,b[t],e,m));b[t]=q;b[f]="."
 if q in"Pp"and t==e:b[t-8 if q=="P"else t+8]="."
 if p:b[t]=(T[p-1],T[p-1].upper())[q<"a"]
 if q in"Kk"and t-f in(2,-2):
  if t>f:b[f+1]=b[f+3];b[f+3]="."
  else:b[f-1]=b[f-4];b[f-4]="."
 e=(t+f)//2 if q in"Pp"and t-f in(16,-16)else -1
 w=1-w
def um():
 global e,w
 q,z,E,m=h.pop();f=m&63;t=m>>6&63;b[f]=q;b[t]=z
 if q in"Pp"and t==E:b[t-8 if q=="P"else t+8]="p"if q=="P"else"P"
 if q in"Kk"and t-f in(2,-2):
  if t>f:b[f+3]=b[f+1];b[f+1]="."
  else:b[f-4]=b[f-1];b[f-1]="."
 e=E;w=1-w
def v():
 s=0;t=[0,0]
 for i in Q:
  p=b[i]
  if p!=".":
   l=p.lower();y=V[l]+P[l][i if p<"a"else i^56]
   s+=y if p<"a"else-y
   t[p<"a"]+=V[l]*(l<"k")
 if s*s>16e4 and"K"in b and"k"in b and t[s<0]<500:k,K=b.index("k"),b.index("K");s+=(14-abs(k%8-K%8)-abs(k//8-K//8))*16*(s>0 or-1)
 return s if w else-s
def ne(d,a,z):
 global n
 n+=1
 if w==M and''.join(b)in RP:return 0
 if n>Z:return v()
 if d<1:
  s=v();B=s
  if d>-2 and C():
   ms=g();B=-99999
   if not ms:return -30000
  else:
   if s>=z:return s
   if s>a:a=s
   ms=[m for m in g()if b[m>>6&63]!="."]
 else:
  B=-99999;ms=g()
  if not ms:return -30000+d if C()else 0
 ms.sort(key=ky)
 for m in ms:
  mk(m);y=-ne(d-1,-z,-a);um()
  if y>B:
   B=y
   if y>a:a=y
   if a>=z:break
 return B
def Bz(lg):
 global n,Z
 ms=[]
 for m in lg:
  f=S[m[:2]];t=S[m[2:4]];p=T.find(m[4])+1 if len(m)>4 else 0
  ms.append(f|t<<6|p<<12)
 ms.sort(key=ky)
 o=ms[0];n=0;Z=200000
 for d in range(1,9):
  r=None;y=-99999;a=-99999
  for m in ms:
   mk(m);x=-ne(d-1,-99999,-a);um()
   if x>y:y=x;r=m
   if x>a:a=x
  if n>Z:break
  o=r;ms=[r]+[m for m in ms if m!=r]
 p=o>>12
 return Y[o&63]+Y[o>>6&63]+(T[p-1]if p else"")
x=R("/game")
while x["status"]!="done":
 if x["status"]=="your_move":
  ld(x["fen"]);q=''.join(b);RP[q]=-~RP.get(q,0);M=w;x=R("/move",{"game":x["game"],"move":Bz(x["legal_moves"])})
 else:x=R("/game")
