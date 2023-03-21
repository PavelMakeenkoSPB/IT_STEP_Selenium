
Feature: Проверка результатов поиска Google в браузерах Chrome и Edge

Scenario: Поиск запроса Google через Chrome

  Given on Chrome website "https://www.google.com/"
  When insert to field text 'Бернский зенненхунд'
  When push Google Search button with text 'Поиск в Google'
  When amount of search results exists 'Результатов: примерно '
  When count the number of results per page is 9
  When image is displayed in results
  Then page include text 'Бернский зенненхунд'
  
Scenario: Поиск запроса Google через Edge

  Given on Edge website "https://www.google.com/"
  When insert to field text 'Бернский зенненхунд'
  When push Google Search button with text 'Поиск в Google'
  When amount of search results exists 'Результатов: примерно '
  When count the number of results per page is 9
  When image is displayed in results
  Then page include text 'Бернский зенненхунд'







  
