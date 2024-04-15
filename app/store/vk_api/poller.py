import asyncio
from app.store import Store


class Poller:
    def __init__(self, store: Store) -> None:
        self.store = store
        self.is_running = False
        self.poll_task: asyncio.Task | None = None

    async def start(self) -> None:
        # TODO: добавить asyncio Task на запуск poll
        if not self.is_running:
            self.is_running = True
            self.poll_task = asyncio.create_task(self.poll())
            # asyncio.create_task() создает фоновую задачу, которая будет выполнять метод poll()

    async def stop(self) -> None:
        # TODO: gracefully завершить Poller
        """
        Остановка опроса VK API и ожидание завершения текущей итерации poll.
        """
        if self.is_running:
            self.is_running = False
            if self.poll_task:
                await self.poll_task
                # Ожидание завершения задачи, если она была запущена

    async def poll(self) -> None:
        """
        Метод для опроса VK API и обработки обновлений.
        """
        try:
            while self.is_running:
                # Здесь должна быть логика для получения данных из VK API
                # Например, использование метода 'get_long_poll_server' и 'long_poll'
                # self.store.update(data) - обновление данных в хранилище
                await asyncio.sleep(1)  # Пауза перед следующим опросом для предотвращения частых запросов
        except Exception as e:
            print(f"Произошла ошибка в poller: {e}")
            self.is_running = False
        finally:
            if self.poll_task:
                self.poll_task = None

