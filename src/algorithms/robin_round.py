# when imported as module.
from src.utils.tmp import processes
import src.utils.table as table
import src.utils.graph as graph


def run(processes):

    # initialize
    gantt = []
    time_quantum = 500
    total_waiting_time = 0
    total_turnaround_time = 0
    total_response_time = 0
    # total_return_time = 0
    processes_cpy = sorted(processes, key=lambda processes_cpy: processes_cpy.p_id) 
    q = []
    nxt_val = processes_cpy[0].arrival_time
    i = 0
    while i < len(processes_cpy) and processes_cpy[i].arrival_time <= nxt_val:
        q.append(processes_cpy[i].p_id)
        i += 1
    while len(q) != 0:
        m = q[0]
        q.pop(0)
        if processes_cpy[m].burst_time >= time_quantum:
            nxt_val = nxt_val + time_quantum
        else:
            nxt_val = nxt_val + processes_cpy[m].burst_time

        if processes_cpy[m].burst_time >= time_quantum :
            processes_cpy[m].burst_time = processes_cpy[m].burst_time - time_quantum
        else:
            processes_cpy[m].burst_time = 0
    
        while i < len(processes_cpy) and processes_cpy[i].arrival_time <= nxt_val:
            q.append(processes_cpy[i].p_id)
            i += 1
        
        if processes_cpy[m].burst_time > 0:
            q.append(m)
        
        if processes_cpy[m].burst_time <= 0:
            processes[m].return_time = nxt_val
            q.pop(0)

    for i in range(len(processes)):
        print(processes[i].burst_time,processes_cpy[i].burst_time)
        processes[i].turnaround_time = processes[i].return_time - processes[i].arrival_time
        processes[i].waiting_time = processes[i].turnaround_time - processes[i].burst_time
        total_turnaround_time += processes[i].turnaround_time
        total_waiting_time += processes[i].waiting_time

        

    return {
        'name': 'ROUND-RBN',
        'avg_waiting_time': total_waiting_time/len(processes),
        'avg_response_time': total_response_time/len(processes),
        'avg_turnaround_time': total_turnaround_time/len(processes),
        'processes': processes,
        'gantt': gantt
    }




# If this file is executed directly -> run temporary test-cases
def main():
    result = run(processes)
    print("Avg Waiting Time: {}".format(result['avg_waiting_time']))
    print("Avg Turnaround Time: {}".format(result['avg_turnaround_time']))
    print("Avg Response Time: {}".format(result['avg_response_time']))
    table.plot(result['processes'])
    graph.plot_gantt(result['gantt'])


if __name__ == '__main__':
    main()
