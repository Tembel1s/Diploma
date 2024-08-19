import allure
import pytest
from allure_commons.types import Severity

from fatsecret_tests_project.data.products import product_1, product_2
from fatsecret_tests_project.pages.web.files_pages import export_file
from fatsecret_tests_project.pages.web.user_actions_page import add_food
from tests.web.conftest import authorization


def fill_cart():
    add_food.go_to_food_diary()
    add_food.click_add_item()
    add_food.choose_product(product_1)
    add_food.check_quantity_of_chosen_product("1")
    add_food.clear_input()
    add_food.choose_product(product_2)
    add_food.check_quantity_of_chosen_product("2")
    add_food.add_selected()


@pytest.mark.delete_content_folder
@allure.tag("UI")
@allure.feature("UI tests")
@allure.story("Export files")
@allure.title("Export PDF file")
@allure.link("https://fatsecret.com/")
@allure.severity(Severity.NORMAL)
def test_export_pdf():
    authorization()
    fill_cart()

    export_file.click_print()
    export_file.check_export_pdf_button()
    export_file.download_pdf()
    export_file.check_pdf_file_has_products_info(product_1, product_2)


@pytest.mark.delete_content_folder
@allure.tag("UI")
@allure.feature("UI tests")
@allure.story("Export files")
@allure.title("Export CSV file")
@allure.link("https://fatsecret.com/")
@allure.severity(Severity.NORMAL)
def test_export_csv():
    authorization()
    fill_cart()

    export_file.click_print()
    export_file.check_export_csv_button()
    export_file.download_csv()
    export_file.check_csv_file_has_product_info()
