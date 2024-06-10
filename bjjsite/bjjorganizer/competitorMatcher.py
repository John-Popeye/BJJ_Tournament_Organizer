from itertools import combinations
from collections import defaultdict

class CompetitorMatcher:
    def match_competitors(self, competitors):
        belt_groups = defaultdict(list)
        for competitor in competitors:
            belt_groups[competitor.belt].append(competitor)

        matches = []

        for belt, group in belt_groups.items():
            group.sort(key=lambda x: x.weight)

            while len(group) > 1:
                best_match = None
                min_weight_diff = float('inf')
                to_remove = None

                for i in range(1, len(group)):
                    weight_diff = abs(group[0].weight - group[i].weight)
                    if weight_diff < min_weight_diff and group[0].team != group[i].team:
                        min_weight_diff = weight_diff
                        best_match = (group[0], group[i])
                        to_remove = i

                if best_match is None:
                    best_match = (group[0], group[1])
                    to_remove = 1

                matches.append(best_match)
                del group[to_remove]
                del group[0]

            if len(group) == 1:
                unmatched_competitor = group[0]
                del group[0]

                best_match = None
                min_weight_diff = float('inf')

                for other_belt, other_group in belt_groups.items():
                    if other_group:
                        for competitor in other_group:
                            weight_diff = abs(unmatched_competitor.weight - competitor.weight)
                            if weight_diff < min_weight_diff:
                                min_weight_diff = weight_diff
                                best_match = (unmatched_competitor, competitor)
                                best_match_group = other_group
                                best_match_index = other_group.index(competitor)

                if best_match:
                    matches.append(best_match)
                    del best_match_group[best_match_index]

        return matches