#!/usr/bin/python

import pyrax
import time

challenge = """Write a script that builds three 512 MB Cloud Servers that
            follow a similar naming convention. (ie., web1, web2, web3)
            and returns the IP and login credentials for each server.
            Use any image you want."""
points = 1

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
delete = False
# Number of attempts
timeout = 9

# Servers to build
servers = ['web1', 'web2', 'web3']

for name in servers:
    network = 0

    # Create server and print attributes
    server = cs.servers.create(name, ubu_image.id, flavor_512.id)
    print "=" * 20
    print "ID:", server.id
    print "Status:", server.status
    print "Admin password:", server.adminPass

    # Check for network configuration
    count = 0
    print "Retrieving Network Configuration . . . "
    while count < timeout:
        count += 1
        print "Attempt %i out of %i" % (count, timeout)
        server = cs.servers.get(server.id)
        time.sleep(5)
        if "public" in server.networks:
            network = 1
            break

    # Check to see if we received network information
    if network == 1:
        print "Networks:", server.networks
    else:
        print "ERROR - Network failed after %i attempts." % timeout

    # Delete server
    if delete == True:
        time.sleep(5)
        print "Deleting:", server.id
        server.delete()
    print "=" * 20
