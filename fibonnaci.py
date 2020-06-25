def fibonnaci(number):
    matrix = [[1, 1], [1, 0]]
    if (number==0): return 0
    power(matrix, number-1)
    return matrix[0][0]

def power(matrix, number):
    matrix2 = [[1, 1], [1,0]]
    for i in range(number-1):
        mul(matrix, matrix2)
def mul(matrix, matrix2):
    a = (matrix[0][0]*matrix2[0][1] + matrix[0][1]*matrix2[1][0])
    b = (matrix[0][0]*matrix2[0][1] + matrix[0][1]*matrix2[1][1])
    c = (matrix[1][0]*matrix2[0][0] + matrix[1][1]*matrix2[1][0])
    d = (matrix[1][0]*matrix2[0][1] + matrix[1][1]*matrix2[1][1])
    matrix[0][0]=a
    matrix[0][1]=b
    matrix[1][0]=c
    matrix[1][1]=d
if __name__ == "__main__":
    number = int(input())
    print(fibonnaci(number))

        