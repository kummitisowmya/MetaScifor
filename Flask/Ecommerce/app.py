from flask import Flask, render_template, request, redirect, url_for, session
from flask_session import Session

app = Flask(__name__)
app.secret_key = 'supersecretkey'

# Configure session
app.config['SESSION_TYPE'] = 'filesystem'
Session(app)

# Sample product data
products = [
    {"id": 1, "name": "Dress", "price": 999, "image": "dress.jpeg"},
    {"id": 2, "name": "Dress1", "price": 1299, "image": "dress1.jpeg"},
    {"id": 3, "name": "Dress2", "price": 1599, "image": "dress2.jpeg"},
    {"id": 4, "name": "Dress3", "price": 999, "image": "dress3.jpeg"},
    {"id": 5, "name": "Dress4", "price": 1199, "image": "dress4.jpg"},
]

users = {}

@app.route('/')
def home():
    return render_template('home.html', products=products, user=session.get('user'))

@app.route('/products')
def product_list():
    return render_template('products.html', products=products, user=session.get('user'))

# ✅ New product detail route
@app.route('/product/<int:product_id>')
def product_detail(product_id):
    product = next((p for p in products if p["id"] == product_id), None)
    if not product:
        return "Product not found", 404
    return render_template('product_detail.html', product=product)

@app.route('/cart')
def cart():
    cart = session.get('cart', [])
    total = sum(item['price'] * item['quantity'] for item in cart)
    return render_template('cart.html', cart=cart, total=total)

@app.route('/cart/add/<int:product_id>', methods=['POST'])
def add_to_cart(product_id):
    product = next((p for p in products if p["id"] == product_id), None)
    if product:
        if 'cart' not in session:
            session['cart'] = []

        for item in session['cart']:
            if item['id'] == product_id:
                item['quantity'] += 1
                break
        else:
            product_copy = product.copy()
            product_copy['quantity'] = 1
            session['cart'].append(product_copy)

        session.modified = True
        return redirect(url_for('cart'))

    return "Product not found", 404

@app.route('/cart/remove/<int:product_id>')
def remove_from_cart(product_id):
    session['cart'] = [item for item in session.get('cart', []) if item['id'] != product_id]
    session.modified = True
    return redirect(url_for('cart'))

@app.route('/checkout')
def checkout():
    cart = session.get('cart', [])
    if not cart:
        return redirect(url_for('cart'))

    total = sum(item['price'] * item['quantity'] for item in cart)
    return render_template('checkout.html', cart=cart, total=total)

@app.route('/order', methods=['POST'])
def order():
    if 'cart' not in session or not session['cart']:
        return redirect(url_for('cart'))

    session.pop('cart', None)  # Clear cart after order
    return "Order placed successfully!"

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        if username in users:
            return "User already exists! Try logging in."

        users[username] = password
        session['user'] = username
        return redirect(url_for('home'))

    return render_template('register.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        if username in users and users[username] == password:
            session['user'] = username
            return redirect(url_for('home'))
        return "Invalid credentials! Try again."

    return render_template('login.html')

@app.route('/logout')
def logout():
    session.pop('user', None)
    return redirect(url_for('home'))

if __name__ == '__main__':
    app.run(debug=True)
