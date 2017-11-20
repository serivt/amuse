function isNumber(n){
    return n != null && !isNaN(Number(n));
}

function isInt(n){
    return !isNaN(Number(n)) && Number(n) % 1 === 0;
}

var getUrlParameter = function getUrlParameter(sParam) {
  var sPageURL = decodeURIComponent(window.location.search.substring(1)),
      sURLVariables = sPageURL.split('&'),
      sParameterName,
      i;

  for (i = 0; i < sURLVariables.length; i++) {
      sParameterName = sURLVariables[i].split('=');

      if (sParameterName[0] === sParam) {
          return sParameterName[1] === undefined ? true : sParameterName[1];
      }
  }
};

function generarGrafico(titulo, columnas, distribucion) {
  $('#generar-grafico-titulo').text(titulo);
  $('#generar-grafico').modal('show');
  google.charts.setOnLoadCallback(drawChart);
  function drawChart() {
    var data = new google.visualization.DataTable();
    for(i in columnas) {
      data.addColumn(columnas[i], i);
    }
    data.addRows(distribucion);
    var options = {
      pointSize: 5,
      'width': 800,
      'height': 500
    };
    var chart = new google.visualization.LineChart(document.getElementById('chart_div'));
    chart.draw(data, options);
  }
}

function error(XMLHttpRequest){
  swal('Error ' + XMLHttpRequest.status + ': ' + XMLHttpRequest.statusText, 'Ha ocurrido un error al realizar la operación, por favor notifique al administrador del sistema.', 'error');
}

function intcomma(value) {
  intcomma(value, false);
}

function intcomma(value, entero) {
  intcomma(value, entero, false);
};

function intcomma(value, entero, porcentual) {
  var origValue = String(value);
  if(origValue === '') {
    origValue = '0';
  }
  if(origValue.indexOf('.') === -1 && !entero) {
    origValue = origValue + '.0';
  }
  // inspired by django.contrib.humanize.intcomma
  var newValue = origValue.replace(/^(-?\d+)(\d{3})/, '$1,$2');
  if(origValue == newValue){
    if(porcentual && newValue.indexOf('%') === -1) {
      return newValue + '%';
    }else{
      return newValue;
    }
  }else {
      return intcomma(newValue, entero, porcentual);
  }
}

function getCursorPosition(element) {
  if (element.selectionStart) return element.selectionStart;
  else if (document.selection)
  {
    element.focus();
    var r = document.selection.createRange();
    if (r == null) return 0;

    var re = element.createTextRange(),
        rc = re.duplicate();
    re.moveToBookmark(r.getBookmark());
    rc.setEndPoint('EndToStart', re);
    return rc.text.length;
  }
  return 0;
}


  $('input.numerico').each(function(){
    var entero = $(this).attr('entero') === 'true';
    var porcentual = $(this).attr('porcentual') === 'true';
    $(this).val(intcomma(parseFloat($(this).val() || 0), entero, porcentual)) ;
  })
  $(document).on('focus', 'input.numerico', function(){
    if(!$(this).is('[readonly]')) {
      $(this).val(rintcomma($(this).val()));
    }
  });
  $(document).on('keypress', 'input.numerico', function (event) {
    var inputCode = event.which;
    var currentValue = $(this).val();
    var entero = $(this).attr('entero') === 'true';

    if (inputCode > 0 && (inputCode < 48 || inputCode > 57)) {

      if($(this).hasClass('calculable')){
        if ( ( (inputCode > 39 && inputCode < 44) || (inputCode > 44 
          && inputCode < 48)) && currentValue.trim()[0] == '=')
          return true;
        
        if (inputCode == 61 && (currentValue.trim() == '' || getCursorPosition(this) == 0))
          return true;
      }
      

      if (entero && inputCode == 46) {
        return false;
      }
      if (inputCode == 46 && currentValue.trim()[0] != '=') {
          if (getCursorPosition(this) == 0 && currentValue.charAt(0) == '-') return false;
          if (currentValue.match(/[.]/)) return false;
      }
      else if (inputCode == 45) {
          if (currentValue.charAt(0) == '-') return false;
          if (getCursorPosition(this) != 0) return false;
      }
      else if (inputCode == 8 || inputCode == 37) return true;
      else return false;
    }
    else if (inputCode > 0 && (inputCode >= 48 && inputCode <= 57)) {
        if (currentValue.charAt(0) == '-' && getCursorPosition(this) == 0) return false;
    }
  });
  $(document).on('blur', 'input.numerico', function(){
    var currentValue = $(this).val();
    var entero = $(this).attr('entero') === 'true';
    var porcentual = $(this).attr('porcentual') === 'true';
    if(currentValue[0] == '='){
      try {
        currentValue = String(math.eval(currentValue.substr(1)));
      }
      catch(err) {
        currentValue = "0";
      }
    }
    $(this).val(intcomma(currentValue.replace(/,/g, ''), entero, porcentual));
    // $(this).val(currentValue);
  });

  $(document).on("keypress", ".float_number", function(event){
    if ((event.which != 46 || $(this).val().indexOf('.') != -1) && (event.which < 48 || event.which > 57) || event.which == 46 ){
      event.preventDefault();
    }
  });

