import importlib
python_notifications = importlib.import_module("python-notifications")
#from python_notifications-1.0.1.dist-info import PythonNotifications
import time


notifyer = python_notifications.PythonNotifications(token='5892926535:AAH8NH0e-AT1VYQLA9psWChZQb5Y_mET7GM', id = '5883320667', appName='test')
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