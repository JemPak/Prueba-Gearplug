# Test-Gearplug
Technical test for Gearplug selection process
## Steps for compiling the program:
1. Install docker and docker compose
2. ``docker compose build``
3. Use my custom sh script to raise the services
4. `. run.sh` - This command raise a local container db with postgres and a web service running in your localhost port 8000
5. `. run.sh bash` - Open bash inside **web** container and install fixtures.json to populate the db `python manage.py loaddata fixture.json`
6. Now the services is available to test.

    6.1 Check `<localhost:8000>/redoc/` and `<localhost:8000>/swagger/` documentation created with drf-spectacular that contains Open API 3 specification and provides more support that drf-yasg
7. Check **insomnia.json** file that contains test for all endpoints better than Postman XD!

### Created by:
-  Juan Jose Monsalve Patiño
-  Software Engineering
-  juanjomonsa45890@gmail.com
-  2022-11-20
