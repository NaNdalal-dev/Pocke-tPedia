from flask import *
import wikipedia as wk
app=Flask(__name__)

@app.route('/')
def home():
	return render_template('index.html',title='PocketPedia')

@app.route('/result',methods=['POST'])
def res():
		try:
			global lang,srh,q,fullink,title,srh_res,related_search
			lang=request.form['lang']
			wk.set_lang(lang)
			srh=request.form['search']
			q=wk.page(str(srh))
			fullink=q.url
			title=q.original_title
			srh_res=wk.summary(srh)
			related_search=wk.search(title)
			'''rs=[]
			title_rs=[]
			for i in range(len(related_search)):
				try:
					rs.append(wk.summary(related_search[i]))
					title_rs.append(related_search[i])
				except:
					pass'''


			return render_template('result.html',title=title,summary=srh_res,fullink=fullink)
		except:
			return "<h3 style='color:red;'><center>Error! page not found </center></h3>"

@app.route('/related_search',methods=['POST'])
def related_srh():
			rs=[]
			title_rs=[]
			l=0
			for i in range(5):
				try:
					rs.append(wk.summary(related_search[i]))
					title_rs.append(related_search[i])
					l+=1
				except:
					pass
			return render_template('related.html',title_rs=title_rs,related_search=rs,l=l)


@app.route('/result')
def not_found():
	return '<h3 style="color:red;"><center>Error 404!page not found <br>  Go to main <a href="/">page</a></center></h3>'
@app.route('/related_search')
def not_found2():
	return '<h3 style="color:red;"><center>Error 404!page not found <br>  Go to main <a href="/">page</a><center></h3>'


if(__name__=='__main__'):
	app.run(debug=True)
