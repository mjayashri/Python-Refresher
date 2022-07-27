fav_friends = ['Rahul', 'Dhoni', 'Dravid']

for i, friend in enumerate(fav_friends):
    print(f'My top {i + 1} friend is {friend}')


friend_gen = enumerate(fav_friends)
print(list(friend_gen))