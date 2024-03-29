/****************************************** ADAPTER ***********************/
// adapt pyplasm code to plasm.js code

T = function (dims) {
  dims = dims.map(function (dim) {
    return dim - 1;
  });

  return function (values) {
    return function (object) {
     return object.clone().translate(dims, values);
   };
 };
};

R = function (dims) {
  dims = dims.map(function (dim) {
    return dim - 1;
  });

  return function (angle) {
    return function (object) {
      return object.clone().rotate(dims, angle);
    };
  };
};

S = function (dims) {
  dims = dims.map(function (dim) {
    return dim - 1;
  });

  return function (values) {
    return function (object) {
      return object.clone().scale(dims, values);
    };
  };
};

S3 = S2;
S2 = S1;
S1 = S0;

GRID = SIMPLEX_GRID;

NN = REPLICA;

VIEW = DRAW;
/******************************************************************/
//Piano terra
//Piano terra
circle = DISK(0.18)([30,1])
column = EXTRUDE([3.58])(circle)
columns = STRUCT(NN(5)([column,T([1])([3.94])]))
columnOnBalcony = T([2])([7.55])(column)

squarePillars = GRID([[0.36,-1.86,0.36,-3.58+0.36,0.36,-3.58,0.36],[0.36],[3.29]])
squarePillars = T([1,2])([-0.18,-0.18])(squarePillars)
squarePillars = T([1,2,3])([2.08,7.55,0.29])(squarePillars)
pillars0 = STRUCT([columns,columnOnBalcony,squarePillars])
//Primo piano
//Prima riga di colonne di front piu alte
squarePillars1 = GRID([[0.36,-3.58,0.36,-3.58,0.36],[0.36],[3.15*2+0.43]])
squarePillars1 = T([1,2])([-0.18,-0.18])(squarePillars1)
squarePillars1 = T([3])([3.58+0.43])(squarePillars1)
//Prima riga di colonne colonne basse
squarePillars1Basse = GRID([[0.36,-3.58,0.36],[0.36],[3.15]])
squarePillars1Basse = T([1,2])([-0.18,-0.18])(squarePillars1Basse)
squarePillars1Basse = T([1,3])([0.36*3+3.58*3,3.58+0.43])(squarePillars1Basse)
primoPianoPrimaRiga = STRUCT([squarePillars1,squarePillars1Basse])
//Seconda riga di colonne alte dietro
squarePillars2 = GRID([[0.36,-3.58-0.36,0.36],[0.36],[3.15*2+0.43]])
squarePillars2 = T([2,3])([7.55,3.58+0.43])(squarePillars2)
squarePillars2 = T([1,2])([-0.18,-0.18])(squarePillars2)
//Seconda riga di colonna basse
squarePillars2Basse = GRID([[0.36,-3.58*2-0.36,0.36],[0.36],[3.15]])
squarePillars2Basse = T([1,2,3])([0.36*2+3.58*2,7.55,3.58+0.43])(squarePillars2Basse)
squarePillars2Basse = T([1,2])([-0.18,-0.18])(squarePillars2Basse)
primoPianoSecondaRiga = STRUCT([squarePillars2,squarePillars2Basse])
//Colonna tonda secondo piano
column = EXTRUDE([3.15])(circle)
column = T([1,2,3])([0.36*3+3.58*3,7.55,3.58+0.43])(column)
pillars1 = STRUCT([primoPianoPrimaRiga,primoPianoSecondaRiga,column])

//Secondo piano
//Prima fila
columnFront = GRID([[-0.36*4-3.58*4,0.36],[0.36],[3.15]])
columnFront = T([1,2])([-0.18,-0.18])(columnFront)
columnFront = T([3])([3.58*2+0.43])(columnFront)
//Seconda fila
columnBehind = GRID([[-0.36*2-3.58*2,0.36,-3.58,0.36,-3.58,0.36],[0.36],[3.15]])
columnBehind = T([1,2])([-0.18,-0.18])(columnBehind)
columnBehind = T([2,3])([7.55,3.58*2+0.43])(columnBehind)
pillars2 = STRUCT([columnFront,columnBehind])
//Terzo piano
//Dietro Prima 
columnBehindPrima = GRID([[0.22],[0.22],[1.57]])
columnBehindPrima = T([1,2,3])([-0.18,-0.11,3.58*3+0.43+1.62])(columnBehindPrima)
//Dietro seconda
colomnBehindSeconda = GRID([[-0.11-0.07-0.18-0.36-3.58,0.18],[0.22],[3.15]])
colomnBehindSeconda = T([1,2])([-0.11,-0.11])(colomnBehindSeconda)
colomnBehindSeconda = T([2,3])([7.55,3.58*3+0.43])(colomnBehindSeconda)
//Dietro terza
columnBehindTerza = GRID([[-0.36*2-3.58*2,0.36,-3.58,0.36,-3.58,0.36],[0.36],[3.15]])
columnBehindTerza = T([1,2])([-0.18,-0.18])(columnBehindTerza)
columnBehindTerza = T([2,3])([7.55,3.58*3+0.43])(columnBehindTerza)
//Davanti
columnFront = GRID([[-0.36*2-3.58*2,0.36,-3.58,-0.36,-3.58,0.36],[0.36],[3.15]])
columnFront = T([1,2])([-0.18,-0.18])(columnFront)
columnFront = T([3])([3.58*3+0.43])(columnFront)

