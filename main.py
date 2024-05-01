#!/usr/bin/env python3
import os
import time
import logging
from utils.utils import Utils

# Contains all logic for the way this app should run.

# TODO: Implement a timer to run this every 1 minute
# TODO:  Log when the IP Address changes
# TODO: send me a notification when the IP Address changes
def main():
    utils = Utils(os.getenv('DNS_API_KEY'), os.getenv('DNS_API_SECRET'))
    ip = utils.getCurrentIp()
    stored_ip = utils.getStoredIp()
    if ip == stored_ip:
        logging.info('IP Address has not changed')
        return False
    else:
        logging.info('IP Address has changed')
        response = utils.configureGodaddy(ip, 'egroupus.com')
        if response:
            logging.info('IP Address has been updated')
            utils.storeCurrentIp(ip)
            utils.notify('IP Address has changed', f'The IP Address has changed to %{ip}')


if __name__ == '__main__':
    print(main())
