import ast
from pathlib import Path
import numpy as np
from scipy.optimize import minimize
from scipy.spatial import Delaunay
src=next(Path('ved_read').rglob('051_bulk_relaxation_phase2/bulk_relaxation_phase2.py'))
tree=ast.parse(src.read_text()); tree.body=[n for n in tree.body if getattr(n,'name','') in {'delaunay_edges','relax_nd','spring_energy_nd','spring_grad_nd'}]; exec(compile(tree,str(src),'exec'))
rng=np.random.default_rng(20260702)
for n in (80,160,320):
 x=rng.uniform(0,n**(1/3),size=(n,3)); t=Delaunay(x).simplices; e=delaunay_edges(t)
 i,j=np.array(e).T; x=x/np.mean(np.linalg.norm(x[i]-x[j],axis=1)); energy,y=relax_nd(x,e)
 b=y[i]-y[j]; lengths=np.linalg.norm(b,axis=1); u=b/lengths[:,None]
 Q=(u.T*(lengths-1))@u/len(e); Q-=np.eye(3)*np.trace(Q)/3
 vol=lambda z:np.linalg.det(z[t[:,1:]]-z[t[:,:1]])
 print(n,energy/n,np.linalg.eigvalsh(Q),np.mean(vol(x)*vol(y)<0),flush=True)
 W=(u.T*((lengths-1)*lengths))@u/len(e); print("virial eigenvalues",np.linalg.eigvalsh(W),flush=True)
 np.save('Q'+str(n),Q)
