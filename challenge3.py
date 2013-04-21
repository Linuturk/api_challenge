#!/usr/bin/python
# -*- coding: utf-8 -*-

import pyrax
import logging
import argparse
import os.path

challenge = """
            Write a script that accepts a directory as an argument as well
            as a container name. The script should upload the contents of the
            specified directory to the container (or create it if it doesn't
            exist). The script should handle errors appropriately.
            (Check for invalid paths, etc.)
            """
points = 2

# Logging
#logging.basicConfig(level=logging.INFO)
logging.info("Challenge: %s", challenge)
logging.info("Points: %i", points)

# Setup pyrax creds and objects
pyrax.set_credential_file(".rackspace_cloud_credentials")
cf = pyrax.cloudfiles

# Handle arguments
parser = argparse.ArgumentParser()
parser.add_argument('directory', type=str,
                    help="Full path the the directory being uploaded.")
parser.add_argument('container', type=str,
                    help="Container where to upload the directory.")

args = parser.parse_args()

if os.path.exists(args.directory):
    logging.info("Syncing all objects to %s container from folder %s." %
                 (args.container, args.directory))
    try:
        cf.sync_folder_to_container(args.directory, args.container,
                                    delete=True, include_hidden=True,
                                    ignore_timestamps=True)
    except pyrax.exceptions.NoSuchContainer:
        logging.warn("Creating nonexistent container: %s", args.container)
        cf.create_container(args.container)
        cf.sync_folder_to_container(args.directory, args.container,
                                    delete=True, include_hidden=True,
                                    ignore_timestamps=True)
    logging.info("Sync complete.")
else:
    logging.warn("Directory doesn't exist: %s", args.directory)
    logging.warn("Check your path and try again.")
