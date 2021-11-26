def prim_algorithm(adj):

    n = len(adj)
    key = [10001]*n
    key[0] = 0
    vertice_set = [None] *n
    vertice_set[0] = -1
    final_mst = [False] * n

    def minimum_key(key,final_mst):
        minimum = 10001
        minimum_index = 0
        for i in range(n):
            if (key[i] < minimum) and (final_mst[i] == False):
                minimum = key[i]
                minimum_index = i

        return minimum_index

    def printer():
        ans_mst = [[False for column in range(n)]
                   for row in range(n)]

        for i in range(1, n):
            ans_mst[i][vertice_set[i]] = True
            ans_mst[vertice_set[i]][i] = True

        return ans_mst


    for _ in range(n):
        mdv = minimum_key(key,final_mst)
        final_mst[mdv] = True

        for vertice in range(n):
            if adj[mdv][vertice] > 0 and final_mst[vertice] == False and key[vertice]>adj[mdv][vertice]:
                key[vertice] = adj[mdv][vertice]
                vertice_set[vertice] = mdv


    return printer()



# The assignment has 10 test cases.
# Store indices of the test cases you want to skip.
# For example,
# [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] => skip all test cases
# [9, 10] => skip test case #9 and #10
# [] => enable all test cases
skip_grading = []


def main():
    '''
    This function is only used when the "Run (실행)" button is clicked.
    The grader calls prim_algorithm directly.
    '''
    adj_example = [
        [0, 7, 0, 0, 1],
        [7, 0, 6, 0, 5],
        [0, 6, 0, 2, 3],
        [0, 0, 2, 0, 4],
        [1, 5, 3, 4, 0]
    ]
    n = len(adj_example)
    mst = prim_algorithm(adj_example)
    for i in range(n):
        s = ''
        for j in range(n):
            s += str(mst[i][j]) + ' '
        print(s)


if __name__ == '__main__':
    main()