# Evaluacion Rockstar 5G

## Requisitos:
- Python 3
- Docker

## Instrucciones:

- Clonar este repositorio.
- Crear imagen de docker.
```
docker build -t <nombre_imagen>
```
- Correr la imagen en modo developer (salir con [CTRL] + [C])
```
docker run  -it -p 6000:5000 --rm --name <nombre_contenedor> <nombre_imagen>
```
- Correr la imagen en modo servicio
```
docker run  -it -p 6000:5000 -d --rm --name <nombre_contenedor> <nombre_imagen>
```
