# POO_2022_C1
Este es un curso introductorio a la programación Orientada a Objetos. Se espera fomentar en el estudiante la habilidad de analizar y proponer  solución a problemas que involucren el uso de un lenguaje de programación y el paradigma de programación orientado a objetos (POO).   El curso cubre los conceptos básicos del paradigma de POO, tales como clases, objetos, métodos, interfaces y polimorfismo. 
## Google Colab: ciencia de datos

**Subir archivos y usarlos en bloques de código**

En Ciencias de Datos necesitamos datos. Para poder usar datos en Google Colab, en la barra izquierda en Archivos (ícono de carpeta), veremos que tenemos una carpeta *sample_data*, dentro de la cuál Colab ya nos provee de algunos datos de prueba.

Para subir archivos simplemente los arrastramos a este menú. Ten en cuenta que después de un tiempo que dejes de usar el Notebook estos archivos serán eliminados.

Dependiendo del tipo de archivo, Colab permitirá mostrarnos su contenido haciendo doble clic en el mismo. Por ejemplo, para archivos ***.csv*** se abrirá una vista de tabla.

Otra forma de subir archivos es haciendo clic en la primera opción (de las tres que se muestran arriba de las carpetas), y seleccionando el archivo a subir.

La tercera opción (la de la carpeta con el logo de Drive) sirve para activar la opción de usar archivos de Drive. Al hacer clic te pedirá que ejecutes un bloque de código (autogenerado) y que pegues un código de autorización, el cuál obtendrás a través de un link que el mismo bloque mostrará. Después de esto en los Archivos aparecerá la carpeta *drive*, donde se encuentran los archivos de tu Drive listos para usarse.

Recordemos que podemos usar comandos de terminal en un bloque de código. Para usar archivos en estos comandos, las rutas se forman de acuerdo al árbol de archivos que nos muestra el panel de Archivos. Por ejemplo, para usar un archivo de drive, su ruta sería `drive/MyDrive/<archivo>`. Sabrás si estas usando una ruta correcta si obtienes autocompletado al escribirla.

**Librerías de Google Colab**

Cuando creamos un Notebook en Colab, este ya tiene algunas librerías instaladas. Algunas de estas son:

- 📊 **matplotlib**: Generación de gráficos a partir de listas o arrays.
- 🧑‍💻 **numpy**: Cómputo científico para la manipulación de vectores.
- 🧑‍💻 **pandas**: Manipulación y análisis de datos de tablas y series temporales.
- 🧑‍💻 **scipy**: Herramientas y algoritmos matemáticos.
- 📊 **seaborn**: Visualización de datos estadísticos.

Algunas de estas librerías funcionan bien con Notebooks. Algunas proveen de métodos que al ejecutarlos nos muestran resultados gráficos, como gráficos estadísticos.

**Snippets de código**

En la barra lateral, en la opción Fragmentos de código (ícono de brackets) podemos explorar algunos fragmentos (snippets) de código para realizar tareas comunes. En la barra de búsqueda, si buscamos `visual`, tendremos algunos snippets para visualización de datos, los cuáles usan las librerías que Colab ya provee.

Para usar un snippet basta con hacer doble clic sobre el mismo y se insertará un bloque de código con el snippet, listo para ser ejecutado.

Atajos de teclado

Si presionamos `Ctrl + Shift + P` aparecerá una barra de comandos (muy parecida a la de VSCode). Esta barra nos permite buscar entre los distintos comandos o acciones que queramos hacer en nuestro proyecto.

Un comando muy útil es el de mostrar atajos.

## Utilizar Deepnote

Deepnote es un servicio en la nube, basado en Jupyter Notebooks, el cuál no requiere configuración y, a diferencia de Colab, trabaja a nivel de proyecto.

Deepnote provee colaboración en tiempo real, integración con múltiples Apps y acceso a una terminal o línea de comandos. También permite almacenar variables de entorno y publicar proyectos (esto te puede servir para construir un portafolio).

