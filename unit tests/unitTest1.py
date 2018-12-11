from tkinter import*
from pbbackend import *
from pbfrontend import *
import unittest

class TestStringMethods(unittest.TestCase):

    def test_max_entries(self):
        entryNumber = 1
        for i in range(100):
            Database.insert("dillon", "test", "florida", "Test")
            entryNumber += 1
        assert entryNumber == 101
        assert Database.rowCount != None
        Database.destroy()

    def test_max_delete(self):
        for i in range(100):
            Database.insert("dillon", "test", "florida", "Test")
        for item in range(100):
            Database.delete(item)
        assert Database.rowCount() == None
        Database.destroy()

    def test_view(self):
        Database.insert("dillon", "test", "florida", "Test")
        view = Database.view()
        assert view == [(1, 'dillon', 'test', 'florida', 'Test')]
        Database.destroy()

    def test_search(self):
        Database.insert("dillon", "test", "florida", "Test")
        Database.insert("nollid", "tset", "adirolf", "tset")
        searchResultsEntryA = Database.search("dillon", "test", "florida", "Test");
        searchResultsEntryB = Database.search("nollid", "tset", "adirolf", "tset");
        searchResultsMispelled = Database.search("nld", "tst", "adlf", "t");
        searchResultsEmptyCheck = Database.search("");
        assert searchResultsEntryA == [(1, 'dillon', 'test', 'florida', 'Test')]
        assert searchResultsEntryB == [(2, 'nollid', 'tset', 'adirolf', 'tset')]
        assert searchResultsMispelled == []
        assert searchResultsEmptyCheck == []
        Database.destroy()

    def test_update(self):
        #args: id, firstName, lastName, location, number

        Database.insert("dillon", "test", "florida", "Test")
        Database.insert("nollid", "tset", "adirolf", "tset")
        Database.update(1,"test","test","test","test")
        Database.update(2, "test2", "test2", "test2", "test2")
        testResults1 = Database.search("test","test","test","test")
        testResults2 = Database.search("test2", "test2", "test2", "test2")
        assert testResults1 == [(1, 'test', 'test', 'test', 'test')]
        assert testResults2 == [(2, 'test2', 'test2', 'test2', 'test2')]
        Database.destroy()

if __name__ == '__main__':
    print(Database.rowCount())
    unittest.main()




