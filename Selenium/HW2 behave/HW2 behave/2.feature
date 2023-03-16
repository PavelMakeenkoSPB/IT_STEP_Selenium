#Укажем что это за фича
Feature: Checking search Yahoo, Google on Chrome and Edge
#Укажем имя сценария (в одной фиче может быть несколько)
Scenario: Сheck some text in search results
#И используем наши шаги.
  Given on Chrome website "https://yahoo.com"
  Then push into field text 'beer'
  Then push button with text 'Найти'
  Then page include text 'Beer'
  Then push Clear button with text 'Clear'
  Then push again into field text 'coffee'
  Then push Search little button with text 'Search the web'
  Then page include text 'coffee'

Scenario: Сheck some text in search results 3

  Given on Edge website "https://yahoo.com"
  Then push into field text 'beer'
  Then push button with text 'Найти'
  Then page include text 'Beer'
  Then push Clear button with text 'Clear'
  Then push again into field text 'coffee'
  Then push Search little button with text 'Search the web'
  Then page include text 'coffee'
  
Scenario: Сheck some text in search results 4

  Given on Edge website "https://www.google.com/"
  Then insert to field text 'beer'
  Then push Google Search button with text 'Поиск в Google'
  Then page include text 'Beer'
  Then push Clear button text 'Очистить'
  Then insert again to field text 'Масло'
  Then push little Google Search button with text 'Поиск'
  Then page include text 'Масло'
  
Scenario: Сheck some text in search results 5

  Given on Chrome website "https://www.google.com/"
  Then insert to field text 'beer'
  Then push Google Search button with text 'Поиск в Google'
  Then page include text 'Beer'
  Then push Clear button text 'Очистить'
  Then insert again to field text 'Масло'
  Then push little Google Search button with text 'Поиск'
  Then page include text 'Масло'
