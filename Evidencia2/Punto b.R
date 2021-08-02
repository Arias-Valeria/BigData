participaciones <- function(Num_Localidades, Delegaciones){
  x = 1
  total = 12546
  while (x < 32) {
    porcentaje = (Num_Localidades[x] * 100) / total
    nombre = Delegaciones[x]
    print(nombre)
    print(porcentaje)
    print("***************************************************")
    x <- x+1
  }
}

participaciones(Num_Localidades, Delegaciones)

library(ggplot2)
datos <-  read.csv("../Evidencia2/Inciso_a.csv", header = TRUE, sep = ",")
p <- ggplot(datos, aes(x = PORCENTAJE)) + geom_bar(aes(fill = ESTADO), 
                                                      position = 'dodge')
p + theme_classic()