columnBehind = STRUCT([columnBehindPrima,colomnBehindSeconda,columnBehindTerza])
pillars3 = STRUCT([columnBehind,columnFront])
building = STRUCT([pillars0,pillars1,pillars2,pillars3])

//VIEW(building)
//Floor zero
bigFloorZero = T([1,2])([1.90,2.64])(CUBOID([10.09,6.81,0.29]))
circleBassoZero = DISK(0.86)([30,1])
circleBassoZero = T([1,2])([2.76,2.6])(circleBassoZero)
circleBassoZero = EXTRUDE([0.29])(circleBassoZero)
quadratoSxZero = CUBOID([2.08,2.08,0.29])
quadratoSxZero = T([1,2])([-0.18,7.55-0.18])(quadratoSxZero)
quadratoDxZero = CUBOID([1.81,3.73,0.29])
quadratoDxZero = T([1,2])([11.63+0.36,5.72])(quadratoDxZero)
circleDxZero = DISK(1.86)([30,1])
circleDxZero = T([1,2])([11.63+0.36+1.86,7.58])(circleDxZero)
circleDxZero = EXTRUDE([0.29])(circleDxZero)
quadratoDxPiccolo = CUBOID([0.93,1.17,0.29])
quadratoDxPiccolo = T([1,2])([11.63+0.36,4.55])(quadratoDxPiccolo)

//Scala Primo Piano ******************************************************>
floor0 = STRUCT([bigFloorZero,circleBassoZero,quadratoSxZero,quadratoDxZero,circleDxZero,quadratoDxPiccolo])
//Primo
rettangoloLungo = CUBOID([3.44,7.55+1.9,0.43])
rettangoloLungo = T([1,2,3])([-0.18,-0.18,3.58])(rettangoloLungo)
rettangoloGrande = CUBOID([16.1-3.40,7.59,0.43])
rettangoloGrande = T([1,2,3])([3.44-0.18,-0.18,3.58])(rettangoloGrande)
arriviDalleScale = CUBOID([16.1-8.5-0.14,9.09-7.59,0.43])
arriviDalleScale = T([1,2,3])([8.5,7.59-0.18,3.58])(arriviDalleScale)
//Balconcino
balconcino = CUBOID([1.65,1.55,0.30])
balconcino = T([1,2,3])([-1.65-0.18,7.55-0.18,3.58+0.13])(balconcino)
floor1 = STRUCT([rettangoloLungo,rettangoloGrande,arriviDalleScale,balconcino])
//Secondo piano
rettangoloGrande = CUBOID([16.1-8.5+0.25,7.59,0.43])
rettangoloGrande = T([1,2,3])([8.5-0.45,-0.18,3.58*2])(rettangoloGrande)
arriviDalleScale = CUBOID([16.1-6.83,9.09-7.59,0.43])
arriviDalleScale = T([1,2,3])([6.83-0.18,7.59-0.18,3.58*2])(arriviDalleScale)

triangolo = SIMPLICIAL_COMPLEX([[6.63,7.45],[8.27,7.45],[8.27,0.05],[7.72,0.05]])([[0,1,2],[2,3,0]])
triangolo = EXTRUDE([0.43])(triangolo)
triangolo = T([3])([3.58*2])(triangolo)

floor2 = STRUCT([rettangoloGrande,arriviDalleScale,triangolo])
//Terzo piano
pavimentoGrande = CUBOID([16.25,7.87,0.43])
pavimentoGrande = T([1,2,3])([-0.18,-0.18,3.58*3])(pavimentoGrande)
pavimentoSx = CUBOID([8.23,1.5,0.43])
pavimentoSx = T([1,2,3])([-0.18,7.59,3.58*3])(pavimentoSx)
pavimentoDx = CUBOID([3.4+0.22,1.5,0.43])
pavimentoDx = T([1,2,3])([12.45,7.59,3.58*3])(pavimentoDx)

floor3 = STRUCT([pavimentoGrande,pavimentoSx,pavimentoDx])
//Ultimo piano
vetrata = T([1,2,3])([-0.2,-0.2,3.58*4])(CUBOID([10,9,1.3]))

floor4 = STRUCT([vetrata])


building = STRUCT([floor1,floor0,building,floor2,floor3,floor4])

VIEW(building)

