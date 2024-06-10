import unittest
import sys
from io import StringIO
sys.path.append("./")
from Factory.Tree_Factory import Tree_Factory
from Factory.Rect_Factory import Rect_Factory

class TestTreeFJEOutput(unittest.TestCase):
    def test_print_output(self):
        captured_output = StringIO()
        sys.stdout = captured_output
        FJE = Tree_Factory().createFJE("Test/icon_test.json")
        FJE.show("Test/test.json")
        sys.stdout = sys.__stdout__
        self.assertEqual(captured_output.getvalue(), 
        "├─♧oranges\n"+
        "|  └─♧mandarin\n"+
        "|     ├─♣clementine\n"+
        "|     └─♣tangerine:cheap & juicy!\n"+
        "└─♧apples\n"+
        "   ├─♣gala\n"+
        "   └─♣pink lady\n")

class TestRectFJEOutput(unittest.TestCase):
    def test_print_output(self):
        captured_output = StringIO()
        sys.stdout = captured_output
        FJE = Rect_Factory().createFJE("Test/icon_test.json")
        FJE.show("Test/test.json")
        sys.stdout = sys.__stdout__
        self.assertEqual(captured_output.getvalue(), 
        "┌─♧oranges───────────────────────────────────────┐\n"+
        "|──├─♧mandarin───────────────────────────────────|\n"+
        "|──|──├─♣clementine──────────────────────────────|\n"+
        "|──|──├─♣tangerine:cheap & juicy!────────────────|\n"+
        "├─♧apples────────────────────────────────────────|\n"+
        "|──├─♣gala───────────────────────────────────────|\n"+
        "└──└─♣pink lady──────────────────────────────────┘\n")

if __name__ == '__main__':
    unittest.main()