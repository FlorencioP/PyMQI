import pymqi
queue_manager = 'Test'
channel = 'SYSTEM.DEF.SVRCONN'
host = '127.0.0.1'
port = '1414'
conn_info = '%s(%s)' % (host, port)

msg= 'Hola Don Jose'


qmgr = pymqi.connect(queue_manager, channel, conn_info)
putq = pymqi.Queue(qmgr, 'DEV.QUEUE.1')
putq.put(msg)

putq.close()

qmgr.disconnect()

print('Mensaje enviado')