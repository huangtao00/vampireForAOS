#include "colors.inc"
#include "metals.inc"
#include "screen.inc"
#declare LX=1.5;
#declare LY=1.5;
#declare LZ=1.5;
#declare CX=18;
#declare CY=18;
#declare CZ=18;
#declare ref=0.05;
global_settings { assumed_gamma 2.0 }
background { color Gray30 }
Set_Camera(<CX,CY,CZ>, <LX,LY,LZ>, 15)
Set_Camera_Aspect(4,3)
Set_Camera_Sky(<0,0,1>)
light_source { <2*CX, 2*CY, 2*CZ> color White}
#declare sscale0=2.0;
#declare rscale0=1.2;
#declare cscale0=3.54;
#declare cones0=0;
#declare arrows0=1;
#declare spheres0=1;
#declare cubes0=0;
#declare spincolors0=1;
#declare spincolor0=pigment {color rgb < 0.1 0.1 0.1 >};
#macro spinm0(cx,cy,cz,sx,sy,sz, cr,cg,cb)
union{
#if(spheres0) sphere {<cx,cy,cz>,0.5*rscale0} #end
#if(cubes0) box {<cx-cscale0*0.5,cy-cscale0*0.5,cz-cscale0*0.5>,<cx+cscale0*0.5,cy+cscale0*0.5,cz+cscale0*0.5>} #end
#if(cones0) cone {<cx+0.5*sx*sscale0,cy+0.5*sy*sscale0,cz+0.5*sz*sscale0>,0.0 <cx-0.5*sx*sscale0,cy-0.5*sy*sscale0,cz-0.5*sz*sscale0>,sscale0*0.5} #end
#if(arrows0) cylinder {<cx+sx*0.5*sscale0,cy+sy*0.5*sscale0,cz+sz*0.5*sscale0>,<cx-sx*0.5*sscale0,cy-sy*0.5*sscale0,cz-sz*0.5*sscale0>,sscale0*0.12}cone {<cx+sx*0.5*1.6*sscale0,cy+sy*0.5*1.6*sscale0,cz+sz*0.5*1.6*sscale0>,sscale0*0.0 <cx+sx*0.5*sscale0,cy+sy*0.5*sscale0,cz+sz*0.5*sscale0>,sscale0*0.2} #end
#if(spincolors0) texture { pigment {color rgb <cr cg cb>}finish {reflection {ref} diffuse 1 ambient 0}}
#else texture { spincolor0 finish {reflection {ref} diffuse 1 ambient 0}} #end
}
#end
#declare sscale1=2.0;
#declare rscale1=1.2;
#declare cscale1=3.54;
#declare cones1=0;
#declare arrows1=1;
#declare spheres1=1;
#declare cubes1=0;
#declare spincolors1=1;
#declare spincolor1=pigment {color rgb < 0.1 0.1 0.1 >};
#macro spinm1(cx,cy,cz,sx,sy,sz, cr,cg,cb)
union{
#if(spheres1) sphere {<cx,cy,cz>,0.5*rscale1} #end
#if(cubes1) box {<cx-cscale1*0.5,cy-cscale1*0.5,cz-cscale1*0.5>,<cx+cscale1*0.5,cy+cscale1*0.5,cz+cscale1*0.5>} #end
#if(cones1) cone {<cx+0.5*sx*sscale0,cy+0.5*sy*sscale1,cz+0.5*sz*sscale1>,0.0 <cx-0.5*sx*sscale1,cy-0.5*sy*sscale1,cz-0.5*sz*sscale1>,sscale0*0.5} #end
#if(arrows1) cylinder {<cx+sx*0.5*sscale1,cy+sy*0.5*sscale1,cz+sz*0.5*sscale1>,<cx-sx*0.5*sscale1,cy-sy*0.5*sscale1,cz-sz*0.5*sscale1>,sscale1*0.12}cone {<cx+sx*0.5*1.6*sscale1,cy+sy*0.5*1.6*sscale1,cz+sz*0.5*1.6*sscale1>,sscale1*0.0 <cx+sx*0.5*sscale1,cy+sy*0.5*sscale1,cz+sz*0.5*sscale1>,sscale1*0.2} #end
#if(spincolors1) texture { pigment {color rgb <cr cg cb>}finish {reflection {ref} diffuse 1 ambient 0}}
#else texture { spincolor1 finish {reflection {ref} diffuse 1 ambient 0}} #end
}
#end
#include "atoms-00000027.inc"
