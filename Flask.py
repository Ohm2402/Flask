from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/api', methods=['POST'])
def handle_post_request():
    # รับ JSON body จาก request
    json_data = request.json
    
    # แสดงข้อมูล JSON body ที่ได้รับ
    print(json_data)
    
    # รับค่าอายุจาก JSON body
    age = json_data.get('age')  # หรือใช้ json_data['age'] ก็ได้
    
    # ประมวลผลข้อมูล JSON ตามต้องการ
    # เช่น ทำสิ่งใดสิ่งหนึ่งกับข้อมูล JSON ที่ได้รับ
    
    # สร้างข้อความ Response พร้อมระบุอายุ
    response_message = {'message': f'Received JSON data successfully! Age: {age}'}
    
    # คืนค่า Response ออกไป
    return jsonify(response_message)

if __name__ == '__main__':
    app.run(debug=True, port=5000)
