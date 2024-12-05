print ("Hà Mạnh Dũng")
print("235752021610006")

def all_even_digits(num):
    return all(int(digit) % 2 == 0 for digit in str(num))
even_digit_numbers = [str(num) for num in range(1000, 3001) if all_even_digits(num)]
output_str = ','.join(even_digit_numbers)
print("Các số có tất cả các chữ số là số chẵn: " + output_str)

