import psutil
import sys
import os
import time
import schedule
import smtplib
from email.message import EmailMessage

LOG_DIR = "MarvellousLogs"
SENDER_EMAIL = "your_email@gmail.com"
APP_PASSWORD = "your_app_password"

def CreateLogDir():
    if not os.path.exists(LOG_DIR):
        os.mkdir(LOG_DIR)

def CreateLog():
    Border = "-" * 60
    timestamp = time.strftime("%Y-%m-%d_%H-%M-%S")
    filename = os.path.join(LOG_DIR, f"Marvellous_{timestamp}.log")

    with open(filename, "w") as f:
        f.write(Border + "\n")
        f.write("Marvellous Platform Surveillance System\n")
        f.write("Log created at : " + time.ctime() + "\n")
        f.write(Border + "\n\n")

        # ---------------- CPU ----------------
        f.write("CPU Usage : %s %%\n" % psutil.cpu_percent())
        f.write(Border + "\n")

        # ---------------- RAM ----------------
        mem = psutil.virtual_memory()
        f.write("RAM Usage : %s %%\n" % mem.percent)
        f.write(Border + "\n")

        # ---------------- Disk ----------------
        f.write("Disk Usage Report\n")
        for part in psutil.disk_partitions():
            try:
                usage = psutil.disk_usage(part.mountpoint)
                f.write(f"{part.mountpoint} -> {usage.percent}% used\n")
            except:
                pass
        f.write(Border + "\n")

        # ---------------- Network ----------------
        net = psutil.net_io_counters()
        f.write("Network Usage\n")
        f.write("Sent : %.2f MB\n" % (net.bytes_sent / (1024 * 1024)))
        f.write("Received : %.2f MB\n" % (net.bytes_recv / (1024 * 1024)))
        f.write(Border + "\n")

        # ---------------- Process Info ----------------
        f.write("Running Processes\n")
        for proc in psutil.process_iter(['pid', 'name', 'memory_percent', 'num_threads']):
            try:
                f.write(
                    f"PID:{proc.info['pid']} | "
                    f"Name:{proc.info['name']} | "
                    f"Memory:{proc.info['memory_percent']:.2f}% | "
                    f"Threads:{proc.info['num_threads']}\n"
                )
            except:
                pass

        f.write(Border + "\n")
        f.write("End of Log File\n")

    return filename

def SendMail(receiver, logfile):
    msg = EmailMessage()
    msg['Subject'] = 'Marvellous System Surveillance Report'
    msg['From'] = "saylimohite1902@gmail.com"
    msg['To'] = receiver   

    msg.set_content("System surveillance log attached.")

    with open(logfile, "rb") as f:
        msg.add_attachment(
            f.read(),
            maintype="application",
            subtype="octet-stream",
            filename=os.path.basename(logfile)
        )

    server = smtplib.SMTP_SSL("smtp.gmail.com", 465)
    server.login("saylimohite1902@gmail.com", "acdmwrrdiiutdkay")
    server.send_message(msg)
    server.quit()


def Job(receiver):
    logfile = CreateLog()
    SendMail(receiver, logfile)

def main():
    if len(sys.argv) != 3:
        print("Usage: Script.py <TimeIntervalMinutes> <ReceiverEmail>")
        return

    interval = int(sys.argv[1])
    receiver = sys.argv[2]

    CreateLogDir()

    schedule.every(interval).minutes.do(Job, receiver)

    print("Marvellous Platform Surveillance Started...")
    print("Press Ctrl + C to stop")

    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__":
    main()
