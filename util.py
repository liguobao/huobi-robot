import os
import os.path
import sys
import json
import logging
import yaml
import redis

config = None

def get_config():
    global config
    if config:
        return config
    with open("config.yaml", 'r') as stream:
        try:
            config = yaml.load(stream)
            return config
        except yaml.YAMLError as exc:
            get_logger().error('Config Error')
            exit(0)

def get_redis():
    config = get_config()
    #return redis.Redis(host=config['redis_host'], port=6379, decode_responses=True, password=config['redis_password'])
    return redis.Redis(host=config['redis_host'], port=6699, decode_responses=True, password=config['redis_password'])
    
    