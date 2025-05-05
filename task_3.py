import random

numbers = [random.randint(1, 1000) for _ in range(10000)]
counter = {}

for num in numbers:
    if num in counter:
        counter[num] += 1
    else:
        counter[num] = 1

most_frequent = max(counter, key=counter.get)
print(f"Число {most_frequent} повторюється {counter[most_frequent]} разів.")
