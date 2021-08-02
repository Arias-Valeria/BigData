preguntas <- c(6.5, 2.8, 11.2, 3.1, 6.3, 9.1, 11.3, 2.3, 5.3, 10.6, 12.1, 9.4,
               8.2, 11.1, 8.1, 2.1, 10.4, 5.4, 6.1, 2.4, 2.11, 7.1, 6.4, 2.12,
               11.12, 12.4, 10.3, 2.7, 2.5, 7.4, 2.9, 2.1, 2.2, 9.2, 10.9, 10.5,
               9.3, 5.8, 11.11, 7.3, 10.7, 11.1, 10.8, 12.6, 6.2, 14.1, 10.2, 
               11.8, 11.9, 11.15, 5.7, 3.2, 12.5, 5.1,11.6, 11.16, 14.2, 10.1, 5.6,
               12.3, 11.7, 5.5, 11.13, 11.5, 12.2, 5.2, 11.14, 2.6,7.2, 12.8)

Respuestas <- c(12341, 12340, 12340, 12338, 12335, 12335, 12335, 12334, 12334,
                  12334, 12334, 12333, 12330, 12330, 12327,  12326, 12325, 12324,
                  12324, 12322, 12322, 12321, 12318, 12317, 12314, 12314, 12313,
                  12309, 12308, 12306, 12304, 12302, 12299, 12299, 12297, 12290,
                  12286, 12283, 12282, 12281, 12275, 12274, 12273, 12272, 12271,
                  12261, 12248, 12246, 12244, 12232, 12231, 12226, 12208, 12193,
                  12191, 12181, 12165, 12164, 12164, 12119, 12116, 12085, 12015,
                  11993, 11965, 11953, 11854, 11789, 11684, 3113)

preguntas_menos <- function(Preguntas, Respuestas){
  valor <- min(Respuestas)
  indice <- which.min(Respuestas)
  pregunta <- Preguntas[indice]
  print("Pregunta menos contestada número: ")
  print(pregunta)
  print("Con esta cantidad de respuestas: ")
  print(valor)
}

preguntas_menos(preguntas, Respuestas)

library(ggplot2)
datos <-  read.csv("../Evidencia2/Inciso_c.csv", header = TRUE, sep = ",")
p <- ggplot(datos, aes(x = PREGUNTA)) + geom_bar(aes(fill = SUMA), 
                                                   position = 'dodge')
p + theme_classic()
