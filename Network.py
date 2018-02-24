from networktables import NetworkTables

#follow FIRST ip naming conventions
#if team # is 4488, ip is 10.44.88.2

ip = '10.64.43.2'
NetworkTables.initialize(ip)
table = NetworkTables.getTable('SmartDashboard')
while True:
    table.putNumber('lenbuntov', 4488)