print('Bienvenido al programa para facilitar el diagnóstico de COVID-19 (Coronavirus) ')
nombre = str(input('Ingrese su nombre completo: ')) + ','
edad = int(input('Ingrese su edad: '))
print('Hola',nombre, "favor de contestar todas las preguntas del siguente diagnóstico exclusivamente con 'Si' o 'No'")
neumonia = str(input('¿Cuenta con diagnóstico clínico y radiológico de neumonía?: '))
if neumonia == 'si' or neumonia == 'Si' or neumonia == 'SI':
    print('Su caso es SOSPECHOSO, por favor pongase en contacto con su servicio medico local.')
else:
    temp = int(input('Ingrese su temperatura corporal: '))
    if temp > 37:
        fiebre = True
        cant_sin_res = 0
        tos = str(input('¿Tiene tos?: '))
        odinofagia = str(input('¿Tiene odinofagia (dolor al tragar)?: '))
        dif_resp = str(input('¿Tiene dificultad respiratoria?: '))
        if tos == 'si' or tos == 'Si' or tos == 'SI':
            tos = True
            cant_sin_res += 1
        if odinofagia == 'si' or odinofagia == 'Si' or odinofagia == 'SI':
            odinofagia = True
            cant_sin_res += 1
        if dif_resp == 'si' or dif_resp == 'Si' or dif_resp == 'SI':
            dif_resp = True
            cant_sin_res += 1
        if cant_sin_res == 0:
            if edad >= 60:
                filtro = True
                print('Su caso NO es sospechoso, pero pertence al "grupo de riesgo"')
            else:
                filtro = True
                print('Su caso NO es sospechoso')
    elif edad >= 60:
        print('Su caso no es sospechoso pero pertence al "grupo de riesgo"')
        filtro = True
        tos = False
        odinofagia = False
        dif_resp = False
    else:
        print('Su caso NO es sospechoso')
        filtro = True
        tos = False
        odinofagia = False
        dif_resp = False
    if tos == True or odinofagia == True or dif_resp == True:
        viajes_ext = str(input('¿Viajó al exterior recientemente?: '))
        cont_casos = str(input('¿Tuvo contacto con casos sospechosos?: '))
        trans_local = str(input('¿Estuvo en lugares de concurrencia masiva?: '))
        if viajes_ext == 'si' or viajes_ext == 'Si' or viajes_ext == 'SI':
            viajes_ext = True
        if cont_casos == 'si' or cont_casos == 'Si' or cont_casos == 'SI':
            cont_casos = True
        if trans_local == 'si' or trans_local == 'Si' or trans_local == 'SI':
            trans_local = True
        if viajes_ext == True or cont_casos == True or trans_local == True:
            filtro = True
            print('Su caso es SOSPECHOSO, por favor pongase en contacto con su servicio medico local.')
        else:
            per_salud = str(input('¿Es usted personal de la salud?: '))
            if per_salud == 'si' or per_salud == 'Si' or per_salud == 'SI' and cant_sin_res >= 1:
                per_salud = True
                filtro = True
                print('Su caso es SOSPECHOSO, por favor pongase en contacto con su servicio médico local.')
            elif cant_sin_res >= 2:
                filtro = True
                print('Su caso es "AUTÓCTONO", por favor pongase en contacto con su servicio médico local.')
            elif edad >= 60:
                filtro = True
                print('Su caso NO es sospechoso, pero pertence al "grupo de riesgo"')
            else:
                filtro = True
                print('Su caso NO es sospechoso')
    if filtro == True:
        pass
    else:
        if edad >= 60:
            print('Su caso NO es sospechoso, pero pertence al "grupo de riesgo"')
        else:
            print('Su caso NO es sospechoso')