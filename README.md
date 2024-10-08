# Generador de QRs para Charlas - UTN

## Descripción
Esta aplicación, desarrollada en Python 3.12 usando la biblioteca Tkinter, permite a los usuarios generar códigos QR para inscribirse en charlas dentro de la Facultad de la UTN vía mail. Es una herramienta simple y efectiva para facilitar la gestión de inscripciones a eventos, permitiendo a los organizadores y participantes interactuar de manera más ágil.

## Características
- **Generación de QR personalizada**: Cada código QR contiene la información del evento y el nombre del participante.
- **Interfaz gráfica**: Aplicación sencilla e intuitiva mediante Tkinter, que facilita el uso sin necesidad de conocimientos técnicos.
- **Exportación de QR**: Los códigos QR pueden ser exportados como imágenes PNG a formato mail.
- **Validación de datos**: Se asegura que los campos requeridos (nombre y evento) estén completos antes de generar el QR.
- **Historial de registros**: Opción para mantener un registro de los QR generados y los participantes inscritos (opcional).

## Requisitos
- Python 3.12
- Tkinter (instalado por defecto en la mayoría de las instalaciones de Python)
- qrcode (biblioteca para generar códigos QR)

---

# Convenciones de git

## Convenciones de Commits
Los commits en este proyecto siguen un conjunto de convenciones que utilizan emojis para categorizar y describir los cambios realizados. A continuación se detallan los principales tipos de commits y sus usos:

- RELEASE(commit_msg): Version final con integración de varias funcionalidades
- STABLE(commit_msg): Commit de una versión estable o probada de una funcionalidad o integración de características.
- ADD(commit_msg): Commit que añade nuevo desarrollo a una funcionalidad existente.
- MOD(commit_msg): Commit que modifica el código de una funcionalidad existente.
- REF(commit_msg): Commit que realiza refactorizaciones en una funcionalidad para mejorar su estructura o rendimiento.
- FIX(commit_msg): Commit que corrige un error específico en una funcionalidad.

```
    git commit -m "FIX(Fix de button guardar en pantalla de inicio ticket_1203)"
```


## Convenciones de ramas:
Este proyecto utiliza ramas para organizar el desarrollo y las características. Aquí están los principales tipos de ramas utilizadas:

MAIN: Rama principal del proyecto que refleja el estado estable y producible.
FEATURE: Rama para el desarrollo de una funcionalidad o caracteristicas del sistema.