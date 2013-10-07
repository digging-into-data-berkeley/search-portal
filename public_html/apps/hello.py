import os
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
        titlelist = []
        for rsi in rs:
            rec = rsi.fetch_record(session)
            ext = db.get_object(session, 'SimpleExtractor')
            title = None
            sel = None
            try:
                sel = db.get_object(session, 'titleXPathSelector')
            except ObjectDoesNotExistException:
                try:
                    sel = db.get_object(session, 'titleSelector')
                except ObjectDoesNotExistException:
                    pass
            if sel is not None:
                titleData = sel.process_record(session, rec)
                for selRes in titleData:
                    if selRes:
                        for title in ext.process_xpathResult(session, [selRes]).keys():
                            if title:
                                break
                        if title:
                            # Strip leading/trailing whitespace
                            title = title.strip()
                            titlelist.append(os.path.splitext(os.path.basename(title)))
                            break
        # in title, we now have the path and filename
        #return render_template("result_table.html", urls=titlelist)
	# dummy data
	titlelist = ['birdbookillustra00reedrich', 'mobydickorwhale02melvuoft']
	return render_template("result_table.html", urls=titlelist, query='swamp')

    # the initial search form
    return render_template("search.html")

@app.route('/')
def hello_world():
    return render_template("index.html") 

if __name__ == '__main__':
    app.run()
