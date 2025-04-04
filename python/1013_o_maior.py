A, B, C = map(int, input().split())
MaiorAB = (A+B+abs(A-B))//2
MaiorFinal = (MaiorAB+C+abs(MaiorAB-C))//2
print(f'{MaiorFinal} eh o maior')
