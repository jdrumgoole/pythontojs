import unittest

import pymag

"""
Default test cluster mongodb+srv://readonly:readonly@demodata.rgl39.mongodb.net/<dbname>?retryWrites=true&w=majority
use demo.zipcodes collection
"""

import pprint

import pymongo


def add_a_string():
    return "this is a string"


class TestOperators(unittest.TestCase):


    def setUp(self):
        cluster = "mongodb+srv://readonly:readonly@demodata.rgl39.mongodb.net/<dbname>?retryWrites=true&w=majority"
        client = pymongo.MongoClient(host=cluster)
        db = client["demo"]
        self.col = db["zipcodes"]

    def test_limit(self):
        p = pymag.Pipeline()
        limiter = pymag.limit(10)
        p.append(limiter)
        print(p)
        c = p.aggregate(self.col)
        for d in c:
            print(d)


    def test_function(self):

        p = pymag.Pipeline()
        func = pymag.function(pymag.FuncToJS(add_a_string, "bongo"))
        print("func")
        pprint.pprint(func())
        limiter = pymag.limit(10)
        adder = pymag.addFields({"new_field": func()})
        p.append(limiter)
        p.append(adder)
        pprint.pprint(p)
        c = p.aggregate(self.col)
        for d in c:
            print(d)

    def test_abs(self):
        _ = pymag.abs(1)
        with self.assertRaises(TypeError):
            _ = pymag.abs("hello")

        with self.assertRaises(TypeError):
            _ = pymag.abs(1.0)

    def test_add(self):
        _ = pymag.add([2, 3, 5, 8])
        _ = pymag.add([2])

        with self.assertRaises(TypeError):
            _ = pymag.add(None)

    def test_ceil(self):
        _ = pymag.ceil(1)
        _ = pymag.ceil(12.5)
        with self.assertRaises(TypeError):
            _ = pymag.ceil("hello")

    def test_divide(self):
        _ = pymag.divide(10, 2)
        _ = pymag.divide(18.5, 6.1)

        with self.assertRaises(TypeError):
            _ = pymag.divide("bus", "truck")

    def test_exp(self):
        _ = pymag.exp(1.0)
        _ = pymag.exp(1.5)
        x = pymag.exp(4)

        print(x)
        print(x())
        with self.assertRaises(TypeError):
            _ = pymag.exp("hello")


if __name__ == '__main__':
    unittest.main()
