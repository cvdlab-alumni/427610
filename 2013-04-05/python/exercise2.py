from pyplasm import *

GRID = COMP([INSR(PROD),AA(QUOTE)])
#Piano terra
circle = CIRCLE(0.18)([30,1])
column = EXTRUDE([1,circle,3.58])
columns = STRUCT(NN(5)([column,T([1])([3.94])]))
columnOnBalcony = T([2])([7.55])(column)

squarePillars = GRID([[0.36,-1.86,0.36,-3.58+0.36,0.36,-3.58,0.36],[0.36],[3.29]])
squarePillars = T([1,2])([-0.18,-0.18])(squarePillars)
squarePillars = T([1,2,3])([2.08,7.55,0.29])(squarePillars)
pillars0 = STRUCT([columns,columnOnBalcony,squarePillars])
#Primo piano
#Prima riga di colonne di front piu alte
squarePillars1 = GRID([[0.36,-3.58,0.36,-3.58,0.36],[0.36],[3.15*2+0.43]])
squarePillars1 = T([1,2])([-0.18,-0.18])(squarePillars1)
squarePillars1 = T([3])([3.58+0.43])(squarePillars1)
#Prima riga di colonne colonne basse
squarePillars1Basse = GRID([[0.36,-3.58,0.36],[0.36],[3.15]])
squarePillars1Basse = T([1,2])([-0.18,-0.18])(squarePillars1Basse)
squarePillars1Basse = T([1,3])([0.36*3+3.58*3,3.58+0.43])(squarePillars1Basse)
primoPianoPrimaRiga = STRUCT([squarePillars1,squarePillars1Basse])
#Seconda riga di colonne alte dietro
squarePillars2 = GRID([[0.36,-3.58-0.36,0.36],[0.36],[3.15*2+0.43]])
squarePillars2 = T([2,3])([7.55,3.58+0.43])(squarePillars2)
squarePillars2 = T([1,2])([-0.18,-0.18])(squarePillars2)
#Seconda riga di colonna basse
squarePillars2Basse = GRID([[0.36,-3.58*2-0.36,0.36],[0.36],[3.15]])
squarePillars2Basse = T([1,2,3])([0.36*2+3.58*2,7.55,3.58+0.43])(squarePillars2Basse)
squarePillars2Basse = T([1,2])([-0.18,-0.18])(squarePillars2Basse)
primoPianoSecondaRiga = STRUCT([squarePillars2,squarePillars2Basse])
#Colonna tonda secondo piano
column = EXTRUDE([1,circle,3.15])
column = T([1,2,3])([0.36*3+3.58*3,7.55,3.58+0.43])(column)
pillars1 = STRUCT([primoPianoPrimaRiga,primoPianoSecondaRiga,column])

#Secondo piano
#Prima fila
columnFront = GRID([[-0.36*4-3.58*4,0.36],[0.36],[3.15]])
columnFront = T([1,2])([-0.18,-0.18])(columnFront)
columnFront = T([3])([3.58*2+0.43])(columnFront)
#Seconda fila
columnBehind = GRID([[-0.36*2-3.58*2,0.36,-3.58,0.36,-3.58,0.36],[0.36],[3.15]])
columnBehind = T([1,2])([-0.18,-0.18])(columnBehind)
columnBehind = T([2,3])([7.55,3.58*2+0.43])(columnBehind)
pillars2 = STRUCT([columnFront,columnBehind])
#Terzo piano
#Dietro Prima 
columnBehindPrima = GRID([[0.22],[0.22],[1.57]])
columnBehindPrima = T([1,2,3])([-0.18,-0.11,3.58*3+0.43+1.62])(columnBehindPrima)
#Dietro seconda
colomnBehindSeconda = GRID([[-0.11-0.07-0.18-0.36-3.58,0.18],[0.22],[3.15]])
colomnBehindSeconda = T([1,2])([-0.11,-0.11])(colomnBehindSeconda)
colomnBehindSeconda = T([2,3])([7.55,3.58*3+0.43])(colomnBehindSeconda)
#Dietro terza
columnBehindTerza = GRID([[-0.36*2-3.58*2,0.36,-3.58,0.36,-3.58,0.36],[0.36],[3.15]])
columnBehindTerza = T([1,2])([-0.18,-0.18])(columnBehindTerza)
columnBehindTerza = T([2,3])([7.55,3.58*3+0.43])(columnBehindTerza)
#Davanti
columnFront = GRID([[-0.36*2-3.58*2,0.36,-3.58,-0.36,-3.58,0.36],[0.36],[3.15]])
columnFront = T([1,2])([-0.18,-0.18])(columnFront)
columnFront = T([3])([3.58*3+0.43])(columnFront)

columnBehind = STRUCT([columnBehindPrima,colomnBehindSeconda,columnBehindTerza])
pillars3 = STRUCT([columnBehind,columnFront])
building = STRUCT([pillars0,pillars1,pillars2,pillars3])

