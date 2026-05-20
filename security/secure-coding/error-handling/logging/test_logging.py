import logging
import pytest

LOG = logging.getLogger(__name__)


def test_debug(caplog):
    with caplog.at_level(logging.DEBUG):
        LOG.debug('This is a debug message')
    assert 'This is a debug message' in caplog.text
    assert caplog.records[0].levelno == logging.DEBUG


def test_info(caplog):
    with caplog.at_level(logging.INFO):
        LOG.info('This is an info message')
    assert 'This is an info message' in caplog.text
    assert caplog.records[0].levelno == logging.INFO


def test_warning(caplog):
    with caplog.at_level(logging.WARNING):
        LOG.warning('This is a warning message')
    assert 'This is a warning message' in caplog.text
    assert caplog.records[0].levelno == logging.WARNING


def test_error(caplog):
    with caplog.at_level(logging.ERROR):
        LOG.error('This is an error message')
    assert 'This is an error message' in caplog.text
    assert caplog.records[0].levelno == logging.ERROR


def test_critical(caplog):
    with caplog.at_level(logging.CRITICAL):
        LOG.critical('This is a critical message')
    assert 'This is a critical message' in caplog.text
    assert caplog.records[0].levelno == logging.CRITICAL


def test_warning_suppresses_debug_and_info(caplog):
    with caplog.at_level(logging.WARNING):
        LOG.debug('debug - should be suppressed')
        LOG.info('info - should be suppressed')
        LOG.warning('warning - should appear')
    assert 'debug - should be suppressed' not in caplog.text
    assert 'info - should be suppressed' not in caplog.text
    assert 'warning - should appear' in caplog.text

