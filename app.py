from flask import Flask, render_template, request
app = Flask(__name__)

@app.route('/')
def top():
    return render_template('index.html', **vars())

@app.route('/vote', methods=['POST'])
def answer():
    kinoko_count = 3
    takenoko_count = 5
    messages = ['Kinoko is wonrderful!', 'Takenoko is awesome!']
    return render_template('vote.html', **vars())

if __name__ == '__main__':
    app.run(debug=True)
    
