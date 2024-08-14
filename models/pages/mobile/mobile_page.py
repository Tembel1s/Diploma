import allure
from appium.webdriver.common.appiumby import AppiumBy
from selene import browser, have, be


class UserFlow:

    def click(self, button):
        browser.element(button).should(
            be.clickable).click()

    def click_next(self):
        browser.element((AppiumBy.ID, 'com.fatsecret.android:id/floating_action_next_button')).should(
            be.clickable).click()

    def click_back(self):
        browser.element((AppiumBy.XPATH, '//android.widget.ImageButton')).should(be.clickable).click()

    def check_if_user_directed_to_page(self, element, page_text):
        browser.element(element).should(
            have.text(page_text))

    def choose_option(self, element):
        browser.element(element).should(
            be.clickable).click()

    def check_pop_up(self, element):
        browser.element(element).should(be.present)

    def send_keys(self, input_row, value):
        browser.element(input_row).should(
            be.clickable).click().send_keys(value)


class Pages:
    def check_main_page(self):
        with allure.step('Check and click "I am a new user" button'):
            browser.element((AppiumBy.ID, 'com.fatsecret.android:id/registration_lets_begin_text_solid')).should(
                have.text('I am a new user')).should(be.clickable).click()
            return self

    def check_data_collect_agreement_page(self):
        with allure.step('Check the user was directed to "How we use your data" page'):
            browser.element((AppiumBy.ID, 'com.fatsecret.android:id/how_we_use_your_data_text')).should(
                have.text('How we use your data'))
            with allure.step('Check and click "I agree" button'):
                browser.element(
                    (AppiumBy.ID, 'com.fatsecret.android:id/existing_user_data_optin_disagree_go_back')).should(
                    have.text('Yes, I Agree')).should(be.clickable).click()
                return self

    def check_fill_first_name_page(self):
        with allure.step('Check the user was directed to "First name" page'):
            browser.element((AppiumBy.ID, 'com.fatsecret.android:id/title_text')).should(
                have.text('First name'))
            with allure.step('Check "Next" button is disabled"'):
                browser.element((AppiumBy.ID, 'com.fatsecret.android:id/floating_action_next_button')).should(
                    have.attribute(name='enabled', value='false'))
                with allure.step('Fill First name'):
                    browser.element((AppiumBy.ID, 'com.fatsecret.android:id/edit_text')).should(
                        be.clickable).click().send_keys('QA Guru')
                    with allure.step('Check "Next" button is enabled'):
                        browser.element((AppiumBy.ID, 'com.fatsecret.android:id/floating_action_next_button')).should(
                            have.attribute(name='enabled', value='true')).should(be.clickable).click()
                        return self

    def check_setting_up_your_profile_page(self):
        with allure.step('Check the user was directed to "Setting Up Your Profile'):
            browser.element((AppiumBy.ID, 'com.fatsecret.android:id/title_text')).should(
                have.text('Setting Up Your Profile'))
            with allure.step('Check and click "Next" button'):
                browser.element((AppiumBy.ID, 'com.fatsecret.android:id/floating_action_next_button')).should(
                    be.clickable).click()
                return self

    def check_setting_your_goal_page(self):
        with allure.step('Check the user was directed to "What is your goal?" page'):
            browser.element((AppiumBy.ID, 'com.fatsecret.android:id/title_text')).should(
                have.text('What is your goal?'))
            with allure.step('Check "Next" button is disabled"'):
                browser.element((AppiumBy.ID, 'com.fatsecret.android:id/floating_action_next_button')).should(
                    have.attribute(name='enabled', value='false'))
                with allure.step('Check "Weight loss" button is unpressed"'):
                    browser.element((AppiumBy.XPATH, '//android.widget.TextView[@text="Weight loss"]')).should(
                        have.attribute(name='selected', value='false'))
                    with allure.step('Check and click "Weight los" button'):
                        browser.element((AppiumBy.XPATH, '//android.widget.TextView[@text="Weight loss"]')).should(
                            be.clickable).click()
                        with allure.step('Check "Weight loss" button is pressed"'):
                            browser.element((AppiumBy.XPATH, '//android.widget.TextView[@text="Weight loss"]')).should(
                                have.attribute(name='selected', value='true'))
                            with allure.step('Check "Next" button is enabled"'):
                                browser.element(
                                    (AppiumBy.ID, 'com.fatsecret.android:id/floating_action_next_button')).should(
                                    have.attribute(name='enabled', value='true')).should(be.clickable).click()
                                return self

    def check_weight_loss_goal_setting_page(self):
        with allure.step('Check the user was directed to goal setting page'):
            browser.element((AppiumBy.ID, 'com.fatsecret.android:id/title_text')).should(
                have.text('How much weight would you like to lose?'))
            with allure.step('Check "Next" button is disabled"'):
                browser.element((AppiumBy.ID, 'com.fatsecret.android:id/floating_action_next_button')).should(
                    have.attribute(name='enabled', value='false'))
                with allure.step('Fill desired weight to loose"'):
                    browser.element((AppiumBy.ID, 'com.fatsecret.android:id/edit_text')).should(
                        be.clickable).click().send_keys('1')
                    with allure.step('Check "Next" button is enabled"'):
                        browser.element((AppiumBy.ID, 'com.fatsecret.android:id/floating_action_next_button')).should(
                            have.attribute(name='enabled', value='true'))
                        with allure.step('Check metric system switch"'):
                            browser.element((AppiumBy.XPATH, '//android.widget.TextView[@text="kg"]')).should(
                                be.present).click()
                            browser.all((AppiumBy.ID, 'android:id/text1')).element_by(have.text('lb')).should(
                                be.present).should(
                                be.clickable)
                            browser.all((AppiumBy.ID, 'android:id/text1')).element_by(have.text('kg')).should(
                                be.present).should(
                                be.clickable).click()
                            with allure.step('Click "Next" button'):
                                browser.element(
                                    (AppiumBy.ID, 'com.fatsecret.android:id/floating_action_next_button')).should(
                                    be.clickable).click()
                                return self

    def check_gender_choosing_page(self):
        with allure.step('Check the user was directed to gender choosing page'):
            browser.element((AppiumBy.ID, 'com.fatsecret.android:id/title_text')).should(
                have.text('What is your gender?'))
            browser.element((AppiumBy.ID, 'com.fatsecret.android:id/registration_gender_female')).should(
                have.attribute(name='selected', value='false'))
            with allure.step('Check "Next" button is disabled"'):
                browser.element((AppiumBy.ID, 'com.fatsecret.android:id/floating_action_next_button')).should(
                    have.attribute(name='enabled', value='false'))
                with allure.step('Check "Male" button is unpressed"'):
                    browser.element((AppiumBy.ID, 'com.fatsecret.android:id/registration_gender_male')).should(
                        have.attribute(name='selected', value='false'))
                    with allure.step('Click "Male" button'):
                        browser.element((AppiumBy.ID, 'com.fatsecret.android:id/registration_gender_male')).click()
                        with allure.step('Check "Male" button is pressed"'):
                            browser.element((AppiumBy.ID, 'com.fatsecret.android:id/registration_gender_male')).should(
                                have.attribute(name='selected', value='true'))
                            with allure.step('Check "Next" button is enabled"'):
                                browser.element(
                                    (AppiumBy.ID, 'com.fatsecret.android:id/floating_action_next_button')).should(
                                    have.attribute(name='enabled', value='true'))
                                with allure.step('Click "Next" button'):
                                    browser.element(
                                        (AppiumBy.ID, 'com.fatsecret.android:id/floating_action_next_button')).click()
                                return self

    def check_activity_level_choosing_page(self):
        with allure.step('Check the user was directed to "What is your activity level?" page'):
            browser.element((AppiumBy.ID, 'com.fatsecret.android:id/title_text')).should(
                have.text('What is your activity level?'))
            with allure.step('Check and click "Sedentary" button'):
                browser.element(
                    (AppiumBy.ID, 'com.fatsecret.android:id/registration_activity_list_sedentary_holder')).should(
                    be.clickable).click()
                with allure.step('Click "Next" button'):
                    browser.element((AppiumBy.ID, 'com.fatsecret.android:id/floating_action_next_button')).click()
                return self

    def check_fill_current_weight_page(self):
        with allure.step('Check the user was directed to "What is your current weight?" page'):
            browser.element((AppiumBy.ID, 'com.fatsecret.android:id/title_text')).should(
                have.text('What is your current weight?'))
            with allure.step('Check "Next" button is disabled"'):
                browser.element((AppiumBy.ID, 'com.fatsecret.android:id/floating_action_next_button')).should(
                    have.attribute(name='enabled', value='false'))
                with allure.step('Fill current weight'):
                    browser.element((AppiumBy.ID, 'com.fatsecret.android:id/edit_text')).should(
                        be.clickable).click().send_keys('80')
                    with allure.step('Check "Next" button is enabled"'):
                        browser.element((AppiumBy.ID, 'com.fatsecret.android:id/floating_action_next_button')).should(
                            have.attribute(name='enabled', value='true'))
                        with allure.step('Check "metric system switch"'):
                            browser.element((AppiumBy.XPATH, '//android.widget.TextView[@text="kg"]')).should(
                                be.present).click()
                            browser.all((AppiumBy.ID, 'android:id/text1')).element_by(have.text('lb')).should(
                                be.present).should(
                                be.clickable)
                            browser.all((AppiumBy.ID, 'android:id/text1')).element_by(have.text('kg')).should(
                                be.present).should(
                                be.clickable).click()
                            with allure.step('Click "Next" button'):
                                browser.element(
                                    (AppiumBy.ID, 'com.fatsecret.android:id/floating_action_next_button')).should(
                                    be.clickable).click()
                                return self

    def check_fill_current_height_page(self):
        with allure.step('Check the user was directed to "What is your current height?" page'):
            browser.element((AppiumBy.ID, 'com.fatsecret.android:id/title_text')).should(
                have.text('What is your height?'))
            with allure.step('Check "Next" button is disabled"'):
                browser.element((AppiumBy.ID, 'com.fatsecret.android:id/floating_action_next_button')).should(
                    have.attribute(name='enabled', value='false'))
                with allure.step('Fill current height'):
                    browser.element((AppiumBy.ID, 'com.fatsecret.android:id/edit_text')).should(
                        be.clickable).click().send_keys('180')
                    with allure.step('Check "Next" button is enabled"'):
                        browser.element((AppiumBy.ID, 'com.fatsecret.android:id/floating_action_next_button')).should(
                            have.attribute(name='enabled', value='true'))
                        with allure.step('Check "metric system switch"'):
                            browser.element((AppiumBy.XPATH, '//android.widget.TextView[@text="cm"]')).should(
                                be.present).click()
                            browser.all((AppiumBy.ID, 'android:id/text1')).element_by(have.text('ft/in')).should(
                                be.present).should(
                                be.clickable)
                            browser.all((AppiumBy.ID, 'android:id/text1')).element_by(have.text('cm')).should(
                                be.present).should(
                                be.clickable).click()
                            with allure.step('Click "Next" button'):
                                browser.element(
                                    (AppiumBy.ID, 'com.fatsecret.android:id/floating_action_next_button')).should(
                                    be.clickable).click()
                                return self

    def check_fill_date_of_birth_page(self):
        with allure.step('Check the user was directed to "What is your date of birth?" page'):
            browser.element((AppiumBy.ID, 'com.fatsecret.android:id/title_text')).should(
                have.text('What is your date of birth?'))
            with allure.step('Fill date of birth'):
                browser.element((AppiumBy.XPATH, '//android.widget.Button[@text="Feb"]')).should(
                    be.present).click()
                browser.element((AppiumBy.XPATH,
                                 '//android.widget.Button[@text="02"]')).should(
                    be.present).click()
                browser.element((AppiumBy.XPATH,
                                 '//android.widget.Button[@text="1991"]')).should(
                    be.present).click()
                with allure.step('Click "Next" button'):
                    browser.element((AppiumBy.ID, 'com.fatsecret.android:id/floating_action_next_button')).should(
                        be.clickable).click()
                    return self

    def check_choose_region_page(self):
        with allure.step('Check the user was directed to "Choose your region" page'):
            browser.element((AppiumBy.ID, 'com.fatsecret.android:id/title_text')).should(
                have.text('Choose your region'))
            with allure.step('Check "United States" option is present'):
                browser.element((AppiumBy.ID, 'com.fatsecret.android:id/registration_default_region_text')).should(
                    have.text('United States')).should(be.present)
                with allure.step('Check "Other" option is present'):
                    browser.element((AppiumBy.XPATH, '//android.widget.TextView[@text="Other"]')).should(be.present)
                    with allure.step('Click "United States" button'):
                        browser.element(
                            (AppiumBy.ID, 'com.fatsecret.android:id/registration_default_region_holder')).click()
                        with allure.step('Click "Next" button'):
                            browser.element(
                                (AppiumBy.ID, 'com.fatsecret.android:id/floating_action_next_button')).should(
                                be.clickable).click()
                            return self

    def check_create_account_suggest_pop_up(self):
        with allure.step('Check the pop-up "Create an account" is appeared'):
            browser.element((AppiumBy.ID, 'com.fatsecret.android:id/create_account_title_text')).should(
                have.text('Create an account'))
            with allure.step('Click "Skip"'):
                browser.element((AppiumBy.ID, 'com.fatsecret.android:id/create_account_skip_text')).should(
                    have.text('Skip')).should(be.clickable).click()
                return self

    def check_create_account_skip_confirmation(self):
        with allure.step('Check the confirmation text "Are you sure you want to skip?" is appeared'):
            browser.element((AppiumBy.ID, 'com.fatsecret.android:id/create_account_skip_title_text')).should(
                have.text('Are you sure you want to skip?'))
            with allure.step('Click "Continue"'):
                browser.element((AppiumBy.ID, 'com.fatsecret.android:id/create_account_email_continue_button')).should(
                    have.text('CONTINUE')).should(be.clickable).click()
                return self

    def check_user_logged_in_as_guest(self):
        with allure.step('Check user has successfully logged in as a guest'):
            browser.element((AppiumBy.ID, 'com.fatsecret.android:id/tab_home')).should(be.present)

    def go_to_goal_setting_page(self):
        browser.element((AppiumBy.ID, 'com.fatsecret.android:id/registration_lets_begin_text_solid')).should(
            be.clickable).click()

        browser.element((AppiumBy.ID, 'com.fatsecret.android:id/existing_user_data_optin_disagree_go_back')).should(
            be.clickable).click()

        browser.element((AppiumBy.ID, 'com.fatsecret.android:id/edit_text')).should(
            be.clickable).click().send_keys('QA Guru')
        browser.element((AppiumBy.ID, 'com.fatsecret.android:id/floating_action_next_button')).should(
            be.clickable).click()
        browser.element((AppiumBy.ID, 'com.fatsecret.android:id/title_text')).should(
            have.text('Setting Up Your Profile'))
        browser.element((AppiumBy.ID, 'com.fatsecret.android:id/floating_action_next_button')).should(
            be.clickable).click()
