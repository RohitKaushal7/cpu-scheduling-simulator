class Process:
    def __init__(self, p_id, arrival_time, burst_time, priority=1):
        self.p_id = p_id
        self.arrival_time = arrival_time
        self.burst_time = burst_time
        self.priority = priority

        self.waiting_time = 0
        self.return_time = 0
        self.turnaround_time = 0
        self.response_time = 0
        self.completed = False
