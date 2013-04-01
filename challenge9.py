#!/usr/bin/python

import pyrax

challenge = """
            Write an application that when passed the arguments FQDN, image,
            and flavor, it creates a server of the specified image and flavor
            with the same name as the FQDN, and creates a DNS entry for the
            FQDN pointing to the server's public IP.
            """
points = 2
