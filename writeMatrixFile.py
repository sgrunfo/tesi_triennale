
def writeMatrixFile(file, matrix):
    open(file, 'w').close()
    f = open(file, "a")
    i = 1

    while i <= len(matrix[0]):
        f.write(';'+str(i))
        i = i + 1

    f.write('\n')
    i = 1
    for riga in matrix:
        f.write(str(i))
        for colonna in riga:
            f.write(';'+str(colonna))
        f.write('\n')
        i = i + 1
