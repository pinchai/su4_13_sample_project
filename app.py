from flask import Flask, render_template, request, json
from products import products as products_list
from telegram import sendMessage
from tabulate import tabulate
from flask_mail import Mail, Message

app = Flask(__name__)
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = 'e16153937@gmail.com'
app.config['MAIL_PASSWORD'] = 'fsny yzsm kehv lwib'  # Use App Password from Google
app.config['MAIL_DEFAULT_SENDER'] = 'e16153937@gmail.com'

mail = Mail(app)


@app.route('/sendMail')
def send_email():
  msg = Message('Invoice From SU4.13 Shop', recipients=['pinchai.pc@gmail.com'])
  msg.body = 'This is a plain text email sent from Flask.'
  message = render_template('mail/invoice.html')
  msg.html = message
  mail.send(msg)
  return 'Email sent succesfully!'


@app.get('/')
def home():
    products = products_list
    return render_template('home.html', products=products, module='home')


@app.get('/product')
def product():
    products = products_list
    return render_template('product.html', products=products, module='product')


@app.get('/cart')
def cart():
    return render_template('cart.html', module='cart')


@app.get('/checkout')
def checkout():
    return render_template('checkout.html', module='checkout')


@app.get('/support')
def support():
    return render_template('support.html', module='support')


@app.post('/place-order')
def placeOrder():
    form = request.form
    full_name = form.get('full_name')
    email = form.get('email')
    phone = form.get('phone')
    address = form.get('address')
    cart_item_str = form.get('cart_item')
    cart_item = json.loads(cart_item_str)
    chat_id = '@su413_FAFA168'

    index = 0
    item_row = []
    for item in cart_item:
        item_row.append(
            [
                index+1,
                f"{item['title'][0:8]}...",
                item['price'],
                item['qty'],
            ]
        )
        index += 1

    table = tabulate(
        tabular_data=item_row,
        headers=['Title', 'Price', "Quantity"]
    )

    html = f"<strong>👑 Customer Name: {full_name}</strong>\n"
    html += f"<strong>📱 Customer Phone: {phone}</strong>\n"
    html += f"<strong>📩 Customer Email: {email}</strong>\n"
    html += f"<strong>🪙 Customer Address: {address}</strong>\n"
    html += f"<strong>------------------------</strong>\n"
    html += f"<pre>{table}</pre>\n"

    res = sendMessage(
        chat_id=chat_id,
        message=html
    )

    # send mail to customer
    msg = Message('Invoice From SU4.13 Shop', recipients=[email])
    msg.body = 'This is a plain text email sent from Flask.'
    message = render_template('mail/invoice.html')
    msg.html = message
    mail.send(msg)

    return f"{res}"


if __name__ == '__main__':
    app.run()
