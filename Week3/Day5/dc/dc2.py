# Class: A class is a blueprint for creating objects. It defines the properties and behaviors that objects of that class will have.

# Instance: An instance, also known as an object, is a specific occurrence of a class. It represents a unique entity with its own state and behavior.

# Encapsulation: Encapsulation is the bundling of data and methods within a class. It allows for data hiding and protects the internal implementation details of a class.

# Abstraction: Abstraction is the concept of representing essential features and hiding unnecessary details. It focuses on the high-level behavior of an object or class, without exposing its internal workings.

# Inheritance: Inheritance is a mechanism that allows a class to inherit properties and methods from another class. It promotes code reuse and facilitates the creation of a hierarchy of classes.

# Multiple Inheritance: Multiple Inheritance is a feature that enables a class to inherit from multiple parent classes. It allows the child class to inherit and combine the attributes and behaviors of multiple classes.

# Polymorphism: Polymorphism refers to the ability of objects to take on different forms or behave differently based on the context. It allows objects of different classes to be treated interchangeably based on their common interface or base class.

# Method Resolution Order (MRO): Method Resolution Order is the order in which classes are searched to find a method or attribute. It is relevant in cases of inheritance and multiple inheritance, determining the sequence in which the base classes are traversed to locate the desired method or attribute.

import random


class Card:
    def __init__(self, suit, value):
        self.suit = suit
        self.value = value

    def __str__(self):
        return f"{self.value} of {self.suit}"


class Deck:
    def __init__(self):
        suits = ["Hearts", "Diamonds", "Clubs", "Spades"]
        values = ["A", "2", "3", "4", "5", "6",
                  "7", "8", "9", "10", "J", "Q", "K"]
        self.cards = [Card(suit, value) for suit in suits for value in values]

    def shuffle(self):
        random.shuffle(self.cards)

    def deal(self):
        if len(self.cards) == 0:
            return None
        card = self.cards.pop(0)
        return card

    def get_num_cards(self):
        return len(self.cards)


# Example usage
deck = Deck()
deck.shuffle()
while deck.get_num_cards() > 0:
    card = deck.deal()
    if card:
        print(f"Dealt card: {card}")
    else:
        print("No cards left in the deck.")

print("All cards have been dealt.")
