from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/api/data', methods=['GET'])
def get_data():
    # สร้างข้อมูล JSON ที่ต้องการ retrun
    data = {
        'message': 'สวัสดี, โลก!',
        'status': 'success'
    }
    # ใช้ jsonify เพื่อแปลงข้อมูล Python เป็น JSON
    response = jsonify(data)
    # ปริ้นค่า JSON ที่ถูกส่งกลับมา
    print(response.json)
    return response

if __name__ == '__main__':
    app.run(debug=True, port=2020)
