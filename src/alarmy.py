import threading
from typing import Protocol
from events.handler import post_event

# from events import Events


class Buzzer(Protocol):
    """Represents a simple buzzer."""

    def buzz(self) -> None:
        """Buzz the buzzer."""
        ...


class Alarm:
    """docstring for Alarm"""

    def __init__(self, buzzer: Buzzer) -> None:
        self.buzzer = buzzer
        self.is_active = False
        self.total_time = 0
        # self.timer: threading.Timer

    def set_time(self, hour: int = 0, minute: int = 0, second: int = 0) -> None:
        """Sets the alarm time."""
        self.total_time = (hour * 60 + minute) * 60 + second
        self.timer = threading.Timer(self.total_time, self.on_finish)

    def start(self) -> None:
        """Start the alarm."""
        self.is_active = True
        self.timer.start()

    def stop(self) -> None:
        """Stop the alarm."""
        self.timer.cancel()
        self.is_active = False

    def on_finish(self) -> None:
        self.buzzer.buzz()
        post_event(topic="alarm_finish", data=None)
