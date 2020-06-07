from ClimbingLeaderboard.codeForTest import climbingLeaderboard
from unittest import TestCase
import difflib


class TestCode(TestCase):
    def test_leaderboard(self):
        with open('input.txt', 'r') as fptr:
            scores_count = int(fptr.readline())
            scores = list(map(int, fptr.readline().rstrip().split()))
            alice_count = int(fptr.readline())
            alice = list(map(int, fptr.readline().rstrip().split()))
            result = climbingLeaderboard(scores, alice)

        with open('output.txt', 'w') as fptr:
            fptr.write('\n'.join(map(str, result)))
            fptr.write('\n')

        with open('output.txt', 'r') as out:
            with open('expected_output.txt', 'r') as correct:
                output = out.readlines()
                corr = correct.readlines()
                for diff in difflib.ndiff(output, corr):
                    print(diff)
                self.assertEqual(output, corr)
