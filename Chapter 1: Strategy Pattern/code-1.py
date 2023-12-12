from abc import ABC, abstractmethod


class Duck(ABC):
    def __init__(self):
        self.fly_behavior = None
        self.quack_behavior = None

    def perform_fly(self):
        self.fly_behavior.fly()

    def perform_quack(self):
        self.quack_behavior.quack()
    
    def set_fly_behavior(self, fb):
        self.fly_behavior = fb
    
    def set_quack_behavior(self, qb):
        self.quack_behavior = qb
    
    def swim(self):
        print("All ducks float, even decoys!")
    
    @abstractmethod
    def display(self):
        pass


class MallardDuck(Duck):
    def __init__(self):
        super().__init__()
        self.fly_behavior = FlyWithWings()
        self.quack_behavior = Quack()

    def display(self):
        print("I'm a real Mallard duck")


class ReadHeadDuck(Duck):
    def __init__(self):
        super().__init__()
        self.fly_behavior = FlyWithWings()
        self.quack_behavior = Quack()

    def display(self):
        print("I'm a real ReadHead duck")
    

class RubberDuck(Duck):
    def __init__(self):
        super().__init__()
        self.fly_behavior = FlyNoWay()
        self.quack_behavior = Squeak()

    def display(self):
        print("I'm a real Rubber duck")


class FlyBehaviorInterface(ABC):
    @abstractmethod
    def fly(self):
        pass


class FlyWithWings(FlyBehaviorInterface):
    def fly(self):
        print("I'm flying!!")


class FlyNoWay(FlyBehaviorInterface):
    def fly(self):
        print("I can't fly")


class QuackBehaviorInterface(ABC):
    @abstractmethod
    def quack(self):
        pass


class Quack(QuackBehaviorInterface):
    def quack(self):
        print("Quack")


class Squeak(QuackBehaviorInterface):
    def quack(self):
        print("Squeak")


class MuteSqueak(QuackBehaviorInterface):
    def quack(self):
        print("<< Silence >>")


if __name__ == "__main__":
    mallard = MallardDuck()
    mallard.perform_fly()
    mallard.perform_quack()
    mallard.set_fly_behavior(FlyNoWay())
    mallard.perform_fly()
    mallard.set_quack_behavior(MuteSqueak())
    mallard.perform_quack()
    mallard.display()
    mallard.swim()
    print()

    rubber = RubberDuck()
    rubber.perform_fly()
    rubber.perform_quack()
    rubber.set_fly_behavior(FlyWithWings())
    rubber.perform_fly()
    rubber.set_quack_behavior(Quack())
    rubber.perform_quack()
    rubber.display()
    rubber.swim()
    print()

    red_head = ReadHeadDuck()
    red_head.perform_fly()
    red_head.perform_quack()
    red_head.set_fly_behavior(FlyNoWay())
    red_head.perform_fly()
    red_head.set_quack_behavior(MuteSqueak())
    red_head.perform_quack()
    red_head.display()
    red_head.swim()
    print()