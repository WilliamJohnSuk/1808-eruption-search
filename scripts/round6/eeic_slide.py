import pandas as pd, numpy as np
d=pd.read_csv('/tmp/claude-0/work/eeic_at_anoms.csv.gz')
d['m']=(d.yr-1789)*12+d.mo-1
tr=d[d.lat.abs()<=30]
def step(m0,w=3,minn=8,drop=()):
    pre=tr[(tr.m>=m0-w)&(tr.m<m0)]; post=tr[(tr.m>=m0)&(tr.m<m0+w)]
    a=pre.groupby('file').anom.agg(['mean','size']); b=post.groupby('file').anom.agg(['mean','size'])
    j=a.join(b,lsuffix='_pre',rsuffix='_post',how='inner'); j=j[(j.size_pre>=minn)&(j.size_post>=minn)]
    j=j.loc[[not any(k in f for k in drop) for f in j.index]] if len(j) else j
    return len(j),(j.mean_post-j.mean_pre).mean(),(j.mean_post-j.mean_pre).std()/np.sqrt(max(len(j),1))
def lab(m): return f'{1789+m//12}-{m%12+1:02d}'
allm=[]
for m0 in range(12*1,12*45):
    n,s,se=step(m0); allm.append((m0,n,s))
A=pd.DataFrame(allm,columns=['m','n','step']).dropna(); A=A[A.n>=5]
ex=A[~A.m.between((1808-1789)*12,(1811-1789)*12)&~A.m.between((1815-1789)*12,(1818-1789)*12)]
print('null steps (3-mo window, n>=5 voyages): mean %.2f sd %.2f, 2.5%% %.2f, 1%% %.2f, N=%d'%(ex.step.mean(),ex.step.std(),ex.step.quantile(.025),ex.step.quantile(.01),len(ex)))
for y0,y1 in [(1808,1809),(1815,1816)]:
    print('--',y0)
    for m0 in range((y0-1789)*12+3,(y1-1789)*12+6):
        n,s,se=step(m0); n2,s2,se2=step(m0,drop=('Lord_Keith',))
        print(lab(m0),'n=%2d step=%+.2f se=%.2f | without Lord Keith %+.2f'%(n,s,se,s2))
