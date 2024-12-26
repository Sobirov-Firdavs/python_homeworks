import statistics

universities = [
    ['California Institute of Technology', 2175, 37704],
    ['Harvard', 19627, 39849],
    ['Massachusetts Institute of Technology', 10566, 40732],
    ['Princeton', 7802, 37000],
    ['Rice', 5879, 35551],
    ['Stanford', 19535, 40569],
    ['Yale', 11701, 40500]
]

def enrollment_status(uni_list, index):
    element_list = []

    for i in range (len(universities)):
        element_list.append(uni_list[i][index])
    return element_list

def mean(x):
    mean_value = round(statistics.mean(x), 2)
    return mean_value

def median(y):
    median_value = statistics.median(y)
    return median_value

print(f'Total students: {sum(enrollment_status(universities, 1))}.')
print(f'Total tuition: {sum(enrollment_status(universities, 2))}.\n')

print(f'Student mean: {mean(enrollment_status(universities, 1))}')
print(f'Student median: {median(enrollment_status(universities, 1))}\n')

print(f'Tuition mean: {mean(enrollment_status(universities, 2))}')
print(f'Tuition median: {median(enrollment_status(universities, 2))}')