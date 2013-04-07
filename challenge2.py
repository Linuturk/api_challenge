#!/usr/bin/python

import pyrax
import logging
import random


challenge = """
            Write a script that clones a server (takes an image and deploys
            the image as a new server). Get a listing of servers on an
            account, grab a random server, image it, and then create a new
            server from this image.
            """
points = 2

# Logging
#logging.basicConfig(level=logging.INFO)
logging.warn("Change logging level to INFO for more details.")
logging.info("Challenge: %s", challenge)
logging.info("Points: %i", points)

# Setup pyrax creds and objects
pyrax.set_credential_file(".rackspace_cloud_credentials")
cs = pyrax.cloudservers

output = []

# Choose a random server
logging.info("Choosing a random server.")
servers = cs.servers.list()
server = random.choice(servers)
logging.info("Server %s chosen.", server.name)
output.append("Source Server: " + str(server.name))

# Image this server
image_name = server.name + "-clone"
logging.info("Image Name: %s", image_name)
output.append("Image Name: " + str(image_name))
image_id = server.create_image(image_name)
image = cs.images.get(image_id)
logging.info("Image %s in progress...", image_id)

# Wait for image to complete
logging.info("Waiting for image to complete. Grab a snickers.")
pyrax.utils.wait_until(image, "status", "ACTIVE", attempts=0, verbose=True)
logging.info("Image %s complete.", image.name)

# Clone server
clone_name = image_name
logging.info("Server Name: %s", clone_name)
clone = cs.servers.create(clone_name, image, server.flavor['id'])
output.append("Clone Server:")
output.append("\tName: " + str(clone.name))
output.append("\tID: " + str(clone.id))
output.append("\tStatus: " + str(clone.status))
output.append("\tAdmin Password: " + str(clone.adminPass))
logging.info("Server clone %s in progress...", clone.id)

# Wait for clone to finish building
logging.info("Waiting for clone build to complete. Grab another snickers.")
pyrax.utils.wait_until(clone, "status", ('ACTIVE', 'ERROR'), verbose=True)
clone = cs.servers.get(clone.id)
output.append("\tNetworks: " + str(clone.networks))
logging.info("Server %s complete.", clone.name)

for message in output:
    print message
