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
/* ESERCIZIO 1*/
//Piano terra
circle = DISK(0.18)([30,1])
column = EXTRUDE([3.58])(circle)
columns = STRUCT(NN(5)([column,T([1])([3.94])]))
columnOnBalcony = T([2])([7.55])(column)
//Quadrati
squarePillars = GRID([[0.36,-1.86,0.36,-3.58,0.36,-3.58,0.36],[0.36],[3.29]])
squarePillars = T([1,2])([-0.18,-0.18])(squarePillars)
squarePillars = T([1,2,3])([2.08,7.55,0.29])(squarePillars)
pillars0 = STRUCT([columns,columnOnBalcony,squarePillars])
//Primo piano
//Prima riga di colonne di front piu alte
squarePillars1 = GRID([[0.36,-3.58,0.36,-3.58,0.36],[0.36],[3.15*2+0.43]])
squarePillars1 = T([1,2])([-0.18,-0.18])(squarePillars1)
squarePillars1 = T([3])([3.58+0.43])(squarePillars1)
//Prima riga di colonne basse
squarePillars1Basse = GRID([[0.36,-3.58,0.36],[0.36],[3.15]])
squarePillars1Basse = T([1,2])([-0.18,-0.18])(squarePillars1Basse)
squarePillars1Basse = T([1,3])([0.36*3+3.58*3,3.58+0.43])(squarePillars1Basse)
primoPianoPrimaRiga = STRUCT([squarePillars1,squarePillars1Basse])
//Seconda riga di colonne alte dietro
squarePillars2 = GRID([[0.36,-3.58-0.36,0.36],[0.36],[3.15*2+0.43]])
squarePillars2 = T([2,3])([7.55,3.58+0.43])(squarePillars2)
squarePillars2 = T([1,2])([-0.18,-0.18])(squarePillars2)
//Seconda riga di colonna basse
squarePillars2Basse = GRID([[0.36,-3.58*2,0.36],[0.36],[3.15]])
squarePillars2Basse = T([1,2,3])([0.36*3+3.58*2,7.55,3.58+0.43])(squarePillars2Basse)
squarePillars2Basse = T([1,2])([-0.18,-0.18])(squarePillars2Basse)
primoPianoSecondaRiga = STRUCT([squarePillars2,squarePillars2Basse])
//Colonna tonda secondo piano
column = EXTRUDE([3.15])(circle)
column = T([1,2,3])([0.36*4+3.58*3,7.55,3.58+0.43])(column)
pillars1 = STRUCT([primoPianoPrimaRiga,primoPianoSecondaRiga,column])
//Secondo piano
//Prima fila
columnFront = GRID([[-0.36*4-3.58*4,0.36],[0.36],[3.15]])
columnFront = T([1,2])([-0.18,-0.18])(columnFront)
columnFront = T([3])([3.58*2+0.43])(columnFront)
//Seconda fila
columnBehind = GRID([[-0.36*3-3.58*2,0.36,-3.58,0.36,-3.58+0.36,0.36],[0.36],[3.15]])
columnBehind = T([1,2])([-0.18,-0.18])(columnBehind)
columnBehind = T([2,3])([7.55,3.58*2+0.43])(columnBehind)
pillars2 = STRUCT([columnFront,columnBehind])
//Terzo piano
//Dietro Prima 
columnBehindPrima = GRID([[0.22],[0.22],[1.57]])
columnBehindPrima = T([1,2])([-0.18,-0.11])(columnBehindPrima)
columnBehindPrima = T([2,3])([7.55,3.58*3+0.43+1])(columnBehindPrima)
//Dietro seconda
colomnBehindSeconda = GRID([[-0.11-0.07-0.18-0.36-3.58,0.18],[0.22],[3.15]])
colomnBehindSeconda = T([1,2])([-0.11,-0.11])(colomnBehindSeconda)
colomnBehindSeconda = T([2,3])([7.55,3.58*3+0.43])(colomnBehindSeconda)
//Dietro terza
columnBehindTerza = GRID([[-0.36*3-3.58*2,0.36,-3.58,0.36,-3.58+0.36,0.36],[0.36],[3.15]])
columnBehindTerza = T([1,2])([-0.18,-0.18])(columnBehindTerza)
columnBehindTerza = T([2,3])([7.55,3.58*3+0.43])(columnBehindTerza)
//Davanti
columnFront = GRID([[-0.36*2-3.58*2,0.36,-3.58,-0.36,-3.58,0.36],[0.36],[3.15]])
columnFront = T([1,2])([-0.18,-0.18])(columnFront)
columnFront = T([3])([3.58*3+0.43])(columnFront)
//Dietro
columnBehind = STRUCT([columnBehindPrima,colomnBehindSeconda,columnBehindTerza])
pillars3 = STRUCT([columnBehind,columnFront])
//Risultato
building = STRUCT([pillars0,pillars1,pillars2,pillars3])
DRAW(building)