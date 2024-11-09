import unittest
from unittest import TestCase

class Runner:
    def __init__(self, name):
        self.name = name
        self.distance = 0

    def run(self):
        self.distance += 10

    def walk(self):
        self.distance += 5

    def __str__(self):
        return self.name

class RunnerTest(TestCase):
    def test_walk(self):
        runner = Runner('Test Runner') # создаем объект класса Runner с произвольным именем

        for _ in range(10): # вызываем метод walk 10 раз
            runner.walk()

        self.assertEquals(runner.distance, 50) # сравниваем distance этого объекта со значением 50

    def test_run(self):
        runner = Runner('Test Runner')
        for _ in range(10):
            runner.run()
        self.assertEquals(runner.distance, 100) # сравниваем distance этого объекта со значением 100

    def test_challenge(self):
        runner1 = Runner('Test Runner1')
        runner2 = Runner('Test Runner2')
        for _ in range(10):
            runner1.run()
            runner2.walk()
        self.assertNotEqual(runner1.distance, runner2.distance)

# Запускаем тест

if __name__ == '__main__':
    unittest.main()


