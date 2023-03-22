
Feature: Проверка результатов поиска Google в браузерах Chrome и Edge

Scenario: Поиск запроса Google через Chrome

  Given on Chrome website "https://www.google.com/"
  When insert to field text 'world of'
  When push Google Search button with text 'Поиск в Google'
  When page include text 'world of'
  When click into search field
  When first falling object in field
  
  