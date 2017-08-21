# svp-oma
Svendeprøve projekt August 2017

Når projeket klones fra github med `git clone` skal det virtuelle python miljø genoprettes.

Dette gøres med `virtualenv -p python3 projektnavn`.

Følgøende skal afvikles for at genskabe alle 3 virtuelle miljøer:
```
virtualenv -p python3 om
virtualenv -p python3 control
virtualenv -p python3 embedded
virtualenv ml
```

Husk at Python 3 skal være installeret på den lokale arbejdsstation for at det virker.

Machine Learning skal gerne køre Python 2.7, men er understøttet på Python 3.

Forefindes der flere udgaver af Python 3, kan det være nødvendigt at skrive `-p python3.5` i stedet for `-p python3` for at få Python 3.5 i stedet for den version der normalt ville vælges.

De virtuelle miljøer medtages ikke i versionsstyring og skal derfor genoprettes hver gang projektet hentes på en ny enhed.

Når der installeres pakker i et virtuelt miljø, er det vigtigt at requirements.txt på den enkelte miljø opdateres inden koden afleveres med `git push`.
Opdatering foregår med `pip freeze > requirements.txt`

Følgende side bruges til opsætning af Django
```
https://www.codingforentrepreneurs.com/blog/create-a-blank-django-project/
```
## IP addresser
| Server        | IP            |
| ------------- |:-------------:|
| Application server 1 |10.135.17.51 |
| Application server 2 |10.135.17.154 |
| PostgreSQL server |10.135.17.153 |
| Load Balancer |10.135.17.50 |

