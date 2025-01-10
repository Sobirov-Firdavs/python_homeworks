file_path = r'python_homeworks\lesson-1\example.txt'

a = ['a', 'b', 3]
with open(file_path, 'w') as file:
    file.writelines(f'{i}\n' for i in a)

with open(file_path) as file:
    txt = file.read()
    print(txt)