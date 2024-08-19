import allure
from allure_commons.types import Severity

from fatSecret_tests_project.data.products import product_1, product_2
from fatSecret_tests_project.pages.web.files_pages import ExportFile
from fatSecret_tests_project.pages.web.user_actions_page import AddFood
from fatSecret_tests_project.tests.web.test_user_actions import authorization


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
    add_food.go_to_food_diary()
    add_food.click_add_item()
    add_food.choose_product(product_1)
    add_food.check_quantity_of_chosen_product("1")
    add_food.clear_input()
    add_food.choose_product(product_2)
    add_food.check_quantity_of_chosen_product("2")
    add_food.add_selected()

    export_file.click_print()
    export_file.check_export_pdf_button()
    export_file.download_pdf()
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
    add_food.go_to_food_diary()
    add_food.click_add_item()
    add_food.choose_product(product_1)
    add_food.check_quantity_of_chosen_product("1")
    add_food.clear_input()
    add_food.choose_product(product_2)
    add_food.check_quantity_of_chosen_product("2")
    add_food.add_selected()

    export_file.click_print()
    export_file.check_export_csv_button()
    export_file.download_csv()
    export_file.check_csv_file_has_product_info()
