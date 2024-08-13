import time

from selene import browser, query
from selene import have, be
import allure


class FoodSearch:
    @allure.step('Search product')
    def search_product(self, product):
        browser.element('#multiSearchText').should(be.clickable).click().send_keys(product).press_enter()

    @allure.step('Check search results')
    def check_search_results(self, product):
        browser.element('.generic.searchResult').all("tr").should(have.size(10))
        browser.element('.generic.searchResult').all("tr").should(have.text(product).each)
        browser.element('.searchRelated').should(be.present).should(have.text('Related searches for: ')).should(
            have.text(product))
        browser.element('.searchRelated').all('a').should(have.size_greater_than(0))
        browser.element(f"[href='/calories-nutrition/search?q={product}&pg=1']").should(be.clickable).click()

        browser.element('.generic.searchResult').all("tr").element_by(have.text(product)).should(be.present)
        browser.element('.searchRelated').should(be.present).should(have.text('Related searches for: ')).should(
            have.text(product))
        browser.element('.searchRelated').all('a').should(have.size_greater_than(0))


class AddFood:
    @allure.step('Go to Food Diary')
    def go_to_food_diary(self):
        browser.element('[href="/Diary.aspx?pa=fj"]').should(be.visible)
        browser.execute_script('arguments[0].click();', browser.element('[href="/Diary.aspx?pa=fj"]')())
        browser.element('.MyFSHeader').should(have.text('My Food Diary'))

    @allure.step('Click Add Item')
    def click_add_item(self):
        browser.element('#addBfast').should(be.clickable).click()

    @allure.step('Choose product')
    def choose_product(self, product):
        browser.element('#searchBfastExp').should(be.clickable).click().send_keys(product.name)
        browser.element('#searchBfastButton').should(be.clickable).click()
        browser.element(f'#checkbox_1_0_{product.id}').should(be.clickable).click()

    @allure.step('Check quantity of chosen product')
    def check_quantity_of_chosen_product(self, value):
        browser.element('#add_selected_count_1').should(have.text(value))

    @allure.step('Clear input')
    def clear_input(self):
        browser.element('#searchBfastExp').clear()

    @allure.step('Add selected product')
    def add_selected(self):
        browser.element('#add_selected_count_1').click()

    @allure.step('Check added product in diary')
    def check_added_products_in_diary(self, *products):
        for product in products:
            browser.all('.generic.foodsNutritionTbl').element_by(have.text(product)).should(be.visible)


class DeleteFood:
    @allure.step('Click Delete button')
    def click_delete_button(self, product):
        browser.all("[title='edit']").element_by(have.text(product)).element('../..').element(
            "[title='delete this item']").should(be.present).click()
        browser.switch_to.alert.accept()

    @allure.step('Check deleted product in diary')
    def check_deleted_products_not_in_diary(self, product):
        browser.all("[title='edit']").element_by(have.text(product)).should(be.not_.present)

    @allure.step('Clear Diary')
    def clear_diary(self):
        while browser.all("[title='delete this item']").matching(have.size_greater_than(0)):
            browser.element("[title='delete this item']").should(be.present).click()
            browser.switch_to.alert.accept()
            time.sleep(5)


class CaloriesCount:
    @allure.step('Get product calories count')
    def get_product_calories_count(self, product):
        product_info = browser.all(f'#rec_info_link_1_0_{product.id} [title="View info"]').element_by(
            have.text('kcal')).should(be.present).get(
            query.text_content)

        start_index = product_info.find("-") + 2
        end_index = product_info.find("kcal")
        calories_quantity_with_text_kcal = product_info[start_index:end_index].strip()
        calories_quantity_number = ''.join(filter(str.isdigit, calories_quantity_with_text_kcal))
        return int(calories_quantity_number)

    @allure.step('Check correct calories quantity in diary')
    def check_correct_calories_quantity_in_diary(self, quantity):
        browser.all('.foodsNutritionTbl').element_by(have.text('Cals')).element('..').should(have.text(f'{quantity}'))

    @allure.step('Check correct calories quantity in header')
    def check_correct_calories_quantity_in_header(self, quantity):
        browser.all('.subheading').element_by(have.text(f'{quantity} kcal')).should(be.present)
