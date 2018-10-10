from flask import Flask, render_template
from flask import request
from summary import trending, get_summary
app = Flask(__name__,static_url_path='/static')

@app.route('/')
def index():
	trending_terms,trending_urls=trending()
	return render_template('index.html',trending_terms=trending_terms,trending_urls=trending_urls)

@app.route('/output', methods=['GET','POST'])
def summariser():
	text = request.form['text']
	if(len(text)>0):
		print("got it")
	text,text_summary=get_summary(text)
	return render_template('output.html', text=text,text_summary=text_summary)

if __name__ == '__main__':
	app.run(debug=True)