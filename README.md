# Programmeertheorie - RailNL

Dit project maakt een lijnvoering op basis van twintig trajecten door heel Nederland. Het doel van het project is om een zo hoog mogelijke score te krijgen (tussen 0 en 10.000). Het doel hierbij is dat de treinen zoveel mogelijk stations bereiken binnen een tijdsframe van 3 uur. Gedurende dit project hebben wij een aantal verbeteringen doorgevoerd om de score gaandeweg te doen stijgen.

### Wat zijn de trajecten waarover treinen gedurende de dag heen en weer rijden?

#### Opdracht 1.1 - Noord en Zuid Holland
- 22 stations
- maximaal zeven trajecten
- tijdsframe: 120 minuten
- voorwaarde: alle verbindingen worden bereden

- .csv bestand met tussenliggende spoorverbindingen
- .csv bestand met locaties stations


#### Opdracht 1.2 - Toets met formule
K = p*10.000 - (T*100 + Min)

- K = kwaliteit lijnvoering (max. 10.000)
- p = fractie van bereden treinsporen (tussen 0 en 1)
- T = aantal trajecten
- Min = aantal minuten van alle trajecten samen


#### Opmerkingen
- Wij hebben geprobeerd om zoveel mogelijk object-georienteerd te programmeren
- Wij hebben geprobeerd om zoveel ons project zoveel mogelijk te visualiseren. In de map "visualisations" staan twee plots; een plot visueliseert de trajecten die de treinen afleggen en de andere laat zien hoeveel verbetering elk algoritme oplevert


## Lokaal runnen

Clone het project

```bash
  git clone https://link-to-project
```

Ga naar de juiste directory

```bash
  cd my-project
```

Installeer de dependecies

```bash
  pip3 install requirements.txt
```

Run het project

```bash
  python3 main.py
```
  

## Auteurs

- [@Julia Smeets](https://github.com/Cliothalia)
- [@Max Westerman](https://github.com/maxwesterman)
- [@Mart Marconi](https://github.com/Martino-Marconi)

