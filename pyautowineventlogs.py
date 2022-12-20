import win32evtlog
import os

# Get the host computer name and use it to create the output file name
computer_name = os.environ["COMPUTERNAME"]
output_file_name = "eventviewer_errors_" + computer_name + ".txt"
output_file_path = os.path.join("C:\\", "logs", output_file_name)

# Get a list of all available log names
log_names = win32evtlog.GetAllLogNames()

# Open the output file for writing
with open(output_file_path, "w") as output_file:
# Iterate over the log names and read the events from each log
    for log_name in log_names:
        log = win32evtlog.OpenEventLog(log_name)
        flags = win32evtlog.EVENTLOG_BACKWARDS_READ | win32evtlog.EVENTLOG_SEQUENTIAL_READ
        events = win32evtlog.ReadEventLog(log, flags, 0)

# Iterate over the events and write the errors to the output file
        for event in events:
            if event.EventType == win32evtlog.EVENTLOG_ERROR_TYPE:
                output_file.write(str(event))

# Close the event log
        win32evtlog.CloseEventLog(log)
