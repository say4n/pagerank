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
