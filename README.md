# API for portofolio

## Features:
1. Get all data
2. Get data by slug
3. Login user (Django)
4. Admin page (Django)
5. CRUD (Django)

## How to use:

1. #### clone / download this repo
2. #### install modules
``` bash
pip3 install -r requirement.txt
```

5. #### migration
```bash
python3 manage.py makemigrations
python3 manage.py migrate
```

6. #### create super user
```bash
python3 manage.py createsuperuser
```

5. #### run server
```bash
python3 manage.py runserver
```

6. #### create data

## End point
### All Projects
localhost:8000/api/v1/projects/all/
### Project by slug
localhost:8000/api/v1/projects/slug-project/
### Project by project-type
localhost:8000/api/v1/projects/FE/
localhost:8000/api/v1/projects/BE/
localhost:8000/api/v1/projects/FS/
localhost:8000/api/v1/projects/PL/
### All Tech
localhost:8000/api/v1/tech/all/
### Tech by slug
localhost:8000/api/v1/tech/slug-tech/