$('form').submit(function(){
  $('.numerico').each(function(){
    $(this).val(rintcomma($(this).val()));
  })
});

function agregar_error_input(element, error){
  $(element).addClass("has-error");
  if($(element).find("small").length == 0)
    $(element).append("<small class='help-block'>"+error+"</small>");
  else
    $(element).find("small").text(error);
}

function agregar_error_chosen_select(element, error){
  $(element).css("border-bottom","1px solid #f6675d");
  if($(element).parent().parent().find("small").length == 0)
    $(element).parent().after("<small class='help-block' style='color:#f6675d;'>"+error+"</small>");
  else
    $(element).parent().find("small").text(error);
}

function remover_error_input(element){
  $(element).removeClass("has-error");
  $(element).find("small").remove();
}

function remover_error_chosen_select(element){
  $(element).css("border-bottom","1px solid #e0e0e0");
  $(element).parent().parent().find("small.help-block").remove();
}

function int(valor){
  return valor.replace(/,/g, '');
}

function round(num, n) {
  var n = Math.pow(10, n);
  return Math.round(num * n) / n;
}

$(document).on({
    mouseenter: function () {
      $(this).find(".boton").show();
    },
    mouseleave: function () {
      $(this).find(".boton").hide();
    }
}, ".mostrar_botones"); //pass the element as an argument to .on



$('input.numerico').on('focus',  function(){
    $(this).select();
});

$(document).on('click', '.clickable', function(){
  var url = $(this).attr('data-url');
  window.location.href = url;
})

function rintcomma(valor) {
  return rintcomma(valor, false);
}
function rintcomma(valor, entero) {
  valor = valor.replace('%', '').trim();
  if(entero) {
    return parseInt(valor.replace(/,/g, '')) || 0;
  }
  return parseFloat(valor.replace(/,/g, '')) || 0;
}

function wait() {
  $('#wait').show();
}

function rwait() {
  $('#wait').hide();
}

