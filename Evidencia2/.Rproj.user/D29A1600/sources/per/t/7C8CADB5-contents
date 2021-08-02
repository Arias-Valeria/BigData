#arreglos de los estados y sus participantes.
Delegaciones <- c('E_Mexico', 'Jalisco', 'C_Mexico', 'Nuevo_Leon', 'Chihuahua', 
             'Baja_California', 'Sonora', 'Tamaulipas', 'Veracruz', 'Coahuila',
             'Guanajuato', 'Sinaloa', 'Aguascalientes', 'Michoacan', 'Puebla',
             'Yucatan', 'Queretaro', 'Morelos', 'SL_Potosi', 'Zacatecas',
             'Quintana_Roo', 'Colima', 'Nayarit', 'Hidalgo', 'Durango', 'Oaxaca', 
             'BJ_Sur', 'Chiapas', 'Guerrero', 'Campeche', 'Tabasco', 'Tabasco')

Num_Localidades <- c(877, 853, 827, 804, 797, 764, 672, 672, 593, 556, 543, 449,
                     440, 352, 325, 311, 284, 277, 275, 267, 206, 201,  166, 158,
                     153, 145, 136, 129, 126, 69, 66, 53)

max_participantes <- function (Delegaciones, Num_Localidades){
  maximo <- max(Num_Localidades)
  indice <- which.max(Num_Localidades)
  nom_max <- Delegaciones [indice]
  print(nom_max)
  print(maximo)
}

max_participantes(Delegaciones, Num_Localidades)

library(ggplot2)
datos <-  read.csv("../Evidencia2/Inciso_a.csv", header = TRUE, sep = ",")
p <- ggplot(datos, aes(x = PARTICIPANTES)) + geom_bar(aes(fill = ESTADO), 
                                                      position = 'dodge')
p + theme_classic()
