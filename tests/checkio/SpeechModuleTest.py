'''
Created on Nov 28, 2015

@author: francisparan
'''
import unittest

import checkio.speech_module


class Test(unittest.TestCase):


    def check_against_number_range(self, func, number_range, expected_values):
        for expected, value in zip(expected_values, number_range):
            self.assertEquals(expected, func(value))

    def test_parse_first_ten(self):
        self.assertEqual('four', checkio.speech_module.checkio(4))
    
        self.check_against_number_range(
                                        checkio.speech_module.parse_first_ten,
                                        range(1,10), checkio.speech_module.FIRST_TEN)
            
            
    def test_parse_second_ten(self):
        self.assertEquals("nineteen", checkio.speech_module.parse_second_ten(19))
        self.assertEquals('twelve', checkio.speech_module.parse_second_ten(12))
        
        self.check_against_number_range(
                                        checkio.speech_module.parse_second_ten,
                                        range(10,20), checkio.speech_module.SECOND_TEN)
        
        
    def test_parse_other_tens(self):
        self.assertEquals("twenty nine", checkio.speech_module.parse_other_tens(29))
        self.assertEquals('thirty five', checkio.speech_module.parse_other_tens(35))
        self.assertEquals('twenty three', checkio.speech_module.parse_other_tens(23))
        self.assertEquals('ninety nine', checkio.speech_module.parse_other_tens(99))
        
        
    assert checkio.speech_module.checkio(12) == 'twelve', "3rd example"
    assert checkio.speech_module.checkio(101) == 'one hundred one', "4th example"
    assert checkio.speech_module.checkio(212) == 'two hundred twelve', "5th example"
    assert checkio.speech_module.checkio(40) == 'forty', "6th example"
    assert not checkio.speech_module.checkio(212).endswith(' '), "Don't forget strip whitespaces at the end of string"