function graficar_tir(elemento, valores, tio){
  var maxY = -1;
  var maxX = -1;
	for (var i = 0; i < valores.length; i ++) {
	  maxY = Math.max(maxY, valores[i][0][1])
	  maxX = Math.max(maxX, valores[i][valores[i].length-1][0])
	}
	maxX = maxX + (maxX*1.1)
	var datos = []
	var colores = []
	colores.push("#00cde2","#ffb700","#7ac70c","#2a469a","#fc3232","#1cb0f6","#00c07f");

	$("#"+elemento).parent().append("<div id='info_tir'><table><tbody></tbody></table></div>");
	for (var i = 0; i < valores.length; i ++){
	  datos.push({"data":valores[i], "label":"Agrupacion "+(i+1), "color":colores[i%colores.length]})
	  $("#info_tir table tbody").append("<tr><td style='padding: 0px 5px;' class='legendColorBox'><div style='border:1px solid #ccc;padding:1px'><div style='width:4px;height:0;border:5px solid "+colores[i%colores.length]+";overflow:hidden'></div></div>"+
	    "</td><td style='padding: 0px 5px;'><b>Agrupacion "+(i+1)+"</b></td><td style='padding: 0px 5px;'></td></tr><tr><td style='padding: 0px 5px;'></td><td style='padding: 0px 5px;'><b>VPN Maximo</b></td><td style='padding: 0px 5px;'>"+valores[i][0][1]+"</td></tr><tr><td style='padding: 0px 5px;'></td><td style='padding: 0px 5px;'><b>Tasa Maximo</b></td><td style='padding: 0px 5px;'>"+Math.round(valores[i][valores[i].length-1][0] * 100) / 100+"</td></tr>")
	 }

	plot = $.plot("#"+elemento, datos, {
		series: {
			lines: {
				show: true
			}
		},
		points: {
			show: true
		},
		crosshair: {
			mode: "x"
		},
		grid: {
		  clickable: true,
			hoverable: true,
			autoHighlight: false
		},
		xaxis: {
      axisLabel : 'Tasa',
		// 	zoomRange: [-maxX*2, maxX*2],
		// 	panRange: [-0.1, maxX]
		},
		yaxis: {
      show : true,
      axisLabel : 'Valor presente neto',
      position: 'left',
		// 	zoomRange: [-maxX*2, maxY],
		// 	panRange: [-maxY*0.1, maxY+(maxY*0.1)]
		},
		zoom: {
			interactive: true
		},
		pan: {
			interactive: true
		}
	});

	$("<div id='tooltip'></div>").css({
		position: "absolute",
		border: "1px solid #fdd",
		padding: "2px",
		color: "#000",
		"background-color": "#FFF",
		opacity: 0.80
	}).appendTo("body");

	var updateLegendTimeout = null;
	var latestPosition = null;

	function updateLegend() {
		updateLegendTimeout = null;
		var pos = latestPosition;
		var axes = plot.getAxes();
		if (pos.x < axes.xaxis.min || pos.x > axes.xaxis.max ||
			pos.y < axes.yaxis.min || pos.y > axes.yaxis.max) {
			return;
		}

		var i, j, dataset = plot.getData();
		for (i = 0; i < dataset.length; ++i) {
			var series = dataset[i];
			for (j = 0; j < series.data.length; ++j) {
				if (series.data[j][0] > pos.x) {
					break;
				}
			}
			var y,p1 = series.data[j - 1],p2 = series.data[j];
			if (p1 == null) {
				y = p2[1];
			} else if (p2 == null) {
				y = p1[1];
			} else {
				y = p1[1] + (p2[1] - p1[1]) * (pos.x - p1[0]) / (p2[0] - p1[0]);
			}
			$("#"+elemento+" .legendLabel").eq(i).text(series.label+"= " + y.toFixed(2));
		}
	}

	$("#"+elemento).bind("plothover",  function (event, pos, item) {
		latestPosition = pos;
		if (!updateLegendTimeout) {
			updateLegendTimeout = setTimeout(updateLegend, 50);
		}
    if (item) {
      var x = item.datapoint[0].toFixed(2), y = item.datapoint[1].toFixed(2);
      $(".flot-tooltip").remove();
			$("#tooltip").html(item.series.label+", VPN: "+x+", TASA: "+y).css({top: item.pageY+5, left: item.pageX+5}).fadeIn(100);
	  }else{
			$("#tooltip").hide();
      $(".flot-tooltip").remove();
	  }
	});

  plot.hooks.drawOverlay.push(function (plot, ctx) {
    tabla_label_tio();
  });

  function tabla_label_tio(){
    if(document.getElementById("label_tio") == null){
	    $("#"+elemento+" .legend table").append("<tr id='label_tio'><td class='legendColorBox'><div style='border:1px solid #ccc;padding:1px'>"+
	    "<div style='width:4px;height:0;border:5px solid #2a9a48;overflow:hidden'></div></div></td>"+
	    "<td>TIO= "+tio+"</td></tr>")
    }
  }

  plot.hooks.drawOverlay.push(function (plot, ctx) {
    var plotOffset = plot.getPlotOffset();
    ctx.save();
    ctx.translate(plotOffset.left, plotOffset.top);

    //LINEAS VERTICALEs
    for (var i = 0; i < datos.length; i++) {
      ctx.strokeStyle = datos[i]['color'];
      ctx.lineWidth = 2;
      ctx.lineJoin = "round";
      ctx.beginPath();
      var drawX = plot.p2c({x:datos[i]['data'][datos[i]['data'].length-1][0],y:0})['left'];
      ctx.moveTo(drawX, 0);
      ctx.lineTo(drawX, plot.height());
      ctx.stroke();
    }

    //TIO
    ctx.strokeStyle = "#2a9a48";
    ctx.lineWidth = 2;
    ctx.lineJoin = "round";
    ctx.beginPath();
    var drawX = plot.p2c({x:tio,y:0})['left'];
    ctx.moveTo(drawX, 0);
    ctx.lineTo(drawX, plot.height());
    ctx.stroke();

    //EJES
    ctx.strokeStyle = "#727272";
    ctx.lineWidth = 1;
    ctx.beginPath();
    var drawY = plot.p2c({x:0,y:0})['top'];
    ctx.moveTo(0, drawY);
    ctx.lineTo(plot.width(), drawY);
    ctx.stroke();
    ctx.beginPath();
    var drawX = plot.p2c({x:0,y:0})['left'];
    ctx.moveTo(drawX, 0);
    ctx.lineTo(drawX, plot.height());
    ctx.stroke();
    ctx.restore();
  });

}

