print ("Hà Mạnh Dũng")
print("235752021610006")
def fibonacci_list(n):

    fib_list = []
    a, b = 0, 1
    
    while a < n:
        fib_list.append(a)
        a, b = b, a + b
    
    return fib_list

n = int(input("Nhập số nguyên n: "))

fib_list = fibonacci_list(n)
print("Danh sách các số Fibonacci nhỏ hơn", n, "là:", fib_list)
