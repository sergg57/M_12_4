# -*- coding: utf-8 -*-
import unittest
import rt_with_exerptions
import logging

class RunnerTest(unittest.TestCase):
    # def setUp(self):
    #     self.first = rt_with_exerptions.Runner('Вася', 10)
        #self.second = rt_with_exerptions.Runner('Илья', -5)

    # def test_name(self):
    #     self.assertIsInstance(self.first.name, str)
    #     #self.assertIsInstance(self.second.name, str)


    def test_run(self):
        #try:
        self.first = rt_with_exerptions.Runner(20, 10)
        self.second = rt_with_exerptions.Runner('Илья', 5)
        self.first.run()
        self.second.run()
        self.assertEqual(self.first.distance, 20)
        self.assertEqual(self.second.distance, 10)

        # except TypeError as error:
        #     logging.warning(f'Неверное имя для Runner {error}')
            #self.name = 'Unknown'

    def test_walk(self):
        self.first = rt_with_exerptions.Runner('Вася', 10)
        self.second = rt_with_exerptions.Runner('Илья', -5)
        self.first.walk()
        self.second.walk()
        self.assertEqual(self.first.distance, 10)
        self.assertEqual(self.second.distance, 5)



if __name__ == '__main__':
    unittest.main()
