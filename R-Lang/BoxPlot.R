library(readxl)
employee_data <- read_excel("Employee.xls", col_types = c("numeric", 
                                                     "text", "date", "numeric", "numeric", 
                                                     "numeric", "numeric", "numeric"))
View(employee_data)


##############################################BOXPLOT#############################################################

boxplot(employee_data$Salary ~ employee_data$Gender)

#label in terms of x and y axis

boxplot(Salary ~ Gender,data=employee_data,main="BoxPlot of Gender wise Salary",
        xlab = "Gender",ylab = "salaries")
#coloring
boxplot(Salary ~ Gender,data=employee_data,main="BoxPlot of Gender wise Salary",
        xlab = "Gender",ylab = "salaries",
        col="#34deeb",border="#4f0e6b")

#groupings
library(readxl)
employee_data <- read_excel("Employee.xls", col_types = c("numeric", 
                                                     "text", "date", "numeric", "numeric", 
                                                     "numeric", "numeric", "numeric"))
View(employee_data)
employee_data$Gender <- factor(employee_data$Gender, levels = c("m","f"))
boxplot(employee_data$Salary ~ employee_data$Gender * employee_data$Minority,main="boxplot of salaries to gender",xlab ="Employee Gender",ylab = "Employee Salary")
