print ("Hà Mạnh Dũng")
print("235752021610006")

def is_divisible_by_5(binary_str):
    decimal = int(binary_str, 2)
    return decimal % 5 == 0

input_str = input("Nhập các số nhị phân 4 chữ số, phân tách bởi dấu phẩy: ")
binary_numbers = input_str.split(',')

divisible_by_5 = [binary for binary in binary_numbers if is_divisible_by_5(binary)]

output_str = ','.join(divisible_by_5)
print("Các số nhị phân chia hết cho 5 là: " + output_str)
