library("plotly")

wcc <- rnorm(100,15, 4)
summary(wcc)

p1 <- plot_ly(x = ~wcc,
              type = "histogram")
p1


