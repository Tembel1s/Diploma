import allure
from allure_commons.types import Severity
from appium.webdriver.common.appiumby import AppiumBy

from fatsecret_tests_project.pages.mobile.mobile_page import pages, user_flow


@allure.tag("Mobile")
@allure.feature("Android tests")
@allure.story("Login")
@allure.title("Captcha")
@allure.severity(Severity.CRITICAL)
def test_capcha():
    with allure.step("Check user is on the welcome page"):
        user_flow.check_if_user_directed_to_page(
            (
                AppiumBy.ID,
                "com.fatsecret.android:id/registration_lets_begin_text_solid",
            ),
            "I am a new user",
        )
        with allure.step('Click "I already have an account" button'):
            user_flow.click(
                (AppiumBy.ID, "com.fatsecret.android:id/registration_sign_in_outline")
            )
            with allure.step("Choose sign in with e-mail or member name option"):
                user_flow.choose_option(
                    (AppiumBy.ID, "com.fatsecret.android:id/sign_in_sign_up_with_email")
                )
                with allure.step("Fill Member Name"):
                    user_flow.click(
                        "//*[@resource-id='com.fatsecret.android:id/sign_in_email_member_name_input']//*[@resource-id='com.fatsecret.android:id/input_row']//*[@resource-id='com.fatsecret.android:id/edit_text']"
                    )
                    user_flow.send_keys(
                        "//*[@resource-id='com.fatsecret.android:id/sign_in_email_member_name_input']//*[@resource-id='com.fatsecret.android:id/input_row']//*[@resource-id='com.fatsecret.android:id/edit_text']",
                        "login",
                    )
                    with allure.step("Fill password"):
                        user_flow.send_keys(
                            "//*[@resource-id='com.fatsecret.android:id/sign_in_password_input']//*[@resource-id='com.fatsecret.android:id/input_row']//*[@resource-id='com.fatsecret.android:id/edit_text']",
                            "password",
                        )
                        with allure.step("Click Sign In"):
                            user_flow.click(
                                (
                                    AppiumBy.ID,
                                    "com.fatsecret.android:id/sign_in_sign_in_button",
                                )
                            )
                            with allure.step("Check captcha is appeared"):
                                user_flow.check_pop_up(
                                    (
                                        AppiumBy.XPATH,
                                        '//android.widget.TextView[@text="Quick Verification"]',
                                    )
                                )


@allure.tag("Mobile")
@allure.feature("Android tests")
@allure.story("Login")
@allure.title("Guest login")
@allure.severity(Severity.CRITICAL)
def test_guest_login():
    (
        pages.check_main_page()
        .check_data_collect_agreement_page()
        .check_fill_first_name_page()
        .check_setting_up_your_profile_page()
        .check_setting_your_goal_page()
        .check_weight_loss_goal_setting_page()
        .check_gender_choosing_page()
        .check_activity_level_choosing_page()
        .check_fill_current_weight_page()
        .check_fill_current_height_page()
        .check_fill_date_of_birth_page()
        .check_choose_region_page()
        .check_create_account_suggest_pop_up()
        .check_create_account_skip_confirmation()
    )


@allure.tag("Mobile")
@allure.feature("Android tests")
@allure.story("Login")
@allure.title("Goal setting")
@allure.severity(Severity.NORMAL)
def test_goal_setting_interface():
    pages.go_to_goal_setting_page()

    with allure.step('Set "Weight loss" goal'):
        user_flow.choose_option(
            (AppiumBy.XPATH, '//android.widget.TextView[@text="Weight loss"]')
        )
        with allure.step('Click "Next"'):
            user_flow.click_next()
            with allure.step(
                    'Check user directed to "How much weight would you like to lose?" page'
            ):
                user_flow.check_if_user_directed_to_page(
                    (AppiumBy.ID, "com.fatsecret.android:id/title_text"),
                    "How much weight would you like to lose?",
                )
                with allure.step('Click "Back"'):
                    user_flow.click_back()
                    with allure.step('Set "Maintain my current weight" goal'):
                        user_flow.choose_option(
                            (
                                AppiumBy.XPATH,
                                '//android.widget.TextView[@text="Maintain my current weight"]',
                            )
                        )
                        with allure.step('Click "Next"'):
                            user_flow.click_next()
                            with allure.step(
                                    'Check user directed to "What is your gender?" page'
                            ):
                                user_flow.check_if_user_directed_to_page(
                                    (
                                        AppiumBy.ID,
                                        "com.fatsecret.android:id/title_text",
                                    ),
                                    page_text="What is your gender?",
                                )
                                with allure.step('Click "Back"'):
                                    user_flow.click_back()
                                    with allure.step('Set "Weight gain" goal'):
                                        user_flow.choose_option(
                                            (
                                                AppiumBy.XPATH,
                                                '//android.widget.TextView[@text="Weight gain"]',
                                            )
                                        )
                                        with allure.step('Click "Next"'):
                                            user_flow.click_next()
                                            with allure.step(
                                                    'Check user directed to "How much weight would you like to gain?" page'
                                            ):
                                                user_flow.check_if_user_directed_to_page(
                                                    (
                                                        AppiumBy.ID,
                                                        "com.fatsecret.android:id/title_text",
                                                    ),
                                                    page_text="How much weight would you like to gain?",
                                                )
