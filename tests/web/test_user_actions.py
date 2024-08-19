import time

import allure
from allure_commons.types import Severity

from fatsecret_tests_project.data.products import product_1, product_2
from fatsecret_tests_project.pages.web.home_page import home_page
from fatsecret_tests_project.pages.web.user_actions_page import (add_food,
                                                                 food_search,
                                                                 delete_food, calories_count
                                                                 )
from tests.web.conftest import authorization


@allure.tag("UI")
@allure.feature("UI tests")
@allure.story("User actions")
@allure.title("Main page")
@allure.link("https://fatsecret.com/")
@allure.severity(Severity.NORMAL)
def test_main_page():
    authorization()
    time.sleep(2)

    home_page.check_my_fatsecret_tab()
    time.sleep(2)
    home_page.check_foods_tab()
    time.sleep(2)
    home_page.check_recipies_tab()
    time.sleep(2)
    home_page.check_challenges_tab()
    time.sleep(2)
    home_page.check_fitness_tab()
    time.sleep(2)
    home_page.check_community_tab()
    time.sleep(2)


@allure.tag("UI")
@allure.feature("UI tests")
@allure.story("User actions")
@allure.title("Food search")
@allure.link("https://fatsecret.com/")
@allure.severity(Severity.NORMAL)
def test_food_search():
    authorization()
    time.sleep(2)

    food_search.search_product(product_1.name)
    time.sleep(2)
    food_search.check_search_results(product_1.name)
    time.sleep(2)


@allure.tag("UI")
@allure.feature("UI tests")
@allure.story("User actions")
@allure.title("Add food to Diary")
@allure.link("https://fatsecret.com/")
@allure.severity(Severity.CRITICAL)
def test_add_food_to_diary():
    authorization()
    time.sleep(2)
    add_food.go_to_food_diary()
    time.sleep(2)

    add_food.click_add_item()
    time.sleep(2)
    add_food.choose_product(product_1)
    time.sleep(2)
    add_food.check_quantity_of_chosen_product("1")
    time.sleep(2)
    add_food.clear_input()
    time.sleep(2)
    add_food.choose_product(product_2)
    time.sleep(2)
    add_food.check_quantity_of_chosen_product("2")
    time.sleep(2)
    add_food.add_selected()
    time.sleep(2)
    add_food.check_added_products_in_diary(product_1.name, product_2.name)
    time.sleep(2)


@allure.tag("UI")
@allure.feature("UI tests")
@allure.story("User actions")
@allure.title("Delete food from Diary")
@allure.link("https://fatsecret.com/")
@allure.severity(Severity.CRITICAL)
def test_delete_food_from_diary():
    authorization()
    time.sleep(2)
    add_food.go_to_food_diary()
    time.sleep(2)
    add_food.click_add_item()
    time.sleep(2)
    add_food.choose_product(product_1)
    time.sleep(2)
    add_food.clear_input()
    time.sleep(2)
    add_food.choose_product(product_2)
    time.sleep(2)
    add_food.add_selected()
    time.sleep(2)

    delete_food.click_delete_button(product_1.name)
    time.sleep(2)
    delete_food.click_delete_button(product_2.name)
    time.sleep(2)
    delete_food.check_deleted_products_not_in_diary(product_1.name)
    time.sleep(2)
    delete_food.check_deleted_products_not_in_diary(product_2.name)
    time.sleep(2)


@allure.tag("UI")
@allure.feature("UI tests")
@allure.story("User actions")
@allure.title("Calories count")
@allure.link("https://fatsecret.com/")
@allure.severity(Severity.CRITICAL)
def test_calories_count():
    authorization()
    time.sleep(2)

    add_food.go_to_food_diary()
    time.sleep(2)
    add_food.click_add_item()
    time.sleep(2)
    add_food.choose_product(product_1)
    time.sleep(2)

    product_1_calories_quantity = calories_count.get_product_calories_count(product_1)
    time.sleep(2)
    add_food.add_selected()
    time.sleep(2)

    calories_count.check_correct_calories_quantity_in_diary(product_1_calories_quantity)
    time.sleep(2)
    calories_count.check_correct_calories_quantity_in_header(
        product_1_calories_quantity
    )

    add_food.click_add_item()
    time.sleep(2)
    add_food.choose_product(product_2)
    time.sleep(2)

    product_2_calories_quantity = calories_count.get_product_calories_count(product_2)
    time.sleep(2)
    add_food.add_selected()
    time.sleep(2)
    total_calories = product_1_calories_quantity + product_2_calories_quantity

    calories_count.check_correct_calories_quantity_in_diary(total_calories)
    time.sleep(2)
    calories_count.check_correct_calories_quantity_in_header(total_calories)
    time.sleep(2)
