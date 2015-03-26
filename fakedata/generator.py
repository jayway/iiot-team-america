from boto import kinesis
import testdata
import json
import time
import datetime

stream_name = "iiot-team-america"
kinesis = kinesis.connect_to_region("eu-west-1")
kinesis.describe_stream(stream_name)

class SensorEvent(testdata.DictFactory):
    timestamp = testdata.DateIntervalFactory(datetime.datetime.now(), datetime.timedelta(seconds=10))
    installationId = testdata.RandomSelection(['test'])
    tag = testdata.RandomSelection(['temp1', 'temp1', 'humidity1'])
    metric = testdata.RandomFloat(20, 30)
    humidity = testdata.RandomFloat(60, 99)
    
for event in SensorEvent().generate(50):
    event["timestamp"] = event["timestamp"].isoformat()
    if event["tag"].startswith('humidity'):
        event["metric"] = event["humidity"]
    event["humidity"] = None
    print(event)
    
    kinesis.put_record(stream_name, json.dumps(event), event["installationId"])
    

