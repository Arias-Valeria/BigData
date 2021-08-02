info <- read.csv("../Act_10/Datos_clientes.csv", header = TRUE, sep = ",")
info.nom <- info[, c('Temporada', 'Enero',"Febrero","Junio", 'Diciembre')]
pairs(info.nom)
