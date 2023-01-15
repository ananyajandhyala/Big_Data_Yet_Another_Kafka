#!/bin/python3

import json
#from util import os_utils,http_utils

def _allBrokersHealthy(expected_brokers, current_brokers):
    return not _getOfflineBrokers(expected_brokers, current_brokers)

def getBrokerStatus(x,y):
    expected_brokers = x
    current_brokers  = y
    
    if _allBrokersHealthy(expected_brokers,current_brokers):
        return '{"status": "green"}'
    elif not current_brokers:
        return '{"status": "red", "reasons": ["all brokers offline"]}'
    else:
        return '{"status":"yellow","reasons": ["brokers offline: ' + str(_getOfflineBrokers(expected_brokers, current_brokers)) + '"]}'

def _getOfflineBrokers(expected_brokers, current_brokers):
    return expected_brokers - current_brokers


