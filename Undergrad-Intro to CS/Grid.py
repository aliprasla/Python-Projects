def main():
    in_file = open ("grid.txt", "r")
    dim = in_file.readline()
    dim = dim.strip()
    dim = int(dim)
    grid = []
    #creates grid
    for i in range (dim):
        row = in_file.readline()
        row = row.strip()
        row = row.split()
        for j in range (dim):
            row [j] = int(row[j])
        grid.append(row)
    max_prod = 0
    #find largest product in rows
    for row in grid:
        for i in range (dim - 3):
            prod = 1
            for j in range (i, i+4):
                prod = row[i] * row[i+1] * row [i + 2] * row [i + 3]
                if (prod > max_prod):
                    max_prod = prod
    #finds largest product in columns
    prod = 1
    for j in range(dim):
        for i in range(dim - 3):
            prod = 1
            for k in range (i,i+4):
                prod = grid[k][j] * prod
                if (prod > max_prod):
                    max_prod = prod
    #this set of code reads all the grid from L to R
    temp = dim - 3
    for j in range (temp - 1):
        temp = temp - 1
        for i in range (temp):
            prod = 1
            for k in range (i,i+4):
                prod = grid[k][j+ k + 1] * prod
                if (prod > max_prod):
                    max_prod = prod
    temp = dim - 3
    for j in range (temp - 1):
        temp = temp - 1
        for i in range (temp):
            prod = 1
            for k in range (i,i+4):
                prod = grid[j+ k + 1][k] * prod
                if (prod > max_prod):
                    max_prod = prod
    #read along major diagonal from R to L
    for i in range (dim - 3):
        prod = 1
        for j in range (i, i+4):
            prod = prod * grid [j][dim - j -1]
            if (prod > max_prod):
                    max_prod = prod

    #upper half of right to left
    temp = dim - 3
    for j in range(temp-1):
        temp = temp - 1
        for i in range(temp):
            prod = 1
            for k in range(i, i + 4):
                prod = prod * grid[k][temp +2  - k]
                if (prod > max_prod):
                    max_prod = prod

    #lower half right to left
    temp = dim - 3
    for j in range(temp-1):
        temp = temp - 1
        for i in range(temp):
            prod = 1
            for k in range(i, i + 4):
                prod = prod * grid[k+1 + j][dim - 1 - k]
                if (prod > max_prod):
                    max_prod = prod
    print("The greatest product is " + str(max_prod)+ ".")
    in_file.close()
    
    
main()
