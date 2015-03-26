from boto import kinesis
import time
import json

import argparse
import logging

logging.getLogger("boto").setLevel(logging.WARNING)

def _get_args():
    parser = argparse.ArgumentParser(prog='reader', description='reads data from kinesis')

    parser.add_argument("-d", "--debug", help="debug logging", dest="log_level", action="store_const", const=logging.DEBUG)
    parser.add_argument("-q", "--quiet", help="less output", dest="log_level", action="store_const", const=logging.WARNING)
    parser.set_defaults(log_level=logging.INFO)

    parser.add_argument('--region', help='AWS region', default ="eu-west-1")
    parser.add_argument('stream', help='stream name')
    
    args = parser.parse_args()
    return vars(args)
    
    
def get_shard_ids(kinesis, stream_name):
    shard_ids = []
    
    response = kinesis.describe_stream(stream_name)
    if response and 'StreamDescription' in response:
        stream_name = response['StreamDescription']['StreamName']                   
        for shard_id in response['StreamDescription']['Shards']:
             shard_id = shard_id['ShardId']
             shard_iterator = kinesis.get_shard_iterator(stream_name, shard_id, "TRIM_HORIZON")
             shard_ids.append({'shard_id' : shard_id ,'shard_iterator' : shard_iterator['ShardIterator'] })
    return shard_ids

def process_shard(kinesis,shard_it):
    out = kinesis.get_records(shard_it, limit=100)
    for record in out["Records"]:
        data = json.loads(record["Data"])
        print data
    return out["NextShardIterator"]

if __name__ == "__main__":
    args = _get_args()

    logging.basicConfig(level=args["log_level"])

    kinesis = kinesis.connect_to_region(args["region"])
    
    stream_name = args["stream"] 
    shard_ids = get_shard_ids(kinesis, stream_name )
    
    while 1 == 1:
        for shard_id in shard_ids:
            # print shard_id
            shard_it = shard_id["shard_iterator"]
            shard_id["shard_iterator"] = process_shard(kinesis, shard_it)
            time.sleep(0.2)