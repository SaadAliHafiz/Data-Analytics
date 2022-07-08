install.packages('ggplot2')
#ggplot (function)
#data (dat1) 
#mapping (xaxis, y axis)
#geometry (scatter, box, line)
library(ggplot2)
library(readxl)
Employee <- read_excel("Employee.xls", col_types = c("numeric", 
                                                     "text", "date", "numeric", "numeric", 
                                                     "numeric", "numeric", "numeric"))
View(Employee)
ggplot(Employee,mapping=aes(x=Gender,y=Salary))+geom_point(size=5)
ggplot(Employee,aes(Gender,Salary))+geom_point()+geom_line()
ggplot(Employee,aes(Gender,Salary))+geom_boxplot()+geom_point(color="red",alpha=0.6)
ggplot(Employee,aes(Jobcat,Salary,fill=Gender))+geom_boxplot()+facet_wrap(~Minority)+
  labs(x="Job Category",y="Salary",title="Job category wise salary")+
  theme_bw()+ggsave("ggplot1.tiff",units="in",width=8,height=4,dpi=300,compression='lzw')
 