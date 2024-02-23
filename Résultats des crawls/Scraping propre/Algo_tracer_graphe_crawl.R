# Parametres constants

x <- c(0,1,2,3,4,5,6)           # Axe des abscisses
y <- c(1,4,13,40,121,364,1093)  # Courbe majorante vidéos
z <- c(1,4,13,15,15,15,15)      # Courbe majorante genres

## Modifier les valeurs

y2 <- c(1,4,13,37,107,290,775)  ## Nombre de vidéos uniques
y3 <- c(1,3,7,12,37,101,233)    ## Nombre de chaines uniques
y4 <- c(1,2,5,7,8,11,14)         ## Nombre de genres uniques




## Graphe avec videos et chaines

plot.new() 

par(mar=c(4,4,3,5))
plot(x,y, col="red", type="b", axes=F,xlab="", ylab="")

axis(2, ylim=c(0,1100),col="black",col.axis="black",at=seq(0, 1100, by=110)) 
mtext("Vidéos (bleu) - Chaines (jaune)",side=2,line=2.5,col="black")  
axis(1, ylim=c(0,6),col="black",col.axis="black",at=seq(0, 6, by=1))
mtext("Crawl",side=1,line=2.5,col="black")  

par(new = T) 
plot(x,y2, col="blue", type="b", axes=F,xlab="", ylab="",ylim=c(0,1100)) 

par(new = T) 
plot(x,y3, col="yellow", type="b", axes=F,xlab="", ylab="",ylim=c(0,1100)) 




## Graphe des vidéos seulement

plot.new() 

par(mar=c(4,4,3,5))
plot(x,y, col="red", type="b", axes=F,xlab="", ylab="")

axis(2, ylim=c(0,1100),col="black",col.axis="black",at=seq(0, 1100, by=110)) 
mtext("Vidéos",side=2,line=2.5,col="black")  
axis(1, ylim=c(0,6),col="black",col.axis="black",at=seq(0, 6, by=1))
mtext("Crawl",side=1,line=2.5,col="black")  

par(new = T) 
plot(x,y2, col="blue", type="b", axes=F,xlab="", ylab="",ylim=c(0,1100)) 





## Graphe des chaines seulement

plot.new() 

par(mar=c(4,4,3,5))
plot(x,y, col="red", type="b", axes=F,xlab="", ylab="")

axis(2, ylim=c(0,1100),col="black",col.axis="black",at=seq(0, 1100, by=110)) 
mtext("Chaines",side=2,line=2.5,col="black")  
axis(1, ylim=c(0,6),col="black",col.axis="black",at=seq(0, 6, by=1))
mtext("Crawl",side=1,line=2.5,col="black")  

par(new = T) 
plot(x,y3, col="yellow", type="b", axes=F,xlab="", ylab="",ylim=c(0,1100)) 






## Graphe des genres

plot.new() 

par(mar=c(4,4,3,5))
plot(x,z, col="red", type="b", axes=F,xlab="", ylab="")

axis(2, ylim=c(0,1100),col="black",col.axis="black",at=seq(0, 15, by=1)) 
mtext("Genres",side=2,line=2.5,col="black")  
axis(1, ylim=c(0,6),col="black",col.axis="black",at=seq(0, 6, by=1))
mtext("Crawl",side=1,line=2.5,col="black")  

par(new = T) 
plot(x,y4, col="blue", type="b", axes=F,xlab="", ylab="", ylim=c(1,15)) 



