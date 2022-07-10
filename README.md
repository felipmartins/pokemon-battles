# Pokemon Battles

1. Clone o repositório e entre na pasta do projeto

```bash
git clone https://github.com/felipmartins/Pokemon-API.git && cd Pokemon-API
```

2. Crie o ambiente virtual

```bash
python3 -m venv .venv
```

3. Ative o ambiente virtual

```bash
source .venv/bin/activate
```

4. Instale os requerimentos para a aplicação

```bash
pip install -r requirements.txt
```

5. Crie a migrações necessárias

```bash
python3 manage.py makemigrations
```

6. Realize as migrações

```bash
python3 manage.py migrate
```

7. Popule o banco de dados

```bash
./manage.py shell < pokemons/populate.py
```

8. Rode a aplicação

```bash
python3 manage.py runserver
```

9. Abra o servidor

```bash
localhost:8000
```
