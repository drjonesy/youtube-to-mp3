from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from YouTubeToMp3 import YouTubeToMp3


app = Flask(__name__)
app.secret_key = 'converttoaudio'

class ConvertForm(FlaskForm):
    url = StringField()
    fileDir = StringField()
    submit = SubmitField()


@app.route('/', methods=['GET', 'POST'])
def index():

    form = ConvertForm()
    
    if form.validate_on_submit():
        YouTubeToMp3(url=form.url.data, path=form.fileDir.data)
        

    return render_template('index.html', form=form)

if __name__ == '__main__':
  app.run(host='127.0.0.1', port=5000, debug=True)
 