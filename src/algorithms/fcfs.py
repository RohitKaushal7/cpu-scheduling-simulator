# when imported as module.
from src.utils.tmp import processes


def run(processes):
    # will expect some arguments and run the scheduling
    print('Running FCFS')


# If this file is executed directly

def main():
    for p in processes:
        print(p.arrival_time, end=" ")
    print()


if __name__ == '__main__':
    main()
