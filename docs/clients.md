Billing documentation
=====================

Clients
-------

### Clients table

**tbl_clients**

| field                    | type     | comment                                                    |
|:-------------------------|:--------:|:-----------------------------------------------------------|
| id                       | uuid     | this field we use to split data by shards                  |
| created_at               | datetime | when the client was registered                             |
| updated_at               | datetime | when the client profile was modified last time             |
| name                     | varchar  | full name                                                  |
| country                  | varchar  | it could be also country code or fk to the countries table |
| city                     | varchar  | it could be also a fk to the cities table                  |

We don't make additional geographical tables to store countries & cities to not complicate that.
