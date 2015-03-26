from boto import kinesis
import testdata
import json
import time
import datetime

stream_name = "iiot-team-america"
kinesis = kinesis.connect_to_region("eu-west-1")
kinesis.describe_stream(stream_name)

class SensorEvent(testdata.DictFactory):
    timestamp = testdata.DateIntervalFactory(datetime.datetime.now() - datetime.timedelta(hours=4), datetime.timedelta(seconds=10))
    installationId = testdata.RandomSelection(['Malmo', 'Stockholm', 'Lund'])
    tag = testdata.RandomSelection(['temp1', 'temp2', 'temp3', 'humidity1', 'humidity2'])
    metric = testdata.RandomFloat(20, 30)
    humidity = testdata.RandomFloat(60, 99)
    
for event in SensorEvent().generate(20000):
    event["timestamp"] = event["timestamp"].isoformat()
    if event["tag"].startswith('humidity'):
        event["metric"] = event["humidity"]
    event.pop("humidity", None)
    print(event)
    
    kinesis.put_record(stream_name, json.dumps(event), event["installationId"])
    

