class SubjectInterface:
    # Both of these methods take an Observer as an argument; that is, the
    # Observer to be registered or removed.
    def registerObserver(self, observer):
        pass

    def removeObserver(self, observer):
        pass

    # This method is called to notify all observers when the Subject's state
    def notifyObservers(self):
        pass


class ObserverInterface:
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


class DisplayElementInterface:
    """
    The DisplayElement interface just includes one method, display(), that we
    will call when the display element needs to be displayed.
    """
    def display(self):
        pass
