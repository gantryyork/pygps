from unittest import TestCase
import gps.convert


class TestConvert(TestCase):

    def test_nm_to_km_positive(self):
        answer = 186.126
        result = gps.convert.nm_to_km(100.5)
        self.assertAlmostEqual(result, answer, 3)

    def test_nm_to_km_negative(self):
        answer = -59.4697572
        result = gps.convert.nm_to_km(-32.1111)
        self.assertAlmostEqual(result, answer, 3)

    def test_km_to_nm_positive(self):
        answer = 41.95464
        result = gps.convert.km_to_nm(77.7)
        self.assertAlmostEqual(result, answer, 3)

    def test_km_to_nm_negative(self):
        answer = -53.9951404
        result = gps.convert.km_to_nm(-99.999)
        self.assertAlmostEqual(result, answer, 3)

    def test_mi_to_nm_positive(self):
        answer = 8.68976328798
        result = gps.convert.mi_to_nm(10.00001)
        self.assertAlmostEqual(result, answer, 3)

    def test_mi_to_nm_negative(self):
        answer = -261.562
        result = gps.convert.mi_to_nm(-301)
        self.assertAlmostEqual(result, answer, 3)

    def test_mi_to_km_positive(self):
        answer = 16.0932791
        result = gps.convert.mi_to_km(9.9999)
        self.assertAlmostEqual(result, answer, 3)

    def test_mi_to_km_negative(self):
        answer = -4.83108975
        result = gps.convert.mi_to_km(-3.0019)
        self.assertAlmostEqual(result, answer, 3)

    def test_dms_correct_neg_degrees(self):
        result = gps.convert.dms_correct(-10, 10, 10, 'north')
        self.assertEqual((-10, 10, 10, 'N'), result)

    def test_dms_correct_pos_degrees(self):
        result = gps.convert.dms_correct(10, 10, 10, 'W')
        self.assertEqual((10, 10, 10, 'W'), result)

    def test_dms_correct_seconds_carry_1(self):
        result = gps.convert.dms_correct(10, 10, 90, 'W')
        self.assertEqual((10, 11, 30, 'W'), result)

    def test_dms_correct_seconds_carry_2(self):
        result = gps.convert.dms_correct(10, 10, 121, 'W')
        self.assertEqual((10, 12, 1, 'W'), result)

    def test_dms_correct_minutes_carry_1(self):
        result = gps.convert.dms_correct(10, 61, 30, 'W')
        self.assertEqual((11, 1, 30, 'W'), result)

    def test_dms_correct_minutes_carry_2(self):
        result = gps.convert.dms_correct(10, 125, 30, 'W')
        self.assertEqual((12, 5, 30, 'W'), result)

    def test_dms_correct_degrees_exceed_90(self):
        result = gps.convert.dms_correct(92, 10, 30, 'west')
        self.assertEqual((92, 10, 30, 'W'), result)

    def test_dms_correct_degrees_exceed_180(self):
        result = gps.convert.dms_correct(372, 59, 59, 'W')
        self.assertEqual((372, 59, 59, 'W'), result)

    def test_dms_correct_truncation(self):
        result = gps.convert.dms_correct(10.5, 59.1, 59.9999, 'W')
        self.assertEqual((10, 59, 59, 'W'), result)

    def test_dms_correct_negative_values(self):
        result = gps.convert.dms_correct(-89.111, -65.111, -65.222, 'sOUth')
        self.assertEqual((-90, 6, 5, 'S'), result)

    def test_dec_to_longitude_positive(self):
        result = gps.convert.dec_to_longitude(45.1111)
        self.assertEqual(45.1111, result)

    def test_dec_to_longitude_negative(self):
        result = gps.convert.dec_to_longitude(-37.9999)
        self.assertEqual(-37.9999, result)

    def test_dec_to_longitude_pos_wrap1(self):
        result = gps.convert.dec_to_longitude(182)
        self.assertEqual(-88, result)

    # def test_dec_to_longitude_pos_wrap2(self):
    #     result = gps.convert.dec_to_longitute(362.2)
    #     self.assertEqual(2.2, result)
    #
    # def test_dms_to_longitude_neg_wrap1(self):
    #     result = gps.convert.dms_to_longitute(-180.9999)
    #     self.assertEqual(179.0001, result)
    #
    # def test_dms_to_longitude_neg_wrap2(self):
    #     result = gps.convert.dms_to_longitute(-180.9999)
    #     self.assertEqual(179.0001, result)
