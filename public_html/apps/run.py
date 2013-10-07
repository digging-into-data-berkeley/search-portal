#!/usr/bin/python
import sys
import os
from cheshire3.baseObjects import Session
from cheshire3.server import SimpleServer
from cheshire3.internal import cheshire3Root

# Build environment...
session = Session() # a Session - used to store
print cheshire3Root

serv = SimpleServer(session, os.path.join(cheshire3Root, 'configs', 'serverConfig.xml'))
session.logger = serv.get_path(session, 'defaultLogger') # a logger
db = serv.get_object(session, 'db_tdo_index') # the Database
session.database = db.id

#qf = db.get_object(session, 'defaultQueryFactory')

def testVec():
    recordStore = db.get_object(session, 'recordStore')
    rec = recordStore.fetch_record(session, 1)
    idx= db.get_object(session, 'idx-topic')
    vec = idx.fetch_vector(session, rec)
