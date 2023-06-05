## Instructions: 
для локального запуска тестов 
```
docker-compose up --build
pip install requirements.txt
py.test -v -s --junitxml=out_report.xml test1.py 
```
