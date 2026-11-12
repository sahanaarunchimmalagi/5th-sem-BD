from flask import Flask,request,jsonify
app = Flask(__name__)
@app.route('/')
def home():
    return"server is running.send Post request to/n8n-webhook"
@app.route('/n8n-webhook',methods=['POST'])
def n8n_webhook():
    data=request.get_json()
    print("received from n8n:",data)
    return jsonify({"status":"received","data":data})
if __name__ == '__main__':
    app.run(debug=True,port=5000)