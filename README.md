
# Entrega inicial - Django MVT
---

Hola a todos! los invito a descargar y probar mi primera pagina web con Django, utilizando el modelo MVT (Model View Template).

En dicho proyecto, se crearon models para gestionar la comunicación con la DB, views para comunicar dichos models con los templates, y templates para que el usuario pueda visualizar los datos cargados en la DB y gestionar los mismos.

Para evitar utilizar el Django Admin, se crearon formularios que permitan ingresar nueva información a la DB, como asi también formularios para consultar la misma.

A su vez, se creo una app para gestionar todas las actividades relacionadas a la agenda de clientes, proveedores y artículos. Si en algún futuro se agregan nuevas funcionalidades, vamos a agregar mas apps según necesitemos, dejando los archivos del proyecto solo para configuración global del mismo.

Con respecto al frontend, se utilizo una plantilla de Bootstrap, la cual se adapto a las necesidades del cliente. Esta plantilla adaptada, se utilizo como "Template base", para poder realizar "herencia de HTML", la cual consiste en dejar "fijo" el head, header y footer, e insertar otros templates HTML diseñados para la view que corresponda, insertando dicho bloque de código en el template padre.

**¿Como utilizar la pagina web?**

Con lo primero que nos encontramos, es con el **inicio** de la pagina web.  
Contamos un menu de 3 opciones, pudiendo acceder a las URLS correspondientes a cada sección (clientes, proveedores y artículos).

![imagen](https://raw.githubusercontent.com/matilorenzatti/Django-MVT-Coder/main/app_agenda/static/app_agenda/assets/img/inicio.png)

Todas las secciones comparten la misma estructura y lógica:

- Contamos con 2 botones para acceder a los formularios correspondientes (agregar un nuevo registro, o consultar registros en base a alguna condición).
- Podemos visualizar todos los datos cargados en la DB correspondientes a la sección en la cual estemos, es decir, en la sección clientes vamos a visualizar todos los clientes cargados en la DB, y a su vez, contamos con dos botones para agregar un nuevo cliente o buscar clientes en base a una condición. Esto mismo se repite para las demás secciones.

Observemos como son cada una de las secciones, y sus formularios:

### Sección CLIENTES:

Observemos la sección correspondiente a clientes:

![imagen](https://raw.githubusercontent.com/matilorenzatti/Django-MVT-Coder/main/app_agenda/static/app_agenda/assets/img/clientes%201.png)

Formulario para ingresar un nuevo cliente:

![imagen](https://raw.githubusercontent.com/matilorenzatti/Django-MVT-Coder/main/app_agenda/static/app_agenda/assets/img/clientes%202.png)

Formulario para buscar clientes en base a alguna condición:

![imagen](https://raw.githubusercontent.com/matilorenzatti/Django-MVT-Coder/main/app_agenda/static/app_agenda/assets/img/clientes%203.png)


## Sección ARTÍCULOS:

Observemos la sección correspondiente a artículos:

![imagen](https://raw.githubusercontent.com/matilorenzatti/Django-MVT-Coder/main/app_agenda/static/app_agenda/assets/img/articulos%201.png)

Formulario para ingresar un nuevo articulo:

![imagen](https://raw.githubusercontent.com/matilorenzatti/Django-MVT-Coder/main/app_agenda/static/app_agenda/assets/img/articulos%202.png)

Formulario para buscar artículos en base a alguna condición:

![imagen](https://raw.githubusercontent.com/matilorenzatti/Django-MVT-Coder/main/app_agenda/static/app_agenda/assets/img/articulos%203.png)

## Sección PROVEEDORES:

Observemos la sección correspondiente a proveedores.

![imagen](https://raw.githubusercontent.com/matilorenzatti/Django-MVT-Coder/main/app_agenda/static/app_agenda/assets/img/provee_2.png)

Formulario para ingresar un nuevo proveedor:

![imagen](https://raw.githubusercontent.com/matilorenzatti/Django-MVT-Coder/main/app_agenda/static/app_agenda/assets/img/provee_1.png)

Formulario para buscar proveedores en base a alguna condición:

![imagen](https://raw.githubusercontent.com/matilorenzatti/Django-MVT-Coder/main/app_agenda/static/app_agenda/assets/img/provee_3.png)

---

De esta forma, podremos gestionar clientes, proveedores y artículos, de forma ágil y sencilla.

PD: En este proyecto, no se agrego al **.gitignore** la base de datos, por lo cual, al descargar el proyecto van a tener la base de datos con los registros de prueba. En este caso, pueden ingresar al panel de ADMIN, brindado por Django, y eliminar los registros correspondientes (username: admin) --> Con este usuario, se puede resetear la contraseña y acceder al panel de administrador.

Se prevé para futuras versiones, agregar las funcionalidades DELETE y UPDATE de registros, para poder crear un CRUD completo.

