import allure
from selene import browser
from selene import have, be


class HomePage:
    @allure.step('Check "My FatSecret" tab')
    def check_my_fatsecret_tab(self):
        browser.element('[title="My FatSecret"]').should(be.present)
        browser.element('[title="My FatSecret"]').element("..").should(
            have.css_class("highlight")
        )
        browser.element('[title="My FatSecret"]').should(
            have.attribute("href", "https://www.fatsecret.com/Default.aspx?pa=m")
        )

    @allure.step('Check "Foods" tab')
    def check_foods_tab(self):
        browser.element('[title="Foods"]').should(be.present)
        browser.element('[title="Foods"]').element("..").should(
            have.no.css_class("highlight")
        )
        browser.element('[title="Foods"]').should(
            have.attribute("href", "https://www.fatsecret.com/calories-nutrition/")
        )

    @allure.step('Check "Recipies" tab')
    def check_recipies_tab(self):
        browser.element('[title="Recipes"]').should(be.present)
        browser.element('[title="Recipes"]').element("..").should(
            have.no.css_class("highlight")
        )
        browser.element('[title="Recipes"]').should(
            have.attribute("href", "https://www.fatsecret.com/Default.aspx?pa=recsh")
        )

    @allure.step('Check "Challenges" tab')
    def check_challenges_tab(self):
        browser.element('[title="Challenges"]').should(be.present)
        browser.element('[title="Challenges"]').element("..").should(
            have.no.css_class("highlight")
        )
        browser.element('[title="Challenges"]').should(
            have.attribute("href", "https://www.fatsecret.com/challenges/")
        )

    @allure.step('Check "Fitness" tab')
    def check_fitness_tab(self):
        browser.element('[title="Fitness"]').should(be.present)
        browser.element('[title="Fitness"]').element("..").should(
            have.no.css_class("highlight")
        )
        browser.element('[title="Fitness"]').should(
            have.attribute("href", "https://www.fatsecret.com/fitness/")
        )

    @allure.step('Check "Community" tab')
    def check_community_tab(self):
        browser.element('[title="Community"]').should(be.present)
        browser.element('[title="Community"]').element("..").should(
            have.no.css_class("highlight")
        )
        browser.element('[title="Community"]').should(
            have.attribute("href", "https://www.fatsecret.com/Community.aspx?pa=fms")
        )


home_page = HomePage()
