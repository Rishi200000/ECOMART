from flask import Flask, render_template, request, redirect
from application import app
from vault import agent, User, Product, Category, update ,Cart, Order_Detail, Order_Items
import os,time
from authentication import *

from flask import request, redirect, url_for, flash
from vault import agent, User, Product, Category, Cart, Order_Detail, Order_Items


@app.route('/')
@app.route('/home')
def home():
    if 'user' in session:
        user = agent.query(User).filter(User.id == session['user']).first()
        categories = agent.query(Category).order_by(Category.id.desc()).all()
        products = agent.query(Product).order_by(Product.id.desc()).all()
        recent_products = agent.query(Product).order_by(Product.id.desc()).limit(5).all()
        return render_template('user/index.html', user=user, categories=categories, products=products, recent_products=recent_products)
    else:
        return render_template('login/login.html')


@app.route('/category/')
def category():
    if 'user' in session:
        categories = agent.query(Category).all()
        user = agent.query(User).filter(User.id == session['user']).first()
        return render_template('user/category.html', categories=categories, user=user)
    else:
        return render_template('login/new.html')

@app.route('/profile/<int:pid>')
def profile(pid):
    if 'user' not in session:
        return render_template('login/login.html')
    else:
        user = agent.query(User).filter(User.id == pid).first()
        return render_template('user/profile.html', user=user)


@app.route('/product/<int:pid>', methods=['POST', 'GET'])
def product(pid):
    if 'user' in session:
        if request.method == 'POST':
            # Retrieve form data to create a new product
            new_cart = Cart(
                user_id=session['user'],
                product_id=request.form['product_id'],
                product_name=request.form['product_name'],
                quantity=int(request.form['quantity']),
                price=int(request.form['price'])

            )
            # Add the new product to the database
            agent.add(new_cart)
            agent.commit()
            return redirect('/home')
        else:
            # Fetch the product with the given ID and display it
            item = agent.query(Product).filter(Product.id == pid).first()

            return render_template('user/buy.html', product=item)
    else:
        return render_template('login/login.html')


@app.route('/cart/<int:user_id>')
def cart(user_id):
    cart_items = agent.query(Cart).filter(Cart.user_id == user_id).all()

    total = sum(item.price * item.quantity for item in cart_items)

    # Add available payment methods
    payment_methods = ['Cash on Delivery', 'Credit Card', 'UPI', 'Net Banking']

    return render_template(
        'user/cart.html',
        user_id=user_id,
        cart_items=cart_items,
        total=total,
        payment_methods=payment_methods
    )


@app.route('/cart/del/<int:cid>')
def car_delete(cid):
    if request.method == 'GET':
        # Delete the product with the given ID from the database
        agent.query(Cart).filter(Cart.cart_id == cid).delete()
        agent.commit()

        return redirect(url_for('cart', user_id=session['user']))


@app.route('/cart/place_order/<int:pid>', methods=['POST'])
def place_order(pid):
    # Get values from form
    user_id = int(request.form.get('user_id', pid))
    total = float(request.form.get('total', 0))
    payment_method = request.form.get('payment_method', 'Cash on Delivery')

    # 1. Create new order
    new_order = Order_Detail(
        user_id=user_id,
        total=total,
        payment_method=payment_method
    )
    agent.add(new_order)
    agent.commit()

    # 2. Move items from cart to order_items
    cart_items = agent.query(Cart).filter(Cart.user_id == user_id).all()
    for item in cart_items:
        # Save order item
        order_item = Order_Items(
            user_id=user_id,
            order_id=new_order.id,
            product_id=item.product_id,
            quantity=item.quantity,
            amount=item.price,
            product_price=item.price,
            product_name=item.product_name
        )
        agent.add(order_item)

        # Decrease product stock
        product = agent.query(Product).get(item.product_id)
        if product:
            product.quantity = max(product.quantity - item.quantity, 0)
            agent.add(product)

    agent.commit()

    # 3. Clear the user's cart
    agent.query(Cart).filter(Cart.user_id == user_id).delete()
    agent.commit()

    flash("✅ Order placed successfully!", "success")
    return redirect(url_for('cart', user_id=user_id))  # ✅ Use correct endpoint

@app.route('/orders/<int:pid>')
def my_orders(pid):
    if 'user' not in session:
        return render_template('login/login.html')
    else:
        orders = agent.query(Order_Detail).filter(Order_Detail.user_id == pid).all()
        return render_template('user/orders.html', orders=orders)

@app.route('/ordered_products/<int:oid>')
def ordered_products(oid):
    if 'user' not in session:
        return render_template('login/login.html')
    else:
        products = agent.query(Order_Items).filter(Order_Items.order_id == oid).all()
        order = agent.query(Order_Detail).filter(Order_Detail.id == oid).first()

        return render_template('user/ordered_products.html', items=products, order=order, user_id=session['user'], cart_items=order)


@app.route('/search', methods=['POST', 'GET'])
def search():
    if request.method == 'POST':
        search_value = request.form['search']
        user = agent.query(User).filter(User.id == session['user']).first()
        categories = agent.query(Category).filter(Category.name.like('%'+search_value+'%')).all()
        products = agent.query(Product).filter(Product.name.like('%'+search_value+'%')).all()

        return render_template('user/search.html', user=user, categories=categories, products=products,sv=search_value)


@app.route('/user/payments/<int:user_id>')
def user_payments(user_id):
    payments = agent.query(Order_Detail).filter(Order_Detail.user_id == user_id).all()
    return render_template('user/payments.html', payments=payments)

