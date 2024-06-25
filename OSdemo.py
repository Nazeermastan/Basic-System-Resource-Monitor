import psutil
import time
import datetime
import matplotlib.pyplot as plt

def log_resource_usage(interval, duration):
    timestamps = []
    cpu_usage = []
    memory_usage = []
    io_counters = []
    network_counters = []

    iterations = int(duration / interval)

    for i in range(iterations):
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        timestamps.append(timestamp)

        cpu_percent = psutil.cpu_percent(interval=interval)
        cpu_usage.append(cpu_percent)

        mem_stats = psutil.virtual_memory()
        memory_usage.append(mem_stats.percent)

        io_stats = psutil.disk_io_counters()
        io_counters.append(io_stats.read_bytes + io_stats.write_bytes)

        net_stats = psutil.net_io_counters()
        network_counters.append(net_stats.bytes_sent + net_stats.bytes_recv)

        time.sleep(interval)

    plt.plot(timestamps, cpu_usage)
    plt.title("CPU Usage")
    plt.xlabel("Timestamp")
    plt.ylabel("Usage (%)")
    plt.show()

    plt.plot(timestamps, memory_usage)
    plt.title("Memory Usage")
    plt.xlabel("Timestamp")
    plt.ylabel("Usage (%)")
    plt.show()

    plt.plot(timestamps, io_counters)
    plt.title("Disk I/O Usage")
    plt.xlabel("Timestamp")
    plt.ylabel("Usage (Bytes)")
    plt.show()

    plt.plot(timestamps, network_counters)
    plt.title("Network Usage")
    plt.xlabel("Timestamp")
    plt.ylabel("Usage (Bytes)")
    plt.show()

log_resource_usage(1, 5)
