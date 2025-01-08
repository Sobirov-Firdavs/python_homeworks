file_path = r'python_homeworks\lesson-7\homework\employee.txt'
with open(file_path) as file:
    lines = file.readlines()
    lines = [line.replace('\n', '').replace(' ', '').split(',') for line in lines]
print(lines[-1])