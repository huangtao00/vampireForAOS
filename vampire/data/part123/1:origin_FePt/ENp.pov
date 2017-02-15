#include "colors.inc"
#include "metals.inc"
#include "screen.inc"
#declare LX=1.4435;
#declare LY=1.4435;
#declare LZ=1.4435;
#declare CX=8;
#declare CY=8;
#declare CZ=-12;
#declare ref=0;
#declare boner=0.05;
global_settings { assumed_gamma 2.0 }
background { color <1 1 1> }

Set_Camera(<CX,CY,CZ>, <LX,LY,LZ>, 30)
Set_Camera_Aspect(4,3)
 camera {
  location < CX,CY CZ>
  look_at < LX,LY,LZ>
  up    < 0, 1, 0>
  right   < 1, 0, 0>
  rotate  <90, 0, 0>

  rotate <0,0,5>

 }


light_source { <2*CX, 2*CY, 2*CZ> color White
  rotate  <90, 0, 0>
}

#macro Bone(sx,sy,sz,endx,endy,endz,r,cr,cg,cb) union{     cylinder { <sx, sy,
sz>, <endx,endy,endz>,r     texture {         pigment {         color <cr cg
cb>         }         finish {reflection {0} diffuse 1 ambient 0}     }
no_shadow     }

}
#end 

#macro Bone1(sx,sy,sz,endx,endy,endz,r)
union{
	cylinder { <sx, sy, sz>, <endx,endy,endz>,r
	texture {
		pigment {
		color <0.0 0.9 .1>
		}
		finish {reflection {0} diffuse 1 ambient 0}
	}
	no_shadow
	}

}
#end 

#macro Bone2(sx,sy,sz,endx,endy,endz,r)
union{
	cylinder { <sx, sy, sz>, <endx,endy,endz>,r
	texture {
		pigment {
		color <0.0 0.0 .9>
		}
		finish {reflection {0} diffuse 1 ambient 0}
	}
	no_shadow
	}

}
#end 



#declare sscale0=1;
#declare rscale0=1;
#declare cscale0=1;
#declare cones0=0;
#declare spheres0=1;
#declare arrows0=0;
#declare cubes0=0;
#declare spincolors0=1;
#declare spincolor0=pigment {color rgb < 0.1 0.1 0.1 >};


#macro spinm0(cx,cy,cz,sx,sy,sz, cr,cg,cb)
union{
#if(spheres0) sphere {<cx,cy,cz>,0.3*rscale0 no_shadow} 
#end

#if(cubes0) box {<cx-cscale0*0.5,cy-cscale0*0.5,cz-cscale0*0.5>,<cx+cscale0*0.5,cy+cscale0*0.5,cz+cscale0*0.5>} 
#end

#if(cones0) cone {<cx+0.5*sx*sscale0,cy+0.5*sy*sscale0,cz+0.5*sz*sscale0>,0.0 <cx-0.5*sx*sscale0,cy-0.5*sy*sscale0,cz-0.5*sz*sscale0>,sscale0*0.5} #end
#if(arrows0) cylinder {<cx+sx*0.5*sscale0,cy+sy*0.5*sscale0,cz+sz*0.5*sscale0>,<cx-sx*0.5*sscale0,cy-sy*0.5*sscale0,cz-sz*0.5*sscale0>,sscale0*0.12}cone {<cx+sx*0.5*1.6*sscale0,cy+sy*0.5*1.6*sscale0,cz+sz*0.5*1.6*sscale0>,sscale0*0.0 <cx+sx*0.5*sscale0,cy+sy*0.5*sscale0,cz+sz*0.5*sscale0>,sscale0*0.2} #end
#if(spincolors0) 
texture 
{ 
pigment {color rgb <cr cg cb>}finish {reflection {ref} diffuse 1 ambient 0}
}
#else 
texture 
{ 
spincolor0 finish {reflection {ref} diffuse 1 ambient 0}} #end
}
#end


#declare sscale1=1;
#declare rscale1=1;
#declare cscale1=1;
#declare cones1=0;
#declare spheres1=1;
#declare arrows1=0;
#declare cubes1=0;
#declare spincolors1=1;
#declare spincolor1=pigment {color rgb < 0.1 0.1 0.1 >};
#macro spinm1(cx,cy,cz,sx,sy,sz, cr,cg,cb)
union{
#if(spheres1) sphere {<cx,cy,cz>,0.3*rscale1 no_shadow} #end
#if(cubes1) box {<cx-cscale1*0.5,cy-cscale1*0.5,cz-cscale1*0.5>,<cx+cscale1*0.5,cy+cscale1*0.5,cz+cscale1*0.5>} #end
#if(cones1) cone {<cx+0.5*sx*sscale0,cy+0.5*sy*sscale1,cz+0.5*sz*sscale1>,0.0 <cx-0.5*sx*sscale1,cy-0.5*sy*sscale1,cz-0.5*sz*sscale1>,sscale0*0.5} #end
#if(arrows1) cylinder {<cx+sx*0.5*sscale1,cy+sy*0.5*sscale1,cz+sz*0.5*sscale1>,<cx-sx*0.5*sscale1,cy-sy*0.5*sscale1,cz-sz*0.5*sscale1>,sscale1*0.12}cone {<cx+sx*0.5*1.6*sscale1,cy+sy*0.5*1.6*sscale1,cz+sz*0.5*1.6*sscale1>,sscale1*0.0 <cx+sx*0.5*sscale1,cy+sy*0.5*sscale1,cz+sz*0.5*sscale1>,sscale1*0.2} #end
#if(spincolors1) texture { pigment {color rgb <0 1 1> }finish {reflection {ref} diffuse 1 ambient 0}}
#else texture { spincolor1 finish {reflection {ref} diffuse 1 ambient 0}} #end
}
#end



#include "ENp_py.inc"
