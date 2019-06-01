from flask import Flask, render_template
app = Flask(__name__)

# @app.route('/')
# def index():
#     return """
#     <html>
#     <hl>C4E</hl>
#     <a href='horntor.art'>horntor.art</a>
#     <br />
#     <img width = "300" heigh = "300" src = 'https://i.pinimg.com/564x/f3/d6/37/f3d637a7fe2dc3992bac2deb53bd9526.jpg' />
#     """

# @app.route('/say-hi/<gender>/<name>')
# def say_hi_name(gender,name):
#     if gender == 'nam':
#         return "Hello anh " + name
#     else:
#         return "Hello chi " + name

# @app.route('/cong/<a>/<b>')
# def cong(a,b):
#     return str( int(a)+int(b))

# @app.route('/say-hi')
# def say_hi():
#     return "Hello"

@app.route('/')
def index():
    poem = {
       'title' : ' Tĩnh dạ tứ',
       'body' : ' Nội dung bài thơ',
       'author' : 'Lý Bạch',
       'gender': 1
    }
    
    poems = []
    poems.append(poem)
    poems.append({
        'title':'Thúy Kiều',
        'body':'Nội dung bài Thúy Kiều',
        'author':'Nguyễn Du',
        'gender': 1
    })
    return render_template("index.html", poems = poems)

if __name__ == '__main__':
  app.run(host='127.0.0.1', port=8000, debug=True)
 