num_users = 8
update_direction = 3

num_users = (num_users + 1) if (update_direction == 3) else (num_users - 1)

print('New value is:', num_users)