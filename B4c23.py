print ("Hà Mạnh Dũng")
print("235752021610006")
def count_letters_and_digits(sentence):
    letters = sum(c.isalpha() for c in sentence)
    digits = sum(c.isdigit() for c in sentence)
    return letters, digits
sentence = input("Nhập câu của bạn: ")
letters, digits = count_letters_and_digits(sentence)
print(f"Số chữ cái là: {letters}")
print(f"Số chữ số là: {digits}")
