import mysql.connector
from flask import Flask, redirect, render_template, request, url_for

app = Flask(__name__)

# MySQL Configuration
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="1234@aman",
    database="information",
    auth_plugin='mysql_native_password'

)

@app.route('/')
def index():
    return render_template('home.html')

@app.route('/submit', methods=['POST'])
def submit():
    if request.method == 'POST':
        name = request.form['name']
        contact = request.form['contact']
        email = request.form['email']
        gender = request.form['gender']
        home_station = request.form['home_station']
        bottomwear = ',  '.join(request.form.getlist('bottomwear'))
        upwear = ', '.join(request.form.getlist('upwear'))
        ledies_wear = ', '.join(request.form.getlist('ledies-wear'))
        footwear = request.form['footwear']
        color = request.form['color']
        chest_size = request.form['chest_size']
        waist_size = request.form['waist_size']

        cursor = db.cursor()
        insert_query = "INSERT INTO feedback (name, contact, email, gender, home_station, bottomwear, upwear, ledies_wear, footwear, color, chest_size, waist_size) VALUES ('{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}')".format(name, contact, email, gender, home_station, bottomwear, upwear, ledies_wear, footwear, color, chest_size, waist_size)
        print(insert_query)
        
        cursor.execute(insert_query)
        db.commit()

        cursor.close()
        return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
