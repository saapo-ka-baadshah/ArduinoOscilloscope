import threading
from pathlib import Path


class memoryManager(threading.Thread):
    def __init__(self, buffer_file):
        self.buffer = buffer_file
        self.thread_killed = False
        threading.Thread.__init__(self)
        self.start()

    def run(self):
        while(not self.thread_killed):
            size = Path(self.buffer).stat().st_size
            print(size)
            if(size> 300000):
                with open(self.buffer, "w") as file:
                    file.write("")
        pass


