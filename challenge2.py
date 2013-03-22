#!/usr/bin/python

import pyrax
import time

challenge = "Write a script that clones a server (takes an image and deploys the image as a new server). get a listing of servers on an account, grab a random server, image it, and then create a new server from this image."
points = 2

# Setup pyrax creds and objects
pyrax.set_credential_file(".rackspace_cloud_credentials")
cs = pyrax.cloudservers

id_of_server = "8ae80604-cac4-415a-98b2-8a5716f41909"
image_name = "deleteme"

server = cs.servers.get(id_of_server)
image = server.create_image(image_name)

while image.progress != 100:
    image = cs.images.get(image_id)
    time.sleep(5)
    print "Image at %i%" % image.progress
