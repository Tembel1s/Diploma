import os

from appium.options.android import UiAutomator2Options

import utils
import utils.file

remote_url = os.getenv('remote_url', 'http://127.0.0.1:4723')
deviceName = os.getenv('deviceName', 'emulator-5554')
appWaitActivity = os.getenv('appWaitActivity', 'org.wikipedia.*')
app = os.getenv('app', './app-alpha-universal-release.apk')
runs_on_bstack = app.startswith('bs://')
if runs_on_bstack:
    remote_url = 'http://hub.browserstack.com/wd/hub'

def to_driver_options():
    options = UiAutomator2Options()

    if deviceName:
        options.set_capability('deviceName', deviceName)

    if appWaitActivity:
        options.set_capability('appWaitActivity', appWaitActivity)

    options.set_capability('app', (
        app if (app.startswith('/') or runs_on_bstack)
        else utils.file.abs_path_from_project(app)
    ))

    if runs_on_bstack:
        options.set_capability(
            'bstack:options', {
                "projectName": "First Python project",
                "buildName": "browserstack-build-1",
                "sessionName": "BStack first_test",

                "userName": os.getenv("USER_NAME"),
                "accessKey": os.getenv("ACCESS_KEY"),
            },
        )

    return options