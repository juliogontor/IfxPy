# 
#  Licensed Materials - Property of IBM
#
#  (c) Copyright IBM Corp. 2007-2008
#

import unittest, sys
import ifx_db
import config
from testfunctions import IfxDbTestFunctions

class IfxDbTestCase(unittest.TestCase):

  def test_157b_FetchAssocScrollableCursor_02(self):
    obj = IfxDbTestFunctions()
    obj.assert_expect(self.run_test_157b)

  def run_test_157b(self):
    conn = ifx_db.connect(config.ConnStr + 'ENABLESCROLLABLECURSORS=1', config.user, config.password)
    server = ifx_db.server_info( conn )

    if conn:
      sql = "SELECT id, name, breed, weight FROM animals ORDER BY breed"
      if (server.DBMS_NAME[0:3] != 'Inf'):
        stmt = ifx_db.prepare(conn, sql, {ifx_db.SQL_ATTR_CURSOR_TYPE: ifx_db.SQL_CURSOR_KEYSET_DRIVEN})
      else:
        stmt = ifx_db.prepare(conn, sql, {ifx_db.SQL_ATTR_CURSOR_TYPE: ifx_db.SQL_CURSOR_STATIC})
      result = ifx_db.execute(stmt)
      i = 2
      row = ifx_db.fetch_assoc(stmt, i)
      while ( row ):
        if (server.DBMS_NAME[0:3] == 'Inf'):
          #printf("%-5d %-16s %-32s %10s\n", row['id'], row['name'], row['breed'], row['weight'])
          print "%-5d %-16s %-32s %10s" % (row['id'], row['name'], row['breed'], row['weight'])
        else:
          #printf("%-5d %-16s %-32s %10s\n", row['ID'], row['NAME'], row['BREED'], row['WEIGHT'])
          print "%-5d %-16s %-32s %10s" % (row['ID'], row['NAME'], row['BREED'], row['WEIGHT'])
        i = i + 2
        row = ifx_db.fetch_assoc(stmt, i)

#__END__
#__LUW_EXPECTED__
#0     Pook             cat                                    3.20
#5     Rickety Ride     goat                                   9.70
#2     Smarty           horse                                350.00
#__ZOS_EXPECTED__
#0     Pook             cat                                    3.20
#5     Rickety Ride     goat                                   9.70
#2     Smarty           horse                                350.00
#__SYSTEMI_EXPECTED__
#0     Pook             cat                                    3.20
#5     Rickety Ride     goat                                   9.70
#2     Smarty           horse                                350.00
#__IDS_EXPECTED__
#0     Pook             cat                                    3.20
#5     Rickety Ride     goat                                   9.70
#2     Smarty           horse                                350.00
