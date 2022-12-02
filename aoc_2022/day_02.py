class Shape:
    def __init__(self, value):
        self.value = value

    shape_scores = dict(
        X=1,
        Y=2,
        Z=3
    )

    mapping = dict(
        X=dict(X=3, Y=0, Z=6),
        Y=dict(X=6, Y=3, Z=0),
        Z=dict(X=0, Y=6, Z=3)
    )

    def compare(self, other):
        return self.mapping[self.value][other.value]

    @property
    def score(self):
        return self.shape_scores[self.value]


class RPS:
    """Game of Rock Paper Scissors"""
    score_1 = 0
    score_2 = 0

    player_shape_mapping = dict(
        A='X', B='Y', C='Z'
    )
    outcome_mapping = {'X': 0, 'Y': 3, 'Z': 6}
    outcome_choice = {key:
                          {6 - score: shape for shape, score in val.items()}
                      for key, val in Shape.mapping.items()}

    def play_round(self, player_1, player_2):
        self.score_1 += player_1.score + player_1.compare(player_2)
        self.score_2 += player_2.score + player_2.compare(player_1)

    def evaluate_strategy(self, input):
        rounds = [x.split(' ') for x in input.split('\n')]
        for a, b in rounds:
            self.play_round(Shape(self.player_shape_mapping[a]), Shape(b))
        return self.score_2

    def evaluate_strategy_advanced(self, input):
        rounds = [x.split(' ') for x in input.split('\n')]
        for a, b in rounds:
            chosen_shape = self.outcome_choice[self.player_shape_mapping[a]][self.outcome_mapping[b]]
            self.play_round(Shape(self.player_shape_mapping[a]), Shape(chosen_shape))
        return self.score_2
