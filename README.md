# Svendeprøve projekt August 2017

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
| Application server 1 |10.135.17.158 |
| Application server 2 |10.135.17.154 |
| PostgreSQL server |10.135.17.153 |
| Load Balancer |10.135.17.50 |

## Tools
I `tools`mappen findes der 4 scripts som afvikles med kommandoen `sh scriptnavn.sh` på raspberry pi. Scriptet skal afvikles uden brug af `sudo`.

Scriptet `start_control.sh` afvikler en opstart af `nginx`og `gunicorn`, såfremt disse er stoppet

Scriptet `stop_control.sh` afvikler en nedlukning af `nginx`og `gunicorn`, såfremt disse er startet

Scriptet `restart_control.sh` afvikler en genstart af `nginx`og `gunicorn`

Scriptet `status_control.sh` viser en status for `nginx`og `gunicorn`


## Dokumentation
Til dokumentation benyttes `sphinx` biblioteket.

Sphinx kan være lidt kompliceret at få opsat, men herunder følger skridt til at opsætte ny dokumentation og til at opdatere eksisterende dokumentation

### Opsætning af ny dokumentation
Sørg for at din `python` kode har dokumentation til metoder og klasser.

Dokumentation i python koden opsættes som følger:

```
class MyFancyClass(object):

"""
A simple class that creates objects with names and values
:type name: string
:param name: A name of the object to create

:type value: integer
:param value: A numeric value for your object

"""

def __init__(self, name, value)
```

Når koden er dokumenteret med en kort beskrivelse og parametre, enten med eller uden type, skal vi have lavet dokumentationen.

Først sørg for at `sphinx` er installeret. Dette tjekkes ved at se om der er adgang til kommandoen `sphinx-quickstart` og kommanden `sphinx-apidoc`.

Hvis disse kommandoer ikke findes, så installeres sphinx med `pip install sphinx`. Husk herefter at genopbygge `requirements.txt` med `pip freeze > requirements.txt`.

Opret herefter en mappe kaldet `docs` i samme niveau som `src`.

Inde i `docs` oprettes mapperne `rst` og `html`.

Fra en kommandkrompt/terminal tilgå `docs mappen`.

Herfra køres `sphinx-quickstart`.

Udfyld som følger:
```
Enter the root path for documentation.
> Root path for the documentation [.]:

You have two options for placing the build directory for Sphinx output.
Either, you use a directory "_build" within the root path, or you separate
"source" and "build" directories within the root path.
> Separate source and build directories (y/n) [n]:

Inside the root directory, two more directories will be created; "_templates"
for custom HTML templates and "_static" for custom stylesheets and other static
files. You can enter another prefix (such as ".") to replace the underscore.
> Name prefix for templates and static dir [_]:

The project name will occur in several places in the built documentation.
Operation & Maintenance platform
> Author name(s): Kenneth Hansen, Dennis Asmussen, Daniel M. Nielsen

Sphinx has the notion of a "version" and a "release" for the
software. Each version can have multiple releases. For example, for
Python the version is something like 2.5 or 3.0, while the release is
something like 2.5.1 or 3.0a1.  If you don't need this dual structure,
just set both to the same value.
> Project version []: 1.0
> Project release [1.0]:

If the documents are to be written in a language other than English,
you can select a language here by its language code. Sphinx will then
translate text that it generates into that language.

For a list of supported codes, see
http://sphinx-doc.org/config.html#confval-language.
> Project language [en]:

The file name suffix for source files. Commonly, this is either ".txt"
or ".rst".  Only files with this suffix are considered documents.
> Source file suffix [.rst]:

One document is special in that it is considered the top node of the
"contents tree", that is, it is the root of the hierarchical structure
of the documents. Normally, this is "index", but if your "index"
document is a custom template, you can also set this to another filename.
> Name of your master document (without suffix) [index]:

Sphinx can also add configuration for epub output:
> Do you want to use the epub builder (y/n) [n]: n

Please indicate if you want to use one of the following Sphinx extensions:
> autodoc: automatically insert docstrings from modules (y/n) [n]: y
> doctest: automatically test code snippets in doctest blocks (y/n) [n]:
> intersphinx: link between Sphinx documentation of different projects (y/n) [n]:
> todo: write "todo" entries that can be shown or hidden on build (y/n) [n]: y
> coverage: checks for documentation coverage (y/n) [n]:
> imgmath: include math, rendered as PNG or SVG images (y/n) [n]:
> mathjax: include math, rendered in the browser by MathJax (y/n) [n]:
> ifconfig: conditional inclusion of content based on config values (y/n) [n]:
> viewcode: include links to the source code of documented Python objects (y/n) [n]: y
> githubpages: create .nojekyll file to publish the document on GitHub pages (y/n) [n]: y

A Makefile and a Windows command file can be generated for you so that you
only have to run e.g. `make html' instead of invoking sphinx-build
directly.
> Create Makefile? (y/n) [y]:
> Create Windows command file? (y/n) [y]:
```

I felter hvor der ikke fremkommer noget efter `]:`, trykkes der blot for `Enter` for at acceptere standard værdien.

VIGTIGT!
Inden dokumentationen oprettes, er det vigtigt at der ikke afvikles kode udenfor funktioner, metoder eller klasser. Sphinx afvikler koden udenfor disse defintioner og dette kan medføre fejl i dokumentationen eller på det system der afvikler` sphinx`. Koden skal være, det man kalder, `self contained`.

Dernæst tilrettes den oprettede `conf.py` fil at indeholde følgende linjer fra linje 20:
```
import os
import sys
import django
cwd = os.getcwd()
parent = os.path.dirname(cwd)
sys.path.append(os.path.join(parent, "src"))
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "om.settings")
django.setup()
```

`om.settings` udskiftes med `projektnavn.settings`, såsom `control.settings`. Bemærk at dette er specifikt til Django baserede applikationer.

I tilfælde af projekter som ikke er Django skal det se således ud:
```
import os
import sys
cwd = os.getcwd()
parent = os.path.dirname(cwd)
sys.path.append(os.path.join(parent, "src"))
```

For at lave dokumentationen den første gang skal vi have oprettet de `rst` filer som `sphinx` bruger til at oprette HTML-versionen af vores dokumentation.

Dette gøres med følgende kommando:

```
sphinx-apidoc -o /Users/kenneth/Code/svp-oma/om/docs/rst/ /Users/kenneth/Code/svp-oma/om/src/
```

Herefter kan vi lave `html` udgaven af vores dokumentation. Kør `make html` og vent til den er færdig.

I mappen `_build/html` ligger dokumentationen nu klar. Problemet er dog at denne ikke medtages i VCS, så vi skal lige kopiere den færdige dokumentation til en anden mappe. Det er her mappen `html` kommer i brug.

Kopier indholdet af `_build/html` til `html` og commit til VCS.

### Opdatering af eksisterende dokumentation
For at opdatere eksisterende dokumentation  slettes indholdet af `docs/rst` og herefter køres nedenstående kommandoer imens man står i `docs` mappen.
```
sphinx-apidoc -o /Users/kenneth/Code/svp-oma/om/docs/rst/ /Users/kenneth/Code/svp-oma/om/src/

make html
```

Herefter er der opdateret dokumentation tilgængelig.

Dokumentationen er lavet som "flade" `html` filer og kræver derfor ikke en specifik webserver for at fungere.

I mappen `_build/html` ligger dokumentationen nu klar. Problemet er dog at denne ikke medtages i VCS, så vi skal lige kopiere den færdige dokumentation til en anden mappe. Det er her mappen `html` kommer i brug.

Kopier indholdet af `_build/html` til `html` og commit til VCS.
