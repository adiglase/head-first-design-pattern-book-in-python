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
    def notifyObservers(self):
        # This method is called to notify all observers when the Subject's state
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


class HeatIndexDisplay(ObserverInterface, DisplayElementInterface):
    def __init__(self, weather_data: SubjectInterface):
        self.heat_index = None
        self.weather_data = weather_data

        weather_data.registerObserver(self)

    def update(self, temperature: float, humidity: float, pressure: float) -> None:
        self.heat_index = self.compute_index(temperature, humidity)
        self.display()

    def display(self) -> None:
        print(f"Heat index is {self.heat_index}")

    def compute_index(self, t, rh):
        index = (float)((16.923 + (0.185212 * t) + (5.37941 * rh) - (0.100254 * t * rh) +
		(0.00941695 * (t * t)) + (0.00728898 * (rh * rh)) +
		(0.000345372 * (t * t * rh)) - (0.000814971 * (t * rh * rh)) +
		(0.0000102102 * (t * t * rh * rh)) - (0.000038646 * (t * t * t)) + (0.0000291583 *  
		(rh * rh * rh)) + (0.00000142721 * (t * t * t * rh)) +
		(0.000000197483 * (t * rh * rh * rh)) - (0.0000000218429 * (t * t * t * rh * rh)) +     
		0.000000000843296 * (t * t * rh * rh * rh)) -
		(0.0000000000481975 * (t * t * t * rh * rh * rh)))
        
        return index;


class WeatherStation:
    def main(self):
        weather_data = WeatherData()
        current_display = CurrentConditionsDisplay(weather_data)
        heat_index_display = HeatIndexDisplay(weather_data)

        weather_data.setMeasurements(80, 65, 30.4)
        weather_data.setMeasurements(82, 70, 29.2)
        weather_data.setMeasurements(78, 90, 29.2)


if __name__ == "__main__":
    WeatherStation().main()
