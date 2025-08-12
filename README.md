# Utility Package

This package contains the core set of utilities that are commonly used by other
functions.

The package includes the following sub-packages:

- database
- geographic
- plotting
- units

In addition, the package also includes modules with common utilities for
interaction with files and time and a `plotting` package that contains functions
to make figures.

### `database` package

This package includes two modules: one for interface with a postgres database
and another for sqlite database. Each module includes functions to create a
connection with the database, execute a query, read and upload data, and close
connection.

### `geographic` package

This package includes the `geojson` module to create output in compliance with
the GeoJSON spec.

### `units` package

This package includes universal constants and a module convert quantities from
one system of units to another.