Para trabajar con Deepnote nos dirigimos a [deepnote.com](http://deepnote.com). Tendremos que iniciar sesión y lo podremos hacer con Google o con Github. Una vez iniciada sesión veremos nuestro Dashboard.

Deepnote trabaja a nivel de proyectos. Para crear un proyecto hacemos clic en el botón `+ New Project`. Esto creará el proyecto con nuestro primer Notebook.

Para ejecutar los bloques de código de un Notebook hacemos clic en `> Run notebook` en la parte superior.

Para subir archivos simplemente los arrastramos desde nuestro equipo al panel izquierdo donde se encuentra el árbol de archivos (Files).

En la barra lateral, en `Integrations` (ícono de 4 cuadrados), podemos seleccionar las integraciones con otras apps que queramos, haciendo clic en `Add` en la integración. Dependiendo de la integración se deben seguir algunos pasos. Por ejemplo, para integrar con Google Drive debemos autorizar a Drive y luego darle un nombre a la integración. Después de esto, la integración aparecerá arriba en la parte de Active Integrations.

Algunas integraciones nos proveen de un botón `How to use` para saber como usarlas. Por ejemplo, para acceder a nuestro drive usamos la ruta `/datasets/drive`

Al igual que Google Colab (y otras herramientas), Deepnote provee a los proyectos librerías de comunes de ciencias de datos.

Una diferencia importante con Colab, es que en Colab podemos agregar solo bloques de código o de texto cuando nos posicionamos entre dos bloques. En Deepnote, tenemos las opciones Block y Code, donde en Block se nos muestra una lista extensa con más tipos de bloque.

Un bloque especial es el de Graph, el cuál nos permite visualizar una gráfica de un dataframe de forma interactiva, con un menú de opciones al lado.

Deepnote también tiene una barra de comandos. Para abrirla usamos el atajo `Ctrl + P` (nota que es diferente al de Colab).

Podemos publicar nuestro proyecto. Para ello en la barra de navegación hacemos clic en Share y activamos la opción Share Project. Una vez publicado, cualquiera que tenga el link del proyecto podrá abrirlo y verlo. También podemos especificar que pueden hacer con el Notebook (si pueden solo verlo o también pueden editarlo).

En este mismo menú también podemos administrar los colaboradores del proyecto. La sección Publishing sirve para publicar el proyecto pero como si fuese una página web, la cuál podremos compartir en redes sociales.

En la barra lateral, en la opción `Terminal` (ícono de terminal) podemos ver las terminales de nuestro proyecto. Al principio no habrá ninguna, pero una vez agregada una podremos usar una terminal en nuestro proyecto.

 # Creando un ambiente virtual 
## Creación de ambiente Virtual:

https://cmder.net/

 pip install virtualenv -->para instalar entornos virtuales
 
 virtualenv env_nombre_proyecto  ->Crear el entorno virtual
 
 .\env_nombre_proyecto\Scripts\activate  ->activar el entorno
 
 python --version -->para saber que version de python tiene mi entorno
 
 pip freeze -->para saber que tiene instalado mi entorno
 
 deactivate  --> desactivar mi entorno
 
 py proyecto.py -->correr en la terminarl el archivo py
 
 touch nombre_archivo.py  -->crear un archivo desde la terminal
 

# Comandos de Git


**git init**: lo usamos para determinar la carpeta en la que vamos a trabajar.

git status: lo usamos para saber si tenemos un archivo añadido o borrado en nuestro proyecto, para saber en la rama en la que estamos y si tenemos commits.

git add: es para añadir un archivo a nuestra rama seguidamente ponemos entre comillas el nombre de nuestro archivo o poner un punto para añadir todos los archios de nuestra carpeta.

git rm: lo usamos para borrar un archivo que hayamos añadido, para eliminarlo por completo de nuestra rama usamosgit rm --cached.

git commit: se usa para añadir un commit a nuestra rama, también podemos ponerle un -m seguidamente ponemos entre comillas nuestro ensaje.

git config: muestra configuraciones de git también podemos usar –list para mostrar la configuración por defecto de nuestro git y si añadimos --show-origin inhales nos muestra las configuraciones guardadas y su ubicación.

git config --global user.name: cambia de manera global el nombre del usuario, seguidamente ponemos entre comillas nuestro nombre.

git config --global user.email: cambia de manera global el email del usuario, seguidamente ponemos entre comillas nuestro nombre.

git log: se usa para ver la historia de nuestros archivos, los commits, el usuario que lo cambió, cuando se realizaron los cambios etc. seguidamente ponemos el nombre de nuestro archivo.
