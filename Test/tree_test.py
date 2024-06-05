import unittest
import sys
from io import StringIO
sys.path.append("./")
from Factory.Tree_Factory import TreeFJE_Factory

class TestTreeFJEOutput(unittest.TestCase):
    def test_print_output(self):
        captured_output = StringIO()
        sys.stdout = captured_output
        FJE = TreeFJE_Factory("Test/icon_test.json").create_FJE()
        FJE.load("Test/test.json")
        FJE.show()
        sys.stdout = sys.__stdout__
        self.assertEqual(captured_output.getvalue(), 
        "├─♧oranges\n"+
        "|  └─♧mandarin\n"+
        "|     ├─♣clementine\n"+
        "|     └─♣tangerine:cheap & juicy!\n"+
        "└─♧apples\n"+
        "   ├─♣gala\n"+
        "   └─♣pink lady\n")

if __name__ == '__main__':
    unittest.main()