import file_operations as fo

# Write data
print(fo.write_file("example.txt", "Hello, World!\n"))

# Append data
print(fo.append_file("example.txt", "This is an appended line.\n"))

# Read data
print(fo.read_file("example.txt"))
