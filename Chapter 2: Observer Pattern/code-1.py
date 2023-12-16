from abc import ABC


class ObserverInterface(ABC):
    """
    The Observer interface is implemented by all observers, so they all have to
    implement the update() method.
    """
    def update(self, temp, humidity, pressure):
        """
        We got three state values from the Subject when a weather measurement
        changes: temp, humidity, and pressure.
        """
        pass


class DisplayElementInterface(ABC):
    """
    The DisplayElement interface just includes one method, display(), that we
    will call when the display element needs to be displayed.
    """
    def display(self):
        pass


class SubjectInterface(ABC):
    # Both of these methods take an Observer as an argument; that is, the
    # Observer to be registered or removed.
    def registerObserver(self, observer: ObserverInterface):
        pass

    def removeObserver(self, observer: ObserverInterface):
        pass

    # This method is called to notify all observers when the Subject's state
    def notifyObservers(self):
        pass


class WeatherData(SubjectInterface):
    """
    WeatherData now implements the Subject interface. It includes an array of
    Observers as an instance variable, as well as implementations of the
    registerObserver(), removeObserver(), and notifyObservers() methods.
    """
    def __init__(self):
        # We've added a list to hold the Observers.
        self.observers = []

        self.temperature = None
        self.humidity = None
        self.pressure = None
    
    def registerObserver(self, observer: ObserverInterface) -> None:
        """
        When an observer registers, we just add it to the end of the list.
        """
        self.observers.append(observer)

    def removeObserver(self, observer: ObserverInterface) -> None:
        """
        If an observer wants to un-register, we just take it off the list.
        """
        self.observers.remove(observer)
    
    def notifyObservers(self) -> None:
        """
        Here's the fun part; this is where we tell all the observers about the
        state. Because they are all Observers, we know they all implement the
        update() method.
        """
        for observer in self.observers:
            observer.update(self.temperature, self.humidity, self.pressure)
    
    def measurementsChanged(self) -> None:
        """
        We notify the observers when we get updated measurements from the
        Weather Station.
        """
        self.notifyObservers()
    
    def setMeasurements(self, temperature: float, humidity: float, pressure: float) -> None:
        self.temperature = temperature
        self.humidity = humidity
        self.pressure = pressure

        self.measurementsChanged()
    
    # other WeatherData methods here.
