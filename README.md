Holbertonschool-# HBNB - Holberton School Project

Este repositorio contiene la implementación del proyecto **HBNB**, desarrollado como parte del programa de Holberton School. El objetivo del proyecto es construir una aplicación web completa, comenzando desde una consola de comandos básica hasta una interfaz web funcional y un sistema de almacenamiento conectado a bases de datos.

## Contenido

El proyecto está dividido en varias partes, que evolucionan progresivamente:

1. **Consola**: 
   - Una consola interactiva para crear, actualizar, eliminar y gestionar objetos de diferentes clases (usuarios, lugares, etc.).
   - Los datos se almacenan en archivos JSON o en una base de datos relacional (según la configuración).

2. **Modelos**: 
   - Clases que representan las distintas entidades del sistema (por ejemplo, usuarios, estados, ciudades).
   - Implementación del sistema de almacenamiento.

3. **Base de datos**: 
   - Uso de MySQL para almacenar datos de manera persistente.
   - Conexión entre la aplicación y la base de datos usando SQLAlchemy.

4. **Interfaz web**:
   - Plantillas HTML para mostrar y gestionar los datos almacenados.
   - Aplicación web basada en Flask para manejar solicitudes y respuestas.

5. **Despliegue**:
   - Configuración para implementar la aplicación en un servidor.

## Requisitos

Para ejecutar este proyecto, necesitas:

- **Python 3.8+**
- **MySQL 8.0+**
- Librerías:
  - `Flask`
  - `SQLAlchemy`
  - `Jinja2`

## Uso

1. **Clonar el repositorio**:
   ```bash
   git clone https://github.com/OwenFernandez9/holbertonschool-hbnb.git
   cd holbertonschool-hbnb
