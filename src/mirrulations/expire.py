import redis
from mirrulations.redis_manager import RedisManager
import time
import logging

FORMAT = '%(asctime)-15s %(clientip)s %(user)-8s %(message)s'
logging.basicConfig(filename='expire.log', format=FORMAT)
d = {'clientip': '192.168.0.1', 'user': 'EXPIRE'}
logger = logging.getLogger('tcpserver')

r = RedisManager(redis.Redis())


def expire():
    """
    Checks to see if any of the in-progress jobs have expired
    :return:
    """
    logger.info('Checking for expired jobs...')
    while(True):
        logger.debug('Awake: %s', 'expire: expire is active', extra=d)
        logger.debug('Calling Function: %s', 'expire: attempting to find expired', extra=d)
        r.find_expired()
        logger.debug('Function Successful: %s', 'expire: find expired successfully', extra=d)
        logger.debug('Sleep: %s', 'expire: sleep for 1 hours', extra=d)
        logger.info('Returning to sleep')
        time.sleep(3600)


if __name__ == '__main__':
    expire()
