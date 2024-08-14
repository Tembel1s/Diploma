import time
import os
from selene.support.shared import browser
import requests
from models.pages.web.user_actions_page import (
    FoodSearch,
    AddFood,
    DeleteFood,
    CaloriesCount,
)
from models.pages.web.home_page import HomePage
from data.products import product_1, product_2
from dotenv import load_dotenv
import allure
from allure_commons.types import Severity

load_dotenv()

login = os.getenv("FATSECRET_LOGIN")
password = os.getenv("FATSECRET_PASSWORD")


def get_cookies():
    form_data = {
        "__EVENTTARGET": "ctl00$ctl11$Logincontrol1$Login",
        f"ctl00$ctl11$Logincontrol1$Name": {login},
        f"ctl00$ctl11$Logincontrol1$Password": {password},
    }

    headers = {"Content-Type": "application/x-www-form-urlencoded"}

    response = requests.post(
        "https://www.fatsecret.com/Auth.aspx?pa=s",
        data=form_data,
        headers=headers,
        allow_redirects=False,
    )
    auth_cookie_value = response.cookies.get(".FSASPXAUTH")
    auth_cookie = {
        "name": ".FSASPXAUTH",
        "value": auth_cookie_value,
    }

    return auth_cookie


def authorization():
    browser.open("/")
    browser.driver.add_cookie(get_cookies())
    time.sleep(2)
    browser.driver.refresh()


@allure.tag("UI")
@allure.feature("UI tests")
@allure.story("User actions")
@allure.title("Main page")
@allure.link("https://fatsecret.com/")
@allure.severity(Severity.NORMAL)
def test_main_page():
    home_page = HomePage()

    authorization()

    time.sleep(2)
    home_page.check_my_fatsecret_tab()

    time.sleep(2)
    home_page.check_foods_tab()

    time.sleep(2)
    home_page.check_recipies_tab()
    home_page.check_challenges_tab()

    time.sleep(2)
    home_page.check_fitness_tab()

    time.sleep(2)
    home_page.check_community_tab()


@allure.tag("UI")
@allure.feature("UI tests")
@allure.story("User actions")
@allure.title("Food search")
@allure.link("https://fatsecret.com/")
@allure.severity(Severity.NORMAL)
def test_food_search():
    food_search = FoodSearch()

    authorization()
    time.sleep(2)

    food_search.search_product(product_1.name)
    time.sleep(2)
    food_search.check_search_results(product_1.name)


@allure.tag("UI")
@allure.feature("UI tests")
@allure.story("User actions")
@allure.title("Add food to Diary")
@allure.link("https://fatsecret.com/")
@allure.severity(Severity.CRITICAL)
def test_add_food_to_diary():
    add_food = AddFood()
    authorization()
    time.sleep(2)

    add_food.go_to_food_diary()
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
    #
    time.sleep(2)
    add_food.check_added_products_in_diary(product_1.name, product_2.name)


@allure.tag("UI")
@allure.feature("UI tests")
@allure.story("User actions")
@allure.title("Delete food from Diary")
@allure.link("https://fatsecret.com/")
@allure.severity(Severity.CRITICAL)
def test_delete_food_from_diary():
    add_food = AddFood()
    delete_food = DeleteFood()

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

    delete_food.click_delete_button(product_1.name)
    time.sleep(2)
    delete_food.click_delete_button(product_2.name)
    time.sleep(2)

    delete_food.check_deleted_products_not_in_diary(product_1.name)

    time.sleep(2)
    delete_food.check_deleted_products_not_in_diary(product_2.name)


@allure.tag("UI")
@allure.feature("UI tests")
@allure.story("User actions")
@allure.title("Calories count")
@allure.link("https://fatsecret.com/")
@allure.severity(Severity.CRITICAL)
def test_calories_count():
    authorization()
    add_food = AddFood()
    calories_count = CaloriesCount()

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
