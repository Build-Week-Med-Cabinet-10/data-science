# data-science
## https://medcabinet10.herokuapp.com/

## FLASK web application that returns the Effect and Flavor request with recommendations for strains of Cannabis  


```
{
  'effect':'Creative', 
  'flavor':'Apple'
  }
```

# = 

```
[{"description":{"0":"Alien Sour Apple is a sativa-dominant hybrid that mixes the genetics of Alien Dawg with Sour Apple. Bred by Franchise Genetics, Alien Sour Apple tastes sweet and sour, like a Granny Smith apple. Its heady sativa effects provide a lift of energy and incite an optimistic sense of euphoria."},"effect":{"0":"Euphoric,Relaxed,Uplifted,Creative,Happy"},"flavor":{"0":"Sweet,Lemon,Apple"},"id":{"0":82},"rating":{"0":4.6},"strain":{"0":"Alien-Sour-Apple"},"type":{"0":"hybrid"}},{"description":{"0":"Colorado Seed Inc. pays homage to new school and old school genetics in Cello Sweet OG. This cross combines DJ Short\u2019s Flo, a living cannabis virtuoso, and Secret Garden OG, CO Seed\u2019s Kush\u00a0bomb, to create a connoisseur-quality strain with potency and dimension. With effects that range from cerebral to sedative, this strain contains movements like a symphony, rising into a meditative mind with a decrescendo into full-body relaxation.\u00a0"},"effect":{"0":"Sleepy,Relaxed,Uplifted,Creative,Euphoric"},"flavor":{"0":"Sweet,Spicy/Herbal,Pineapple"},"id":{"0":469},"rating":{"0":4.0},"strain":{"0":"Cello-Sweet-Og"},"type":{"0":"hybrid"}}]
```

## Setup 
```
pipenv shell
```


## Usage
```
FLASK_APP=web_app flask run
```