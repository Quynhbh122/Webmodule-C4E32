uri = 'mongodb://c4e:12345678Abc@ds231307.mlab.com:31307/c4e'
# python -m pip install pymongo/dnspython

import pymongo

client = pymongo.MongoClient(uri)
db = client.c4e
collection = db.bhquy
# collection.insert_one({'name':'Quy'})

# db.bhquy.update_one({'name':'Quy'},{'$set':{'age':48}})


def insert_user(name:str,age:int):
    """[Thêm một user]
    
    Arguments:
        name {str} -- [tên]
        age {int} -- [tuổi]
    """
    
    collection.insert_one({'name':name,'age':age})

insert_user('Qua','40')

print(list(db.bhquy.find()))
