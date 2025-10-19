
from django import forms

#FORMS SE USA PARA RECIVBIR Y VALIDAR DATOS QUE EL USUARIO INGRESA EN UNA PAGINA WEB
#TAMBIEN PARA GENERAR FORMULARIOS DE FORMA AUTOMATICA


def validadorCadena(valorR):
        if len(valorR)> 45:
            raise forms.ValidationError("El limite de dijitos ingresados es 44")
        elif valorR.isdigit():
            raise forms.ValidationError("Ingrese un valor valido como cadenas de texto")
        elif len(valorR)< 3:
            raise forms.ValidationError("El campo acepta un minimo de tres dijitos")
        return valorR


#EQUIPO--------------------------------------------------------------------

class FormEquipo(forms.Form):
    nombre = forms.CharField(   
        required=True,
        error_messages={'required': 'Este campo es obligatorio.'}
        ) #<-----El campo tiene que coincidir con el atributo name del input para capturar el valor
    uniforme = forms.CharField(     
        required=True,
        error_messages={'required': 'Este campo es obligatorio.'}
        )#<-----Campo


    def clean_nombre(self):#<------Metodo clean_ para validar
        nombre = self.cleaned_data['nombre']#<<------Accedemos al valor
        nombre = validadorCadena(nombre)
        return nombre

    def clean_uniforme(self):
        uniforme = self.cleaned_data['uniforme']
        uniforme = validadorCadena(uniforme)
        if uniforme.isdigit():
            raise forms.ValidationError("Ingrese un valor valido como cadenas de texto")
        return uniforme

#ESTADIO--------------------------------------------------------

class FormEstadio(forms.Form):
    nombre = forms.CharField(   
        required=True,
        error_messages={'required': 'Este campo es obligatorio.'}
        )#------CAMPO
    capacidad = forms.IntegerField(     
        required=True,
        error_messages={'required': 'Este campo es obligatorio.'}
        )#------CAMPO


    def clean_nombre(self):
        nombre = self.cleaned_data['nombre']
        nombre = validadorCadena(nombre)
        return nombre

    def clean_capacidad(self):
        capacidad = self.cleaned_data['capacidad']
        if capacidad<0:
            raise forms.ValidationError('Ingrese numeros enteros positivos')
        return capacidad
    
    
#JUGADOR------------------------------------------------------------

from django import forms

class FormJugador(forms.Form):
    nombre = forms.CharField(
        required=True,
        error_messages={'required': 'Este campo es obligatorio.'}
        )
    apellido = forms.CharField(
        required=True,
        error_messages={'required': 'Este campo es obligatorio.'}
        )
    dorsal = forms.IntegerField(
        required=True,
        error_messages={'required': 'Este campo es obligatorio.'}
        )
    nacionalidad = forms.CharField(
        required=True,
        error_messages={'required': 'Este campo es obligatorio.'}
        )
    posicion = forms.CharField(
        required=True,
        error_messages={'required': 'Este campo es obligatorio.'}
        )

    # Validadores personalizados
    def clean_nombre(self):
        nombre = self.cleaned_data['nombre']
        nombre = validadorCadena(nombre)
        return nombre

    def clean_apellido(self):
        apellido = self.cleaned_data['apellido']
        apellido = validadorCadena(apellido)
        return apellido

    def clean_dorsal(self):
        dorsal = self.cleaned_data['dorsal']
        if dorsal <= 0:
            raise forms.ValidationError('El campo acepta números enteros superiores a 0.')
        return dorsal

    def clean_nacionalidad(self):
        nacionalidad = self.cleaned_data['nacionalidad']
        nacionalidad = validadorCadena(nacionalidad)
        return nacionalidad

    def clean_posicion(self):
        posicion = self.cleaned_data['posicion']
        posicion =  validadorCadena(posicion)
        return posicion


#PARTIDO----------------------------------------------------------------------------
class FormPartido(forms.Form):
    fecha = forms.DateTimeField(
        required=True,
        error_messages={'required':'Este campo es obligatorio.'}
        )

    def clean_fecha(self):
        fecha = self.cleaned_data['fecha'] 
        return fecha

#ARBITRO-------------------------------------------------------------------------------
class FormArbitro(forms.Form):
    nombre = forms.CharField(   
        required=True,
        error_messages={'required': 'Este campo es obligatorio.'}
        )
    apellido = forms.CharField( 
        required=True,
        error_messages={'required':'Este campo es obligatorio.'}
        )
    edad = forms.IntegerField(  
        required=True,
        error_messages={'required':'Este campo es obigatorio.'}
        )
    nacionalidad = forms.CharField(
        required=True,
        error_messages={'required':'Este campo es obligatorio.'}
        )


    def clean_nombre(self):
        nombre = self.cleaned_data['nombre']
        nombre = validadorCadena(nombre)
        return nombre

    def clean_apellido(self):
        apellido = self.cleaned_data['apellido']
        apellido = validadorCadena(apellido)
        return apellido

    def clean_edad(self):
        edad = self.cleaned_data['edad']
        if edad<=0:
            raise forms.ValidationError('El campo acepta numeros enteros positivos')
        return edad

    def clean_nacionalidad(self):
        nacionalidad = self.cleaned_data['nacionalidad']
        nacionalidad = validadorCadena(nacionalidad)
        return nacionalidad



#USUARIO------------------------------------------------------------

class FormUsuario(forms.Form):
    nombre = forms.CharField()
    correo = forms.CharField()
    contrasena = forms.CharField(label='Contraseña', widget=forms.PasswordInput())









#NO ESTA CONECTADO CON MODEL ASI QUE PARA GUARDAR LOS DATOS 
# SE DEBE DE HACER EN VISTA LO SIGUIENTE (view.py):


"""📌 Para que los errores aparezcan en el navegador:

Tu plantilla HTML (userRegistration.html) debe tener algo como esto:

<form method="POST">
    {% csrf_token %}
    {{ form.as_p }}  <!-- Esto renderiza el formulario con errores incluidos -->
    <button type="submit">Registrarse</button>
</form>


O si lo haces de forma personalizada:

<form method="POST">
    {% csrf_token %}

    <label for="id_nombre">Nombre:</label>
    {{ form.nombre }}
    {{ form.nombre.errors }}

    <label for="id_email">Email:</label>
    {{ form.email }}
    {{ form.email.errors }}

    <!-- Resto del formulario -->

    <button type="submit">Enviar</button>
</form>

🔍 Ejemplo de cómo se vería el error:

Si alguien escribe un nombre de más de 20 caracteres, Django mostrará debajo del campo:

El largo máximo del nombre son 20 caracteres."""

