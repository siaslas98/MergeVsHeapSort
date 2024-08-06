import time

class Timer:
    def __init__(self):
        self.start_time = None
        self.elapsed_time = 0
        self.running = False

    def start(self):
        if not self.running:
            self.start_time = time.time()
            self.running = True

    def stop(self):
        if self.running:
            self.elapsed_time += time.time() - self.start_time
            self.running = False

    def resume(self):
        if not self.running:
            self.start_time = time.time()
            self.running = True

    def get_value(self):
        if self.running:
            value = self.elapsed_time + (time.time() - self.start_time)
        else:
            value = self.elapsed_time
        return round(value, 2)
    def reset(self):
        self.start_time = None
        self.elapsed_time = 0
        self.running = False