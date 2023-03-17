
Feature: Проверка результатов поиска Google в браузерах Chrome и Edge

Scenario: Поиск запроса Google через Chrome

  Given on Chrome website "https://www.google.com/"
  When insert to field text 'Гарфилд'
  When push Google Search button with text 'Поиск в Google'
  When count the number of results per page
  
  Then page include text 'Гарфилд'







  
