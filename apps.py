from flask import Flask, render_template
import os

apps = Flask(__name__)

    

picFolder = os.path.join('static','pics')

apps.config['UPLOAD_FOLDER'] = picFolder



@apps.route('/')
def helloworld():
    pic1 = os.path.join(apps.config['UPLOAD_FOLDER'], 'a.jpg')
    pic2 = os.path.join(apps.config['UPLOAD_FOLDER'], 'b.jpg')
    pic3 = os.path.join(apps.config['UPLOAD_FOLDER'], 'c.jpg')
    pic4 = os.path.join(apps.config['UPLOAD_FOLDER'], 'd.jpg')
    pic5 = os.path.join(apps.config['UPLOAD_FOLDER'], 'e.jpg')
    pic6 = os.path.join(apps.config['UPLOAD_FOLDER'], 'f.jpg')
    pic7 = os.path.join(apps.config['UPLOAD_FOLDER'], 'g.jpg')
    pic8 = os.path.join(apps.config['UPLOAD_FOLDER'], 'h.jpg')
    pic9 = os.path.join(apps.config['UPLOAD_FOLDER'], 'i.jpg')
    return render_template('index.html', user_image = pic1, pic2 = pic2, pic3 = pic3, pic4 = pic4, pic5 = pic5, pic6 = pic6, pic7 = pic7, pic8 = pic8, pic9 = pic9)



if __name__ == '__main__':
    apps.run(debug=True)