#VIEW(building)
#Floor zero
bigFloorZero = T([1,2])([1.90,2.64])(CUBOID([10.09,6.81,0.29]))
circleBassoZero = CIRCLE(0.86)([30,1])
circleBassoZero = T([1,2])([2.76,2.6])(circleBassoZero)
circleBassoZero = EXTRUDE([1,circleBassoZero,0.29])
quadratoSxZero = CUBOID([2.08,2.08,0.29])
quadratoSxZero = T([1,2])([-0.18,7.55-0.18])(quadratoSxZero)
quadratoDxZero = CUBOID([1.81,3.73,0.29])
quadratoDxZero = T([1,2])([11.63+0.36,5.72])(quadratoDxZero)
circleDxZero = CIRCLE(1.86)([30,1])
circleDxZero = T([1,2])([11.63+0.36+1.86,7.58])(circleDxZero)
circleDxZero = EXTRUDE([1,circleDxZero,0.29])
quadratoDxPiccolo = CUBOID([0.93,1.17,0.29])
quadratoDxPiccolo = T([1,2])([11.63+0.36,4.55])(quadratoDxPiccolo)

#Scala Primo Piano ******************************************************>
prova = CUBOID([8.05-3.44,1.5,3.58+0.43])
prova = T([1,2])([3.44,7.59+0.18])(prova)
floor0 = STRUCT([bigFloorZero,circleBassoZero,quadratoSxZero,quadratoDxZero,circleDxZero,quadratoDxPiccolo,prova])
#Primo
rettangoloLungo = CUBOID([3.44,7.55+1.9,0.43])
rettangoloLungo = T([1,2,3])([-0.18,-0.18,3.58])(rettangoloLungo)
rettangoloGrande = CUBOID([16.1-3.40,7.59,0.43])
rettangoloGrande = T([1,2,3])([3.44-0.18,-0.18,3.58])(rettangoloGrande)
arriviDalleScale = CUBOID([16.1-8.5-0.14,9.09-7.59,0.43])
arriviDalleScale = T([1,2,3])([8.5,7.59-0.18,3.58])(arriviDalleScale)
#Balconcino
balconcino = CUBOID([1.65,1.55,0.30])
balconcino = T([1,2,3])([-1.65-0.18,7.55-0.18,3.58+0.13])(balconcino)
floor1 = STRUCT([rettangoloLungo,rettangoloGrande,arriviDalleScale,balconcino])
#Secondo piano
#Scala Secondo Piano ******************************************************>
prova = CUBOID([8.05-3.44,1.5,3.58+0.43])
prova = T([1,2,3])([1.7,7.59+0.18,3.58+0.43])(prova)

rettangoloGrande = CUBOID([16.1-8.5+0.25,7.59,0.43])
rettangoloGrande = T([1,2,3])([8.5-0.45,-0.18,3.58*2])(rettangoloGrande)
arriviDalleScale = CUBOID([16.1-6.83,9.09-7.59,0.43])
arriviDalleScale = T([1,2,3])([6.83-0.18,7.59-0.18,3.58*2])(arriviDalleScale)

#triangolo = MKPOL([[[6.83-0.20 ,7.59],[8.27,7.59],[8.27,1]],[[1,2,3]],None]) 
triangolo = MKPOL([[[6.63,7.45],[8.27,7.45],[8.27,0.05],[7.72,0.05]],[[1,2,3,4]],None])
triangolo = EXTRUDE([1,triangolo,0.43])
triangolo = T([3])([3.58*2])(triangolo)

floor2 = STRUCT([prova,rettangoloGrande,arriviDalleScale,triangolo])
#Terzo piano
prova = CUBOID([5.07,1.36,3.58])
prova = T([1,2,3])([8.23,7.59,3.58*2])(prova)
pavimentoGrande = CUBOID([16.25,7.87,0.43])
pavimentoGrande = T([1,2,3])([-0.18,-0.18,3.58*3])(pavimentoGrande)
pavimentoSx = CUBOID([8.23,1.5,0.43])
pavimentoSx = T([1,2,3])([-0.18,7.59,3.58*3])(pavimentoSx)
pavimentoDx = CUBOID([3.4+0.22,1.5,0.43])
pavimentoDx = T([1,2,3])([12.45,7.59,3.58*3])(pavimentoDx)

floor3 = STRUCT([prova,pavimentoGrande,pavimentoSx,pavimentoDx])
#Ultimo piano
vetrata = T([1,2,3])([-0.2,-0.2,3.58*4])(CUBOID([10,9,1.3]))

floor4 = STRUCT([vetrata])


building = STRUCT([floor1,floor0,building,floor2,floor3,floor4])

VIEW(building)

#floor1 = STRUCT()
#floor2 = STRUCT()
#floor3 = STRUCT()
#floor4 = STRUCT()