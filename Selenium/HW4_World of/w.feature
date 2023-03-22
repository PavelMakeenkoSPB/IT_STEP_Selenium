Feature: Проверка результатов поиска "World of tanks" через Google в браузерах Chrome и Edge

Scenario: Поиск запроса "World of tanks" в Google через Chrome

  Given on Chrome website "https://www.google.com/"
  When insert to field text "World of tanks"
  When push Google Search button with text 'Поиск в Google'
  
  When number of search results per page is 9
  When all of 4 images are displayed in results correctly
  Then page include text "World of tanks"
  
  