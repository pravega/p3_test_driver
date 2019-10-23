#!/usr/bin/env python
# Written by Claudio Fahey (claudio.fahey@emc.com)

from __future__ import division

import time

# P3 Libraries
from .application_status_tree import StatusTreeServer

root = StatusTreeServer(status_file='/tmp/status.html')
with root.context():
	if True:
		root.set_status('this is root', html='<div><h1>hi</h1><h2>h2</h2></div>')
	if False:
		for i in range(0,5):
			root.set_status('this is root')
			c1 = root.create_child('c1')
			c1.set_status('this is c1')
			c2 = root.create_child('c2')
			c2.set_status('this is c2')
			#root.print_tree()
			#root.set_status('root with no children', destroy_children=True)
			#root.print_tree()
			root.set_status('this is root again %d' % i)
			# root.write_status_file()
			time.sleep(5)

