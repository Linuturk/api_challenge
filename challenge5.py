#!/usr/bin/python
# -*- coding: utf-8 -*-

import pyrax
import logging

challenge = """
            Write a script that creates a Cloud Database instance. This
            instance should contain at least one database, and the database
            should have at least one user that can connect to it.
            """
points = 1

# Logging
#logging.basicConfig(level=logging.INFO)
logging.info("Challenge: %s", challenge)
logging.info("Points: %i", points)

# Setup pyrax creds and objects
pyrax.set_credential_file(".rackspace_cloud_credentials")
cdb = pyrax.cloud_databases

# Create the instance
name = "cdbTest"
flavors = cdb.list_flavors()
size = 1
instance = cdb.create(name, flavor=flavors[0], volume=size)
pyrax.utils.wait_until(instance, "status", ("ACTIVE", "ERROR"), attempts=0,
                       verbose=True)
logging.info("Name: %s", instance.name)
logging.info("ID: %s", instance.id)
logging.info("Status: %s", instance.status)
logging.info("Flavor: %s", instance.flavor.name)

# Create the database
db_name = "databaseTest"
db = instance.create_database(db_name)
logging.info("Database %s created.", db.name)

# Create the user
username = "databaseUser"
password = "secret1"
db_user = instance.create_user(username, password, database_names=db.name)
logging.info("User %s created.", db_user.name)
logging.info("Password is '%s'", password)
