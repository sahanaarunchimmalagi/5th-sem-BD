from flask import Flask,request,jsonify
app = Flask(__name__)
Orders = []
@app.route('/addOrders',methods = ['POST'])
def add_Orders():
    data = request.get_json()
    Orders.append(data)
    return jsonify({"message":"order add successfully",
                    "Orders":data})
@app.route('/ShowOrders', methods = ['GET'])
def  Show_Orders():
    return jsonify(Orders)
if __name__ == '__main__':
    app.run(debug=True)