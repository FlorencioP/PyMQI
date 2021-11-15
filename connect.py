import pymqi

queue_manager = 'Test'
channel = 'SYSTEM.DEF.SVRCONN'
host = '127.0.0.1'
port = '1414'
conn_info = '%s(%s)' % (host, port)

qmgr = pymqi.connect(queue_manager, channel, conn_info)

pcf = pymqi.PCFExecute(qmgr)
pcf.MQCMD_PING_Q_MGR()

qmgr.disconnect()