# Übungen

## Unterschiedliche Schreibweisen

### Ennio

Ennio - Ennjo - Ennyo - Enio - Enjo - Enyo

```
En.*?o
```

### Marleen

Marleen - Marlene - Marlen

```
Marle+ne?
```

## Zahlen über 999

### Ohne Tausenderstrich

```
\b\d{4,}\b
```

### Mit Tausenderstrich

```
\b[\d']{4,}\b
```

### Mehrere Leerzeichen durch eines ersetzen

Nach ` {2,}` suchen (Leerschlag im Pattern beachten!) und mit einem einfachen Leerschlag ersetzen.
