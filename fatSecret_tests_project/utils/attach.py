import os

import allure
import requests
from allure_commons.types import AttachmentType
from selene import browser


def add_screenshot():
    png = browser.driver.get_screenshot_as_png()
    allure.attach(
        body=png, name="Screenshot", attachment_type=allure.attachment_type.PNG
    )


def add_video(session_id):
    browserstack_session = requests.get(
        url=f"https://api.browserstack.com/app-automate/sessions/{session_id}.json",
        auth=(os.getenv("USER_NAME"), os.getenv("ACCESS_KEY")),
    ).json()
    video_url = browserstack_session["automation_session"]["video_url"]

    allure.attach(
        "<html><body>"
        '<video width="100%" height="100%" controls autoplay>'
        f'<source src="{video_url}" type="video/mp4">'
        "</video>"
        "</body></html>",
        name="video recording",
        attachment_type=allure.attachment_type.HTML,
    )

def add_video_web():
    selenoid_url = os.getenv("SELENOID_URL")
    video_url = f"https://{selenoid_url}/video/{browser.driver.session_id}.mp4"
    html = (
        f"<html><body>"
        f"<video width='100%' height='100%' controls autoplay>"
        f"<source src='{video_url}' type='video/mp4'>"
        f"</video></body></html>"
    )
    allure.attach(html, "video_url" + browser.driver.session_id, AttachmentType.HTML, '.html')


def add_logs():
    log = "".join(f"{text}\n" for text in browser.driver.get_log(log_type="browser"))
    allure.attach(log, "browser_logs", AttachmentType.TEXT, ".log")

