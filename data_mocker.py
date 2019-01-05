import random
import argparse

parser = argparse.ArgumentParser(description='data mocker to generate arbitrary data for testing')
parser.add_argument('--data_file', type=str, help='path to the data file')

parser.add_argument('--height', type=int, help='height of the map')
parser.add_argument('--width', type=int,  help='width of the map')
parser.add_argument('--num_people', type=int, help='number of people')
parser.add_argument('--num_bikes', type=int, help='number of bikes')
args = parser.parse_args()

if args.num_people>args.num_bikes:
    print("people must be less than bikes, however is (%d,%d), now exit..."%(args.num_people,args.num_bikes))
    exit()

# generate random matrix
indices = random.sample([x for x in range(args.height*args.width)], args.num_people+args.num_bikes)

# write to file
with open(args.data_file,"w") as f:
    f.write(
    """# pound key for linewise comment
# m n // m ~ #(human), n ~ #(bikes), m<n
# x_0 y_0 
# x_1 y_1 
# ...
# x_{m+n-1} y_{m+n-1} // m lines for human coords, then n lines for bike coords
#
# example:
# 2 3
# 1 0
# 0 1
# 3 3
# 0 2
# 2 2
#
#.---->(y)
#|OPBO
#|POOO
#|OOBO
#|OOOB
#v(x)
#
# optimal:=1+3=4
#)
""")
    f.write("%d %d\n"%(args.num_people,args.num_bikes))
    for x in indices:
        f.write("%d %d\n"%(x//args.width, x%args.width))


data=[list(map(int,line.strip().split(" "))) for line in open(args.data_file).readlines() if (line.startswith("#")==False and len(line)>0)]

# visualization
m,n=data[0]
people=data[1:m+1]
bikes=data[m+1:]
max_x=max([d[0] for d in data[1:]])
max_y=max([d[1] for d in data[1:]])

vis=[["O" for _ in range(max_y+1)] for __ in range(max_x+1)]

for p in people:
    vis[p[0]][p[1]]="P"
for b in bikes:
    vis[b[0]][b[1]]="B"

print("MAP:")
print("."+"-"*len(vis[0])+">(y)")
[print("|"+"".join(line)) for line in vis]
print("v(x)\n")