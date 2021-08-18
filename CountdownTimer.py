import time


def countdown(time_sec):
    while time_sec:
        mins, secs = divmod(time_sec, 60)
        time_format = '{:02d}:{:02d} '.format(mins, secs)
        print(time_format, end='')
        time.sleep(1)
        time_sec -= 1

    print("\nStop!")


x = int(input("Enter Countdown Time in Seconds: "))
countdown(x)
