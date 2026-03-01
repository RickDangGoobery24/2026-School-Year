grades = {90:'A', 80:'B', 70:'C'}
list(grades.items())
[(80, 'B'), (90, 'A'), (70, 'C')]
[(80, 'B'), (90, 'A'), (70, 'C')]
for (key, value) in grades.items():
    print(key, value)
theKeys = list(info.keys())
theKeys.sort()
for key in theKeys:
    print(key, info[key])
