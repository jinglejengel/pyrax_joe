#!/usr/bin/env python

# Simply lists the containers you have

import os
import pyrax

pyrax.set_setting("identity_type", "rackspace")
creds_file = os.path.expanduser("~/.rackspace_cloud_credentials")
pyrax.set_credential_file(creds_file)
cf = pyrax.cloudfiles

print "Your current cloud files containers are:"
print cf.get_all_containers()
