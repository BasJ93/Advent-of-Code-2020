import unittest

from solver import AoC7

class SolverUnitTests(unittest.TestCase):
    def test_bag_generator(self):
        solver = AoC7()
        data = ["light red bags contain 1 bright white bag, 2 muted yellow bags.",
                "dark orange bags contain 3 bright white bags, 4 muted yellow bags.",
                "bright white bags contain 1 shiny gold bag.",
                "muted yellow bags contain 2 shiny gold bags, 9 faded blue bags.",
                "shiny gold bags contain 1 dark olive bag, 2 vibrant plum bags.",
                "dark olive bags contain 3 faded blue bags, 4 dotted black bags.",
                "vibrant plum bags contain 5 faded blue bags, 6 dotted black bags.",
                "faded blue bags contain no other bags.",
                "dotted black bags contain no other bags."]
        result = solver.generateBags(data)
        self.assertEqual(9, len(result))
        self.assertEqual("light red", result[0].Color)
        self.assertEqual(2, len(result[0].Contains))
        self.assertEqual(1, len(result[2].Contains))
        self.assertEqual(0, len(result[-1].Contains))

    def test_bag_generator_more_than_2_contents(self):
        solver = AoC7()
        data = ["mirrored bronze bags contain 3 striped maroon bags, 4 shiny gold bags, 4 light indigo bags, 5 clear orange bags."]
        result = solver.generateBags(data)
        self.assertEqual(1, len(result))
        self.assertEqual("mirrored bronze", result[0].Color)
        self.assertEqual(4, len(result[0].Contains))

    def test_Task1_directContents(self):
        solver = AoC7()
        input_data = ["light red bags contain 1 bright white bag, 2 muted yellow bags.",
                      "dark orange bags contain 3 bright white bags, 4 muted yellow bags.",
                      "bright white bags contain 1 shiny gold bag.",
                      "muted yellow bags contain 2 shiny gold bags, 9 faded blue bags.",
                      "shiny gold bags contain 1 dark olive bag, 2 vibrant plum bags.",
                      "dark olive bags contain 3 faded blue bags, 4 dotted black bags.",
                      "vibrant plum bags contain 5 faded blue bags, 6 dotted black bags.",
                      "faded blue bags contain no other bags.",
                      "dotted black bags contain no other bags."]
        solver.data = solver.generateBags(input_data)
        count = solver.Task1("shiny gold")
        self.assertEqual(4, count)

    def test_CalculateChildBags(self):
        solver = AoC7()
        input_data = ["vibrant plum bags contain 5 faded blue bags, 6 dotted black bags.",
                      "faded blue bags contain no other bags.",
                      "dotted black bags contain no other bags."]
        solver.data = solver.generateBags(input_data)
        bag = solver.GetBagByColor("vibrant plum")
        count = solver.CalculateChildBags(bag)
        self.assertEqual(12, count)

    def test_Task2_single_input(self):
        solver = AoC7()
        input_data = ["vibrant plum bags contain 5 faded blue bags, 6 dotted black bags.",
                      "faded blue bags contain no other bags.",
                      "dotted black bags contain no other bags."]
        solver.data = solver.generateBags(input_data)
        count = solver.Task2("vibrant plum")
        self.assertEqual(11, count)

    def test_Task2(self):
        solver = AoC7()
        input_data = ["light red bags contain 1 bright white bag, 2 muted yellow bags.",
                      "dark orange bags contain 3 bright white bags, 4 muted yellow bags.",
                      "bright white bags contain 1 shiny gold bag.",
                      "muted yellow bags contain 2 shiny gold bags, 9 faded blue bags.",
                      "shiny gold bags contain 1 dark olive bag, 2 vibrant plum bags.",
                      "dark olive bags contain 3 faded blue bags, 4 dotted black bags.",
                      "vibrant plum bags contain 5 faded blue bags, 6 dotted black bags.",
                      "faded blue bags contain no other bags.",
                      "dotted black bags contain no other bags."]
        solver.data = solver.generateBags(input_data)
        count = solver.Task2("shiny gold")
        self.assertEqual(32, count)

    def test_Task2_2(self):
        solver = AoC7()
        input_data = ["shiny gold bags contain 2 dark red bags.",
                      "dark red bags contain 2 dark orange bags.",
                      "dark orange bags contain 2 dark yellow bags.",
                      "dark yellow bags contain 2 dark green bags.",
                      "dark green bags contain 2 dark blue bags.",
                      "dark blue bags contain 2 dark violet bags.",
                      "dark violet bags contain no other bags."]
        solver.data = solver.generateBags(input_data)
        count = solver.Task2("shiny gold")
        self.assertEqual(126, count)

if __name__ == '__main__':
    unittest.main()
