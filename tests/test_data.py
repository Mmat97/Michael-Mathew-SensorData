from json import load
from requests import get, post, delete






def get_response(path, method, data=None):
    return method("http://localhost:8080%s" % path, json=data)
def check_data(filename, main_c):
    all_inf = load(open(filename))
    for info in all_inf:
        r = get_response("/data", post, data=info)
        assert r.status_code == main_c













# Check if correct(204) 
def test_healthz():
    r = get_response("/healthz", get)
    assert r.status_code == 204
    assert len(r.text) == 0


# Check POST data
def test_data():
    check_data("post_data.json", 204)


# Check GET 
def test_get_stats():
    data = load(open("sensor1_check.json"))
    r2 = get_response("/statistics/sensor1", get)
    r2_json = r2.json()
    #assert r2_json == "wewewevw"
    assert r2_json["last_measurement"] == data["last_measurement"]
    assert r2_json["count"] == data["count"]
    assert r2_json["avg"] == data["avg"]
    get_response("/statistics/sensor100", delete)


# Check Delete
def test_delete_stats():
    r3 = get_response("/statistics/sensor500", delete)
    r4 = get_response("/statistics/sensor500", get)
    assert r4.json()["count"] == 0