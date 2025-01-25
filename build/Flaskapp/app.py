from flask import Flask, render_template
from flask import Flask, render_template, redirect, url_for, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        # Process login or registration logic here
        # For now, we simply redirect back to the main page
        return redirect(url_for('index'))
    return render_template('register.html')

@app.route('/about')
def about_us():
    return render_template('about.html')


@app.route('/our-work')
def our_work():
    return "Our Work Page - Content Coming Soon!"

@app.route('/learn-more')
def learn_more():
    return redirect("http://localhost:8501/")

if __name__ == '__main__':
    app.run(debug=True)
