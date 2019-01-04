import time
import hungarian

# distance measure
def cal_dist(p,b):
    return abs(p[0]-b[0])+abs(p[1]-b[1])

# fetch data
data=[list(map(int,line.strip().split(" "))) for line in open("data.txt").readlines() if (line.startswith("#")==False and len(line)>0)]

# visualization
m,n=data[0]
people=data[1:m+1]
bikes=data[m+1:]
max_y=max([d[0] for d in data[1:]])
max_x=max([d[1] for d in data[1:]])

vis=[["O" for _ in range(max_x+1)] for __ in range(max_y+1)]

for p in people:
    vis[p[0]][p[1]]="P"
for b in bikes:
    vis[b[0]][b[1]]="B"

print("MAP:")
[print("".join(line)) for line in vis]
print()

print("SOLUTION:")
# algorithm (metrics, {(p_i, b_i)})
t0=time.time()
solution = hungarian.solve(people, bikes)
t1=time.time()
print("algorithm took %.4f sec"%(t1-t0))
print("optimal distance is %d"%(solution[0]))
for (p,b) in solution[1]:
    print("person[%d](%d,%d) -> bike[%d](%d,%d) = %d"%(p,people[p][0],people[p][1],b,bikes[b][0],bikes[b][1],cal_dist(people[p],bikes[b])))
