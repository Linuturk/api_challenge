#!/usr/bin/python
# -*- coding: utf-8 -*-

import pyrax

challenge = """
            Write a script that will create a static webpage served out of
            Cloud Files. The script must create a new container, CDN enable
            it, enable it to serve an index file, create an index file object,
            upload the object to the container, and create a CNAME record
            pointing to the CDN URL of the container.
            """
points = 3
