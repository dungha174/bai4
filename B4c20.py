print ("Hà Mạnh Dũng")
print("235752021610006")
def generate_pascals_triangle(n):
    triangle = []
    for i in range(n):
        row = [1] * (i + 1)
        for j in range(1, i):
            row[j] = triangle[i-1][j-1] + triangle[i-1][j]
        triangle.append(row)
    return triangle

def print_pascals_triangle(triangle):
    for row in triangle:
        print(' '.join(map(str, row)))

n = int(input("Nhập số dòng đầu tiên của tam giác Pascal: "))
triangle = generate_pascals_triangle(n)
print_pascals_triangle(triangle)
