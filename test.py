from pagerank import SimplifiedPageRank
import unittest


class TestSimplifiedPageRank(unittest.TestCase):
    def test_graph_with_four_nodes(self):
        """
        The function `test_graph_with_four_nodes` tests the `compute_page_rank`
        function on a graph with four nodes.
        """
        outlinks = {
            "A": [],
            "B": ["A", "C"],
            "C": ["A"],
            "D": ["A", "B", "C"],
        }

        spr = SimplifiedPageRank(outlinks)
        self.assertEqual(
            spr.compute_page_rank(),
            {'A': 0.4583333333333333, 'B': 0.08333333333333333, 'C': 0.20833333333333331, 'D': 0.0}
        )

    def test_graph_with_rank_sink(self):
        """
        The function `test_graph_with_four_nodes` tests the `compute_page_rank`
        function on a graph with rank sinks.
        """
        outlinks = {
            "A": ["B"],
            "B": ["A"],
        }

        spr = SimplifiedPageRank(outlinks)
        self.assertEqual(
            spr.compute_page_rank(),
            {'A': 0.5, 'B': 0.5}
        )

if __name__ == '__main__':
    unittest.main()
