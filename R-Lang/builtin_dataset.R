data()
View(CO2)
View(LakeHuron) 
View(iris)
View(mtcars)
View(trees)
View(npk)

#save dataset to excel

install.packages("writexl")
library(writexl)
write_xlsx(CO2,path="C:\\Users\\Saad\\OneDrive\\Desktop\\DataAnalysis\\CO2.xlsx")
library(ggplot2)
ggplot(trees,aes(Girth,Height))+geom_point()+geom_smooth(method="lm")
