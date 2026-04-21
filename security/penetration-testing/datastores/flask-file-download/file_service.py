# app.py
from flask import Flask, send_from_directory

app = Flask(__name__)

@app.route('/<filename>', methods = ['GET'])
def download_file(filename):
    # The directory where the files are  located
    directory = 'images'
    # Flask's send_from_directory to send the file to the client
    return send_from_directory(directory, filename, as_attachment=True)

if __name__ == '__main__':
     app.run(host='0.0.0.0', port=5000, debug=True)
