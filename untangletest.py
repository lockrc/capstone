import untangle

obj = untangle.parse('http://152.10.10.162/sm101.xml')
print obj.Maverick.NodeID.cdata
