"""Test the clean_logger.py"""
import os
import sys
import tempfile

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../../../')))

from Moby_Land.custom_logging.clean_logger import get_clean_logger

class Test_Logger:
    def test_get_clean_logger(self):

        # Set up a tempdir for logging
        with tempfile.TemporaryDirectory() as temp_dir:

            # Get logger
            log_filepath = os.path.join(temp_dir, 'test.log')
            log = get_clean_logger(logger_name='testy_loggy', log_filename=log_filepath)

            # Write some stuff
            log.info('testttyyyyy info')
            log.warning('testttyyyyy warning')
            log.error('testttyyyyy error')
            log.debug('testttyyyyy debug')

            # Get content from the logfile
            with open(log_filepath, 'r') as f:
                log_content = f.read()

        # Check that logfile contents are accurate
        expected_lines = [' - testy_loggy - INFO - testttyyyyy info',
                         ' - testy_loggy - WARNING - testttyyyyy warning',
                         ' - testy_loggy - ERROR - testttyyyyy error',
                         ' - testy_loggy - DEBUG - testttyyyyy debug']
        for line, ex_line in zip(log_content.split('\n'), expected_lines):
            assert line[23:] == ex_line  # assert everything but the date is accurate
