from django.shortcuts import render

def renderFormulario(request):
    return render(request,'importacionApp/Formulario.html')

def renderTotal(request):
   
    #capturamos los valores recibido via POST
    t_cantidad = request.POST["txt_cantidad"]
    t_costo = request.POST["txt_costo"]
    costoEnvio = request.POST["txt_costoEnvio"]
    #funcion para calcular el total de importacion
    t_cantidad = float(input('ingrese cantidad: '))
    t_costo = float(input('Ingrese el costo: '))
    costoEnvio = float(input('Ingrese el costo de envío: '))
    
    costoPedido = costo_pedido(t_cantidad, t_costo)
    cif = costoPedido + costoEnvio
    impuestoAduana = tasa_aduana(cif)
    impuestoIva = iva(cif)
    impuestos = impuestoAduana + impuestoIva
    costoTotal = cif + impuestos
    
    #print(f'El costo de pedido es {to_clp(costoPedido)} CLP')
    #print(f'El costo de envío es {to_clp(costoEnvio)} CLP')
    #print(f'El impuesto de aduana es de {to_clp(impuestoAduana)} CLP')
    #print(f'El impuesto de iva es de {to_clp(impuestoIva)} CLP')
    #print(f'Total impuestos y aduana: {to_clp(impuestos)} CLP')
    #print(f'Total del pedido: {to_clp(costoTotal)} CLP costoTotal USD')
    data = {
             "Costo pedido" : costoPedido,
             "Costo envio" : costoEnvio,
             "Impuesto Aduana" : impuestoAduana,
             "Impuesto Iva": impuestoIva,
             "Total Impuesto y Aduana": impuestos,
             "Costo total" : costoTotal}
    return render(request,'importacionApp/total.html',data)



def costo_pedido(t_cantidad, t_costo):
    return t_cantidad * t_costo

def tasa_aduana(cif):
    return cif * 0.06

def iva(cif):
    return cif * 0.19
        
def total_impuesto(aduana, iva):
    return aduana + iva

def to_clp(dolar):
    return dolar * 890 

    




    


