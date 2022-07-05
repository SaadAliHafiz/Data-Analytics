library(readxl)
employee_data <- read_excel("Employee.xls", 
                            col_types = c("numeric", "text", "date", 
                                          "numeric", "numeric", "numeric", 
                                          "numeric", "numeric"))
View(employee_data)
mean(employee_data$Salary)
mean(employee_data$`Job Time`)
median(employee_data$Salary)
median(employee_data$`Job Time`)
min(employee_data$Salary)
min(employee_data$`Job Time`)
max(employee_data$Salary)
range(employee_data$Salary)

quantile(employee_data$Salary)
#25% quantile
quantile(employee_data$Salary,.25)
#standard Deviation
sd(employee_data$Salary)
#Variance
var(employee_data$Salary)

#extract data from specific rows
lapply(employee_data[,5:6],mean)
lapply(employee_data[,5:6],median)
lapply(employee_data[,5:6],sd)
#Summary of  data
summary(employee_data)


#Analysis Of Variance ANOVA

#use to differ two variables

#we'll see gender-wise salaries differ or not

aov(employee_data$Salary ~ employee_data$Gender)

#to determine whether anova is significant : groups are different to eachother or not


a1<-aov(employee_data$Salary ~ employee_data$Gender)
summary(a1)
#tukey test



TukeyHSD(a1)
#padj value< 0.5,value are significant on 95% confidence level

#group anova

a2<- aov(employee_data$Salary ~ employee_data$Gender * employee_data$Minority)
summary(a2)
