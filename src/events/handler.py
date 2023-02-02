from typing import Any


subscibers = dict[str, Any]()


def subscribe(topic: str, callback: Any) -> None:
    if not topic in subscibers:
        subscibers[topic] = []
    subscibers[topic].append(callback)


def post_event(topic: str, data: Any) -> None:
    if not topic in subscibers:
        return
    for callback in subscibers[topic]:
        callback(data)
