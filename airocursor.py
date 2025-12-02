from flask import Flask, render_template, redirect, url_for
import subprocess

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/run', methods=['POST'])
def run_virtual_mouse():
    print("Button clicked! Attempting to run virtualmouse.py")
    subprocess.Popen(['python', 'virtualmouse.py'])
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
