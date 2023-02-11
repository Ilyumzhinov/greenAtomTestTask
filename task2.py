from typing import Callable

def create_handlers(callback: Callable[[int], None]) -> list[Callable[[int], None]]:
    handlers = []
    for step in range(5):
        # добавляем обработчики для каждого шага (от 0 до 4)
        handlers.append(lambda step=step: callback(step))
    return handlers

def execute_handlers(handlers: list[Callable[[int], None]]) -> None:
    # запускаем добавленные обработчики (шаги от 0 до 4)
    for handler in handlers:
        handler()