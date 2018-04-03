from flask import Flask, render_template#request

app = Flask(__name__)


#video 7:
@app.route("/")
def index():
  return 'hi'

@app.route("/shopping")
def shopping():
  food = ["Cheese", "Tuna", "Beef"]
  return render_template("shopping.html", food=food)


'''
#video 6
@app.route("/")
@app.route("/<user>")
def index(user=None):
  return render_template("user.html", user=user)
  '''


''' #video 4 & 5
@app.route("/profile/<name>")
def profile(name):
  return render_template('profile.html', name=name)
  '''

''' #video 3
@app.route('/')
def index():
  return 'method used: %s' % request.method

@app.route('/bacon', methods=['GET', 'POST'])
def bacon():
  if request.method == 'POST':
    return 'you are using POST'#use POSTMAN to test this
  else:
    return 'you are probably using GET'
    '''

''' #video 2
@app.route('/')
def index():
  return 'this is the homepage'

@app.route('/tuna')
def tuna():
  return '<h2>tuna is good!</h2>'

@app.route('/profile/<username>')
#need to use angle brackets anytime your are passing in a variable as a url
def profile(username):
  return '<h2>Hi, %s</h2>' % username

@app.route('/post/<int:post_id>')
#you have to declare int when using integers
def show_post(post_id):
  return '<h2>this is the post %s</h2>' % post_id
'''

if __name__=="__main__":
  app.run(debug=True)
