#!/usr/bin/env python
# coding=utf-8

import unittest

from aeneas.logger import Logger

class TestLogger(unittest.TestCase):

    def test_log(self):
        logger = Logger(tee=False, indentation=4)
        logger.log(u"Message 1", Logger.DEBUG)
        logger.log(u"Message 2", Logger.INFO)
        logger.log(u"Message 3", Logger.WARNING)
        logger.log(u"Message 4", Logger.CRITICAL)
        self.assertEqual(len(logger), 4)

    def test_clear(self):
        logger = Logger(tee=False, indentation=4)
        logger.log(u"Message 1", Logger.DEBUG)
        logger.log(u"Message 2", Logger.INFO)
        logger.log(u"Message 3", Logger.WARNING)
        logger.log(u"Message 4", Logger.CRITICAL)
        self.assertEqual(len(logger), 4)
        logger.clear()
        self.assertEqual(len(logger), 0)

    def test_change_indentation(self):
        logger = Logger(tee=False, indentation=4)
        self.assertEqual(logger.indentation, 4)
        logger.log(u"Message 1", Logger.DEBUG)
        logger.log(u"Message 2", Logger.INFO)
        logger.indentation = 2
        self.assertEqual(logger.indentation, 2)
        logger.log(u"Message 3", Logger.WARNING)
        logger.log(u"Message 4", Logger.CRITICAL)
        logger.indentation = 0
        self.assertEqual(logger.indentation, 0)

    def test_tag(self):
        logger = Logger(tee=False, indentation=4)
        logger.log(u"Message 1", Logger.DEBUG, tag=u"TEST")
        logger.log(u"Message 2", Logger.DEBUG)
        logger.log(u"Message 3", Logger.DEBUG, tag=u"TEST")
        logger.log(u"Message 4", Logger.DEBUG)
        strings = logger.pretty_print(as_list=True)
        self.assertEqual(strings[0].find(u"TEST") > -1, True)
        self.assertEqual(strings[1].find(u"TEST") > -1, False)
        self.assertEqual(strings[2].find(u"TEST") > -1, True)
        self.assertEqual(strings[3].find(u"TEST") > -1, False)

    def run_test_multi(self, msg):
        logger = Logger(tee=False)
        logger.log(msg)
        self.assertEqual(len(logger), 1)

    def test_bytes(self):
        with self.assertRaises(TypeError):
            self.run_test_multi(b"These are bytes")

    def test_multi_01(self):
        self.run_test_multi(u"Message ascii")

    def test_multi_02(self):
        self.run_test_multi(u"Message with unicode chars: à and '…'")

    def test_multi_03(self):
        self.run_test_multi([u"Message ascii"])

    def test_multi_04(self):
        self.run_test_multi([u"Message with unicode chars: à and '…'"])

    def test_multi_05(self):
        self.run_test_multi([u"Message %s", u"1"])

    def test_multi_06(self):
        self.run_test_multi([u"Message %d", 1])

    def test_multi_07(self):
        self.run_test_multi([u"Message %.3f", 1.234])

    def test_multi_08(self):
        self.run_test_multi([u"Message %.3f %.3f", 1.234, 2.345])

    def test_multi_09(self):
        self.run_test_multi([u"Message with unicode chars: à and '…' and %s", u"ascii"])

    def test_multi_10(self):
        self.run_test_multi(u"unicode but only with ascii chars")

    def test_multi_11(self):
        self.run_test_multi(u"unicode with non-ascii chars: à and '…'")

    def test_multi_12(self):
        self.run_test_multi([u"Message with unicode chars: %s and '…' and ascii", u"àbc"])

    def test_multi_13(self):
        self.run_test_multi([u"Message with unicode chars: %s and '…' and ascii", u"àbc"])

    def test_multi_14(self):
        self.run_test_multi([u"Message %.3f %s %.3f", 1.234, "--->", 2.345])

    def test_multi_15(self):
        self.run_test_multi([u"Message %.3f %s %.3f", 1.234, u"-à->", 2.345])


if __name__ == '__main__':
    unittest.main()



