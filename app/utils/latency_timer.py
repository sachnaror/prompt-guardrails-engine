import time

"""
Utility for measuring latency of API calls or LLM responses.
"""


class LatencyTimer:

    def __init__(self):
        self.start_time = None

    def start(self):
        self.start_time = time.time()

    def stop(self):
        if not self.start_time:
            return None

        elapsed = time.time() - self.start_time
        return round(elapsed, 3)
