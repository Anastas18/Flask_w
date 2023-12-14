from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def main():
    return render_template('index.html')

@app.route('/1')
def second():
    return render_template('second.html')

@app.route('/2')
def third():
    return render_template('index.html')

@app.route('/3')
def firth():
    return render_template('index.html')


if __name__ == "__main__":
    app.run(debug=True)