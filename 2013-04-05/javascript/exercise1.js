//Pillars first floor
//Pillar's radius and height in dm
var r = 1.25
var h = 25
var l = 2.5

CYLINDER = function (params) {
  var R = params[0];
  var h = params[1];
  return function (dims) {
    var domain = DOMAIN([[0,2*PI], [0,R]])([dims, 1]);
    var mapping = function (v) {
      var a = v[0];
      var r = v[1];
      return [r*COS(v[0]),r*SIN(v[0])]
    }
    var circle = MAP(mapping)(domain);
    return EXTRUDE([h])(circle)
  }
}

//Pillar trasnlation
var t_bottom = T([1])([25+2.5])
var t_top = T([2])([52+2.5]) 
var t_top_x = T([1])([110])

//Pillars
var pillar = T([1,2,3])([1.25,1.25,0.1])((CYLINDER([r,h])(80))) 
var square_pillar = CUBOID([l,l,h])
var square_pillar_translate = T([1,2])([25+2.5,52+2.5])(square_pillar)
var bottom_pillars = STRUCT(NN(5) ([pillar,t_bottom]))
var top_pillars = STRUCT([t_top,pillar,t_top_x,pillar])
var square_top_pillars = STRUCT(NN(3) ([square_pillar_translate,t_bottom]))

//FLOOR 0
var pillars0 = STRUCT([bottom_pillars,top_pillars,square_top_pillars])


//FLOOR 1

var first_floor_square_pillars = GRID([[2.5,-25,2.5,-25,2.5,-25,-2.5,-25,2.5,-25],[2.5,-52,2.5],[-25,-2,25]])
var square_pillar_floor1 = T([1,3])([3*2.5+3*25,25+2])(square_pillar)
var round_pillar_floor2 = T([1,2,3])([3*2.5+3*25,52+2.5,25+2+25+2])(pillar)

var pillars1 = STRUCT([first_floor_square_pillars,square_pillar_floor1,round_pillar_floor2])


//FLOOR 2
var second_floor_square_pillars = GRID([[2.5,-25,2.5,-25,-2.5,-25,-2.5,-25,2.5,-25],[2.5,-52,2.5],[-25,-2,-25,-2,25]])
var square_pillar1_floor2 = T([1,2,3])([2*2.5+2*25,52+2.5,25+2+25+2])(square_pillar)
var square_pillar2_floor2 = T([1,2,3])([3*2.5+3*25,52+2.5,25+2+25+2])(square_pillar)

var pillars2 = STRUCT([second_floor_square_pillars,square_pillar2_floor2,square_pillar1_floor2])

//FLOOR 3
var third_floor_square_pillars = GRID([[-2.5,-25,-2.5,-25,2.5,-25,-2.5,-25,2.5],[2.5,-52,2.5],[-25,-2,-25,-2,-25,-2,25]])
var square_pillars_top =  GRID([[1.5,-1-25,1.5,-1-25,-2.5,-25,2.5,-25],[-2.5,-52,2.5],[-25,-2,-25,-2,-25,-2,25]])

var pillars3 = STRUCT([third_floor_square_pillars,square_pillars_top])

//Building
var building = STRUCT([pillars0,pillars1,pillars2,pillars3])
VIEW(building)


//FLOOR 1

var first_floor_square_pillars = GRID([[2.5,-25,2.5,-25,2.5,-25,-2.5,-25,2.5,-25],[2.5,-52,2.5],[-25,-2,25]])
var square_pillar_floor1 = T([1,3])([3*2.5+3*25,25+2])(square_pillar)
var round_pillar_floor2 = T([1,2,3])([3*2.5+3*25,52+2.5,25+2+25+2])(pillar)

var pillars1 = STRUCT([first_floor_square_pillars,square_pillar_floor1,round_pillar_floor2])


//FLOOR 2
var second_floor_square_pillars = GRID([[2.5,-25,2.5,-25,-2.5,-25,-2.5,-25,2.5,-25],[2.5,-52,2.5],[-25,-2,-25,-2,25]])
var square_pillar1_floor2 = T([1,2,3])([2*2.5+2*25,52+2.5,25+2+25+2])(square_pillar)
var square_pillar2_floor2 = T([1,2,3])([3*2.5+3*25,52+2.5,25+2+25+2])(square_pillar)

var pillars2 = STRUCT([second_floor_square_pillars,square_pillar2_floor2,square_pillar1_floor2])

//FLOOR 3
var third_floor_square_pillars = GRID([[-2.5,-25,-2.5,-25,2.5,-25,-2.5,-25,2.5],[2.5,-52,2.5],[-25,-2,-25,-2,-25,-2,25]])
var square_pillars_top =  GRID([[1.5,-1-25,1.5,-1-25,-2.5,-25,2.5,-25],[-2.5,-52,2.5],[-25,-2,-25,-2,-25,-2,25]])

var pillars3 = STRUCT([third_floor_square_pillars,square_pillars_top])

//Building
var building = STRUCT([pillars0,pillars1,pillars2,pillars3])
VIEW(building)
