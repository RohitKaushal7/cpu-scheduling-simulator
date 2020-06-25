from src.utils.tmp import processes
import src.utils.table as table

def run(processes):
    total_waiting_time = 0
    total_turnaround_time = 0
    total_response_time = 0
    total_return_time = 0
    procc = sorted(processes,key = lambda procc: procc.priority)
    proc = sorted(procc,key = lambda proc: proc.arrival_time)

    service = [0]*len(proc)
    wt = [0]*len(proc)
    tat = [0]*len(proc)
    for i in range(1,len(proc)):
        service[i] = proc[i-1].burst_time + service[i-1]
        wt[i] = service[i-1] - proc[i].arrival_time + 1

        if wt[i] < 0:
            wt[i] = 0

    proc[0].return_time = proc[0].burst_time
    for i in range(len(proc)):
        tat[i] = proc[i].burst_time  + wt[i]

    proc[0].response_time = 0
    for i in range(1,len(proc)):
        proc[i].return_time = proc[i-1].return_time + proc[i].burst_time
        proc[i].response_time = proc[i].return_time - proc[i].arrival_time
    

    for i in range(len(proc)):
        total_return_time += proc[i].return_time
        proc[i].waiting_time = total_return_time - proc[i].arrival_time
        proc[i].turnaround_time = tat[i]
        total_waiting_time += proc[i].waiting_time
        total_response_time += proc[i].response_time
        total_turnaround_time += proc[i].turnaround_time
        
    return {
        'avg_waiting_time': total_waiting_time/len(proc),
        'avg_response_time': total_response_time/len(proc),
        'avg_turnaround_time': total_turnaround_time/len(proc),
        'processes': proc
    }

def main():
    result = run(processes)
    print("Avg Waiting Time: {}".format(result['avg_waiting_time']))
    print("Avg Turnaround Time: {}".format(result['avg_turnaround_time']))
    print("Avg Response Time: {}".format(result['avg_response_time']))
    table.plot(result['processes'])


if __name__ == '__main__':
    main()