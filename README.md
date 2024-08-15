<h1> Тестирование фитнес-приложения трекинга диеты FatSecret</h1>

> <a target="_blank" href="https://fatsecret.com/">Ссылка на сайт</a>

![This is an image](images/main_page.png)

#### Список проверок, реализованных в автотестах:

#### UI-тестирование:

* ✅ Проверка авторизации (позитивные и негативные сценарии)
* ✅ Проверка главной страницы (наличие всех необходимых графических и функциональных элементов)
* ✅ Проверка функционала поиска продукта
* ✅ Проверка функционала добавления продукта в дневник диеты
* ✅ Проверка функицонала удаления продукта из дневника диеты
* ✅ Проверка корректности подсчета каллорий в дневнике диеты
* ✅ Проверка функционала экспорта дневника диеты в файл формата PDF
* ✅ Проверка функционала экспорта дневника диеты в файл формата CSV

#### API-тестирование:

* ✅ Проверка авторизации (позитивные и негативные сценарии)
* ✅ Проверка функционала подгрузки ранее выбранных продуктов во вкладку Recently Eaten
* ✅ Проверка функционала подгрузки часто выбираемых продуктов во вкладку Most Eaten
* ✅ Проверка корректного перехода на страницу профиля пользователя
* ✅ Проверка функционала заполнения поля Bio
* ✅ Проверка функционала добавления фото в профиль пользователя

#### Мобильное тестирование:

* ✅ Проверка появления капча-теста при авторизации в приложении
* ✅ Проверка возможности гостевой авторизации в приложении
* ✅ Проверка кастомизации интерфейса в зависимости от выбора пользователем фитнес-цели

----

## Технологии и инструменты

## Технологии и инструменты
<p  align="center">
<img src="images/logos/python-original.svg" width="50" title="Python"> <img src="images/logos/pytest.png" width="50" title="Pytest"> <img src="images/logos/intellij_pycharm.png" width="50" title="PyCharm"> <img src="images/logos/selene.png" width="50" title="Selene"> <img src="images/logos/selenium.png" width="50" title="Selenium"> <img src="images/logos/selenoid.png" width="50" title="Selenoid"> <img src="images/logos/jenkins.png" width="50" title="Jenkins"> <img src="images/logos/allure_report.png" width="50" title="Allure Report"> <img src="images/logos/allure_testops.png" width="50" title="Allure TestOps"> <img src="images/logos/tg.png" width="50" title="Telegram"> <img src="images/logos/jira.png" width="50" title="Jira"> <img src="images/logos/github.png" width="50" title="GitHub">
</p>

----

### Запуск автотестов выполняется на сервере Jenkins

> <a target="_blank" href="FatSecret_tests_project/">Ссылка на проект в Jenkins</a>

#### Для запуска автотестов в Jenkins

1. Открыть <a target="_blank" href="https://jenkins.autotests.cloud/job/FatSecret_tests_project/">Проект в Jenkins</a>
2. Выбрать пункт `Build with Parameters`
3. Выбрать окружение в выпадающем списке ENVIRONMENT
4. Указать комментарий в поле COMMENT
7. Нажать кнопку `Build`
8. Результат запуска сборки можно посмотреть в отчёте Allure

<img alt="This is an image" src="images/Allure_fatsecret.png" width="900"/>

----

### Allure-отчет

#### Общие результаты

![This is an image](images/allure_owerview.png)

#### Список тест-кейсов

![This is an image](images/Allure_test_cases.png)

----

### Allure TestOps

#### Общий список всех кейсов, имеющихся в системе

![This is an image](images/testops_test_cases.png)

#### Пример dashboard с результатами тестирования

![This is an image](images/testops_dash.png)

----

### Интеграция с Jira

![This is an image](images/jira.png)

----

### Оповещение о результатах прохождения тестов в Telegram

<img alt="This is an image" height="250" src="images/tg_notifications.png"/>

### Пример видео прохождения автотеста

![autotest_gif](images/autotestgif.gif)
