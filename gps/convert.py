from enum import Enum


class Unit(Enum):

    FEET = 'ft'
    KILOMETERS = 'km'
    METERS = 'm'
    MILES = 'mi'
    NAUTICAL_MILES = 'nmi'


def km(distance, unit):
    """
    Coverts the specified distance of a particular unit of measurement into
    kilometers

    Args:
        distance (float):  distance
        unit (Unit): units specified by the Enum Unit

    Returns:
        float: distance in kilometers
    """

    scalar = {
        Unit.KILOMETERS:       1.0,
        Unit.METERS:           0.001,
        Unit.MILES:            1.609344,
        Unit.NAUTICAL_MILES:   1.852,
        Unit.FEET:             0.0003048,
    }

    return distance * scalar[unit]


def m(distance, unit):

    scalar = {
        Unit.KILOMETERS:       1000,
        Unit.METERS:           1.0,
        Unit.MILES:            1609.344,
        Unit.NAUTICAL_MILES:   1852,
        Unit.FEET:             0.3048,
    }

    return distance * scalar[unit]


def ft(distance, unit):

    scalar = {
        Unit.KILOMETERS:       3280.839895013,
        Unit.METERS:           3.280839895,
        Unit.MILES:            5280,
        Unit.NAUTICAL_MILES:   6076.115485564,
        Unit.FEET:             1.0,
    }

    return distance * scalar[unit]


def nmi(distance, unit):

    scalar = {
        Unit.KILOMETERS:       0.539956803,
        Unit.METERS:           0.000539957,
        Unit.MILES:            0.86897798,
        Unit.NAUTICAL_MILES:   1.0,
        Unit.FEET:             0.000164579
    }

    return distance * scalar[unit]


def mi(distance, unit):

    scalar = {
        Unit.KILOMETERS:       0.621369949,
        Unit.METERS:           0.00062137,
        Unit.MILES:            1.0,
        Unit.NAUTICAL_MILES:   1.150777146,
        Unit.FEET:             0.000189394,
    }

    return distance * scalar[unit]


def dec_to_dms(decimal):
    """
    Takes any decimal number and converts it to degrees, minutes, seconds,
    direction.

    Args:
        decimal (float): a number representing half of a GPS Coordinate

    Returns:
        tuple: (degrees (int), minutes (int), seconds (int), N/S/E/W (str))
    """
    pass


def dms_to_dec(degrees, minutes, seconds, direction):
    """
    Calculates degrees, minutes, seconds to a decimal number with the
    direction determinining if it is positive or negagive.

    Degrees will not be corrected if it is greater than 90/180.  Use
    dec_to_longitude or dec_to_latitude to correct for this

    Args:
        degrees (int): degrees, truncated if decimal
        minutes (int): minutes, truncated if decimal
        seconds (int): seconds, truncated if decimal
        direction (str): N|W|S|E

    Returns:
        float

    """
    sign = 1
    if direction.casefold()[0] in ['w', 's']:
        sign = -1

    degrees, minutes, seconds = dms_correct(
        degrees, minutes, seconds, direction)

    decimal = sign * (degrees + minutes/60 + seconds/3600)
    return decimal


def dms_correct(degrees, minutes, seconds, direction):
    """
    Will correct degrees, minutes, seconds for rollover.  It will not
    return a direction, but rather a positive or negative number.

    Degrees will be corrected to a positive number
    If seconds is greater than 60 it rolls over into minutes.
    If minutes is greater than 60, it rolls over into degrees.

    Degrees will not be corrected if it is greater than 90/180.  Use
    dec_to_longitude or dec_to_latitude to correct for this

    Args:
        degrees (int): degrees, truncated if decimal
        minutes (int): Minutes, truncated if decimal
        seconds (int): Seconds, truncated if decimal

    Returns:
        tuple: (degrees(int), minutes (int), seconds (int))
    """

    direction = direction.upper()[:1]

    sign = 1
    if direction in ['W', 'S']:
        sign = -1

    if degrees < 0:
        sign = -1

    degrees = abs(degrees)
    minutes = abs(minutes)
    seconds = abs(seconds)

    corrected_seconds = int(seconds % 60)
    minutes = minutes + int(seconds/60)

    corrected_minutes = int(minutes % 60)
    degrees = degrees + int(minutes/60)

    corrected_degrees = sign * int(degrees)

    return corrected_degrees, corrected_minutes, corrected_seconds


def dec_to_longitude(decimal):
    """
    Converts a decimal number into a longitudinal number ranging from -90
    to 90

    Args:
        decimal (float): degrees represented by a decimal

    Returns:
        float: between -90 and 90
    """
    sign = 1
    if decimal < 0:
        sign = -1

    half = int(decimal/180*sign) % 2

    if half == 0:
        longitude = 0 + (decimal % (sign*180))
    elif half == 1:
        longitude = -180*sign + (decimal % (sign*180))

    return longitude


def dec_to_latitude(decimal):
    """
    Converts a decimal number into a latitudinal number ranging from -180
    to 180

    Args:
        decimal (float): degrees represented by a decimal

    Returns:
        float: between -180 and 180
    """

    sign = 1
    if decimal < 0:
        sign = -1

    quadrant = int(decimal/90*sign) % 4
    decimal_mod = decimal % (sign*180)

    if quadrant == 0:
        latitude = 0 + decimal_mod
    elif quadrant == 1:
        latitude = sign*(180) - decimal_mod
    elif quadrant == 2:
        latitude = 0 - decimal_mod
    elif quadrant == 3:
        latitude = sign*(-180) + decimal_mod

    return latitude
