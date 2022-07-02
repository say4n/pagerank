"""
Implementation of the PageRank algorithm.
"""
import typing


class SimplifiedPageRank:
    def __init__(self, outlinks: typing.Dict):
        self.graph = outlinks

    def compute_page_rank(self) -> typing.Dict:
        num_nodes = len(self.graph)
        v = dict((node, 1/num_nodes) for node in self.graph)
        r = dict((node, 0.0) for node in self.graph)

        for node in self.graph:
            outlinks = self.graph[node]

            for outlink in outlinks:
                r[outlink] += v[node] / len(outlinks)

        return r


if __name__ == "__main__":
    outlinks = {
        "A": [],
        "B": ["A", "C"],
        "C": ["A"],
        "D": ["A", "B", "C"],
    }

    spr = SimplifiedPageRank(outlinks)
    assert spr.compute_page_rank() == {'A': 0.4583333333333333, 'B': 0.08333333333333333, 'C': 0.20833333333333331, 'D': 0.0}