"""
counter
defaultdict
ordereddict
namedtuple
deque
"""

from collections import Counter, defaultdict

temperature = [12, 45.0, 78, 34.5, 79, 36,36, 45, 36]

counter = Counter(temperature)
print(counter[36])

