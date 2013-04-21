#!/usr/bin/python
# -*- coding: utf-8 -*-

import pyrax

challenge = """
            Write an application that will:
             - Create 2 servers, supplying a ssh key to be installed at
             /root/.ssh/authorized_keys
             - Create a load balancer
             - Add the 2 new servers to the LB
             - Set up LB monitor and custom error page
             - Create a DNS record based on a FQDN for the LB VIP
             - Write the error page html to a file in cloud files for backup
            """
points = 8
