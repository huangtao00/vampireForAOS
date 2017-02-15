#include "colors.inc"
#include "metals.inc"
#include "screen.inc"
#declare LX=21.144;
#declare LY=21.144;
#declare LZ=21.144;
#declare CX=180.728;
#declare CY=75.728;
#declare CZ=75.728;
#declare ref=0.05;
global_settings { assumed_gamma 2.0 }
background { color White }
Set_Camera(<CX,CY,CZ>, <LX,LY,LZ>, 15)
Set_Camera_Aspect(4,3)
Set_Camera_Sky(<0,0,1>)
light_source { <8*CX, 3*CY,  12*CZ> color <0.96,0.96,0.96>}
#declare sscale0=2.0;
#declare rscale0=1.2;
#declare cscale0=3.54;
#declare cones0=0;
#declare arrows0=0;
#declare spheres0=1;
#declare cubes0=0;
#declare spincolors0=1;
#declare spincolor0=pigment {color rgb < 0.1 0.1 0.1 >};
#macro spinm0(cx,cy,cz,sx,sy,sz, cr,cg,cb)
union{
#if(spheres0) sphere {<cx,cy,cz>,1*rscale0} #end
#if(cubes0) box {<cx-cscale0*0.5,cy-cscale0*0.5,cz-cscale0*0.5>,<cx+cscale0*0.5,cy+cscale0*0.5,cz+cscale0*0.5>} #end
#if(cones0) cone {<cx+0.5*sx*sscale0,cy+0.5*sy*sscale0,cz+0.5*sz*sscale0>,0.0 <cx-0.5*sx*sscale0,cy-0.5*sy*sscale0,cz-0.5*sz*sscale0>,sscale0*0.5} #end
#if(arrows0) cylinder {<cx+sx*0.5*sscale0,cy+sy*0.5*sscale0,cz+sz*0.5*sscale0>,<cx-sx*0.5*sscale0,cy-sy*0.5*sscale0,cz-sz*0.5*sscale0>,sscale0*0.12}cone {<cx+sx*0.5*1.6*sscale0,cy+sy*0.5*1.6*sscale0,cz+sz*0.5*1.6*sscale0>,sscale0*0.0 <cx+sx*0.5*sscale0,cy+sy*0.5*sscale0,cz+sz*0.5*sscale0>,sscale0*0.2} #end

#if(spincolors0) texture { pigment {color rgb <1 1 1>}finish {phong 0.8 diffuse 0.98 ambient 0.001}}
#else texture { spincolor0 finish {reflection {ref} diffuse 1 ambient 0}} #end
}
#end




#macro my_location(len,rad,axie_color,xd,yd,zd)
union{
cylinder {

	<-len,0,0>
	<len,0,0> rad
	pigment {
	color axie_color

	}


}
cone{
<len,0,0> rad
<len+2,0,0> 0
color  Black
	
}
rotate <xd,yd,zd>

}
#end

/*
my_location(30,0.5,Red,0,0,0) //x
my_location(30,0.5,Green,0,0,90)//y
my_location(30,0.5,Blue,0,-90,0)//z

*/

#include "atoms-00000000.inc"
