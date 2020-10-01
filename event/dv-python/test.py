from dv import Control

c = Control()
val = c.get('/system/logger/', 'limitLogSize', 'long')
print(val)
c.put('/system/logger/', 'limitLogSize', 'long', val - 1)
val = c.get('/system/logger/', 'limitLogSize', 'long')
print(val)
