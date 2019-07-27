msv,ris=list(map(int,input().split()))
lis2=list(map(int,input().split()))
for i in range(ris):
  x1,y1=list(map(int,input().split()))
  print(sum(lis2[x1-1:y1]))
