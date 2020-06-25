# when imported as module.
def run():
    # will expect some arguments and run the scheduling
    print('Running FCFS')


# If this file is executed directly
def main():
    print('this file is executed directly.')


if __name__ == '__main__':
    main()
# when imported as module.
from src.utils.tmp import processes
import src.utils.table as table


def run(processes):
    # expects array of processes as arguments -> run the scheduling -> returns a dictionary/object of the result.

    # initialize
    total_waiting_time = 0
    total_turnaround_time = 0
    total_response_time = 0
    total_return_time = 0

    # sort by arrival_time
    proc = sorted(processes, key=lambda proc: proc.arrival_time)

    # run the first process
    proc[0].return_time = proc[0].burst_time
    proc[0].turnaround_time = proc[0].return_time - \
        proc[0].arrival_time
    proc[0].response_time = 0
    proc[0].waiting_time = 0

    # update total
    total_response_time = proc[0].response_time
    total_waiting_time = proc[0].waiting_time
    total_turnaround_time = proc[0].turnaround_time
    total_return_time = proc[0].burst_time

    # calculate for next processes
    for i in range(1, len(proc)):
        # calc for each
        proc[i].waiting_time = total_return_time - proc[i].arrival_time
        proc[i].return_time = total_return_time + proc[i].burst_time
        proc[i].turnaround_time = proc[i].return_time + proc[i].arrival_time
        proc[i].response_time = total_return_time - proc[i].arrival_time

        # update total
        total_response_time += proc[i].response_time
        total_waiting_time += proc[i].waiting_time
        total_turnaround_time += proc[i].turnaround_time
        total_return_time += proc[i].burst_time

    return {
        'avg_waiting_time': total_waiting_time/len(proc),
        'avg_response_time': total_response_time/len(proc),
        'avg_turnaround_time': total_turnaround_time/len(proc),
        'processes': proc
    }


# If this file is executed directly -> run temporary test-cases
def main():
    result = run(processes)
    print("Avg Waiting Time: {}".format(result['avg_waiting_time']))
    print("Avg Turnaround Time: {}".format(result['avg_turnaround_time']))
    print("Avg Response Time: {}".format(result['avg_response_time']))
    table.plot(result['processes'])


if __name__ == '__main__':
    main()
