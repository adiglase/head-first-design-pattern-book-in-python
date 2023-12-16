from abc import ABC, abstractmethod


class ObserverInterface(ABC):
    """
    The Observer interface is implemented by all observers, so they all have to
    implement the update() method.
    """
    @abstractmethod
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
    @abstractmethod
    def display(self):
        pass


class SubjectInterface(ABC):
    # Both of these methods take an Observer as an argument; that is, the
    # Observer to be registered or removed.
    @abstractmethod
    def registerObserver(self, observer: ObserverInterface):
        pass

    @abstractmethod
    def removeObserver(self, observer: ObserverInterface):
        pass

    @abstractmethod
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


class CurrentConditionsDisplay(ObserverInterface, DisplayElementInterface):
    """
    CurrentConditionsDisplay implements Observer so it can get changes from the
    WeatherData object. It also implements DisplayElement, because our API is
    going to require all display elements to implement this interface.
    """
    def __init__(self, weather_data: SubjectInterface):
        self.temperature = None
        self.humidity = None

        # We keep a reference to the weatherData object so we can use it to
        # register or remove ourselves as an observer.
        self.weather_data = weather_data
        
        weather_data.registerObserver(self)  # register the observer

    def update(self, temperature: float, humidity: float, pressure: float) -> None:
        """
        When update() is called, we save the temp and humidity and call
        display().
        """
        self.temperature = temperature
        self.humidity = humidity
        self.display()
    
    def display(self) -> None:
        """
        display() just prints out the most recent temp and humidity.
        """
        print(f"Current conditions: {self.temperature}F degrees and {self.humidity}% humidity")
