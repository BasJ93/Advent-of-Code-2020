import unittest

from solver import AoC
from ticket import Rule, Ticket

class SolverUnitTests(unittest.TestCase):

    def test_RuleGenerator(self):
        solver = AoC()
        solver.data = ["class: 1-3 or 5-7\nrow: 6-11 or 33-44\nseat: 13-40 or 45-50"]
        solver.generateData()
        self.assertEqual(3, len(solver.rules))

    def test_TicketGenerator(self):
        solver = AoC()
        solver.data = ["nearby tickets:\n7,3,47\n40,4,50\n55,2,20\n38,6,12"]
        solver.generateData()
        self.assertEqual(4, len(solver.nearbyTickets))

    def test_Ticket_validate(self):
        ticket = Ticket("40,4,50")
        rules = [Rule("class: 1-3 or 5-7"), Rule("row: 6-11 or 33-44"), Rule("seat: 13-40 or 45-50")]
        result = ticket.validate(rules)
        self.assertEqual(4, result)    

    def test_Ticket_findValidFields(self):
        ticket = Ticket("3,9,18")
        rules = [Rule("class: 0-1 or 4-19"), Rule("row: 0-5 or 8-19"), Rule("seat: 0-13 or 16-19")]
        result = ticket.findValidFields(rules)
        self.assertEqual(3, len(result))
        self.assertEqual(0, result["row"][0])

        ticket = Ticket("15,1,5")
        result2 = ticket.findValidFields(rules)
        self.assertEqual(3, len(result2))
        #self.assertEqual(0, result2["row"][0])

        ticket = Ticket("5,14,9")
        result3 = ticket.findValidFields(rules)
        self.assertEqual(3, len(result3))
        #self.assertEqual(0, result3["row"][0])

    def test_Task1(self):
        solver = AoC()
        solver.data = ["class: 1-3 or 5-7\nrow: 6-11 or 33-44\nseat: 13-40 or 45-50", "nearby tickets:\n7,3,47\n40,4,50\n55,2,20\n38,6,12"]
        solver.generateData()
        result = solver.Task1()
        self.assertEqual(71, result)

    def test_Task2(self):
        solver = AoC()
        solver.data = ["class: 0-1 or 4-19\nrow: 0-5 or 8-19\nseat: 0-13 or 16-19", "nearby tickets:\n3,9,18\n15,1,5\n5,14,9"]
        solver.generateData()
        result = solver.Task2()

if __name__ == '__main__':
    unittest.main()
