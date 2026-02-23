from abc import ABC, abstractmethod


# 1. Породжувальний патерн - Factory Method
class Transport(ABC):
    @abstractmethod
    def deliver(self):
        pass


class Truck(Transport):
    def deliver(self):
        return "веземо фурою по трасі"


class Ship(Transport):
    def deliver(self):
        return "пливемо морем на кораблі"


class Logistics(ABC):
    @abstractmethod
    def create_transport(self):
        pass

    def plan_delivery(self):
        transport = self.create_transport()
        return f"План такий: {transport.deliver()}"


class RoadLogistics(Logistics):
    def create_transport(self):
        return Truck()


class SeaLogistics(Logistics):
    def create_transport(self):
        return Ship()


# 2. Структурний патерн - Facade
# підсистеми для роботи з відео
class AudioMixer:
    def fix_audio(self):
        return "аудіодоріжку пофікшено"


class VideoConverter:
    def convert(self):
        return "відео конвертовано в mp4"


# сам фасад
class VideoEditorFacade:
    def __init__(self):
        self.audio = AudioMixer()
        self.video = VideoConverter()

    def render(self):
        print("Починаємо рендер...")
        print(self.audio.fix_audio())
        print(self.video.convert())
        print("Готово, відео збережено!")


# 3. Поведінковий патерн - Observer
class Publisher:
    def __init__(self):
        self.subscribers = []
        self.news = ""

    def subscribe(self, sub):
        self.subscribers.append(sub)

    def notify(self):
        for sub in self.subscribers:
            sub.update(self.news)

    def publish_news(self, text):
        self.news = text
        self.notify()


class Subscriber:
    def __init__(self, name):
        self.name = name

    def update(self, news):
        print(f"[{self.name}] прочитав новину: {news}")


if __name__ == "__main__":
    print("--- Factory Method ---")
    road = RoadLogistics()
    sea = SeaLogistics()
    print(road.plan_delivery())
    print(sea.plan_delivery())
    print("\n")

    print("--- Facade ---")
    editor = VideoEditorFacade()
    editor.render()
    print("\n")

    print("--- Observer ---")
    channel = Publisher()
    sub1 = Subscriber("Макс")
    sub2 = Subscriber("Іван")

    channel.subscribe(sub1)
    channel.subscribe(sub2)

    channel.publish_news("Завтра перша пара скасовується!")