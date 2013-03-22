#!/usr/bin/python

import pyrax
import logging
import utils

challenge = """Write a script that accepts a directory as an argument as well
            as a container name. The script should upload the contents of the
            specified directory to the container (or create it if it doesn't
            exist). The script should handle errors appropriately.
            (Check for invalid paths, etc.)
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
