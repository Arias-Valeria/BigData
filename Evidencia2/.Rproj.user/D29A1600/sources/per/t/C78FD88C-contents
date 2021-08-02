localidad <- c("GUERRERO", "ESTADO DE MÉXICO", "QUINTANA ROO", "AGUASCALIENTES",
               "CAMPECHE", "COLIMA", "CHIAPAS", "CHIHUAHUA", "CIUDAD DE MÉXICO",
               "DURANGO", "GUANAJUATO", "HIDALGO", "JALISCO", "MICHOACÁN", 
               "NAYARIT", "NUEVO LEÓN", "PUEBLA", "SINALOA", "SONORA", "TABASCO",
               "TAMAULIPAS", "VERACRUZ", "YUCATÁN", "ZACATECAS", "BAJA CALIFORNIA SUR", 
               "COAHUILA", "OAXACA", "QUERÉTARO", "TLAXCALA", "BAJA CALIFORNIA", 
               "MORELOS", "SAN LUIS POTOSI")

p_contestadas <- c(71, 71, 71, 70, 70, 70, 70, 70, 70, 70, 70, 70, 70, 70, 70,
                   70, 70, 70, 70, 70, 70, 70, 70, 70, 69, 69, 69, 69, 69, 68,
                   68, 66)

porcentaje_preguntas <- function(localidad, p_contestadas){
  x = 1
  total = 71
  while (x < 32) {
    porcentaje = (p_contestadas[x] * 100) / total
    nombre = localidad[x]
    print(nombre)
    print(porcentaje)
    print("***************************************************")
    x <- x+1
  }
}

porcentaje_preguntas(localidad, p_contestadas)
library(ggplot2)
datos <-  read.csv("../Evidencia2/Inciso_d.csv", header = TRUE, sep = ",")
p <- ggplot(datos, aes(x = PUNTAJE)) + geom_bar(aes(fill = ESTADO), 
                                                 position = 'dodge')
p + theme_classic()
