# when imported as module.
from src.utils.tmp import processes
import src.utils.table as table
import src.utils.graph as graph


def run(processes):
    """
        Priority Preemptive

        _
    """

    print('running priority preemptive...')

    gantt = []  # (,())

    # initialize
    total_waiting_time = 0
    total_turnaround_time = 0
    total_response_time = 0
    total_return_time = 0

    n = len(processes)

    # sort by arrival_time
    proc = sorted(processes, key=lambda proc: proc.arrival_time)

    response = []
    prev, st, ct = 0, 0, 0

    for i in range(n):
        response.append(False)

    def findWaitingTime(processes, n):

        rt = [0] * n

        # Copy the burst time into rt[]
        for i in range(n):
            rt[i] = processes[i].burst_time

        complete = 0
        t = 0
        short = 0

        ct = 1  # to count the time the process ran continously
        st = 0  # start time of that process
        # Process until all processes gets
        # completed
        while (complete != n):
            minp = 999999999
            # Find process with highest priority
            # time among the processes that
            # arrives till the current time`
            prev = short

            for j in range(n):
                if ((processes[j].arrival_time <= t) and
                        (processes[j].priority < minp) and rt[j] > 0):
                    minp = processes[j].priority
                    short = j

            # if a process is preempted
            if prev != short:
                gantt.append((processes[prev].p_id, (st, ct)))
                ct = 1
                st = t
            else:
                ct += 1

            # to calculate responce time || process ran for first time
            if(response[short] == False):
                response[short] = True
                processes[short].response_time = t - \
                    processes[short].arrival_time

            # Reduce remaining time by one
            rt[short] -= 1

            # If a process gets completely
            # executed
            if (rt[short] <= 0):
                # Increment complete
                complete += 1

                if prev == short:
                    gantt.append((processes[prev].p_id, (st, ct)))
                # Find finish time of current
                # process
                fint = t + 1

                # Calculate waiting time
                processes[short].waiting_time = (
                    fint - processes[short].arrival_time - processes[short].burst_time)

            # Increment time
            t += 1

    def findTurnAroundTime(processes, n):
        processes[0].waiting_time = 0
        for i in range(n):
            processes[i].turnaround_time = processes[i].burst_time + \
                processes[i].waiting_time

    # setting initial values

    findWaitingTime(proc, n)
    gantt.append((processes[prev].p_id, (st, ct)))

    findTurnAroundTime(proc, n)

    for i in range(0, n):
        proc[i].return_time = proc[i].arrival_time + proc[i].turnaround_time

    # calculate for next processes
    for i in range(1, len(proc)):

        # update total
        total_response_time += proc[i].response_time
        total_waiting_time += proc[i].waiting_time
        total_turnaround_time += proc[i].turnaround_time
        total_return_time += proc[i].burst_time

    return {
        'name': 'PR-P',
        'avg_waiting_time': total_waiting_time/len(proc),
        'avg_response_time': total_response_time/len(proc),
        'avg_turnaround_time': total_turnaround_time/len(proc),
        'processes': proc,
        'gantt': gantt
    }


# If this file is executed directly -> run temporary test-cases
def main():
    result = run(processes)
    print("Avg Waiting Time: {}".format(result['avg_waiting_time']))
    print("Avg Turnaround Time: {}".format(result['avg_turnaround_time']))
    print("Avg Response Time: {}".format(result['avg_response_time']))
    table.plot(result['processes'])
    graph.plot_gantt(result)


if __name__ == '__main__':
    main()
