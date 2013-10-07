from flask import Flask
from flask import request
from run import *
from flask import render_template
from flask import jsonify

app = Flask(__name__)

@app.route('/search', methods=['POST', 'GET'])
def search():
    error = None
    if request.method == 'GET' and request.args.get('q') != None:
        qf = db.get_object(session, 'defaultQueryFactory')
        qString = request.args.get('q')
        query = qf.get_query(session, qString)
        rs = db.search(session, query)
        storelist = []
        for rsi in rs:
            rec = rsi.fetch_record(session)
            storelist.append(str(rec.id))
        #return str(len(rs))
	return ', '.join(storelist)
	#return type(request.args.get('q'))

    # the initial search form
    return render_template("search.html")

@app.route('/')
def hello_world():
    return render_template("index.html") 

if __name__ == '__main__':
    app.run()
