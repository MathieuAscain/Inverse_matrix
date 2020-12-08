import os
from copy import deepcopy

# number of lines and columns fixed at 3
# 3 * 3 matrix
nbrLines = 3
nbrColomns = 3

# boolean initialization to check if the matrix is invertible
invertible = True

# variables initialization to show a dot at each coefficient position
# L represents the space in between 2 coefficients in the x-axis
# H represents the space in between 2 coefficients in the y-axis
L = 6
H = 2

# matrixes inialization
# mstart for starting matrix
mstart = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

# mid for identity matrix
mid = [[1, 0, 0], [0, 1, 0], [0, 0, 1]]

# mtrans for the transition matrix
mtrans = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

# mrev for the reverse matrix
mrev = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

# Terminal clear
os.system('cls' if os.name == 'nt' else 'clear')

# show a dot at each matrix coefficient position
# for the mstart matrix
for i in range(len(mstart)):
    for j in range(len(mstart[i])):
        print(f"\033[{i * H + 1};{j * L + 1}H.")

# for the mid matrix
for i in range(len(mid)):
    for j in range(len(mid[i])):
        print(f"\033[{i * H + 1};{j * L + 1 + nbrColomns * L + 1}H.")

# user coefficient selection
for i in range(len(mstart)):
    for j in range(len(mstart[i])):
        mstart[i][j] = float(input(f"\033[{i * H + 1}; {j * L + 1}H"))

# mstart determinant calculation
main_diag = mstart[0][0] * mstart[1][1] * mstart[2][2] + mstart[0][1] * mstart[1][2] * mstart[2][0] + mstart[1][2] * mstart[2][1] * mstart[0][2]
other_diag = mstart[2][0] * mstart[1][1] * mstart[0][2] + mstart[1][0] * mstart[0][1] * mstart[2][2] + mstart[2][1] * mstart[1][2] * mstart[0][0]
det = main_diag - other_diag

invertible = True
# check if determinant non null
for i in range(len(mstart)):
    for j in range(len(mstart[i])):
        if i == j and mstart[i][j] == 0:
            print("A zero is on the main diagonal, the matrix is not invertible")
            invertible = False
        elif det == 0:
            print("The determinant is null, then the matrix is not invertible")
            invertible = False

if invertible:
    # copy of mid matrix in mrev matrix
    mtrans = deepcopy(mstart)
    mrev = deepcopy(mid)
    
    # calculations
    for i in range(len(mstart)):
        for j in range(len(mstart[i])):
            y = mstart[j][i] / mstart[i][i]
            mtrans[j][i] = round(y, 2)
            z = mrev[j][i] / mstart[i][i]
            mid[j][i] = round(z, 2)

        mstart = deepcopy(mtrans)
        mrev = deepcopy(mid)

        for k in range(len(mstart)):

            if i != k:
                for j in range(len(mstart[i])):
                    x = mstart[j][k] - mstart[j][i] * mstart[i][k]
                    mtrans[j][k] = round(x, 2)
                    y = mrev[j][k] - mrev[j][i] * mstart[i][k]
                    mid[j][k] = round(y, 2)

        mstart = deepcopy(mtrans)
        mrev = deepcopy(mid)


# print of mstart matrix
for i in range(len(mstart)):
    for j in range(len(mstart[i])):
        print(f"\033[{i * H + 1};{j * L + 1}H{mstart[i][j]}")

# print of mid matrix
for i in range(len(mid)):
    for j in range(len(mid[i])):
        print(f"\033[{i * H + 1};{j * L + 1 + nbrColomns * L + 1}H{mid[i][j]}")

# print of mtrans matrix
#for i in range(len(mtrans)):
    #for j in range(len(mtrans[i])):
        #print(f"\033[{i * H + 1};{j * L + 1 + nbrColomns * L * 2 + 2}H{mtrans[i][j]}")

# print of mrev matrix
for i in range(len(mrev)):
    for j in range(len(mrev[i])):
        print(f"\033[{i * H + 1};{j * L + 1 + nbrColomns * L + 1}H{mrev[i][j]}")