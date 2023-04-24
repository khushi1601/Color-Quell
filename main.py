from flask import Flask, render_template, request, redirect, url_for
import os
import protanopia
import deuteranopia
import tritanopia

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'static/uploads'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/', methods=['POST'])
def upload():
    file = request.files['file']
    if file:
        filename = file.filename
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        print(file.filename)
        protanopia.sim(file.filename)
        deuteranopia.sim(file.filename)
        tritanopia.sim(file.filename)
        return redirect(url_for('uploaded_file', filename=filename, prot = 'prot.png'))
    else:
        return "No file uploaded"

@app.route('/uploads/<filename>')
def uploaded_file(filename):
    return render_template('uploaded.html', filename=filename, prot = 'prot.png',deut = 'deut.png', trit = 'trit.png')

if __name__ == '__main__':
    app.run(debug=True)

# https://www.researchgate.net/publication/326626897_Smartphone_Based_Image_Color_Correction_for_Color_Blindness