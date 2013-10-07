#!/usr/bin/python

from run import *

qf = db.get_object(session, 'defaultQueryFactory')

if len(sys.argv[1:]):
    qString = ' '.join(sys.argv[1:])
else:
    qString = raw_input('Query: ')
    
query = qf.get_query(session, qString)
rs = db.search(session, query)
hits = len(rs)
print '{0} hits'.format(hits)
print 'rank\tdocno\t\tscaled\t\traw'
print '-' * 48
for i, rsi in enumerate(rs):
    rec = rsi.fetch_record(session)
    """
    print "rec: ", rec.get_xml(session)
    print "xpath stuff: ", rec.process_xpath(session, '//docno')
    print "type of rec: ", type(rec)
    print "type of xpath: ", type (rec.process_xpath(session, '//docno'))
    """
    docno = rec.process_xpath(session, '//docno/text()')[0]
    print '{0}\t{1}\t{2:.12f}\t{3:.12f}'.format(i, docno, rsi.scaledWeight, rsi.weight)
