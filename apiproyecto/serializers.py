from rest_framework import serializers
from apiproyecto.models import Alumnos, Personal, PeriodosEscolares, Carreras

class AlumnosSerializers(serializers.ModelSerializer):
    class Meta:
        model = Alumnos
        fields = ('no_de_control','apellido_paterno','apellido_materno','nombre_alumno','nip')
        # """
        # fields = ('no_de_control','carrera','reticula','especialidad','nivel_escolar','semestre','clave_interna','estatus_alumno',
        #         'plan_de_estudios','apellido_paterno','apellido_materno','nombre_alumno','curp_alumno','fecha_nacimiento',
        #         'sexo','estado_civil','tipo_ingreso','periodo_ingreso_it','ultimo_periodo_inscrito','promedio_periodo_anterior',
        #         'promedio_aritmetico_acumulado','creditos_aprobados','creditos_cursados','promedio_final_alcanzado','tipo_servicio_medico',
        #         'clave_servicio_medico','escuela_procedencia','tipo_escuela','domicilio_escuela',
        #         'entidad_procedencia','ciudad_procedencia','correo_electronico','foto','firma','periodos_revalidacion',
        #         'indice_reprobacion_acumulado','becado_por','nip','tipo_alumno','nacionalidad','usuario',
        #         'fecha_actualizacion','folio','horario_curso_java','pago_curso_java','periodo_estatus',
        #         'fecha_titulo','op_titula','cedula','libro','hoja','ultimo_login','id_sesion','ip','autoriza_padres')
        #         """
        
class PersonalSerializers(serializers.ModelSerializer):
    class Meta:
        model = Personal
        fields = '__all__'
        """
        exclude = ('id','rfc','clave_centro_seit','clave_area','curp_empleado','no_tarjeta','apellidos_empleado','horas_nombramiento','nombramiento',
                'clases','ingreso_rama','inicio_plantel','domicilio_empleado','colonia_empleado'
                'codigo_postal_empleado','localidad','telefono_empleado','sexo_empleado','estado_civil',
                'fecha_nacimiento','lugar_nacimiento','institucion_egreso','nivel_estudios','grado_maximo_estudios',
                'estudios','fecha_termino_estudios','fecha_titulacion','cedula_profesional','especializacion',
                'idiomas_domina','status_empleado','foto','firma','correo_electronico','padre','madre','conyuge','hijos','num_acta',
                'num_libro','num_hoja','num_ano','num_cartilla_smn','ano_clase','pigmentacion',
                'pelo','frente','cejas','ojos','nariz','boca','estaturamts','pesokg','sanas_visibles',
                'pais','pasaporte','fm','inicio_vigencia','termino_vigencia','entrada_salida',
                'observaciones_empleado','area_academica','tipo_personal','tipo_control','rfc2',
                'tipo_trabajador')
        """

class PeriodosEscolaresSerializers(serializers.ModelSerializer):
    class Meta:
        model = PeriodosEscolares
        fields = '__all__'
        """
        exclude = ('id','periodo','identificacion_larga','identificacion_corta','status','fecha_inicio',
                'fecha_termino','inicio_vacacional_ss','termino_vacacional_ss','num_dias_clase',
                'inicio_especial','fin_especial','cierre_horarios','cierre_seleccion','inicio_enc_estudiantil',
                'fin_enc_estudiantil','inicio_sele_alumnos','fin_sele_alumnos','inicio_vacacional',
                'termino_vacacional','parcial1_inicio','parcial1_fin','parcial2_inicio','parcial2_fin','parcial3_inicio',
                'parcial3_fin','filtro','nota','inicio_captura_calificaciones')
        """

class CarrerasSerializers(serializers.ModelSerializer):
    class Meta:
        model = Carreras
        fields = '__all__'
        """
        field = ('carrera','reticula','nivel_ewcolar','clave_oficial','nombre_carrera','nombre_reducido',
                'siglas','carga_maximo','carga_minimo','fecha_inicio','fecha_termino','clave_cosnet','creditos_totales',
                'fichas','modalidad')
        """