# Filament Management

Kleines Flask-Projekt zur Verwaltung von 3D-Filament-Rollen (Spools).


Alle API-Routen sind unter folgendem Prefix erreichbar:
- `http://localhost:5000/api`

## Datenmodell:

| Feld | Typ | Beschreibung |
|------|-----|--------------|
| `id` | `string` | Eindeutige ID der Spool |
| `name` | `string` | Name der Rolle |
| `manufacturer` | `string` | Hersteller |
| `material` | `string` | Material, z. B. PLA |
| `color` | `string` | Farbe |
| `total_weight_grams` | `integer` | Gesamtgewicht in Gramm |
| `remaining_weight_grams` | `integer` | Verbleibendes Gewicht in Gramm |
| `created_at` | `string` | Erstellungszeitpunkt |
| `updated_at` | `string` | Letzte Änderung |
| `archived` | `boolean` | Ob die Rolle archiviert ist |
### Beispiel

```json
{
  "id": "UUID",
  "name": "PLA Black",
  "manufacturer": "esun",
  "material": "PLA",
  "color": "Black",
  "total_weight_grams": 1000,
  "remaining_weight_grams": 850,
  "created_at": "2026-03-27T12:34:56",
  "updated_at": "2026-03-27T12:40:00",
  "archived": false
}
```

## API-Endpunkte

| Methode | Endpoint | Typ | Beschreibung |
|---------|----------|-----|--------------|
| `GET` | `/api/spools` | `array` | Gibt alle Spools zurück |
| `POST` | `/api/spools` | `object` | Erstellt eine neue Spool |
| `GET` | `/api/spools/<spool_id>` | `object` | Gibt eine einzelne Spool zurück |
| `PATCH` | `/api/spools/<spool_id>` | `object` | Ändert eine Spool teilweise |
| `POST` | `/api/spools/<spool_id>/consume` | `object` | Verbraucht Filament |
| `POST` | `/api/spools/<spool_id>/archive` | `object` | Archiviert eine Spool |

## Query-Parameter für `GET /api/spools`

| Parameter | Typ | Beschreibung |
|-----------|-----|--------------|
| `material` | `string` | Filter nach Material |
| `color` | `string` | Filter nach Farbe |
| `archived` | `boolean` | Filter nach archiviertem Status |

## Pflichtfelder für `POST /api/spools`

| Feld | Typ |
|------|-----|
| `name` | `string` |
| `manufacturer` | `string` |
| `material` | `string` |
| `color` | `string` |
| `total_weight_grams` | `integer` |

## Pflichtfelder für `POST /api/spools/<spool_id>/consume`

| Feld | Typ |
|------|-----|
| `grams` | `integer` |