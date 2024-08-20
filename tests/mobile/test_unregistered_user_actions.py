import allure
from allure_commons.types import Severity

from fatsecret_tests_project.pages.mobile.mobile_page import user_flow, pages


# @allure.tag("Mobile")
# @allure.feature("Android tests")
# @allure.story("Login")
# @allure.title("Captcha")
# @allure.severity(Severity.CRITICAL)
# def test_capcha():
#     (
#         user_flow.check_if_user_on_welcome_page()
#         .click_sign_with_existing_account()
#         .choose_sign_up_with_email()
#         .submit_credentials()
#         .click_sign_in()
#         .check_captcha()
#     )


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
        .check_user_logged_in_as_guest()
    )



#
# @allure.tag("Mobile")
# @allure.feature("Android tests")
# @allure.story("Login")
# @allure.title("Goal setting")
# @allure.severity(Severity.NORMAL)
# def test_goal_setting_interface():
#     pages.go_to_goal_setting_page()
#     (
#
#     user_flow.choose_weight_loss_goal()
#     .click_next()
#     .check_if_directed_to_correct_page("How much weight would you like to lose?")
#     .click_back()
#     .choose_weight_maintain_goal()
#     .click_next()
#     .check_if_directed_to_correct_page("What is your gender?")
#     .click_back()
#     .choose_weight_gain_goal()
#     .click_next()
#     .check_if_directed_to_correct_page("How much weight would you like to gain?")
#     )
#
