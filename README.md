# Filament Management

Smale Flask-Project to manage your 3D-Fillament Spools.

Use the WebUI to easily manage your spools - Web Demo:
- [http://fil-demo.jonasheilig.de/](http://fil-demo.jonasheilig.de/)


All API-Routs are available at following URL (Per Terminal) to create your own scripts or clients (Not on Demo Server - Please use WebUI for Demo):
- https://[your-URL]/api/

Setup => After setting up the project, please call the following URL to initialize the database:
- https://[your-URL]/api/init

## Datamodel of the DB:

| Feld                     | Typ       | Descripton             |
|--------------------------|-----------|------------------------|
| `id`                     | `string`  | Unice ID               |
| `name`                   | `string`  | Name of the Spool      |
| `manufacturer`           | `string`  | Manufacrur             |
| `material`               | `string`  | e.g. PLA               |
| `color`                  | `string`  | Color                  |
| `total_weight_grams`     | `integer` | Weight of full Spool   |
| `remaining_weight_grams` | `integer` | remain weight of spool |
| `created_at`             | `string`  | Date of creation       |
| `updated_at`             | `string`  | Date of Last Update    |
| `archived`               | `boolean` | Spool archived?        |
### Èxample

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

## API-Routes

| Methode | Endpoint                         | Typ      | Beschreibung                                    |
|---------|----------------------------------|----------|-------------------------------------------------|
| `GET`   | `/api/spools`                    | `array`  | All Spools                                      |
| `POST`  | `/api/spools`                    | `object` | Create new Spool                                |
| `GET`   | `/api/spools/<spool_id>`         | `object` | Only gives Spool with the send ID               |
| `PATCH` | `/api/spools/<spool_id>`         | `object` | Change Infos of a specific spool                |
| `POST`  | `/api/spools/<spool_id>/consume` | `object` | Consume a Amount of the spool with the given ID |
| `POST`  | `/api/spools/<spool_id>/archive` | `object` | Archive a Spool                                 |

## Query Parameters for `GET /api/spools`

| Parameter  | Typ       | Beschreibung              |
|------------|-----------|---------------------------|
| `material` | `string`  | filter by material        |
| `color`    | `string`  | filter by color           |
| `archived` | `boolean` | filter by archived Status |

## Mandatory fields for `POST /api/spools`

| Feld                 | Typ       |
|----------------------|-----------|
| `name`               | `string`  |
| `manufacturer`       | `string`  |
| `material`           | `string`  |
| `color`              | `string`  |
| `total_weight_grams` | `integer` |

## Mandatory fields for `POST /api/spools/<spool_id>/consume`

| Feld    | Typ       |
|---------|-----------|
| `grams` | `integer` |
