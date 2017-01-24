from flask import Flask
from flask import render_template
from flask import request
from flask import session
from flask import redirect
app = Flask(__name__)


@app.route('/hello')
def hello():
  if (request.args.get('name')):
    return "Hello %s\n" % request.args.get('name')
  else:
    return "Hello World\n"

if __name__ == '__main__':
   app.run(debug = True)
