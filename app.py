from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html')

@app.route('/add_transaction')
def add_transaction():
    return render_template('add_transaction.html')

@app.route('/edit_transaction')
def edit_transaction():
    return render_template('edit_transaction.html')

@app.route('/manage_categories')
def manage_categories():
    return render_template('manage_categories.html')

@app.route('/reports')
def reports():
    return render_template('reports.html')

if __name__ == "__main__":
    app.run(debug=True)
