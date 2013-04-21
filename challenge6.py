#!/usr/bin/python
# -*- coding: utf-8 -*-

import pyrax
import logging

challenge = """
            Write a script that creates a CDN-enabled container in Cloud Files.
            """
points = 1

# Logging
#logging.basicConfig(level=logging.INFO)
logging.info("Challenge: %s", challenge)
logging.info("Points: %i", points)

# Setup pyrax creds and objects
pyrax.set_credential_file(".rackspace_cloud_credentials")
cf = pyrax.cloudfiles

# Create Container and make it public
name = "testContainer"
container = cf.create_container(name)
container.make_public(ttl=1500)

cont = cf.get_container(container.name)
logging.info("container_name: %s", cont.name)
logging.info("cdn_enabled: %s", cont.cdn_enabled)
logging.info("cdn_ttl: %i", cont.cdn_ttl)
logging.info("cdn_log_retention: %s", cont.cdn_log_retention)
logging.info("cdn_uri: %s", cont.cdn_uri)
logging.info("cdn_ssl_uri: %s", cont.cdn_ssl_uri)
logging.info("cdn_streaming_uri: %s", cont.cdn_streaming_uri)
logging.info("cdn_ios_uri: %s", cont.cdn_ios_uri)

# Cleanup
#cont.delete()
