import numpy as np,itertools as it
from scipy.spatial.distance import cdist
p=(1+5**.5)/2
v=[s*x for x in np.eye(4) for s in (-1,1)]+[np.array(t)/2 for t in it.product([-1,1],repeat=4)]
for perm in it.permutations(range(4)):
 if sum(i>j for i,j in it.combinations(perm,2))%2:continue
 for a,b,c in it.product([-1,1],repeat=3):
  v.append(np.array([0,a,b*p,c/p])[list(perm)]/2)
v=np.array(v);adj=np.isclose(cdist(v,v),1/p)
edges=list(zip(*np.where(np.triu(adj,1))))
dirs=[]; em={}
for i,j in edges:
 a,x=v[i,0],v[i,1:];b,y=v[j,0],v[j,1:]
 d=a*y-b*x-np.cross(x,y);s=np.sign(d[np.where(abs(d)>1e-7)[0][0]]);d=d*s
 k=next((k for k,x in enumerate(dirs) if np.allclose(d,x)),len(dirs))
 if k==len(dirs):dirs.append(d)
 em[i,j]=(k,s)
B=[]
for i,j in edges:
 for k in np.where(adj[i]&adj[j]&(np.arange(120)>j))[0]:
  row=np.zeros(6)
  for e,s in [((i,j),1),((j,k),1),((i,k),-1)]:
   h,t=em[e];row[h]+=s*t
  B.append(row)
B=np.array(B); M=B.T@B/120; D=np.array(dirs);lam=np.vdot(D,M@D)/np.vdot(D,D)
print(len(edges),len(B),np.linalg.eigvalsh(M),lam,np.max(abs(M@D-lam*D)))
from scipy.linalg import eigvalsh
faces=[(i,j,k) for i,j in edges for k in np.where(adj[i]&adj[j]&(np.arange(120)>j))[0]]
fid={f:i for i,f in enumerate(faces)}
tets=[(i,j,k,l) for i,j,k in faces for l in np.where(adj[i]&adj[j]&adj[k]&(np.arange(120)>k))[0]]
def spec(stretch):
 m1=np.zeros(6); m2=np.zeros(len(faces))
 for t in tets:
  g=np.zeros((4,4))
  for i,j in it.combinations(range(4),2):
   g[i,j]=g[j,i]=(stretch[em[t[i],t[j]][0]]/p)**2
  G=(g[0,1:,None]+g[0,None,1:]-g[1:,1:])/2
  x=np.vstack((np.zeros(3),np.linalg.cholesky(G))); ct=np.linalg.solve(2*x[1:],np.diag(G))
  for f in it.combinations(range(4),3):
   a,b,c=x[list(f)]; T=np.stack((b-a,c-a)); cf=a+T.T@np.linalg.solve(2*T@T.T,np.diag(T@T.T)); height=np.linalg.norm(ct-cf)
   m2[fid[tuple(t[i] for i in f)]]+=height/(np.linalg.norm(np.cross(*T))/2)
   for i,j in it.combinations(f,2):
    m1[em[t[i],t[j]][0]]+=.5*height*np.linalg.norm(cf-(x[i]+x[j])/2)/np.linalg.norm(x[i]-x[j])
 print(np.sqrt(eigvalsh(B.T@(m2[:,None]*B),np.diag(m1))))

vdir=D/np.linalg.norm(D,axis=1)[:,None]
spec(np.ones(6))
for n in (80,160,320):
 Q=np.load('Q'+str(n)+'.npy')
 scales=1+np.einsum('ij,jk,ik->i',vdir,Q,vdir)
 print('size',n,'edge scales',scales)
 spec(scales)
