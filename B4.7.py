print ("Hà Mạnh Dũng")
print("MSSV 235752021610006")

input_string = input("Nhập Chuỗi: ")
new_string = ''.join(char for char in input_string if not char.isdigit())
print("Chuỗi sau khi loại bỏ chữ số:", new_string)