//floor1 = STRUCT()
//floor2 = STRUCT()
//floor3 = STRUCT()
//floor4 = STRUCT()
//ES 3
muroBasso = (T([1,2,3])([-0.18,-0.14,3.58])(CUBOID([16,0.36,1.5])))
muroBassoSx = T([1,2,3])([-0.18,-0.18,5.08])(CUBOID([0.36*3+3.58*2,0.36,5.86+1.85]))
muroLatoDx = T([1,2,3])([-0.18+0.36*3+3.58*2,-0.18,9.44+1.43])(CUBOID([0.36+3.58,0.36,1.7]))
muroLatoDx2 = T([1,2,3])([-0.18+0.36*3+3.58*2,-0.18,5.83+1.43])(CUBOID([0.36+3.58,0.36,1.5]))
muroLatoDx3 = T([1,2,3])([-0.18+0.36*3+3.58*3,-0.18,5.06])(CUBOID([0.36*2+3.58,0.36,10.52]))
muroLatoDx4 = T([1,2,3])([-0.18+0.36*3+3.58*3,-0.18,5.06])(CUBOID([0.36*2+3.58,0.36,10.52]))
muroLatoDx5 = T([1,2,3])([9.595,-0.19,14.30])(CUBOID([1.79+0.36,0.36,1.3]))


east = STRUCT([muroBasso,muroBassoSx,muroLatoDx,muroLatoDx2,muroLatoDx3,muroLatoDx4,muroLatoDx5])


finestrone = muroBasso = (T([1,2,3])([-0.18,-0.14,3.58])(CUBOID([16,0.36,1.5])))
muroBassoSx = T([1,2,3])([-0.18,-0.18,5.08])(CUBOID([0.36*3+3.58*2,0.36,5.86+1.85]))
muroLatoDx = T([1,2,3])([-0.18+0.36*3+3.58*2,-0.18,9.44+1.43])(CUBOID([0.36+3.58,0.36,1.7]))
muroLatoDx2 = T([1,2,3])([-0.18+0.36*3+3.58*2,-0.18,5.83+1.43])(CUBOID([0.36+3.58,0.36,1.5]))
muroLatoDx3 = T([1,2,3])([-0.18+0.36*3+3.58*3,-0.18,5.06])(CUBOID([0.36*2+3.58,0.36,10.52]))
muroLatoDx4 = T([1,2,3])([-0.18+0.36*3+3.58*3,-0.18,5.06])(CUBOID([0.36*2+3.58,0.36,10.52]))
muroLatoDx5 = T([1,2,3])([9.595,-0.19,14.30])(CUBOID([1.79+0.36,0.36,1.3]))


east = STRUCT([muroBasso,muroBassoSx,muroLatoDx,muroLatoDx2,muroLatoDx3,muroLatoDx4,muroLatoDx5])

northUno = R([1,2])(PI/2)(GRID([[-0.36,1.79*4],[0.36],[1.72,-1.43,1.72,-1.43,1.72,-1.43,2.7]]))
northUno = T([1,3])([16.14,3.58])(northUno)

northSinistra = T([1,2,3])([15.79,-0.18,3.58])(CUBOID([0.35,0.54,12.12]))

northDestra = T([1,2,3])([15.79,-0.18+0.54+1.79*4,3.58])(CUBOID([0.35,0.54,12.15]))
northDestra2 = R([1,2])(PI/2)(GRID([[-0.15,0.2],[0.36],[-2.86,0.36,-2.86,0.36,-2.86,0.36]]))
northDestra2 = T([1,2,3])([16.14,7.87,3.58])(northDestra2)

northDestra3 = T([1,2,3])([15.79,-0.18+0.54+1.79*4+0.8,3.58])(CUBOID([0.35,0.54,12.15]))
north = STRUCT([northUno,northSinistra,northDestra,northDestra2,northDestra3])

building = STRUCT([building,east,north])
VIEW(building)
// Esercizio 4


finestra = R([1,2])([PI/2])(GRID([[0.38,-0.7],[0.2],[-0.36,2.86,-0.36,2.86,-0.36,2.86,-0.36,2.1]]))
spostata = T([1,2,3])([16.14,8.068,3.58])(finestra)

colore = COLOR([127/255,255/255,212/255,0.7])(spostata)

finestraRuotata = R([1,2])([PI/2])(GRID([[-0.36,1.79*4],[0.36],[-1.72,1.43,-1.72,1.43,-1.72,1.43,-2.7]]))
finestraTrasposta = T([1,3])([16.14,3.58])(finestraRuotata)

wind2 = T([1,2,3])([0.36*3+3.58*2-0.13,-0.13,5.08])(GRID([[4.5],[0.3],[2.2,-1.5,2.7,-1,2]]))
window_color2 = COLOR([127/255,255/255,212/255,0.7])(wind2)
colore_finestra = COLOR([127/255,255/255,212/255,0.7])(finestraTrasposta)
building = STRUCT([window_color2,colore,finestraTrasposta,building])
VIEW(building)