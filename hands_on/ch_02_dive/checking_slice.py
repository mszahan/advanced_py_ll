names = ['sojib', 'tonmoy', 'zahan', 'riman']
nums = [1, 2, 5, 3]

reverse_name = names[::-1]
jumping_name = names[::2]

print('the reversed names \n', reverse_name)
print('the jumping name \n', jumping_name)

for i, name in enumerate(names):
    print(f"{i} {name}")

for name, num in zip(names, nums):
    print(name, nums)