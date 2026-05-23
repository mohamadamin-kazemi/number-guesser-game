class Scorer:
    """
    Manage the player's score in the game.
    """

    def __init__(self, initial_score: int = 100):
        """
        Initialize the scorer with a starting score.

        Args:
            initial_score (int, optional): Starting score value.
                Defaults to 100.
        """
        self.score = initial_score

    def decrement_score(self, penalty: int) -> None:
        """
        Reduce the player's score by a penalty amount.

        Args:
            penalty (int): Amount to subtract from the score.
        """
        self.score -= penalty

    def get_score(self) -> int:
        """
        Return the current score.

        Returns:
            int: Current player score.
        """
        return self.score