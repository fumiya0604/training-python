import unittest
from code import calc_tax


class TestCalcTax(unittest.TestCase):
    """
    テストクラス
    """

    def test_calc_tax_regular(self):
        """
        税を計算する関数のテスト
        税なし
        """
        expected = 1000
        actual = calc_tax(1000, True)

        self.assertEqual(expected, actual)

    def test_calc_tax_regular2(self):
        """
        税を計算する関数のテスト
        税あり
        """
        expected = 1100
        actual = calc_tax(1000, False)

        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()
