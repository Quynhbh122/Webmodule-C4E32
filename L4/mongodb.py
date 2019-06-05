uri = 'mongodb://admin:admin@ds021182.mlab.com:21182/c4e'
# python -m pip install pymongo/dnspython

import pymongo

client = pymongo.MongoClient(uri)
db = client.c4e
collection = db.bhquy

def insert_poem(title:str,content:str,author:str):
    """[thêm 1 bài thơ]
    
    Arguments:
        title {str} -- [tiêu đề]
        content {str} -- [nội dung]
        author {str} -- [tác giả]
    """
    
    collection.insert_one({'title':title,'content':content,'author':author})

insert_poem('Tôi buồn','Tôi buồn thổi khúc tiêu xa. Nhờ cơn gió hạ mang qua bên nàng. Trăng thanh điệp khúc ngàn vàng. Nụ hoa đua nở cùng đàn bay cao. Tôi bay lơ lửng vút vào thinh không. Ngân hà ngơ ngẫn dòng ...','Mãi Yêu Em')
insert_poem('Hà Huyền Chi','Khi vui hạc múa có đôi. Hạc buồn thả tiến buồn rơi xé lòng. Tôi vui tay có tay không. Lại như nước lã ra sông khi buồn. Có em nhẹ gánh còn cùng thôi. Buồn vui gì vẫn mình tôi.','TA')
insert_poem('Tại sao lại nhập thơ','Thơ gì dài vậy nè còn thiếu nội dung','Quy Quy')

print(list(db.bhquy.find()))
