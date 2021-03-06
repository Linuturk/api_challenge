#!/usr/bin/python
# -*- coding: utf-8 -*-

import pyrax

challenge = """
            Write an application that will:
             - Create an SSL terminated load balancer. (Create self-signed
             certificate.)
             - Create a DNS record that should be pointed to the load
             balancer.
             - Create three servers as nodes behind the LB.
              - Each server should have a CBS volume attached to it.
              (Size and type are irrelevant.)
              - All three servers should have a private Cloud Network shared
              between them.
              - Login information to all three servers returned in a readable
              format as the result of the script, including connection
              information.
            """
points = 6
