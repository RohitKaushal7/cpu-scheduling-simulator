import src.algorithms.fcfs as fcfs
import src.algorithms.sjf as sjf
import src.algorithms.sjf_preemptive as sjf_preemptive
import src.algorithms.priority_non_preemptive as priority_non_preemptive
from src.utils.tmp import processes  # tmp processes

# Actual App logic goes in this main function. Like all the options to choose from algorithms input outputs etc.


def main():
    # fcfs.run(processes)
    fcfs.main()
    sjf.main()
    sjf_preemptive.main()
    priority_non_preemptive.main()
