import matplotlib.pyplot as plt
import numpy as np
from src.utils.tmp import processes


def plot_algo_graph(result):
    """
    Plots the line graph for a particular scheduling algorithm.

    Args:
        result (``Dictionary``) : return value of any scheduling process.

    """
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
    """
    Plots the Comparison Bar graph for different scheduling algorithms.

    Args:
        result (``Array : Dictionary``) : Array of return values of any scheduling process.

    """
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
    rects1 = ax.bar(x-width, avg_waiting_time,
                    width, label='avg_waiting_time')
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
    plt.title('Comparison of different Scheduling Algorithms')
    plt.show()


colors = [
    "#ED4264",
    "#13c191",
    "#1FA2FF",
    "#19d905",
    "#fe53bb",
    "#FFC837",
    "#4776E6",
    "#fdf200",
    "#8E54E9",
    "#fd0e30",
    "#A6FFCB",
    "#514A9D",
    "#5eff0f",
    "#1CD8D2",
    "#FFEDBC",
    "#cca4fd",
    "#d1fe49",
    "#00feca",
    "#FF8008",
    "#c2d302",
    "#E00000", "#00E000", "#0000E0", "#E0E000", "#E000E0", "#00E0E0", "#E0E0E0",
    "#800000", "#008000", "#000080", "#808000", "#800080", "#008080", "#808080",
    "#C00000", "#00C000", "#0000C0", "#C0C000", "#C000C0", "#00C0C0", "#C0C0C0",
    "#A00000", "#00A000", "#0000A0", "#A0A000", "#A000A0", "#00A0A0", "#A0A0A0",
    "#FF0000", "#00FF00", "#0000FF", "#FFFF00", "#FF00FF", "#00FFFF", "#000000",
    "#400000", "#004000", "#000040", "#404000", "#400040", "#004040", "#404040",
    "#200000", "#002000", "#000020", "#202000", "#200020", "#002020", "#202020",
    "#600000", "#006000", "#000060", "#606000", "#600060", "#006060", "#606060",
]


def plot_gantt(result):
    """
    Plots the Gantt Chart for a particular scheduling algorithm.

    Args:
        result (``Dictionary``) : return value of any scheduling process.

    """

    gantt = result['gantt']
    fig, ax = plt.subplots(figsize=(15, 3))
    ax.set_ylim(0, 30)
    ax.set_yticks([10])
    ax.set_yticklabels(['1'])
    # ax.grid(True)

    ax.set_xticks(tuple(map(lambda gnt: gnt[1][0], gantt)))

    ax.broken_barh(list(map(lambda gnt: gnt[1], gantt)), (0, 10), facecolors=tuple(map(
        lambda gnt: colors[gnt[0]], gantt)))
    for gnt in gantt:
        ax.annotate('P{}'.format(gnt[0]), (gnt[1][0],
                                           5), color='white', fontweight='bold')
    plt.title(result['name'])
    plt.show()


def main():
    plot_algo_graph({'processes': processes})


if __name__ == '__main__':
    main()
