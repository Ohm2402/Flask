from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/api/post', methods=['POST'])
def post_data():
    # รับค่า name, age, phone จาก request
    name = request.headers.get('name')
    age = request.headers.get('age')
    phone = request.headers.get('phone')

    # ตรวจสอบว่ามีค่าทั้งสามตัวหรือไม่
    if name and age and phone:
        # สร้าง dictionary เพื่อเก็บข้อมูล
        data = {
            'name': name,
            'age': age,
            'phone': phone
        }
        # ส่งค่าทั้งสามกลับไปในรูปแบบ JSON
        return jsonify(data)
    else:
        return "Missing one or more values in headers!"

if __name__ == '__main__':
    app.run(debug=True, port=1010)
