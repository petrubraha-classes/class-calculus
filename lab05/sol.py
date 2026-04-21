import numpy as np
from numpy.linalg import norm, svd, inv, matrix_rank, cond

np.set_printoptions(precision=8, suppress=True, linewidth=120)

#analiza svd pentru p > n
def svd_analysis(A):
    p, n = A.shape
    #verificam sa fie matrice inalta
    assert p > n, f"trebuie p > n, avem {p}x{n}"
    
    #calculam svd propriu-zis
    U_svd, sigma, Vt = svd(A, full_matrices=True)
    V = Vt.T #il transpunem ca sa fie ca in formulele de la curs
    
    print(f"\ndim dimensiuni: A e {p}x{n}")
    
    #valorile singulare sunt deja sortate
    print(f"valori singulare (sigma): {sigma}")
    
    #rangul calculat in doua feluri
    #manual folosind o toleranta mica
    tol = max(p, n) * np.finfo(float).eps * sigma[0]
    rang_manual = np.sum(sigma > tol)
    rang_numpy = matrix_rank(A)
    
    print(f"rang manual: {rang_manual}")
    print(f"rang numpy: {rang_numpy}")
    
    #numarul de conditionare
    sigma_pos = sigma[sigma > tol]
    cond_manual = sigma_pos[0] / sigma_pos[-1]
    cond_numpy = cond(A)
    
    print(f"cond manual: {cond_manual:.8f}")
    print(f"cond numpy: {cond_numpy:.8f}")
    
    #pseudoinversa moore-penrose A^I
    #facem manual matricea S_I de n x p
    S_I = np.zeros((n, p))
    for i in range(len(sigma)):
        if sigma[i] > tol:
            S_I[i, i] = 1.0 / sigma[i]
    
    A_I = V @ S_I @ U_svd.T
    print("\npseudoinversa moore-penrose (A_I):")
    print(A_I)
    
    #pseudoinversa least-squares A^J
    #asta merge doar daca rangul e maxim
    AtA = A.T @ A
    try:
        AtA_inv = inv(AtA)
        A_J = AtA_inv @ A.T
        print("\npseudoinversa least-squares (A_J):")
        print(A_J)
        
        #verificam cat de aproape sunt
        diff_norm = norm(A_I - A_J, 1)
        print(f"\ndiferenta norma 1: {diff_norm:.2e}")
        
    except np.linalg.LinAlgError:
        print("\n[eroare] AtA nu e inversabila, nu putem calcula A_J")
    
    return sigma, rang_manual, cond_manual, A_I

#teste
#cazul 1: rang mic
print("test 1: matrice 5x3 cu rang mic")
A1 = np.array([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
    [2, 1, 0],
    [3, 3, 3]
], dtype=float)
svd_analysis(A1)

#cazul 2: rang maxim
print("\n" + "="*20)
print("test 2: matrice 4x2 cu rang maxim")
A2 = np.array([
    [1, 2],
    [3, 4],
    [5, 6],
    [7, 8]
], dtype=float)
svd_analysis(A2)

#cazul 3: dependente liniare
print("\n" + "="*20)
print("test 3: matrice 6x3 cu dependente")
A3 = np.array([
    [1, 0, 1],
    [0, 1, 1],
    [1, 1, 2],
    [2, 1, 3],
    [0, 0, 0],
    [3, 2, 5]
], dtype=float)
svd_analysis(A3)