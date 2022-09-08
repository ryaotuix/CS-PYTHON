def matrixProduct(A,B):
    if (len(A[1]) != len(B)): # if we can't do matrix mult
        return -1

    # check if the elements have smae length
    alen = len(A[1])
    blen = len(B[1])
    for i in range(len(A)):
        if len(A[i]) != alen:
            return -1
    for i in range(len(B)):
        if len(B[i]) != blen:
            return -1

    b_trans = transpose(B)
    nrow = len(A) # numbers of row 3
    ncol = len(b_trans) # numbers of column 4

    l = []
    for i in range(nrow):
        m = []
        for j in range(ncol):
            dp = dotproduct(A[i],b_trans[j])
            m.append(dp)
        l.append(m)

    return l
    # b_trans = []
    # b_row = len(B)
    # for i in range(ncol):
    #     tran_r = []
    #     for j in range(b_row):
    #         tran_r.append(B[j][i])
    #     b_trans.append(tran_r)


def transpose(B):
    b_trans = []
    ncol = len(B[1])
    b_row = len(B)
    for i in range(ncol):
        tran_r = []
        for j in range(b_row):
            tran_r.append(B[j][i])
        b_trans.append(tran_r)
    return (b_trans)

def dotproduct(a,b):
    sum = 0
    for i in range(len(a)):
        sum += a[i]*b[i]
    return sum

def main():

    A = [[1,2],
        [1,2],
        [2,3]]
    B = [[3,2,1,1],
        [1,2,3,1]]
    print(matrixProduct(A,B))


if __name__ == '__main__':
    # Do not change this part
    main()
