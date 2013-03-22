#!/usr/bin/python

import pyrax
import logging
import argparse

challenge = """
            Write a script that uses Cloud DNS to create a new A record when
            passed a FQDN and IP address as arguments.
            """
points = 1

# Logging
#logging.basicConfig(level=logging.INFO)
logging.info("Challenge: %s", challenge)
logging.info("Points: %i", points)

# Setup pyrax creds and objects
pyrax.set_credential_file(".rackspace_cloud_credentials")
dns = pyrax.cloud_dns

# Handle arguments
parser = argparse.ArgumentParser()
parser.add_argument('FQDN', type=str,
                    help="The name of the new A record.")
parser.add_argument('IP', type=str,
                    help="The IP address for this new record.")

args = parser.parse_args()
