from flask import Flask,jsonify,request

data=[{
    'id':1,
    'Name':"John",
    'Contact':"9987644456",
    "done":False
},
{
    'id':2,
    'Name':"Raju",
    'Contact':"9876543222",
    "done":False
},
]
app = Flask(__name__)

@app.route('/addData',methods=["POST"])
def add_Task():
    if not request.json:
        return jsonify({
            "status":"error",
            "message":"Please provide the data"
        },400)
    contact={
        'id':data[-1]['id']+1,
        'Name':request.json['Name'],
        'Contact':request.json.get('Contact',""),
        'done':False
    }
    data.append(contact)
    return jsonify({
        "status":"success",
        "message":"done"
    })

@app.route('/getData')
def get_Task():
    return jsonify({
        "data":data,
    })

if(__name__ == "__main__"):
    app.run(debug=True)
