def P(m,l,q):
  k = l
  p = 1
  while k<m+1:
    p*=(1+q)
    k+=1
  return p
  
def f1(m,n,q1,q2,p,S):
  l = 2
  S2 = 0
  while l<m+1:
    S2+= P(m,l,q1)
    l+=1
  S2*=p
  S1 = S*((1+q1)**m)
  l = m+2
  S3 = 0
  while l<n+1:
    S3+=P(n,l,q2)
    l+=1
  S3*=p
  S3+=p
  S3/=P(n,m+1,q2)
  return S1-S2-p-S3
 
def MPD(f1,a,b,m,n,q2,p,S):
   while abs(b - a) > 10**(-6):
        q1 = (a + b) / 2.0      
        fx = f1(m,n,q1,q2,p,S)
        fa = f1(m,n,a,q2,p,S)
        fb = f1(m,n,b,q2,p,S)
        if (fa*fx>=0):
          a = q1
        elif(fx==0):
          return q1
        else:
          b = q1    
   return q1
   
for row in exchange.head().itertuples():
  day_lower_rate=row.lower/365

  S=1
  n=row.term
  r0=row.interest/12
  p=S*r0/(1-(1+r0)**(-n))
  m=math.ceil(n/4)
  q2=30*day_lower_rate
  a=0.3/365
  b=60/365

  q1 = MPD(f1,a,b,m,n,q2,p,S)
  x=365*q1/30
  print(x)

dir_name = '/mnt/zeppelin-exchange/i.sabaev/'
file_name = 'net.csv'
data.to_csv(dir_name + file_name, sep = ';', decimal = ',', encoding = 'cp1251')

print('(win) file://fs-nfsmb/zeppelin_exchange$/i.sabaev/' + file_name)
