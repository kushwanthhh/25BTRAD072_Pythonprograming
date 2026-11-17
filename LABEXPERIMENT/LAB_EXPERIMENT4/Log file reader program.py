from builtins import open

try:
    file = open("log.txt", "r")

    error = 0
    warning = 0
    info = 0

    for line in file:
        if "ERROR" in line:
            error += 1
        if "WARNING" in line:
            warning += 1
        if "INFO" in line:
            info += 1

    file.close()

    print("Errors:", error)
    print("Warnings:", warning)
    print("Info:", info)

except FileNotFoundError:
    print("Log file not found")
