How to start?

1. Pull repository
2. docker build -t bjj-app .
3. docker run -p 8000:8000 bjj-app
4. Go to localhost:8000


Use cases:

1. Rejestracja i zalogowanie
   1. Kliknij signup
   2. Wypełnij formularz ( brak walidacji)
   3. Kliknij signup
   4. Nastąpi przekierowanie do strony logowania
   5. Zaloguj sie założonym kontem
   6. Jestez zalogowany powinna pokazac się informacja: Logged in as: *login*

2. Wylogowanie
   1. Kliknij logout
   2. Zostałes wylogowany

3. Stwórz Turniej
4. Stwórz Zawodnika
5. Usuń Turniej
6. Zobacz Turnieje
7. Zobacz detale turnieju ( z listy z punktu 6)
8. Dodaj Zawodnika do Turnieju
9. Nowo założony turniej może zostać wystartowany. Wtedy jeżeli liczba zawodników > 2 zostanie wykonane matchowanie zawodników według pasa, zespołu i wagi. Zostaną wygenerowane "matches" czyli pojedynki w ramach turnieju
10. Wystartowany turniej udostępnia opcje zobaczenia "bracket". To lista pojedynków gdzie użytkownik może zdecydować kto wygrał dany pojedynek
