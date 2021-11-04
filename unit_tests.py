from unittest import TestCase
from gps.coordinate import Coordinate
import gps.convert
import gps.calculate


class TestConvert(TestCase):

    # xx_to_xx fucntions

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

    # dms_correct function

    def test_dms_correct_neg_degrees(self):
        result = gps.convert.dms_correct(-10, 10.5, 10, 'north')
        self.assertEqual((-10, 10, 10), result)

    def test_dms_correct_pos_degrees(self):
        result = gps.convert.dms_correct(10, 10, 10.5, 'W')
        self.assertEqual((-10, 10, 10), result)

    def test_dms_correct_seconds_carry_1(self):
        result = gps.convert.dms_correct(10, 10, 90, 'W')
        self.assertEqual((-10, 11, 30), result)

    def test_dms_correct_seconds_carry_2(self):
        result = gps.convert.dms_correct(10, 10, 121, 's')
        self.assertEqual((-10, 12, 1), result)

    def test_dms_correct_minutes_carry_1(self):
        result = gps.convert.dms_correct(10, 61, 30, 'W')
        self.assertEqual((-11, 1, 30), result)

    def test_dms_correct_minutes_carry_2(self):
        result = gps.convert.dms_correct(10, 125, 30, 'w')
        self.assertEqual((-12, 5, 30), result)

    def test_dms_correct_degrees_exceed_90(self):
        result = gps.convert.dms_correct(92, 10, 30, 'west')
        self.assertEqual((-92, 10, 30), result)

    def test_dms_correct_degrees_exceed_180(self):
        result = gps.convert.dms_correct(372, 59, 59, 'n')
        self.assertEqual((372, 59, 59), result)

    def test_dms_correct_truncation(self):
        result = gps.convert.dms_correct(10.5, 59.1, 59.9999, 'W')
        self.assertEqual((-10, 59, 59), result)

    def test_dms_correct_negative_values(self):
        result = gps.convert.dms_correct(-89.111, -65.111, -65.222, 'sOUth')
        self.assertEqual((-90, 6, 5), result)

    # dec_to_longitude function

    def test_dec_to_longitude_wrap0_neg(self):
        result = gps.convert.dec_to_longitude(-10.999)
        self.assertAlmostEqual(-10.999, result, 3)

    def test_dec_to_longitude_wrap1_neg(self):
        result = gps.convert.dec_to_longitude(-182.000001)
        self.assertAlmostEqual(178.000001, result, 3)

    def test_dec_to_longitude_wrap2_neg(self):
        result = gps.convert.dec_to_longitude(-362.5)
        self.assertAlmostEqual(-2.5, result, 3)

    def test_dec_to_longitude_wrap0_pos(self):
        result = gps.convert.dec_to_longitude(45.9999)
        self.assertAlmostEqual(45.9999, result, 3)

    def test_dec_to_longitude_wrap1_pos(self):
        result = gps.convert.dec_to_longitude(210.000001)
        self.assertAlmostEqual(-150.000001, result, 3)

    def test_dec_to_longitude_wrap2_pos(self):
        result = gps.convert.dec_to_longitude(375.3)
        self.assertAlmostEqual(15.3, result, 3)

    def test_dec_to_latitude_wrap0_pos(self):
        result = gps.convert.dec_to_latitude(10)
        self.assertAlmostEqual(10, result, 3)

    def test_dec_to_latitude_wrap1_pos(self):
        result = gps.convert.dec_to_latitude(95)
        self.assertAlmostEqual(85, result, 3)

    def test_dec_to_latitude_wrap2_pos(self):
        result = gps.convert.dec_to_latitude(190)
        self.assertAlmostEqual(-10, result, 3)

    def test_dec_to_latitude_wrap4_pos(self):
        result = gps.convert.dec_to_latitude(350)
        self.assertAlmostEqual(-10, result, 3)

    def test_dec_to_latitude_wrap0_neg(self):
        result = gps.convert.dec_to_latitude(-10)
        self.assertAlmostEqual(-10, result, 3)

    def test_dec_to_latitude_wrap1_neg(self):
        result = gps.convert.dec_to_latitude(-95)
        self.assertAlmostEqual(-85, result, 3)

    def test_dec_to_latitude_wrap2_neg(self):
        result = gps.convert.dec_to_latitude(-190)
        self.assertAlmostEqual(10, result, 3)

    def test_dec_to_latitude_wrap4_neg(self):
        result = gps.convert.dec_to_latitude(-350)
        self.assertAlmostEqual(10, result, 3)

    # def test_dms_to_dec_bad_dms(self):
    #     self.assertTrue(True)

    def test_dms_to_dec_pos1(self):
        result = gps.convert.dms_to_dec(34, 25, 10, 'N')
        self.assertAlmostEqual(result, 34.41944, 3)

    # def test_dms_to_dec_pos2(self):
    #     result = gps.convert.dms_to_dec(34, 61.3, 0, 'N')
    #     self.assertAlmostEqual(result, 35.01667, 3)
    #
    # def test_dms_to_dec_neg(self):
    #     result = gps.convert.dms_to_dec(-77, 50, 30, 'E')
    #     self.assertAlmostEqual(result, -77.84167)
    #
    # def test_dms_to_dec_wrap(self):
    #     self.assertTrue(True)
