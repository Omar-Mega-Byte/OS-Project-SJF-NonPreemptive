import tkinter as tk


class Process:
    def __init__(self, process_id, burst_time, arrival_time):
        self.process_id = process_id
        self.burst_time = burst_time
        self.arrival_time = arrival_time
        self.waiting_time = 0
        self.turnaround_time = 0


def create_entries_and_calculate_schedule():
    processes = []
    total_waiting_time = 0
    total_turnaround_time = 0
    n = int(processes_entry.get())

    for i in range(n):
        burst = int(burst_entries[i].get())
        arrival = int(arrival_entries[i].get())
        process = Process(i + 1, burst, arrival)
        processes.append(process)

    processes.sort(key=lambda x: x.arrival_time)

    current_time = 0
    for process in processes:
        process.waiting_time = current_time
        current_time += process.burst_time
        process.turnaround_time = process.waiting_time + process.burst_time
        total_waiting_time += process.waiting_time
        total_turnaround_time += process.turnaround_time

    average_waiting_time = total_waiting_time / n
    average_turnaround_time = total_turnaround_time / n

    result_text.delete(1.0, tk.END)
    result_text.insert(tk.END, "\n  Process ID | Burst Time | Arrival Time  | Waiting Time  | Turnaround Time\n")
    result_text.insert(tk.END, "----------------------------------------------------------------------------\n")
    for process in processes:
        result_text.insert(tk.END, f"{process.process_id:^11} | {process.burst_time:^11} | {process.arrival_time:^13} "
                                   f"| {process.waiting_time:^13} | {process.turnaround_time:^15}\n")
    result_text.insert(tk.END, f"\nAverage Waiting Time: {average_waiting_time}\n")
    result_text.insert(tk.END, f"Average Turnaround Time: {average_turnaround_time}\n")

    # Gantt Chart
    gantt_text.delete(1.0, tk.END)
    gantt_text.insert(tk.END, "Gantt Chart:\n")
    gantt_text.insert(tk.END, "|")
    for process in processes:
        gantt_text.insert(tk.END, f" P{process.process_id} |")
    gantt_text.insert(tk.END, "\n")
    for process in processes:
        gantt_text.insert(tk.END, f"{process.waiting_time}    ")
    gantt_text.insert(tk.END, f"{process.turnaround_time}    ")
    gantt_text.insert(tk.END, "\n")


def create_entries():
    n = int(processes_entry.get())
    for i in range(n):
        tk.Label(entries_frame, text=f"Burst Time for Process {i + 1}:").grid(row=i, column=0, padx=5, pady=5,
                                                                              sticky="E")
        burst_entries.append(tk.Entry(entries_frame))
        burst_entries[-1].grid(row=i, column=1, padx=5, pady=5, sticky="W")

        tk.Label(entries_frame, text=f"Arrival Time for Process {i + 1}:").grid(row=i, column=2, padx=5, pady=5,
                                                                                sticky="E")
        arrival_entries.append(tk.Entry(entries_frame))
        arrival_entries[-1].grid(row=i, column=3, padx=5, pady=5, sticky="W")

    tk.Button(root, text="Calculate Schedule", command=create_entries_and_calculate_schedule).grid(row=n + 3, column=0,
                                                                                                   columnspan=4,
                                                                                                   pady=10)


root = tk.Tk()
root.title("Process Scheduling")

tk.Label(root, text="Process Scheduling", font=("Helvetica", 16, "bold")).grid(row=0, column=0, columnspan=5, pady=10)

tk.Label(root, text="Number of Processes:").grid(row=1, column=0, padx=5, pady=5, sticky="E")
processes_entry = tk.Entry(root)
processes_entry.grid(row=1, column=1, padx=5, pady=5, sticky="W")

entries_frame = tk.Frame(root)
entries_frame.grid(row=2, column=0, columnspan=4, padx=5, pady=5)

burst_entries = []
arrival_entries = []

tk.Button(root, text="Create Entries", command=create_entries).grid(row=1, column=2, padx=5, pady=5, sticky="W")

result_text = tk.Text(root, height=15, width=100)
result_text.grid(row=4, column=0, columnspan=4, padx=5, pady=5)

gantt_text = tk.Text(root, height=6, width=100)
gantt_text.grid(row=5, column=0, columnspan=4, padx=5, pady=5)

root.mainloop()
