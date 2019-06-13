def save_data():

    file = shelve.open('data/blog.dat')
    file['users'] = users
    file['essays'] = essays
    file["comment"] = comment
    file["email1"] = email1
    # file['message1'] = message1
    # file['recyclebin'] = recyclebin
    # file['accont'] = accont




#获取数据
def get_data():
    global users, essays, comment, email1, message1
    file =shelve.open('data/blog.dat')
    users = file['users']
    essays = file['essays']
    comment = file['comment']
    email1 = file['email1']