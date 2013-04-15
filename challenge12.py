#!/usr/bin/python

import pyrax

challenge = """
            Write an application that will create a route in mailgun so that
            when an email is sent to <YourSSO>@apichallenges.mailgun.org it
            calls your Challenge 1 script that builds 3 servers.
            Assumptions: 
            Assume that challenge 1 can be kicked off by accessing
            http://cldsrvr.com/challenge1 (I am aware this doesn't work. You
            just need to make sure that your message is getting posted to that
            URL)
            We have an internal mailgun account for this challenge.
            DO NOT PUT THE API KEY IN YOUR SCRIPT. Assume the Mailgun API key
            exists at ~/.mailgunapi. Assume no formatting, the api key will
            be the only data in the file. This should go without saying, but
            I'm going to say it: Do not put the API key in public github.
            If you happen to make that mistake by accident, let me know so
            I can rotate the key please.
            Helpful hints:
            Docs are your friend. Here is an explanation of routes in Mailgun:
            http://documentation.mailgun.net/user_manual.html#um-routes
            Here are some examples:
            http://documentation.mailgun.net/api-routes.html
            """
points = 3
