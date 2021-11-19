from unittest import TestCase
import gps.convert
import gps.calculate


class TestConvert_km(TestCase):

    def test_m_to_km(self):
        distance = 2.5
        unit = gps.convert.Unit.METERS
        answer = 0.0025
        result = gps.convert.km(distance, unit)
        self.assertAlmostEqual(result, answer, 5)

    def test_nmi_to_km(self):
        distance = 77.7
        unit = gps.convert.Unit.NAUTICAL_MILES
        answer = 143.9004
        result = gps.convert.km(distance, unit)
        self.assertAlmostEqual(result, answer, 5)

    def test_mi_to_km(self):
        distance = 32.666
        unit = gps.convert.Unit.MILES
        answer = 52.570831104
        result = gps.convert.km(distance, unit)
        self.assertAlmostEqual(result, answer, 5)

    def test_ft_to_km(self):
        distance = 10.5
        unit = gps.convert.Unit.FEET
        answer = 0.0032004
        result = gps.convert.km(distance, unit)
        self.assertAlmostEqual(result, answer, 5)


class TestConvert_m(TestCase):

    def test_km_to_m(self):
        distance = 5.5
        unit = gps.convert.Unit.KILOMETERS
        answer = 5500
        result = gps.convert.m(distance, unit)
        self.assertAlmostEqual(result, answer, 5)

    def test_mi_to_m(self):
        distance = 101
        unit = gps.convert.Unit.MILES
        answer = 162543.744
        result = gps.convert.m(distance, unit)
        self.assertAlmostEqual(result, answer, 5)

    def test_nmi_to_m(self):
        distance = 70.3
        unit = gps.convert.Unit.NAUTICAL_MILES
        answer = 130195.6
        result = gps.convert.m(distance, unit)
        self.assertAlmostEqual(result, answer, 5)

    def test_ft_to_m(self):
        distance = 32.5
        unit = gps.convert.Unit.FEET
        answer = 9.906
        result = gps.convert.m(distance, unit)
        self.assertAlmostEqual(result, answer, 5)


class TestConvert_ft(TestCase):

    def test_km_to_ft(self):
        distance = 5.5
        unit = gps.convert.Unit.KILOMETERS
        answer = 18044.619422572
        result = gps.convert.ft(distance, unit)
        self.assertAlmostEqual(result, answer, 5)

    def test_mi_to_ft(self):
        distance = 101
        unit = gps.convert.Unit.MILES
        answer = 533280
        result = gps.convert.ft(distance, unit)
        self.assertAlmostEqual(result, answer, 5)

    def test_nmi_to_ft(self):
        distance = 70.3
        unit = gps.convert.Unit.NAUTICAL_MILES
        answer = 427150.91863517
        result = gps.convert.ft(distance, unit)
        self.assertAlmostEqual(result, answer, 5)

    def test_m_to_ft(self):
        distance = 32.5
        unit = gps.convert.Unit.METERS
        answer = 106.627296588
        result = gps.convert.ft(distance, unit)
        self.assertAlmostEqual(result, answer, 5)


class TestConvert_nmi(TestCase):

    def test_km_to_nmi(self):
        distance = 5.5
        unit = gps.convert.Unit.KILOMETERS
        answer = 2.969762419
        result = gps.convert.nmi(distance, unit)
        self.assertAlmostEqual(result, answer, 5)

    def test_mi_to_nmi(self):
        distance = 101
        unit = gps.convert.Unit.MILES
        answer = 87.766775966
        result = gps.convert.nmi(distance, unit)
        self.assertAlmostEqual(result, answer, 5)

    def test_ft_to_nmi(self):
        distance = 70.3
        unit = gps.convert.Unit.FEET
        answer = 0.011569892
        result = gps.convert.nmi(distance, unit)
        self.assertAlmostEqual(result, answer, 5)

    def test_m_to_nmi(self):
        distance = 32.5
        unit = gps.convert.Unit.METERS
        answer = 0.017548596
        result = gps.convert.nmi(distance, unit)
        self.assertAlmostEqual(result, answer, 5)


class TestConvert_mi(TestCase):

    def test_km_to_mi(self):
        distance = 5.5
        unit = gps.convert.Unit.KILOMETERS
        answer = 3.417534722
        result = gps.convert.mi(distance, unit)
        self.assertAlmostEqual(result, answer, 5)

    def test_nmi_to_mi(self):
        distance = 101
        unit = gps.convert.Unit.NAUTICAL_MILES
        answer = 116.228491793
        result = gps.convert.mi(distance, unit)
        self.assertAlmostEqual(result, answer, 5)

    def test_ft_to_mi(self):
        distance = 70.3
        unit = gps.convert.Unit.FEET
        answer = 0.013314367
        result = gps.convert.mi(distance, unit)
        self.assertAlmostEqual(result, answer, 5)

    def test_m_to_mi(self):
        distance = 32.5
        unit = gps.convert.Unit.METERS
        answer = 0.020194523
        result = gps.convert.mi(distance, unit)
        self.assertAlmostEqual(result, answer, 5)


class TestConvert_dms_correct(TestCase):

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


class TestConvert_dec_to_longitude(TestCase):

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


class TestConvert_dec_to_latitude(TestCase):

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


class TestConvert_dms_to_dec(TestCase):

    def test_dms_to_dec_pos1(self):
        result = gps.convert.dms_to_dec(34, 25, 10, 'N')
        self.assertAlmostEqual(result, 34.41944, 3)

    def test_dms_to_dec_pos2(self):
        result = gps.convert.dms_to_dec(34, 61.3, 0, 'N')
        self.assertAlmostEqual(result, 35.01667, 3)

    # def test_dms_to_dec_neg(self):
    #     result = gps.convert.dms_to_dec(-77, 50, 30, 'E')
    #     self.assertAlmostEqual(result, -77.84167)
    #
    # def test_dms_to_dec_wrap(self):
    #     self.assertTrue(True)


class TestCalculate(TestCase):

    def test_distance_equator1(self):
        result = gps.calculate.distance(0, 0, 0, 45.0)
        self.assertAlmostEqual(5004.0, result, 1)
        # self.assertTrue(True)

    def test_distance_equator2(self):
        result = gps.calculate.distance(0, 0, 0, 90)
        self.assertAlmostEqual(10000.1, result, 3)
        # self.assertTrue(True)
    #
    # def test_distance_PN2PP_boundary(self):
    #     result = gps.calculate.distance(10, -45, 45, 10)
    #     #self.asertAlmostEqual(6503, result, 3)
    #     self.assertTrue(True)
    #
    # def test_distance_PP2PN_boundary(self):
    #     result = gps.calculate.distance(10, 179, 45, -10)
    #     #self.asertAlmostEqual(13824, result, 3)
    #     self.assertTrue(True)
