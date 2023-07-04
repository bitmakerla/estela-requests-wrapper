# Generated by CodiumAI
from unittest.mock import Mock
import typeguard

from estela_requests.estela_hub import EstelaHub
from estela_queue_adapter.abc_producer import ProducerInterface
from estela_requests.request_interfaces import HttpRequestInterface
from estela_requests.middlewares.interface import EstelaMiddlewareInterface
from estela_requests.middlewares.spider_status import SpiderStatusMiddleware
from estela_requests.item_pipeline import ItemPipelineInterface
from estela_requests.item_pipeline.exporter import ItemExporterInterface
import logging


import pytest

"""
Code Analysis

Main functionalities:
The EstelaHub class is responsible for containing all the necessary information to communicate with Estela, including the queue platform and the API. It initializes with various parameters such as producer, API host, job, HTTP client, middlewares, job stats topic, job requests topic, job items topic, job logs topic, auth token, item pipelines, item exporters, log level, log flag, and log libraries. It also provides a method to create an instance of the class from settings.

Methods:
- __init__(): Initializes the EstelaHub class with various parameters.
- __repr__(): Returns a string representation of the EstelaHub object.
- cleanup_resources(): Cleans up resources.
- create_from_settings(): Creates an instance of the EstelaHub class from settings.

Fields:
- producer: An instance of the ProducerInterface class.
- api_host: A string representing the API host.
- job: A string representing the job.
- http_client: An instance of the HttpRequestInterface class.
- args: A string representing the spider arguments.
- middlewares: A list of EstelaMiddlewareInterface objects.
- job_stats_topic: A string representing the job stats topic.
- job_requests_topic: A string representing the job requests topic.
- job_items_topic: A string representing the job items topic.
- job_logs_topic: A string representing the job logs topic.
- auth_token: A string representing the authentication token.
- stats: A dictionary representing the statistics.
- item_pipelines: A list of ItemPipelineInterface objects.
- item_exporters: An instance of the ItemExporterInterface class.
- log_level: An integer representing the log level.
- log_flag: A logging.Handler object.
- log_libraries: A list of strings representing the noisy log libraries.
"""
class TestEstelaHub:
    # Tests that an instance of EstelaHub can be created with all required parameters
    def test_create_instance_with_all_parameters(self):
        middleware_mock = Mock(spec=SpiderStatusMiddleware)
        producer_mock = Mock(spec=ProducerInterface)
        estela_hub = EstelaHub(
            producer=producer_mock,
            api_host='api_host',
            job='job',
            http_client=HttpRequestInterface(),
            args='args',
            middlewares=[middleware_mock],
            job_stats_topic='job_stats_topic',
            job_requests_topic='job_requests_topic',
            job_items_topic='job_items_topic',
            job_logs_topic='job_logs_topic',
            auth_token='auth_token',
            item_pipelines=[ItemPipelineInterface()],
            item_exporters=ItemExporterInterface(),
            log_level=logging.DEBUG,
            log_flag=logging.StreamHandler(),
            log_libraries=['log_libraries'],
        )
        assert isinstance(estela_hub, EstelaHub)


    def test_create_instance_with_invalid_types(self):
        middleware_mock = Mock(spec=SpiderStatusMiddleware)
        with pytest.raises(typeguard.TypeCheckError):
            estela_hub = EstelaHub(
                producer="invalid_type",
                api_host='api_host',
                job='job',
                http_client=HttpRequestInterface(),
                args='args',
                middlewares=[middleware_mock],
                job_stats_topic='job_stats_topic',
                job_requests_topic='job_requests_topic',
                job_items_topic='job_items_topic',
                job_logs_topic='job_logs_topic',
                auth_token='auth_token',
                item_pipelines=[ItemPipelineInterface()],
                item_exporters=ItemExporterInterface(),
                log_level=logging.DEBUG,
                log_flag=logging.StreamHandler(),
                log_libraries=['log_libraries'],
            )


    def test_cleanup_methods(self):
        middleware_mock = Mock(spec=SpiderStatusMiddleware)
        producer_mock = Mock(spec=ProducerInterface)
        estela_hub = EstelaHub(
            producer=producer_mock,
            api_host='api_host',
            job='job',
            http_client=HttpRequestInterface(),
            args='args',
            middlewares=[middleware_mock],
            job_stats_topic='job_stats_topic',
            job_requests_topic='job_requests_topic',
            job_items_topic='job_items_topic',
            job_logs_topic='job_logs_topic',
            auth_token='auth_token',
            item_pipelines=[ItemPipelineInterface()],
            item_exporters=ItemExporterInterface(),
            log_level=logging.DEBUG,
            log_flag=logging.StreamHandler(),
            log_libraries=['log_libraries'],
        )
        estela_hub.cleanup_resources()
        producer_mock.flush.assert_called_once()
        producer_mock.close.assert_called_once()
        assert isinstance(estela_hub, EstelaHub)
