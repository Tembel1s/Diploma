from appium.webdriver.common.appiumby import AppiumBy
from Models.pages.mobile.mobile_page import Pages, UserFlow


def test_capcha():
    user_flow = UserFlow()

    user_flow.check_if_user_directed_to_page(
        (AppiumBy.ID, 'com.fatsecret.android:id/registration_lets_begin_text_solid'), 'I am a new user')

    user_flow.click((AppiumBy.ID, 'com.fatsecret.android:id/registration_sign_in_outline'))
    user_flow.choose_option((AppiumBy.ID, 'com.fatsecret.android:id/sign_in_sign_up_with_email'))
    user_flow.click(
        "//*[@resource-id='com.fatsecret.android:id/sign_in_email_member_name_input']//*[@resource-id='com.fatsecret.android:id/input_row']//*[@resource-id='com.fatsecret.android:id/edit_text']")

    user_flow.send_keys(
        "//*[@resource-id='com.fatsecret.android:id/sign_in_email_member_name_input']//*[@resource-id='com.fatsecret.android:id/input_row']//*[@resource-id='com.fatsecret.android:id/edit_text']",
        'login')

    user_flow.send_keys(
        "//*[@resource-id='com.fatsecret.android:id/sign_in_password_input']//*[@resource-id='com.fatsecret.android:id/input_row']//*[@resource-id='com.fatsecret.android:id/edit_text']",
        'password')

    user_flow.click((AppiumBy.ID, 'com.fatsecret.android:id/sign_in_sign_in_button'))

    user_flow.check_pop_up((AppiumBy.XPATH, '//android.widget.TextView[@text="Quick Verification"]'))


def test_guest_login():
    pages = Pages()

    (pages.check_main_page()
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
     .check_create_account_skip_confirmation())


def test_goal_setting_interface():
    pages = Pages()
    user_flow = UserFlow()

    pages.go_to_goal_setting_page()

    user_flow.choose_option((AppiumBy.XPATH, '//android.widget.TextView[@text="Weight loss"]'))
    user_flow.click_next()
    user_flow.check_if_user_directed_to_page((AppiumBy.ID, 'com.fatsecret.android:id/title_text'),
                                             'How much weight would you like to lose?')
    user_flow.click_back()
    user_flow.choose_option((AppiumBy.XPATH, '//android.widget.TextView[@text="Maintain my current weight"]'))
    user_flow.click_next()

    user_flow.check_if_user_directed_to_page((AppiumBy.ID, 'com.fatsecret.android:id/title_text'),
                                             page_text='What is your gender?')
    user_flow.click_back()
    user_flow.choose_option((AppiumBy.XPATH, '//android.widget.TextView[@text="Weight gain"]'))
    user_flow.click_next()
    user_flow.check_if_user_directed_to_page((AppiumBy.ID, 'com.fatsecret.android:id/title_text'),
                                             page_text='How much weight would you like to gain?')
