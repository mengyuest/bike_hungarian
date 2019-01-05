# input: [X, Y]
# output: [dist, matching case]
def solve(dist_mat, people, bikes):
    m=len(dist_mat)
    n=len(dist_mat[0])

    def dfs(assigned, free):
        if len(assigned)==m:
            return 0,assigned
        else:
            min_value=65535
            min_assigned=None
            for x in free:
                tp=dfs(assigned + [x], free-{x})
                curr_value=dist_mat[len(assigned)][x] + tp[0]
                if min_value > curr_value:
                    min_value = curr_value
                    min_assigned = tp[1]
            return min_value,min_assigned
    
    query = dfs([], set([x for x in range(n)]))
    return query[0], [(i,x) for i,x in enumerate(query[1])]
