from flask import Flask
from flask import (render_template,request)
import pyrebase

config = {
    "apiKey": "AIzaSyCkM6uRP1-H8MHmWkEunGJ8fZ8lp8MkP28",
    "authDomain": "eat-me-it.firebaseapp.com",
    "databaseURL": "https://eat-me-it.firebaseio.com",
    "projectId": "eat-me-it",
    "storageBucket": "eat-me-it.appspot.com",
    "messagingSenderId": "734459377789",
    "appId": "1:734459377789:web:99e9c249161bda240c5914",
    "measurementId": "G-1NS6MEQL1B"
}
"""
------------------------------------------------------------------
Data
"""

shop_one = [ {'name_food':'ข้าวผัดกุ้ง','price':'35'}, 
            {'name_food':'ข้าวผัดกุ้ง','price':'35'},
			{'name_food':'ข้าวผัดหมู','price':'35'},
			{'name_food':'ข้าวผัดกระเพราหมู','price':'35'},
			{'name_food':'ข้าวผัดกระเพราะไก่','price':'35'},
			{'name_food':'ข้าวผัดกระเพราเบค่อน','price':'35'},
			{'name_food':'ข้าวผัดกระเพราะหมูกรอบ','price':'35'},
			{'name_food':'ข้าวผัดกระเพราะกุ้ง','price':'35'},
			{'name_food':'ข้าวผัดกระเพราปลาหมึก','price':'35'},
			{'name_food':'ข้าวคะน้าหมูกรอบ','price':'35'}	
        ]
shop_two = [ {'name_food':'ข้าวไข่ข้น','price':'25'},
            {'name_food':'ข้าไข่ข้น พิเศษ','price':'30'},
            {'name_food':'ข้าวไข่เจียว','price':'25'},
            {'name_food':'ข้าวไข่เจียว พิเศษ','price':'30'},	
            {'name_food':'ข้าวหมูทอดเกาหลี','price':'30'},
            {'name_food':'ข้าวไก่เทอริยากิ','price':'30'},
            {'name_food':'ข้าวผัดไข่','price':'50'},
            {'name_food':'ราเมง','price':'30'},
            {'name_food':'ราเมง พิเศษ','price':'40'},
            {'name_food':'สปาเก็ตตี้','price':'30'}	
        ]
shop_three = [ {'name_food':'ข้าวไก่ย่าง','price':'40'},
		    {'name_food':'ข้าวมันไก่ต้ม','price':'35'},
		    {'name_food':'ข้าวมันไก่ต้ม พิเศษ','price':'40'},
		    {'name_food':'ข้าวมันไก่ทอด','price':'30'},
		    {'name_food':'ข้าวมันไก่ทอด พิเศษ','price':'40'},
		    {'name_food':'ข้าวมันไก่ ผสม','price':'40'},
		    {'name_food':'ข้าวหมูแดง','price':'30'},
		    {'name_food':'ข้าวยำไก่ย่าง','price':'40'},
		    {'name_food':'ข้าวขาหมู','price':'30'},
		    {'name_food':'ข้าวขาหมู พิเศษ','price':'40'}	
        ]
shop_four = [ {'name_food':'ก๋วยเตี๋ยวน้ำใส','price':'35'},
			{'name_food':'ก๋วยเตี๋ยวต้มยำ','price':'35'},
			{'name_food':'ก๋วยเตี๋ยวต้มยำน้ำข้น','price':'35'},
			{'name_food':'ก๋วยเตี๋ยวสุโขทัย','price':'35'},
			{'name_food':'ก๋วยเตี๋ยวไก่ฉีก','price':'35'},
			{'name_food':'ก๋วยเตี๋ยวไก่ตุ๋น','price':'35'},
			{'name_food':'ก๋วยเตี๋ยวหมูตุ๋น','price':'35'},
			{'name_food':'ก๋วยเตี๋ยวามาม่าต้มยำ','price':'35'},
			{'name_food':'ก๋วยเตี๋ยวน้ำตก','price':'35'},
			{'name_food':'ก๋วยเตี๋ยวบะหมี่หมูแดง','price':'35'}	
        ]
shop_five = [ {'name_food':'ผัดมาม่า','price':'30'},
			{'name_food':'ผัดมาม่าเบค่อน','price':'40'},
			{'name_food':'ผัดมาม่าขี้เมา','price':'35'},
			{'name_food':'มักกะโรนี','price':'30'},
			{'name_food':'มักกะโรนีคาโบนาร่า','price':'40'},
			{'name_food':'มักกะโรนีอบชีส','price':'50'},
			{'name_food':'สปาเก็ตตี้','price':'30'},
			{'name_food':'สปาเก็ตตี้เบค่อน','price':'40'},
			{'name_food':'สปาเก็ตตี้ผัดขี้เมา','price':'40'},
			{'name_food':'สปาเก็ตตี้คาโบนาร่า','price':'40'}
        ]
shop_six = [{'name_food':'นมสด ปั่น','price':'40'},
			{'name_food':'โกโก้ ปั่น','price':'40'},
			{'name_food':'ชานม ปั่น','price':'40'},
			{'name_food':'ชาเขียว ปั่น','price':'40'},
			{'name_food':'นมาดโอริโ้ ปั่น','price':'45'},
			{'name_food':'นมสดน้ำผึ้ง ปั่น','price':'45'},
			{'name_food':'ขนมปังปิ้ง','price':'15'},
			{'name_food':'ฮันนี่โทส','price':'45'},
			{'name_food':'บิงซู','price':'50'},
			{'name_food':'เฟรนฟราย','price':'30'}	
        ]

"""
End Data
------------------------------------------------------------------
code
"""
app = Flask(__name__)

Q = 0

@app.route('/')
@app.route('/templates/index.html')
def home_web():
    return render_template("index.html")

@app.route('/templates/sell.html')
def sell():
    return render_template("sell.html")

@app.route('/templates/buy.html')
def buy():
    return render_template("buy.html", test = Q)



if __name__ == '__main__':
    app.run(debug="TRUE")