function formError(response, $form) {
  if(response.hasOwnProperty('errores')) {
    var errores = response['errores'];
    $inputs = $form.find('input[id^="id_"]');
    $inputs.each(function() {
      $input = $(this);
      var key = $(this).attr('id').substring(3);
      if(errores.hasOwnProperty(key)) {
        var error = errores[key][0];
        var $form_group = $input.parents('.form-group');
        $form_group.addClass('has-error');
        if($form_group.find('.help-block').length > 0) {
          $form_group.find('.help-block').text(error);
        }else{
          var mensaje = '<small class="help-block">'+ error +'</small>';
          $form_group.append(mensaje);
        }
      }
    });
  }else{
    $('.form-group').removeClass('has-error');
    $('.help-block').remove();
  }
}

function addMonths(date, months) {
  months += 1;
  var month = date.getMonth();
  months += month;
  var years = parseInt(months / 12);
  date.setMonth(months % 12);
  date.setFullYear(date.getFullYear() + years);
  return date;
}

function mensaje_notificacion(mensaje, tipo, tiempo){
  $.bootstrapGrowl(mensaje, {
    type: tipo,
    offset: {
      from: 'top',
      amount: 50
    },
    delay: tiempo,
    width: 350
  });
};

function descargar_tabla_como_excel(tabla, nombre_tabla, delimitador, handsontable, es_string, cerrar){
  // Nombre de libro maximo 31 caracteres
  if(!es_string){
    var nueva_tabla = $(tabla).clone();
  }

  var data_type = '';
  var nombre_libro = nombre_tabla.split("-")[0];

  var docHeader = '<html xmlns:o="urn:schemas-microsoft-com:office:office" xmlns:x="urn:schemas-microsoft-com:office:excel" xmlns="http://www.w3.org/TR/REC-html40">' +
    '<head>' +
    '<meta http-equiv=Content-Type content="text/html; charset=UTF-8">' +
    '<!--[if gte mso 9]><xml>' +
    ' <x:ExcelWorkbook>' +
    '  <x:ExcelWorksheets>' +
    '   <x:ExcelWorksheet>' +
    '    <x:Name>'+nombre_libro+'</x:Name>' +
    '    <x:WorksheetOptions>' +
    '     <x:ProtectContents>False</x:ProtectContents>' +
    '     <x:ProtectObjects>False</x:ProtectObjects>' +
    '     <x:ProtectScenarios>False</x:ProtectScenarios>' +
    '    </x:WorksheetOptions>' +
    '   </x:ExcelWorksheet>' +
    '  </x:ExcelWorksheets>' +
    '  <x:ProtectStructure>False</x:ProtectStructure>' +
    '  <x:ProtectWindows>False</x:ProtectWindows>' +
    ' </x:ExcelWorkbook>' +
    '</xml><![endif]-->' +
    '</head>' +
    '<body>';
  var docFooter = '</body></html>';

  if(!es_string){
    var table_html = $(nueva_tabla);
    if(handsontable){
      table_html = $(table_html).find("tbody");
      $(table_html).find("tr").each(function(){
        $(this).children()[0].remove()
      })
    }

    table_html.find("td").each(function(){
      if(delimitador == "."){
        var text = $(this).text();
        text = text.replace(/,/g, ''); //Comas
        $(this).text(text);
      }else{
        var text = $(this).text()
        text = text.replace(/,/g, ''); //Comas
        text = text.replace(/\./g, ','); //Puntos
        $(this).text(text);
      }
    })

    var table_html = table_html.prop('outerHTML')
  }
  var tabla_final = "";
  if (handsontable) {
    tabla_final = docHeader +'<table>' + table_html + '</table>' + docFooter;
  }else{
    if(es_string){
      tabla_final = docHeader + tabla + docFooter;
    }else{
      tabla_final = docHeader + table_html + docFooter;
    }
  }

  $("#formulario_descargar_excel_tabla").val(tabla_final)
  $("#formulario_descargar_excel_nombre_tabla").val(nombre_tabla)

  formulario = document.getElementById("formulario_descargar_excel").submit();
  if (cerrar) {
    setTimeout(function(){
      window.close();
    }, 5000);
  }
}
