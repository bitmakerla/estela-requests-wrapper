
# Generated by CodiumAI

import pytest
from unittest.mock import Mock

import logging
from estela_requests.log_helpers import init_logging
from estela_requests.estela_hub import EstelaHub
from estela_queue_adapter.abc_producer import ProducerInterface
from estela_requests.log_helpers.handlers import KafkaLogHandler

"""
Code Analysis

Objective:
The objective of the 'init_logging' function is to initialize the logging configuration for the application. It sets the logging level, adds handlers, and formats the log messages. The function also provides the option to use a KafkaLogHandler for logging to a Kafka topic.

Inputs:
- estela_hub: an object containing the log level, producer, job ID, and job logs topic.
- hdlr_flag: a string indicating the type of logging handler to use ('kafka' or 'stream').
- level: the logging level to set for the root logger.
- noisy_log_libraries: a list of noisy log libraries to exclude from logging.

Flow:
1. Set the logging level for the root logger to the specified level.
2. Add a NullHandler to all noisy log libraries to exclude them from logging.
3. If hdlr_flag is 'kafka', create a KafkaLogHandler using the estela_hub object.
4. If hdlr_flag is not 'kafka', create a StreamHandler.
5. Set the logging level for the handler to the specified level.
6. Set the formatter for the handler.
7. Add the handler to the root logger.

Outputs:
- None

Additional aspects:
- The function uses the 'queue_noisy_libraries' list from the 'estela_queue_adapter' module to exclude additional noisy log libraries.
- The function uses the 'KafkaLogHandler' class from the 'estela_requests.log_helpers.handlers' module to create a Kafka logging handler.
- The function sets the logging format to include the timestamp, logger name, log level, and log message.
"""
class TestLoggingHelpers:
    # Tests that the root logger is set to DEBUG level
    def test_root_logger_level(self):
        estela_hub = Mock(spec=EstelaHub)
        producer_mock = Mock(spec=ProducerInterface)
        estela_hub.log_level = logging.DEBUG
        estela_hub.producer = producer_mock
        estela_hub.job = "123"
        estela_hub.job_logs_topic = "logs"
        hdlr_flag = 'kafka'
        level = logging.DEBUG
        noisy_log_libraries = []
        init_logging(estela_hub, hdlr_flag, level, noisy_log_libraries)
        assert logging.getLogger('').getEffectiveLevel() == logging.DEBUG

    # Tests that a KafkaLogHandler is created if hdlr_flag is 'kafka'
    def test_kafka_handler_created(self):
        estela_hub = Mock(spec=EstelaHub)
        producer_mock = Mock(spec=ProducerInterface)
        estela_hub.log_level = logging.DEBUG
        estela_hub.producer = producer_mock
        estela_hub.job = "123"
        estela_hub.job_logs_topic = "logs"
        hdlr_flag = 'kafka'
        level = logging.DEBUG
        noisy_log_libraries = []
        init_logging(estela_hub, hdlr_flag, level, noisy_log_libraries)
        assert any(isinstance(handler, KafkaLogHandler) for handler in logging.getLogger('').handlers)
