from flask import Flask, render_template, request
app = Flask(__name__)

menues = [{
        'name' : 'Cơm rang',
        'price' : 10
    }, 
    {'name' : 'Bún bò',
        'price' : 20
    },
    {'name' : 'Cơm gà',
        'price' : 50
    }]

@app.route('/',methods = ['POST'])
def post_dish():
    dish_name = request.form.get('name')
    dish_price = request.form.get('price')
    dish_price = int(dish_price)
    menues.append({
        'name': dish_name,
        'price': dish_price
    })
    return render_template("menu.html",menues = menues)
@app.route('/')
def index():
    return render_template("menu.html", menues = menues)

if __name__ == '__main__':
    app.run(host='127.0.0.1',port=8000, debug= True)
