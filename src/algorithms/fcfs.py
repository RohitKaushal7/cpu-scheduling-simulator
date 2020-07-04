# when imported as module.
from src.utils.tmp import processes
import src.utils.table as table
import src.utils.graph as graph


def run(processes):
    """
        First Come First Serve

        _
    """

    print('running fcfs...')

    gantt = []

    # initialize
    total_waiting_time = 0
    total_turnaround_time = 0
    total_response_time = 0
    total_return_time = 0

    # sort by arrival_time
    proc = sorted(processes, key=lambda proc: proc.arrival_time)

    # run the first process
    proc[0].return_time = proc[0].burst_time
    proc[0].turnaround_time = proc[0].return_time - proc[0].arrival_time
    proc[0].response_time = 0
    proc[0].waiting_time = 0

    gantt.append((proc[0].p_id, (total_return_time, proc[0].burst_time)))

    # update total
    total_response_time += proc[0].response_time
    total_waiting_time += proc[0].waiting_time
    total_turnaround_time += proc[0].turnaround_time
    total_return_time += proc[0].burst_time

    # calculate for next processes
    for i in range(1, len(proc)):
        # calc for each
        proc[i].response_time = total_return_time - proc[i].arrival_time
        proc[i].waiting_time = total_return_time - proc[i].arrival_time
        proc[i].return_time = total_return_time + proc[i].burst_time
        proc[i].turnaround_time = proc[i].return_time - proc[i].arrival_time

        gantt.append((proc[i].p_id, (total_return_time, proc[i].burst_time)))

        # update total
        total_response_time += proc[i].response_time
        total_waiting_time += proc[i].waiting_time
        total_turnaround_time += proc[i].turnaround_time
        total_return_time += proc[i].burst_time

    return {
        'name': 'FCFS',
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
