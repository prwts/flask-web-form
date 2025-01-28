from flask import Flask, render_template, request

app = Flask(__name__)

# หน้าเลือกแบบฟอร์ม
@app.route('/')
def home():
    return render_template('index.html')

# โหลดฟอร์มที่ผู้ใช้เลือก
@app.route('/form/<form_name>')
def show_form(form_name):
    return render_template(f"{form_name}.html")

# รับข้อมูลจากฟอร์ม
@app.route('/submit', methods=['POST'])
def submit_form():
    form_type = request.form['form_type']
    name = request.form['name']
    email = request.form['email']
    details = request.form.get('details', '')

    print(f"แบบฟอร์ม {form_type} - ชื่อ: {name}, อีเมล: {email}, รายละเอียด: {details}")

    return f"ข้อมูลถูกส่งเรียบร้อยแล้วสำหรับ {form_type}!"

if __name__ == '__main__':
    app.run(debug=True)
