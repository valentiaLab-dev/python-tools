from flask import render_template
from flask import request, jsonify
from services import convert_files
from app import app
from cloudflare import s3_client

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html', 
                           title='Home', 
                           env=app.config["ENV"], 
                           dir=app.config["LOCAL_DIR"]+app.config["ROOT_DIR_NAME"],
                           out=app.config["OUTPUT_DIR_NAME"]
                           )

@app.route('/convert_to_mp3', methods=['POST'])
def convert_to_mp3():
    # TODO: handle online conversion
    # TODO: progress indicator
    # TODO: do not exit page
    # input_path = request.form.get('input_path')
    convert_files()
    return jsonify({"message": f"TEST"}), 200

@app.route('/r2', methods=['POST'])
def r2():
    if 'file' not in request.files:
        return jsonify({"error": "No file part"}), 400
    
    file = request.files['file']
    
    if file.filename == '':
        return jsonify({"error": "No selected file"}), 400

    try:
        # Upload the file stream directly to R2
        s3_client().upload_fileobj(
            file,
            app.config["BUCKET_NAME"],
            file.filename,
            ExtraArgs={'ContentType': file.content_type}
        )
        return jsonify({"message": f"Successfully uploaded {file.filename} to R2"}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500


