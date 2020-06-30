import matplotlib.pyplot as plt
import numpy as np
from src.utils.tmp import processes


def plot_algo_graph(result):
    processes = result['processes']

    x_axis = list(map(lambda proc: proc.p_id, processes))

    plt.plot(
        list(map(lambda proc: proc.burst_time, processes)),
        label="Burst")
    plt.plot(
        list(map(lambda proc: proc.arrival_time, processes)),
        label="Arrival")
    plt.plot(
        list(map(lambda proc: proc.turnaround_time, processes)),
        label="Turnaround")
    plt.plot(
        list(map(lambda proc: proc.response_time, processes)),
        label="Response")
    plt.plot(
        list(map(lambda proc: proc.waiting_time, processes)),
        label="Wait")

    plt.legend()
    plt.xticks(ticks=x_axis)
    plt.show()


def plot_comparision(algorithms):

    labels = list(map(lambda algo: algo['name'], algorithms))

    avg_waiting_time = list(
        map(lambda algo: algo['avg_waiting_time'], algorithms))
    avg_response_time = list(
        map(lambda algo: algo['avg_response_time'], algorithms))
    avg_turnaround_time = list(
        map(lambda algo: algo['avg_turnaround_time'], algorithms))

    x = np.arange(len(labels))  # the label locations
    width = 0.15  # the width of the bars

    fig, ax = plt.subplots()
    rects1 = ax.bar(x-width, avg_response_time,
                    width, label='avg_response_time')
    rects2 = ax.bar(x, avg_turnaround_time,
                    width, label='avg_turnaround_time')
    rects3 = ax.bar(x+width, avg_response_time,
                    width, label='avg_response_time')

    # Add some text for labels, title and custom x-axis tick labels, etc.
    ax.set_ylabel('Algorithms')
    # ax.set_title('Comparision of CPU Scheduling Algorithms')
    ax.set_xticks(x)
    ax.set_xticklabels(labels)
    ax.legend()

    # fig.tight_layout()

    plt.show()


def plot_gantt(gantt):

    fig, ax = plt.subplots()

    ax.set_ylim(0, 30)
    ax.set_yticks([30])
    ax.set_yticklabels(['1'])
    # ax.grid(True)

    ax.broken_barh(list(map(lambda gnt: gnt[1], gantt)), (10, 10), facecolors=(
        'tab:orange', 'tab:green', 'tab:red', 'tab:blue', 'tab:cyan', 'tab:brown', 'tab:grey', 'tab:pink'))
    for gnt in gantt:
        ax.annotate('P{}'.format(gnt[0]), (gnt[1][0],
                                           15), color='white', fontweight='bold')

    plt.show()


def main():
    plot_algo_graph({'processes': processes})


if __name__ == '__main__':
    main()
