import allure
from allure_commons.types import Severity

from fatsecret_tests_project.pages.mobile.mobile_page import user_flow, pages


@allure.tag("Mobile")
@allure.feature("Android tests")
@allure.story("Login")
@allure.title("Captcha")
@allure.severity(Severity.CRITICAL)
def test_capcha():
    (
        user_flow.check_if_user_on_welcome_page()
        .click_sign_with_existing_account()
        .choose_sign_up_with_email()
        .submit_credentials()
        .click_sign_in()
        .check_captcha()
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


#
#
# @allure.tag("Mobile")
# @allure.feature("Android tests")
# @allure.story("Login")
# @allure.title("Goal setting")
# @allure.severity(Severity.NORMAL)
# def test_goal_setting_interface():
#     pages.go_to_goal_setting_page()
#
#     with allure.step('Set "Weight loss" goal'):
#         user_flow.choose_option(
#             (AppiumBy.XPATH, '//android.widget.TextView[@text="Weight loss"]')
#         )
#         with allure.step('Click "Next"'):
#             user_flow.click_next()
#             with allure.step(
#                     'Check user directed to "How much weight would you like to lose?" page'
#             ):
#                 user_flow.check_if_user_directed_to_page(
#                     (AppiumBy.ID, "com.fatsecret.android:id/title_text"),
#                     "How much weight would you like to lose?",
#                 )
#                 with allure.step('Click "Back"'):
#                     user_flow.click_back()
#                     with allure.step('Set "Maintain my current weight" goal'):
#                         user_flow.choose_option(
#                             (
#                                 AppiumBy.XPATH,
#                                 '//android.widget.TextView[@text="Maintain my current weight"]',
#                             )
#                         )
#                         with allure.step('Click "Next"'):
#                             user_flow.click_next()
#                             with allure.step(
#                                     'Check user directed to "What is your gender?" page'
#                             ):
#                                 user_flow.check_if_user_directed_to_page(
#                                     (
#                                         AppiumBy.ID,
#                                         "com.fatsecret.android:id/title_text",
#                                     ),
#                                     page_text="What is your gender?",
#                                 )
#                                 with allure.step('Click "Back"'):
#                                     user_flow.click_back()
#                                     with allure.step('Set "Weight gain" goal'):
#                                         user_flow.choose_option(
#                                             (
#                                                 AppiumBy.XPATH,
#                                                 '//android.widget.TextView[@text="Weight gain"]',
#                                             )
#                                         )
#                                         with allure.step('Click "Next"'):
#                                             user_flow.click_next()
#                                             with allure.step(
#                                                     'Check user directed to "How much weight would you like to gain?" page'
#                                             ):
#                                                 user_flow.check_if_user_directed_to_page(
#                                                     (
#                                                         AppiumBy.ID,
#                                                         "com.fatsecret.android:id/title_text",
#                                                     ),
#                                                     page_text="How much weight would you like to gain?",
#                                                 )
