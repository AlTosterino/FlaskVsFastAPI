# Flask Vs FastAPI

### To repozytorium powstało na potrzeby artykułu: `Rest API w Pythonie: Flask czy FastAPI?`

#### Artykuł: https://geek.justjoin.it/rest-api-w-pythonie-flask-czy-fastapi

Porównuję Flask i FastAPI na podstawie szybkości samego frameworka jak i przyjemności dopisywania kolejnych funkcjonalności na podstawie przykładowego projektu.

Jest to bardzo proste API do tworzenia wiadomości prasowych - Nagłówek, treść oraz imię osoby tworzącej daną wiadomość.

## Uruchamianie za pomocą dockera:
Potrzebujesz dockera i docker-compose

Aby uruchomić `Flask`:
 - `make docker-flask`

Aby uruchomić `FastAPI`:
 - `make docker-fastapi`

## Uruchamianie lokalnie:
- Zainstaluj [pip-tools](https://github.com/jazzband/pip-tools)
- Zaktualizuj wszystkie paczki `make recompile-deps`
- Zainstaluj wszystkie paczki `make sync-deps`

Aby uruchomić `Flask`:
- `make run-flask`

Aby uruchomić `FastAPI`:
- `make run-fastapi`