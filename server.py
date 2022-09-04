from collections import defaultdict
from flask import Flask, request


api = Flask("server-tagup")
measurements = defaultdict(list)  



@api.route('/healthz', methods=["GET"])
def get_healthz():
    return "", 204



@api.route('/data', methods=["POST"])
def post_data():
    global measurements
    try:
        data= request.json
            

        assert "timestamp" in data
        assert "value" in data 
        assert "sensor" in data 
        td_val=type(data["value"])
        assert td_val in [int, float]  
        measurements[data.pop("sensor")].append(data)
        return "", 204

    
    except TypeError:
        return "Formatting issue, need : [{...}, ...]", 400

    except AssertionError:
        return "'sensor' and 'timestamp' are strings while 'value' is numeric", 400


#Handling GET functions 
@api.route('/statistics/<string:id>', methods=["GET"])
def get_stats(id):
    response = {}
    current_measure=measurements[id]
    response["count"] = len(current_measure)
    current_sum=sum(data["value"] for data in current_measure)
    current_count=response["count"]

    response["avg"] = current_sum/(current_count or 1)
    a1=current_count > 0
    if a1:
        response["last_measurement"] =current_measure[-1]["timestamp"]
    else:
        response["last_measurement"] = None
    return response, 200


#DELETE using ID
@api.route('/statistics/<string:id>', methods=["DELETE"])
def delete_stats(id):
    measurements.pop(id, None)
    return "", 204


api.run(host="0.0.0.0", port=8080)