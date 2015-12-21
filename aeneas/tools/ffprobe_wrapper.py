#!/usr/bin/env python
# coding=utf-8

"""
Read audio file properties using the ``ffprobe`` wrapper.
"""

from __future__ import absolute_import
from __future__ import print_function
import sys

from aeneas.ffprobewrapper import FFPROBEParsingError
from aeneas.ffprobewrapper import FFPROBEUnsupportedFormatError
from aeneas.ffprobewrapper import FFPROBEWrapper
from aeneas.tools.abstract_cli_program import AbstractCLIProgram
import aeneas.globalfunctions as gf

__author__ = "Alberto Pettarin"
__copyright__ = """
    Copyright 2012-2013, Alberto Pettarin (www.albertopettarin.it)
    Copyright 2013-2015, ReadBeyond Srl   (www.readbeyond.it)
    Copyright 2015-2016, Alberto Pettarin (www.albertopettarin.it)
    """
__license__ = "GNU AGPL 3"
__version__ = "1.4.0"
__email__ = "aeneas@readbeyond.it"
__status__ = "Production"

class FFPROBEWrapperCLI(AbstractCLIProgram):
    """
    Read audio file properties using the ``ffprobe`` wrapper.
    """
    AUDIO_FILE = gf.get_rel_path("res/audio.mp3")

    NAME = gf.file_name_without_extension(__file__)

    HELP = {
        "description": u"Read audio file properties using the ffprobe wrapper.",
        "synopsis": [
            u"AUDIO_FILE"
        ],
        "examples": [
            u"%s" % (AUDIO_FILE)
        ]
    }

    def perform_command(self):
        """
        Perform command and return the appropriate exit code.

        :rtype: int
        """
        if len(self.actual_arguments) < 1:
            return self.print_help()
        audio_file_path = self.actual_arguments[0]

        if not self.check_input_file(audio_file_path):
            return self.ERROR_EXIT_CODE

        try:
            prober = FFPROBEWrapper(logger=self.logger)
            dictionary = prober.read_properties(audio_file_path)
            for key in sorted(dictionary.keys()):
                self.print_generic("%s %s" % (key, dictionary[key]))
            return self.NO_ERROR_EXIT_CODE
        except (FFPROBEUnsupportedFormatError, FFPROBEParsingError):
            self.print_error("Cannot read properties of file '%s'" % (audio_file_path))
            self.print_error("Make sure the input file has a format supported by ffprobe")

        return self.ERROR_EXIT_CODE



def main():
    """
    Execute program.
    """
    FFPROBEWrapperCLI().run(arguments=sys.argv)

if __name__ == '__main__':
    main()



