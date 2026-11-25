import platform
import socket
import os


def get_system_info():
    info = {
        "Hostname": socket.gethostname(),
        "Operating System": platform.system(),
        "OS Version": platform.version(),
        "Architecture": platform.architecture()[0],
        "Processor": platform.processor(),
        "Python Version": platform.python_version(),
        "Current Directory": os.getcwd()
    }

    return info


def display_info(info):
    print("\n" + "=" * 50)
    print("          PYTHON SYSTEM INFORMATION")
    print("=" * 50)

    for key, value in info.items():
        print(f"{key:<22}: {value}")

    print("=" * 50)


def main():
    print("Collecting system information...")

    system_info = get_system_info()

    display_info(system_info)


if __name__ == "__main__":
    main()