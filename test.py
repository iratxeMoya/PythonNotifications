from pyNotifications import PythonNotifications
import time


notifyer = PythonNotifications(token='TOKEN', id = 'ID', appName='test')
notifyer.addMessage('Info test', 'info')
notifyer.addMessage('Warning test', 'warning')
time.sleep(3)
notifyer.addMessage('Warning test', 'warning')
notifyer.addMessage('Error test', 'error')
notifyer.addMessage('Error test', 'error')
time.sleep(2)
notifyer.addMessage('Error test', 'error')

notifyer.sendMessage('error')
notifyer.sendMessage('warning')
notifyer.sendMessage('info')