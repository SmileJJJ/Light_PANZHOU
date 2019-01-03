import json

def getdata(path):
    with open(path) as jdata:
        jsonData = json.loads(jdata.read(1024))
        shapeData = jsonData['shapes'][0]
        label = shapeData['label']
        points = shapeData['points']
    return points

'''
'../../OpenCV/Light_spot_project/usual_status/light_spot/1545360636.4174533.json'
[[167, 308], [255, 269], [321, 247], [438, 267], [369, 301],
[364, 295], [353, 308], [290, 346]]
'''