# Nützliche Patterns

## Suche nach Schweizer Telefonnummern

```
[\d \+]{10,}
```

## Ungültige Schweizer PLZ

### Einzelne Abfragen

- Suche nach dreistelligen Zahlen: `\b\d{3}\b`
- Suche nach fünfstelligen Zahlen: `\b\d{5}\b`
- Suche nach vierstelligen Zahlen mit führender Null: `\b0\d{3}\b`

### Mit Capturing Group

```
\b(\d{3}|\d{5}|0\d{3})\b
```

### Mit negative Lookahead

Prüfung (nur Zahlen)

```
(?!(\b[1-9]\d{3}\b))(\b\d+\b)
```

Prüfung (alle Zeichen)

```
(?!(\b[1-9]\d{3}\b))(\b.+\b)
```
