import pymqi

queue_manager = 'Test'
channel = 'SYSTEM.DEF.SVRCONN'
host = '127.0.0.1'
port = '1414'
conn_info = '%s(%s)' % (host, port)

qmgr = pymqi.connect(queue_manager, channel, conn_info)
getq = pymqi.Queue(qmgr, 'DEV.QUEUE.1')


print('Mensaje Recibido :', getq.get())