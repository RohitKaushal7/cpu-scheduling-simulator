import src.algorithms.fcfs as fcfs
import src.algorithms.sjf as sjf
import src.algorithms.priority_non_preemptive as priority
import src.algorithms.priority_preemptive as priority_preemptive
import src.algorithms.srtf as srtf
from src.utils.tmp import processes  # tmp processes
import src.utils.graph as graph
import src.utils.table as table

# Actual App logic goes in this main function. Like all the options to choose from algorithms input outputs etc.


def main():
    # fcfs.run(processes)
    result_fcfs = fcfs.run(processes)
    result_sjf = sjf.run(processes)
    result_pr = priority.run(processes)
    result_prp = priority_preemptive.run(processes)
    result_srtf = srtf.run(processes)
    result_srtf = srtf.run(processes)
    # print(result_sjf)
    # table.plot(result_sjf['processes'])

    graph.plot_comparision(
        [result_fcfs, result_sjf, result_srtf, result_pr, result_prp])
    # sjf.main()
    # sjf_preemptive.main()


if __name__ == '__main__':
    main()
