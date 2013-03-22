#!/usr/bin/python

import pyrax
import time
import logging

#logging.basicConfig(level=logging.INFO)
challenge = """
            Write a script that builds three 512 MB Cloud Servers that
            follow a similar naming convention. (ie., web1, web2, web3)
            and returns the IP and login credentials for each server.
            Use any image you want.
            """
points = 1
logging.info("Challenge: %s", challenge)
logging.info("Points: %i", points)

# Setup pyrax creds and objects
pyrax.set_credential_file(".rackspace_cloud_credentials")
cs = pyrax.cloudservers
imgs = cs.images.list()
flvs = cs.flavors.list()

# Select Ubuntu and 512MB
ubu_image = [img for img in cs.images.list()
             if "Ubuntu 12.04" in img.name][0]
flavor_512 = [flavor for flavor in cs.flavors.list()
              if flavor.ram == 512][0]

# Delete servers when finished
delete = True

# Servers to build
servers = ['web1', 'web2', 'web3']

for name in servers:
    network = 0

    # Create server and print attributes
    server = cs.servers.create(name, ubu_image.id, flavor_512.id)
    print "ID:", server.id
    print "Status:", server.status
    print "Admin password:", server.adminPass

    # Check for network configuration
    logging.warn("Waiting for network. This can take a while. Be patient.")
    while "public" not in server.networks:
        server = cs.servers.get(server.id)
        time.sleep(10)
    else:
        print "Network:", server.networks

    # Delete server
    if delete is True:
        time.sleep(10)
        logging.warn("Delete is True. Deleting %s", server.id)
        server.delete()
