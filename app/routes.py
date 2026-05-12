from flask import render_template
from flask import request
from .services import convert_m4a_to_mp3, get_path, test2
from app import app


@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html', title='Home')

@app.route('/convert_to_mp3', methods=['POST'])
def convert_to_mp3():
    input_path = request.form.get('input_path')
    
    print(f"tert")
    
    # convert_m4a_to_mp3(input_path, output_path)
    # test2()


@app.route('/r2')
def r2():
    return app.config["BUCKET_NAME"]


