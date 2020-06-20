from flask import *
import wikipedia as wk
app=Flask(__name__)
@app.route('/')
def home():
	return render_template('index.html',title='PocketPedia')

@app.route('/result',methods=['POST'])
def res():
	try:
		lang=request.form['lang']
		wk.set_lang(lang)
		srh=request.form['search']
		q=wk.page(str(srh))
		related=q.links[:4]
		title=q.original_title
		srh_res=wk.summary(srh)

		return render_template('result.html',title=title,summary=srh_res,related=related)
	except ConnectionError:
		return '<center><h3 style="color:red;">Make sure your internet is connected</h3></center>'
	except:
			return '''<center><h3 style="color:red;">

			This query doesn\'t exist in our file make sure you type full name <br> or else make sure you won\'t type any special characters,symbols,numerals

			</h3></center>'''

	#except:
	#	return '<h3 style="color:red;">Sorry! This query doesn\'t exist in our page</h3>'

if(__name__=='__main__'):
	app.run(debug=True)
