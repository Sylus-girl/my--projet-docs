height_m=8848.18
height_mm=height_m*1000
paper_thick_mm=0.1
fold=0
while paper_thick_mm<=height_mm:
    paper_thick_mm*=2
    fold+=1
print("对折次数为：",fold)
