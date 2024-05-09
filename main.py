def main():
    class Process:
        def __init__(self, process_id, burst_time, arrival_time):
            self.process_id = process_id
            self.burst_time = burst_time
            self.arrival_time = arrival_time
            self.waiting_time = 0
            self.turnaround_time = 0

    total_waiting_time = 0
    total_turnaround_time = 0
    n = int(input("Enter the number of processes: "))
    processes = []
    for i in range(n):
        burst = int(input(f"Enter burst time for process {i + 1}: "))
        arrival = int(input(f"Enter arrival time for process {i + 1}: "))
        process = Process(i + 1, burst, arrival)
        processes.append(process)

    processes.sort(key=lambda x: x.burst_time)

    current_time = 0
    for process in processes:
        process.waiting_time = current_time
        current_time += process.burst_time
        process.turnaround_time = process.waiting_time + process.burst_time
        total_waiting_time += process.waiting_time
        total_turnaround_time += process.turnaround_time

    average_waiting_time = total_waiting_time / n
    average_turnaround_time = total_turnaround_time / n

    print("\n  Process ID | Burst Time | Arrival Time  | Waiting Time  | Turnaround Time")
    print("-" * 75)
    for process in processes:
        print(f"{process.process_id:^12}| {process.burst_time:^11}| {process.arrival_time:^13}| "
              f"{process.waiting_time:^14}| {process.turnaround_time:^17}")
    print("-" * 75)
    print(f"\nAverage Waiting Time: {average_waiting_time}")
    print(f"Average Turnaround Time: {average_turnaround_time}")

    # Gantt Chart
    print("\nGantt Chart:")
    print("|", end="")
    for process in processes:
        print(f" P{process.process_id} |", end="")
    print()
    for process in processes:
        print(f"{process.waiting_time}    ", end="")
    print(f"{process.turnaround_time}    ", end="")


if __name__ == "__main__":
    main()
