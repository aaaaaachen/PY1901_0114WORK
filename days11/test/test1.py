
import shelve

users = {"admin":{"user_name":"admin","passwd":"123"}}
team = {"football":{"player":"liu"},"basketball":{"player":"kobe"}}


# file = shelve.open('./data/5.1')
# file['users'] = users
# file['team'] = team
#
# print(file['users'],file['team'])




with shelve.open('shelve_demo') as file:
    file['users'] = users
    file['team'] = team
# import os
#
# filename = r'/home/tim/workspace/test.txt'
# if os.path.exists(filename):
#     message = 'OK, the "%s" file exists.'
# else:
#     message = 'Sorry, I cannot find the "%s" file.'
# print(message % filename)