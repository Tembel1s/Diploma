import json
import logging

import allure
from allure_commons.types import AttachmentType
from requests import Response


def response_attaching_html(response: Response):
    allure.attach(
        body=response.request.url,
        name="request url",
        attachment_type=AttachmentType.TEXT,
        extension=".txt",
    )

    allure.attach(
        body=response.text,
        name="response text",
        attachment_type=AttachmentType.TEXT,
        extension=".txt",
    )

    allure.attach(
        body=str(response.status_code),
        name="response status code",
        attachment_type=AttachmentType.TEXT,
        extension=".txt",
    )

    allure.attach(
        body=str(response.cookies),
        name="response cookies",
        attachment_type=AttachmentType.TEXT,
        extension=".txt",
    )

    if response.request.body:
        allure.attach(
            body=json.dumps(str(response.request.body)),
            name="request body",
            attachment_type=AttachmentType.JSON,
            extension=".json",
        )


def response_attaching_json(response: Response):
    allure.attach(
        body=json.dumps(response.json(), indent=4, ensure_ascii=True),
        name="response body",
        attachment_type=AttachmentType.JSON,
        extension=".json",
    )

    allure.attach(
        body=str(response.status_code),
        name="response status code",
        attachment_type=AttachmentType.TEXT,
        extension=".txt",
    )

    allure.attach(
        body=str(response.cookies),
        name="response cookies",
        attachment_type=AttachmentType.TEXT,
        extension=".txt",
    )


def response_logging(response: Response):
    logging.info("Request: " + response.request.url)
    logging.info("Response code " + str(response.status_code))
    logging.info("Response text: " + response.text)
