# -*- coding: utf-8 -*-
import xlwt

from django.http import HttpResponse
from django.contrib.auth.models import User

from personas.models import Persona
from proyectos.models import Proyecto
from grupos.models import Pago


def export_proyectos_xls(request):
    response = HttpResponse(content_type='application/ms-excel')
    response['Content-Disposition'] = 'attachment; filename="proyectos.xls"'
    wb = xlwt.Workbook(encoding='utf-8')
    ws = wb.add_sheet('Proyectos')
    row_num = 0
    font_style = xlwt.XFStyle()
    font_style.font.bold = True
    columns = ['Nombre', 'Grupo', 'Categoria', 'Fecha de creacion',
               'FechaPresentacion', 'Lugar', 'Valorde la boleta',]
    for col_num in range(len(columns)):
        ws.write(row_num, col_num, columns[col_num], font_style)
    font_style = xlwt.XFStyle()
    rows = Proyecto.objects.filter(estado=True).order_by(
        'fecha_interpretacion')
    for row in rows:
        row_num += 1
        ws.write(row_num, 0, row.nombre, font_style)
        ws.write(row_num, 1, row.get_grupos(), font_style)
        ws.write(row_num, 2, row.get_categorias(), font_style)
        ws.write(row_num, 3, str(row.fecha_creacion), font_style)
        ws.write(row_num, 4, str(row.fecha_interpretacion), font_style)
        ws.write(row_num, 5, row.lugar, font_style)
        ws.write(row_num, 6, row.valor_boleta, font_style)
    wb.save(response)
    return response


def export_directores_xls(request):
    response = HttpResponse(content_type='application/ms-excel')
    response['Content-Disposition'] = 'attachment; filename="directores.xls"'
    wb = xlwt.Workbook(encoding='utf-8')
    ws = wb.add_sheet('Directores')
    row_num = 0
    font_style = xlwt.XFStyle()
    font_style.font.bold = True
    columns = ['Nombre', 'Correo electronico', 'Telefono',]
    for col_num in range(len(columns)):
        ws.write(row_num, col_num, columns[col_num], font_style)
    font_style = xlwt.XFStyle()
    rows = Persona.objects.filter(
        tipo_persona=Persona.DIRECTOR).order_by('primer_nombre')
    for row in rows:
        row_num += 1
        ws.write(row_num, 0, row.get_nombre_completo(), font_style)
        ws.write(row_num, 1, row.correo, font_style)
        ws.write(row_num, 2, row.telefono, font_style)
    wb.save(response)
    return response


def export_pagos_xls(request):
    response = HttpResponse(content_type='application/ms-excel')
    response['Content-Disposition'] = 'attachment; filename="pagos.xls"'
    wb = xlwt.Workbook(encoding='utf-8')
    ws = wb.add_sheet('Pagos')
    row_num = 0
    font_style = xlwt.XFStyle()
    font_style.font.bold = True
    columns = ['Nombre del Aprendiz', 'Correo', 'Telefono', 'Grupo', 'Categoria',
               'Valor de la cuota', 'Valor pagado', 'Fecha de pago']
    for col_num in range(len(columns)):
        ws.write(row_num, col_num, columns[col_num], font_style)
    font_style = xlwt.XFStyle()
    rows = Pago.objects.filter(
        estado=True).order_by('fecha_pago')
    for row in rows:
        row_num += 1
        ws.write(row_num, 0, row.persona.get_nombre_completo(), font_style)
        ws.write(row_num, 1, row.persona.correo, font_style)
        ws.write(row_num, 2, row.persona.telefono, font_style)
        ws.write(row_num, 3, row.grupo.nombre, font_style)
        ws.write(row_num, 4, row.grupo.categoria.nombre, font_style)
        ws.write(row_num, 5, row.grupo.categoria.valor_cuota, font_style)
        ws.write(row_num, 6, row.valor_pago, font_style)
        ws.write(row_num, 7, str(row.fecha_pago), font_style)
    wb.save(response)
    return response


def export_aprendices_xls(request):
    response = HttpResponse(content_type='application/ms-excel')
    response['Content-Disposition'] = 'attachment; filename="aprendices.xls"'
    wb = xlwt.Workbook(encoding='utf-8')
    ws = wb.add_sheet('Aprendices')
    row_num = 0
    font_style = xlwt.XFStyle()
    font_style.font.bold = True
    columns = ['Nombre', 'Correo', 'Telefono', 'Grupo', 'Categoria',
               'Nombre del Acudiente', 'Telefono del acudiente']
    for col_num in range(len(columns)):
        ws.write(row_num, col_num, columns[col_num], font_style)
    font_style = xlwt.XFStyle()
    rows = Persona.objects.filter(
        tipo_persona=Persona.APRENDIZ).order_by('primer_nombre')
    for row in rows:
        row_num += 1
        ws.write(row_num, 0, row.get_nombre_completo(), font_style)
        ws.write(row_num, 1, row.correo, font_style)
        ws.write(row_num, 2, row.telefono, font_style)
        ws.write(row_num, 3, row.get_grupos(), font_style)
        ws.write(row_num, 4, row.get_categorias(), font_style)
        ws.write(row_num, 5, row.get_acudientes(), font_style)
        ws.write(row_num, 6, row.get_numero_acudientes(), font_style)
    wb.save(response)
    return response