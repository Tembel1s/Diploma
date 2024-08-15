import time

import allure
from allure_commons.types import Severity

from data.products import product_1, product_2
from models.pages.web.files_pages import ExportFile
from models.pages.web.user_actions_page import AddFood
from tests.web.test_user_actions import authorization


@allure.tag("UI")
@allure.feature("UI tests")
@allure.story("Export files")
@allure.title("Export PDF file")
@allure.link("https://fatsecret.com/")
@allure.severity(Severity.NORMAL)
def test_export_pdf():
    add_food = AddFood()
    export_file = ExportFile()

    authorization()
    # time.sleep(2)

    add_food.go_to_food_diary()
    # time.sleep(2)
    add_food.click_add_item()

    # time.sleep(2)
    add_food.choose_product(product_1)
    # time.sleep(2)
    add_food.check_quantity_of_chosen_product("1")
    # time.sleep(2)
    add_food.clear_input()

    # time.sleep(2)
    add_food.choose_product(product_2)
    # time.sleep(2)
    add_food.check_quantity_of_chosen_product("2")

    # time.sleep(2)
    add_food.add_selected()

    # time.sleep(2)

    export_file.click_print()
    # time.sleep(2)
    export_file.check_export_pdf_button()
    export_file.download_pdf()

    # time.sleep(2)

    export_file.check_pdf_file_has_products_info(product_1, product_2)


@allure.tag("UI")
@allure.feature("UI tests")
@allure.story("Export files")
@allure.title("Export CSV file")
@allure.link("https://fatsecret.com/")
@allure.severity(Severity.NORMAL)
def test_export_csv():
    add_food = AddFood()
    export_file = ExportFile()
    authorization()
    # time.sleep(2)

    add_food.go_to_food_diary()
    # time.sleep(2)
    add_food.click_add_item()

    # time.sleep(2)
    add_food.choose_product(product_1)
    # time.sleep(2)
    add_food.check_quantity_of_chosen_product("1")

    # time.sleep(2)
    add_food.clear_input()
    # time.sleep(2)
    add_food.choose_product(product_2)

    # time.sleep(2)
    add_food.check_quantity_of_chosen_product("2")
    # time.sleep(2)
    add_food.add_selected()

    # time.sleep(2)
    export_file.click_print()
    # time.sleep(2)
    export_file.check_export_csv_button()
    # time.sleep(2)
    export_file.download_csv()

    # time.sleep(2)
    export_file.check_csv_file_has_product_info()
