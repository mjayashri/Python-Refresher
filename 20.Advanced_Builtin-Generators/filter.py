def starts_with_r(friend):
    return friend.startswith('R')


friends = ['Jayashri', 'Rahul', 'Dravid', 'William', 'Ravi']

start_with_r = filter(starts_with_r, friends)  # arg 1- takes function that returns True/False

start_with_r_2 = filter(lambda friend: friend.startswith('R'), friends) # more readable

another_starts_with_R = (f for f in friends if f.startswith('R')) # faster

print(list(start_with_r_2))
print(list(start_with_r))
print(list(another_starts_with_R))
# print(next(start_with_r))
# print(next(start_with_r))
