from collections import Counter
from collections import defaultdict
from collections import deque

fruits = ["apple", "banana", "orange", "apple", "banana", "apple"]
fruit_count = Counter(fruits)
print(fruit_count)


text = "This is a sample abcdefghiacegi"
text_count = Counter(text)
print(text_count)

students = defaultdict(int)
print(students("marks"))  # this will return 0 as the default value for int is 0#
# but this will not give error as we are using defaultdict which will return the default value for the key if the key is not present in the dictionary.

a = deque([1, 2, 3, 4, 5])
a.append(6)
a.appendleft(0)
print(a)  # deque([0, 1, 2, 3, 4, 5, 6])
