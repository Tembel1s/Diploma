import os
from appium.options.android import UiAutomator2Options
from utils import file_path


def to_driver_options(context):
    options = UiAutomator2Options()

    if context == 'local_emulator':
        options.set_capability('remote_url', os.getenv('REMOTE_URL'))
        options.set_capability('deviceName', os.getenv('DEVICE_NAME'))
        options.set_capability('appWaitActivity', os.getenv('APP_WAIT_ACTIVITY'))
        options.set_capability('app', file_path.relative_path(os.getenv('APP')))

    if context == 'local_real_device':
        options.set_capability('remote_url', os.getenv('REMOTE_URL'))
        options.set_capability('deviceName', os.getenv('DEVICE_NAME'))
        options.set_capability('appWaitActivity', os.getenv('APP_WAIT_ACTIVITY'))
        options.set_capability('app', file_path.relative_path(os.getenv('APP')))

    if context == 'bstack':
        options.set_capability('remote_url', os.getenv('REMOTE_URL'))
        options.set_capability('deviceName', os.getenv('DEVICE_NAME'))
        options.set_capability('platformName', os.getenv('PLATFORM_NAME'))
        options.set_capability('platformVersion', os.getenv('PLATFORM_VERSION'))
        options.set_capability('appWaitActivity', os.getenv('APP_WAIT_ACTIVITY'))
        options.set_capability('app', os.getenv('APP'))
        options.set_capability(
            'bstack:options', {
                'projectName': 'Fatsecret project',
                'buildName': 'browserstack-build-1',
                'sessionName': 'BStack test',
                'userName': os.getenv('BROWSERSTACK_USER_NAME'),
                'accessKey': os.getenv('BROWSERSTACK_ACCESS_KEY'),
            },
        )

    return options
