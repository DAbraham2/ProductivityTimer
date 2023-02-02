import threading
import time
from typing import Any
from alarmy import Alarm
from buzzer import AlarmRing
from events.handler import subscribe

stopSign = None
original_time: int = 0


def main() -> None:
    global stopSign
    global original_time
    stopSign = bool(False)

    b = AlarmRing()
    a = Alarm(buzzer=b)
    subscribe(topic="alarm_finish", callback=onAlarmSet)

    t = threading.Thread(target=count)

    a.set_time(second=10)

    original_time = int(time.time())

    print("============================")
    print("Starting Alarm")
    print("============================")

    a.start()
    t.start()

    time.sleep(15)

    stopSign = bool(True)

    t.join()


def onAlarmSet(data: Any) -> None:
    global stopSign
    global original_time
    time_cur = int(time.time())
    if not stopSign:
        stopSign = bool(True)
    ellapsed_ms = time_cur - original_time
    print(f"The counter waited for {ellapsed_ms} ms")


def count() -> None:
    c = 0
    while True:
        c = c + 1
        time.sleep(1)
        print(f"Waiting {c} seconds...")
        if stopSign:
            print("Stopping...")
            break


if __name__ == "__main__":
    original_time = 1
    stopSign = bool(False)
    main()
