from flask import Flask, jsonify, request

app = Flask(__name__)
temperatures= [
    
   
]

@app.route('/temperatures', methods=['POST'])
def addTemp():
    temperature = request.get_json()
    temperatures.append(temperature)
    return {'id': len(temperatures)},200

@app.route('/temperatures<int:index>', methods=['PUT'])
def updateTemp(index):
    temperature = request.get_json()
    temperature.append(temperature)
    return {'id': len(temperatures)},200

@app.route('/temperatures', methods=['GET'])
def displayTemp():
    return jsonify(temperatures)

@app.route('/temperatures/<int:index>', methods=['GET'])
def displayTempById(index):
    return jsonify(temperatures[index])

@app.route('/temperatures/<int:index>',methods=['DELETE'])
def deleteTemp(index):
    temperatures.pop(index)
    return 'Temperature was successfully deleted', 200

if __name__ == '__main__':
    app.run()