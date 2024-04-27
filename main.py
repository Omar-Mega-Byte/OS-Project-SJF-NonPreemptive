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
        burst = int(input("Enter burst time for process " + str(i + 1) + ": "))
        arrival = int(input("Enter arrival time for process " + str(i + 1) + ": "))
        process = Process(i + 1, burst, arrival)
        processes.append(process)

    processes.sort(key=lambda x: x.burst_time)  # بتعمل سورت للبروسيس اللي في الليست  من حيث ال burst time

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
    print("----------------------------------------------------------------------------")
    for process in processes:
        print(f"{process.process_id:^11} | {process.burst_time:^11} | {process.arrival_time:^13} "
              f"| {process.waiting_time:^13} | {process.turnaround_time:^15}")
    print("\nAverage Waiting Time:", average_waiting_time)
    print("Average Turnaround Time:", average_turnaround_time)


if __name__ == "__main__":
    main()
