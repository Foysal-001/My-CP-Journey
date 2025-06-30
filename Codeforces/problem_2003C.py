for s in[*open(0)][2::2]:
 i=1;j=len(a:=sorted(s))-1;r=''
 while i<=j:r+=a[i]+a[j]*(i<j);i+=1;j-=1
 print(r)