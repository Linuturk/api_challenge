#!/usr/bin/python

import pyrax
import time
import logging


challenge = """
            Write a script that builds three 512 MB Cloud Servers that
            follow a similar naming convention. (ie., web1, web2, web3)
            and returns the IP and login credentials for each server.
            Use any image you want.
            """
points = 1

# Servers to build
server_names = ['web1', 'web2', 'web3']
delete = False

# Logging
#logging.basicConfig(level=logging.INFO)
logging.warn("Output is logged as INFO by default.")
logging.warn("Change logging level to INFO for more details.")
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

servers = []

for name in server_names:
    network = 0

    # Create server and print attributes
    server = cs.servers.create(name, ubu_image.id, flavor_512.id)
    servers.append(server)
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

# Delete servers
if delete is True:
    for server in servers:
        logging.warn("Deleting %s", server.id)
        server.delete()
