library(readxl)
Employee <- read_excel("Employee.xls", col_types = c("numeric", 
                                                     "text", "date", "numeric", "numeric", 
                                                     "numeric", "numeric", "numeric"))
View(Employee)

boxplot(Employee$Salary~Employee$Gender,xlab="Gender",ylab = "Salary")
#m or f ka mean apas mein kitna differ kr rahe hain
#in order to do that we apply stats on it by applying multiple mean,tukey test,

#Multiple comparision of means

#1-Tukey.HSD TEST

install.packages("agricolae")
library(agricolae)
#help("agricolae-package")

#model
model<-aov(Salary~Gender,data=Employee)
out1 <- HSD.test(model,"Gender",group = TRUE,console=TRUE,main = "Tukey Test")


plot(out)

#2.LSD Test
model<-aov(Salary~Gender,data=Employee)
out <- LSD.test(model,"Gender",group = TRUE,console=TRUE,main = "LSD Test")


plot(out)
# Dunchan Test

model<-aov(Salary~Gender,data=Employee)
out <- duncan.test(model,"Gender",group = TRUE,console=TRUE,main = "duncan.test")


plot(out)

library(readxl)
Employee <- read_excel("Employee.xls", col_types = c("numeric", 
                                                     "text", "date", "numeric", "numeric", 
                                                     "numeric", "numeric", "text"))
View(Employee)

boxplot(Employee$Salary~Employee$Gender*Employee$Minority,las=1)

model1<- aov(Salary~Gender*Minority,data=Employee)
out1<-HSD.test(model1,c("Salary","Gender"),group = TRUE,console=TRUE,main = "Tukey Test")

plot(out1,horiz=TRUE,las=2)


jpeg(file="Tukey test.tiff",
     width=6,height=4,units="in",res=300)
boxplot(Salary~Gender*Minority,data=Employee,las=1)
dev.off()

