print ("Hà Mạnh Dũng")
print("MSSV 235752021610006")

input_string = input("Nhập dãy các từ cách nhau bằng dấu cách:")
words = input_string.split()
max_length = max(len(word) for word in words)
longest_words = [word for word in words if len(word) == max_length]
print("Các từ dài nhất: ", ",".join(longest_words))
