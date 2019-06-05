from flask import Flask, render_template, request,redirect,url_for
from mongo import get_all, insert_food
app = Flask(__name__)

# menues = [{
#         'name' : 'Cơm rang',
#         'price' : 10
#     }, 
#     {'name' : 'Bún bò',
#         'price' : 20
#     },
#     {'name' : 'Cơm gà',
#         'price' : 50
#     }]

# for dish in menues:
#     insert_food(dish['name'],dish['price'])

@app.route('/edit_food/<id>')
def func_name(food_id):
    print(food_id)
    return render_template

@app.route('/',methods = ['POST'])
def post_dish():
    dish_name = request.form.get('name')
    dish_price = request.form.get('price')
    dish_price = int(dish_price)
    insert_food(dish_name,dish_price)
    menues = get_all()
    return render_template("menu.html",menues = menues)

@app.route('/')
def index():
    menues = get_all()
    return render_template("menu.html", menues = menues)

if __name__ == '__main__':
    app.run(host='127.0.0.1',port=8000, debug= True)
