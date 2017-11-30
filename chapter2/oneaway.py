import unittest

def oneAway(pair):
    ''' returns one away truthy '''
    if not isinstance(pair, list) or len(pair) != 2 or any(not isinstance(word, str) for word in pair):
        raise Exception('Invalid Input')
    else:
        len1 = len(pair[0])
        len2 = len(pair[1])
        if len1 == len2:
            if pair[0] == pair[1]:
                return True
            # difference in indices check
            difference = 0
            for i in range(len1):
                if pair[0][i] != pair[1][i]:
                    difference += 1
                if difference > 1:
                    return False
            return True

        elif len1-len2 == 1 or len2-len1 == 1:
            #difference of one
            difference  = 0
            if len1<len2:
                longer_word = pair[1]
                shorter_word = pair[0]
            else:
                longer_word = pair[0]
                shorter_word = pair[1]

            for i in range(len(longer_word)):
                if longer_word[i] not in shorter_word:
                    difference += 1
                if difference > 1:
                    return False
            return True
        else:
            return False

class Tests(unittest.TestCase):
    def test_invalid_input(self):
        with self.assertRaisesRegex(Exception, 'Invalid Input'):
            oneAway(1)

    def test_equal_length(self):
        self.assertFalse(oneAway(['bulk', 'pulp']))
        self.assertTrue(oneAway(['bulk', 'bulk']))
        self.assertTrue(oneAway(['bulk', 'bulb']))

    def test_empty_strings(self):
        self.assertTrue(oneAway(['b','']))
        self.assertTrue(oneAway(['','']))

    def test_one_away(self):
        self.assertTrue(oneAway(['self', 'selfi']))

    def test_two_away(self):
        self.assertFalse(oneAway(['self', 'selfie']))
        self.assertFalse(oneAway(['jodom', 'j0doms']))

if __name__ == '__main__':
    unittest.main()