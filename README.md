# Sistema-Gestion-VeterinariaV2
### Sprint 5: 
## Ejercicio: Sistema Avanzado de Gestión para Veterinaria con Manejo de Excepciones y Logging,
## Contexto:
La Clínica Veterinaria "Amigos Peludos" ha implementado exitosamente un sistema básico para la gestión de mascotas, dueños y consultas veterinarias. Ahora desean mejorar su robustez y capacidad de monitoreo, por lo cual han solicitado incorporar manejo avanzado de excepciones y registro de eventos (logging) en el sistema existente.

## Descripción del Ejercicio:
En equipos de 2 a 3 personas, ampliarán la aplicación previamente desarrollada, integrando manejo estructurado de excepciones y un sistema de logging que permita registrar eventos importantes, advertencias y errores durante la ejecución del programa.

## 📌 Requisitos adicionales de la Aplicación:,
### Manejo de Excepciones:

- Implementar bloques `try-except` para capturar y manejar posibles errores al ingresar información, tales como:
   • Datos incorrectos o inválidos (por ejemplo, números negativos para edades).
   • Intentar registrar consultas a mascotas inexistentes.
- Proveer mensajes claros y amigables al usuario al ocurrir estos errores.

### Implementación de Logging:

- Configurar un sistema de logging utilizando el módulo `logging` de Python.
- Registrar eventos importantes como:
   • Inicio y cierre de la aplicación.
   • Registro exitoso de mascotas y consultas.
   • Captura de excepciones y errores.
- Los logs deben incluir fecha y hora, nivel del evento (INFO, WARNING, ERROR) y mensaje descriptivo.
- Almacenar los logs en un archivo llamado `clinica_veterinaria.log`.


## Interacción en consola actualizada:

- Mantener el menú principal existente, asegurándose que todos los errores estén correctamente gestionados y logueados.


## 🔧  Aspectos técnicos obligatorios adicionales:,
- Uso estructurado de excepciones con try-except.
- Configuración del módulo logging.
- Creación y gestión de archivos de log.
### Consideraciones adicionales:,
- Revisar que el código sea robusto frente a entradas inválidas.
- Proporcionar comentarios claros sobre el uso y configuración del logging.

## 📦 Entregable:
- Código fuente actualizado del proyecto (.py).
- Archivo de logs (clinica_veterinaria.log) generado durante las pruebas del programa.
- Comentarios detallados sobre el manejo de excepciones y la configuración de logging.

## Integrantes
- Daniel Cano Suarez
- Miguel Cerquera Arias
- Esteban Eusse Munera