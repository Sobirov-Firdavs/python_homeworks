letters = "abcdefghijklmnopqrstuvwxyz ' "
file_path = r'python_homeworks\lesson-6\homework\sample.txt'

try:
    with open(file_path) as file:
        txt = file.read()
except FileNotFoundError:
    txt = input('There is no file existing. You can create one by typing its contest:\n')
    file = open(file_path, 'wt')
    file.write(txt)

txt = txt.replace('\n', ' ').lower()

for char in txt:
    if char not in letters:
        txt = txt.replace(char, '')
words = txt.split(' ')

words = [word for word in words if word != '']

unique_words = list(set(words))

times = [words.count(i) for i in unique_words]

occurances = {k: v for k, v in zip(unique_words, times)}
occurances_descending= dict(sorted(occurances.items(), key=lambda x: x[1], reverse=True))
top = int(input('How many top words do you want to see? '))

print(f'Totally, there are {len(unique_words)} words in the text.\nTop {top} words:')

for i, (word, count) in enumerate(occurances_descending.items()):
    if i >= top:
        break
    print(f'{word} - {count} time(s).')