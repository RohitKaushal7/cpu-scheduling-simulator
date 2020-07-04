def plot(processes):
    """
    Displays the given processes in a tabular format

    Args:
        processes (Array : :class:`src.utils.process.Process`): processed processes.

    """

    print('| PID | BURST_TIME | ARRIVAL_TIME | PRIORITY || RESPONSE_TIME | WAITING_TIME | TURNAROUND_TIME | RETURN_TIME |')

    for p in processes:
        print("| {:3} |     {:3}    |     {:4}     |   {:4}   ||     {:3}       |      {:3}     |        {:3}      |     {:3}     |".format(
              p.p_id, p.burst_time, p.arrival_time, p.priority, p.response_time, p.waiting_time, p.turnaround_time, p.return_time))
