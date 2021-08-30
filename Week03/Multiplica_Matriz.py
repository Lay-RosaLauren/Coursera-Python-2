def mat_mul (A, B):
    num_lin_A, num_col_A = len(A), len(A[0])
    num_lin_B, num_col_B = len(B), len(B[0])
    assert num_col_A == num_lin_B
    
    C = []
    for linha in range(num_lin_A):
        # Começando uma nova linha
        C.append([])
        for coluna in range(num_col_B):
            # Adicionando uma nova coluna na linha
            C[linha].append(0)
            for k in range(num_col_A):
                C[linha][coluna] += A[linha][k] * B[k][coluna]
    return C            
            
        
    
if __name__ == '__main__':
    A = [[1, 2, 3], [4, 5, 6]]
    B = [[1, 2], [3, 4], [5, 6]]
    print(mat_mul(A, B))



    



#exemplo

    #1 2 3     1 2     22 28
              
    #4 5 6  *  3 4  =  49 64

              #5 6

    #1*1 + 2*3 + 3*5 = 22
    #1*2 + 2*4 + 3*6 = 28
    #4*1 + 5*3 + 6*5 = 49
    #4*2 + 5*4 + 6*6 = 64
