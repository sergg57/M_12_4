# -*- coding: utf-8 -*-
import logging

class Runner:
    def __init__(self, name, speed=5):
        try:
            if isinstance(name, str):
                self.name = name
                logging.info(f'"test_run" выполнен успешно')
            else:
                raise TypeError(f'Имя может быть только строкой, передано {type(name).__name__}')
        except TypeError as error:
            logging.warning(f'Неверное имя для Runner {error}')
            self.name = 'Unknown'

        try:
            self.distance = 0
            if speed > 0:
                self.speed = speed
                logging.info(f'"test_walk" выполнен успешно')
            else:
                raise ValueError(f'Скорость не может быть отрицательной, сейчас {speed}')
        except ValueError as error:
            logging.warning(f'Неверная скорость для Runner {error}')
            self.speed = -speed
        #return

    def run(self):
        self.distance += self.speed * 2

    def walk(self):
        self.distance += self.speed

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.name

    def __eq__(self, other):
        if isinstance(other, str):
            return self.name == other
        elif isinstance(other, Runner):
            return self.name == other.name


class Tournament:
    def __init__(self, distance, *participants):
        self.full_distance = distance
        self.participants = list(participants)

    def start(self):
        finishers = {}
        place = 1
        while self.participants:
            for participant in self.participants:
                participant.run()
                if participant.distance >= self.full_distance:
                    finishers[place] = participant
                    place += 1
                    self.participants.remove(participant)

        return finishers

logging.basicConfig(level=logging.INFO, filemode='w', filename='runner_test.log',
                        format='%(asctime)s %(levelname)s %(message)s')


# first = Runner('Вося', 10)
# second = Runner('Илья', 5)
# # # third = Runner('Арсен', 10)
# #
# t = Tournament(101, first, second)
# print(t.start())
