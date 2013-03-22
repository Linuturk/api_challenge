#!/usr/bin/python

import pyrax
import logging
import utils

#logging.basicConfig(level=logging.INFO)
challenge = """
            Write a script that clones a server (takes an image and deploys
            the image as a new server). get a listing of servers on an
            account, grab a random server, image it, and then create a new
            server from this image.
            """
points = 2
logging.info("Challenge: %s", challenge)
logging.info("Points: %i", points)

# Setup pyrax creds and objects
logging.info("Creating pyrax.cloudservers object.")
pyrax.set_credential_file(".rackspace_cloud_credentials")
cs = pyrax.cloudservers

# Choose a random server
logging.info("Choosing a random server.")
server = utils.random_server(cs)
logging.info("Server %s chosen.", server.name)

# Image this server
image_name = server.name + "-clone"
logging.info("Image Name: %s", image_name)
image_id = server.create_image(image_name)
image = cs.images.get(image_id)
logging.info("Image %s in progress...", image_id)

# Wait for image to complete
logging.info("Waiting for image to complete. Grab a snickers.")
utils.image_progress(cs, image)
logging.info("Image %s complete.", image.name)

# Clone server
clone_name = image_name
logging.info("Server Name: %s", clone_name)
clone = cs.servers.create(clone_name, image, server.flavor['id'])
logging.info("Server clone %s in progress...", clone.id)

# Wait for clone to finish building
logging.info("Waiting for clone build to complete. Grab another snickers.")
utils.server_progress(cs, clone)
logging.info("Server %s complete.", clone.name)
