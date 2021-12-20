#JUAN RIVERA VARGAS
import cv2
import numpy as np

img1 = cv2.imread('4.2cubo2.png',0)
img2 = cv2.imread('4.2cubo2.png')
img3 = cv2.imread('4.2cubo2.png')


####################################################################### ENCONTRAR LAS ESQUINAD DE LA CARA FRONTAL

renglon_h=img1[250,:]

#encontrar la vertical izquierda
v_left=0
for i in renglon_h:
  v_left=v_left+1
  if i==25 :
    break


#encontrar la vertical derecha
v_right=0
tf=0
for i in renglon_h:
  v_right=v_right+1
  if i==5 :
    tf=tf+1
    if tf==3:
      break


##########################HORIZONTALES
columna=img1[:,v_left+20]

#HORIZONTAL SUPERIOR
h_sup=0
for i in columna:
  h_sup=h_sup+1
  if i==9 :
    break

#HORIZONTAL inferior
h_inf=0
for i in columna:
  h_inf=h_inf+1
  if i==17 :
    break


#ESQUINAS
sup_izq=(v_left,h_sup)
sup_der=(v_right,h_sup)
inf_izq=(v_left,h_inf)
inf_der=(v_right,h_inf)



#############################################################  ESQUINAS DE LA CARA DERECHA

#arista derecha
cd_right=0
for i in renglon_h:
  cd_right=cd_right+1
  if i==20 :
    break


#arista superior
columna2=img1[:,cd_right-100]

cd_sup=0
for i in columna2:
  cd_sup=cd_sup+1
  if i==22 :
    break

columna3=img1[:,cd_right-1]

#encontrar la esquina inferior derecha
cd_id=0
n_u=0
for i in columna3:
  cd_id=cd_id+1
  if i==91 :
    n_u=n_u+1
    if n_u==4:
      break


#ESQUINAS
#la superior izquierda es igual a la superior derecha de la cara anterior
cd_sup_izq=sup_der
cd_sup_der=(cd_right,cd_sup)
#la inferior izquierda esigual a la inferior derecha de la cara anterior
cd_inf_izq=inf_der
cd_inf_der=(cd_right,cd_id)



#elimino los pixeles de color que estan antes del circulo para identificarlo mas facilmente
for i in range(len(columna)):
  for j in range(v_right):
    img2[i,j]=[255,255,255]




################################################# GIRAR LA CARA DEL CIRCULO MORADO
##AMBOS ARREGLOS DEBEN ESTAR EN EL MISMO ORDEN
#array con las esquinas de la imagen derecha
pts1=np.float32([cd_sup_izq,cd_sup_der,cd_inf_izq,cd_inf_der ])
#array con las coordenadas de la imagen frontal
pts2=np.float32([sup_izq,sup_der,inf_izq,inf_der ])

#Calcular la matriz de transformacion con cv2.getPerspectiveTransform
M=cv2.getPerspectiveTransform(pts1, pts2)

#calcular la imagen de salida o destino
dts=cv2.warpPerspective(img2, M, (445,525))




################################################ LIMPIAR LA IMAGEN DEL CIRCULO MORADO
dts2=cv2.cvtColor(dts,cv2.COLOR_BGR2GRAY)

#Toma los tonos grises de toda una columna para ver donde esta el limite
columna4=dts2[:,220]
#encuentra el limite superior del circulo 
l_sup=0
for i in columna4:
  l_sup=l_sup+1
  if i==12 :
    break

#elimino los pixeles de color que estan por encima del circulo para verlo mejor
for i in range(l_sup):
  for j in range(len(dts2[1,:])):
    dts[i,j]=[255,255,255]
#elimino los pixeles que estan por debajo del circulo 
for i in range(20):
  for j in range(len(dts2[1,:])):
    dts[i+505,j]=[255,255,255]

#encuentra la arista inferior del circulo
l_inf=0
for i in columna4:
  l_inf=l_inf+1
  if i==3 :
    break

#arista izquierda
fila=dts2[250,:]
l_left=0
for i in fila:
  l_left=l_left+1
  if i==175 :
    break

#arista derecha
l_right=0
for i in fila:
  l_right=l_right+1
  if i==174 :
    break


#####################################          IMPRESION DE RESULTADOS


#CIRCULO FRONTAL
#Diametro
d_f=h_inf - h_sup
#area
a_f=round(np.pi*(d_f**2)/4)

print()
print(f'********************---RESULTADOS---********************')
print()
print(f'  El diametro del circulo frontal es de:           { d_f} pixeles')
print(f'  El area del circulo frontal es de:             { a_f } pixeles')




#CIRCULO derecha
#Diametro
d_fd=l_right - l_left

#area
a_fd=round(np.pi*(d_fd**2)/4)

print(f'  El diametro del circulo morado es de:            { d_fd} pixeles')
print(f'  El area del circulo morado transformado es de: { a_fd } pixeles')

print(f'  La diferencia entre areas de circulos es de:     { a_fd - a_f} pixeles')


################################


cv2.imshow('Circulo Morado Transformado', dts)
cv2.waitKey(0)
cv2.destroyAllWindows()

