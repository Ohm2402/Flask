from flask import Flask, request

app = Flask(__name__)

@app.route('/api/post_data', methods=['POST'])
def receive_params():
    # รับข้อมูลพารามิเตอร์จาก URL
    params = request.args.to_dict()
    
    # ตรวจสอบว่ามีพารามิเตอร์ 'name' และ 'age' หรือไม่
    if 'name' in params and 'age' in params:
        name = params['name']
        age = params['age']
        
        # พิมพ์และส่งค่า 'name' และ 'age' พร้อมกับข้อความ "successfully!" กลับไป
        message = f'successfully! Name: {name}, Age: {age} '
        print(message)
        return message, 200
    else:
        return 'Missing parameters!', 400
    
if __name__ == '__main__':
    app.run(debug=True, port=1999)
