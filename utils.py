#!/usr/bin/python

import pyrax
import random
import time
import logging


def random_server(cs):
    '''
    Return a random server object from the account.
    Requires a pyrax.cloudservers object.
    '''
    servers = cs.servers.list()
    return random.choice(servers)


def server_progress(cs, server, n=15):
    '''
    Waits for a server to finish building. Once complete:
     - Print Server Information
     - Return True
    Requres a pyrax.cloudservers object and a server object.
    '''
    logging.warn("This fuction waits for the build process to complete.")
    logging.warn("This can take a long time. Please be patient.")
    server = cs.servers.get(server.id)
    while server.progress != 100:
        server = cs.servers.get(server.id)
        time.sleep(n)
    else:
        return True


def image_progress(cs, image, n=15):
    '''
    Waits for an image to finish. Once complete:
     - Print Image Information
     - Return True
    Requres a pyrax.cloudservers object and an image object.
    '''
    logging.warn("This fuction waits for the image process to complete.")
    logging.warn("This can take a long time. Please be patient.")
    image = cs.images.get(image.id)
    while image.progress != 100:
        image = cs.images.get(image.id)
        time.sleep(n)
    else:
        return True
