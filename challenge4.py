#!/usr/bin/python
# -*- coding: utf-8 -*-

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
parser.add_argument('-z', '--zone', type=str,
                    help="Specify the zone where the record is to be added.")

args = parser.parse_args()

# Handle the zone
if args.zone:
    zone = args.zone
else:
    # Give the (hopefully) root domain of the FQDN.
    zone = '.'.join(args.FQDN.split('.')[-2:])

# Build the a record dictionary
a_record = {"type": "A",
            "name": args.FQDN,
            "data": args.IP,
            "ttl": 300}

# Check for the domain
try:
    dom = dns.find(name=zone)
except pyrax.exceptions.NotFound:
    logging.error("Domain %s was not found. Specify your zone using -z.", zone)
else:
    records = dom.add_records(a_record)
    print records
