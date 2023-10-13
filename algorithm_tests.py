import logging
import unittest
import json
from algorithm import Object, ColorOrder, InputOrderCheck

# Настройка логгера
logging.basicConfig(level=logging.DEBUG, filename="logging.log", filemode="w",
                    format="%(asctime)s %(levelname)s %(message)s", encoding='utf-8')

with open('positive_testcases.json', encoding='utf-8') as f:
    positive_testcases = json.load(f)

with open('negative_input_testcases.json', encoding='utf-8') as f:
    negative_input_testcases = json.load(f)

with open('negative_order_testcases.json', encoding='utf-8') as f:
    negative_order_testcases = json.load(f)


class TestSortingAlgorithm(unittest.TestCase):
    def test_sorting_algorithm_positive(self):
        logging.debug("TESTS START")
        for testcase in positive_testcases:
            objectsparsed = testcase['objectstest']
            orders = testcase['order']
            objects = []
            order = []
            for obj in objectsparsed:
                objects.append(Object(obj))
            for obj in orders:
                order.append(obj)
            color_order = ColorOrder(objects, order)
            check = InputOrderCheck(order)
            sorted_objects = color_order.sort()
            assertion = ""
            for obj in sorted_objects:
                assertion += obj.color

            try:
                self.assertEqual(assertion, testcase['result'])
                self.assertEqual(check.check(), "pass")
                logging.info(f"Test test_sorting_algorithm_positive is passed, "
                             f"initial values: '{testcase['objectstest']}', result: '{assertion}'")
            except Exception as error:
                logging.error(f"in test_sorting_algorithm_positive Value is {assertion}, Should be {testcase['result']}"
                              f"ERROR: {error}")


class TestSortingAlgorithmNegativeInput(unittest.TestCase):
    def test_sorting_algorithm_negative_input(self):
        logging.info("********************************************************************")
        for testcase in negative_input_testcases:
            objectsparsed = testcase['objectstest']
            orders = testcase['order']
            objects = []
            order = []
            for obj in objectsparsed:
                objects.append(Object(obj))
            for obj in orders:
                order.append(obj)
            color_order = ColorOrder(objects, order)
            check = InputOrderCheck(order)
            sorted_objects = color_order.sort()

            try:
                self.assertEqual(sorted_objects, testcase['result'])
                self.assertEqual(check.check(), "pass")
                logging.info(f"Test test_sorting_algorithm_negative_input is passed, "
                             f"initial values: '{testcase['objectstest']}', result: {sorted_objects}")
            except Exception as error:
                logging.error(
                    f"in test_sorting_algorithm_positive Value is {sorted_objects}, Should be {testcase['result']} "
                    f"ERROR: {error}")


class TestSortingAlgorithmNegativeOrder(unittest.TestCase):
    def test_sorting_algorithm_negative_order(self):
        logging.info("********************************************************************")
        for testcase in negative_order_testcases:
            orders = testcase['order']
            check = InputOrderCheck(orders)

            try:
                self.assertEqual(check.check(), testcase['result'])
                logging.info(f"Test test_sorting_algorithm_negative_order is passed, "
                             f"initial values: '{testcase['order']}', result: {testcase['result']}")
            except Exception as error:
                logging.error(f"in test_sorting_algorithm_positive Value is {check.check()}, "
                              f"Should be {testcase['result']}, ERROR: {error}")


if __name__ == "__main__":
    unittest.main()
