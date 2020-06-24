# data-science
## https://medcabinet10.herokuapp.com/

## FLASK web application that returns the Effect and Flavor request with recommendations for strains of Cannabis  

# Example
```
https://medcabinet10.herokuapp.com/predict?effect=Creative&flavor=Apple
```
```
{
  'effect':'Creative', 
  'flavor':'Apple'
  }
```
# = 
```
[{"description":{"0":"Alien Sour Apple is a sativa-dominant hybrid that mixe....}]
```
## Setup 
```
pipenv shell
```
## Usage
```
FLASK_APP=web_app flask run
```