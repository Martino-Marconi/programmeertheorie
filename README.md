# Programmeertheorie - RailNL

Dit project maakt een lijnvoering op basis van twintig trajecten door heel Nederland. Het doel van het project is om een zo hoog mogelijke score te krijgen (tussen 0 en 10.000). Het doel hierbij is dat de treinen zoveel mogelijk stations bereiken binnen een tijdsframe van 2 uur. Gedurende dit project hebben wij een aantal verbeteringen doorgevoerd om de score gaandeweg te doen stijgen.

### Wat zijn de trajecten waarover treinen gedurende de dag heen en weer rijden?

### Opdracht - Nederland
In deze opdracht maken wij gebruik van:
- 22 stations
- maximaal zeven trajecten
- tijdsframe: 120 minuten
- voorwaarde: alle verbindingen worden bereden

Als onderdeel van de opdracht hebben wij meegekregen:
- .csv bestand met tussenliggende spoorverbindingen
- .csv bestand met locaties stations


### Opdracht - Toets met formule

De score bereken wij op basis van de volgende formule:

K = p*10.000 - (T*100 + Min)

- K = kwaliteit lijnvoering (max. 10.000)
- p = fractie van bereden treinsporen (tussen 0 en 1)
- T = aantal trajecten
- Min = aantal minuten van alle trajecten samen


### Opmerkingen
- Wij hebben geprobeerd om zoveel mogelijk object-georienteerd te programmeren
- Wij hebben geprobeerd om zoveel ons project zoveel mogelijk te visualiseren. In de map "visualisations" staan twee plots; een plot visueliseert de trajecten die de treinen afleggen en de andere laat zien hoeveel verbetering elk algoritme oplevert

### Optimalisaties

#### Random algoritme:
Het random algoritme kiest een random beginstation uit en ook een willekeurige volgende verbinding. Het doel van het random algoritme is om een "basisscore" te genereren die we kunnen gebruiken om te testen of onze optimalisaties een posititef effect hebben.

#### Semi-Random

#### Shortest connection:
Het "shortest connection algortime" kiest het beginstation en de volgende stops op basis van de kortste connectie. Het idee hierachter is dat er op deze manier meer stations bezocht kunnen worden dan bij het random algoritme omdat de treinen hierbij efficiënter te werk gaan.

#### Random met hill climber
#### Semi-Random met hill climber
#### Shortest connection with hill climber


### Lokaal runnen

Clone het project

```bash
  git clone git@github.com:Martino-Marconi/programmeertheorie.git
```

Ga naar de juiste directory

```bash
  cd programmeertheorie
```

Installeer de dependecies

```bash
  pip3 install requirements.txt
```

Run het project

```bash
  python3 main.py
```

## Gebruik

```bash
  python3 main.py <optie1> <optie2> <optie3> <optie4> 
```
- optie1 = algoritme (random, semi-random, shortest-connection)
- optie2 = runs (aantal runs)
- optie3 = treinen (aantal treinen)
- optie4 = duur (tijd in seconden)

## Auteurs

- [@Julia Smeets](https://github.com/Cliothalia)
- [@Max Westerman](https://github.com/maxwesterman)
- [@Mart Marconi](https://github.com/Martino-Marconi)

