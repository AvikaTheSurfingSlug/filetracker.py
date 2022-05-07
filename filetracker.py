import os
import shutil
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
from_dir = "C:/Users/Avika sama/Downloads"
class fileEventHandler (FileSystemEventHandler):
    def on_created(self,event):
        print("file has been created.")
    def on_deleted(self,event):
        print("file has been deleted.")
    def on_moved(self,event):
        print("file has been moved.")
    def on_modified(self,event):
        print("file has been modified.")
event_handler = FileEventHandler()
observer = Observer()
observer.schedule(event_handler,from_dir,recursive = True)
observer.start()
try:
     while true:
        time.sleep(2)
        print("running...")
except KeyboardInterrupt:
    print("stop")
    observer.stop()