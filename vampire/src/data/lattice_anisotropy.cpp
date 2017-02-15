//-----------------------------------------------------------------------------
//
//  Vampire - A code for atomistic simulation of magnetic materials
//
//  Copyright (C) 2009-2012 R.F.L.Evans
//
//  Email:richard.evans@york.ac.uk
//
//  This program is free software; you can redistribute it and/or modify 
//  it under the terms of the GNU General Public License as published by 
//  the Free Software Foundation; either version 2 of the License, or 
//  (at your option) any later version.
//
//  This program is distributed in the hope that it will be useful, but 
//  WITHOUT ANY WARRANTY; without even the implied warranty of 
//  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU 
//  General Public License for more details.
//
//  You should have received a copy of the GNU General Public License 
//  along with this program; if not, write to the Free Software Foundation, 
//  Inc., 59 Temple Place, Suite 330, Boston, MA 02111-1307 USA.
//
// ----------------------------------------------------------------------------
//
// System headers
//---------------------------
#include <fstream>
#include <sstream>
#include <string>

// vampire headers
#include "errors.hpp"
#include "material.hpp"
#include "vio.hpp"
#include "vmath.hpp"

//--------------------------------------------------
// class functions for lattice anisotropy
//--------------------------------------------------

//--------------------------------------------------
// Add point to list of input points
//
void lattice_anis_t::add_point(double temperature, double anisotropy){

   // check for valid temperature value
   if( temperature < 0.0 && temperature > 10000.0 ){
      std::cerr << "Error: Temperature value " << temperature << " in lattice anisotropy file is invalid. Temperature values must be in the range 0 - 10000 K. Exiting." << std::endl;
      zlog << zTs() << "Error: Temperature value " << temperature << " in lattice anisotropy file is invalid. Temperature values must be in the range 0 - 10000 K. Exiting." << std::endl;
      err::vexit();
   }

   // add values to list
   T.push_back(temperature);
   k.push_back(anisotropy);

   return;
}

//--------------------------------------------------
// Creates a lookup table of interpolated functions
// to calculate lattice anisotropy
//
void lattice_anis_t::set_interpolation_table(){

   // Output informative message to log
   zlog << zTs() << "Determining interpolation variables for tabulated lattice anisotropy." << std::endl;

   // Check for undefined lattice anisotropy
   if(T.size()==0){
      Tmax=0;
      k_Tmax=0.0;
      return;
   }

   // check T(i+1) > T(i)
   for(unsigned int i=1; i<T.size(); i++){
      if(T[i]<T[i-1]){
         std::cerr << "Error: temperature value "<< T[i] <<" on line " << i+2 << " is less than the previous value " << T[i-1] << " and must be given in ascending order. Exiting" << std::endl;
         zlog << zTs() << "Error: temperature value "<< T[i] <<" on line " << i+2 << " is less than the previous value " << T[i-1] << " and must be given in ascending order. Exiting" << std::endl;
         err::vexit();
      }
   }

   // loop over all temperatures up to Tmax and create temporary list of min, max, m and c values
   std::vector<double> tmin;
   std::vector<double> tmax;
   std::vector<double> tm;
   std::vector<double> tc;

   // start from i+1
   for(unsigned int i=1; i<T.size(); i++){
      tmin.push_back(T[i-1]);
      tmax.push_back(T[i]);
      tm.push_back(vmath::interpolate_m(T[i-1],k[i-1],T[i],k[i]));
      tc.push_back(vmath::interpolate_c(T[i-1],k[i-1],T[i],k[i]));
   }

   // determine maximum temperature specified in interpolation table
   Tmax=int(T[T.size()-1]);

   // resize interpolation array to size Tmax
   m.resize(Tmax,0.0);
   c.resize(Tmax,0.0);

   // determine last value of k at Tmax
   k_Tmax = k[k.size()-1];

   // determine first value of k
   double k_Tmin = k[0];
   double Tmin = T[0];

   // loop over all values up to Tmax and substitute m and c interpolation
   for(unsigned int Ti=0; Ti<Tmax; Ti++){ // 1 Kelvin resolution

      bool found_mc=false;

      // Check for T<Tmin
      if(double(Ti)<double(Tmin)){

         m[Ti] = 0;
         c[Ti] = k_Tmin;

         //mark valid value found
         found_mc = true;

         // move to next temperature value
         continue;

      }

      // loop over all possible values
      for(unsigned int mm=0; mm<tmin.size(); mm++){

         double min = tmin[mm];
         double max = tmax[mm];

         // check if Ti is in temperature range
         if( double(Ti) >= min && double(Ti) < max ){

            // copy interpolation values
            m[Ti] = tm[mm];
            c[Ti] = tc[mm];

            // mark valid function found
            found_mc = true;

            // move to next temperature value Ti
            break;

         }
      }

      // check for value not in range
      if(found_mc==false){
         std::cerr << "Code error: Temperature value " << Ti << " in interpolation function is not within range specified in lattice-anisotropy-file. Exiting" << std::endl;
         zlog << zTs() << "Code error: Temperature value " << Ti << " in interpolation function is not within range specified in lattice-anisotropy-file. Exiting" << std::endl;
         err::vexit();
      }

   }

   return;

}

//--------------------------------------------------
// Creates a lookup table of interpolated functions
// to calculate lattice anisotropy
//
double lattice_anis_t::get_lattice_anisotropy_constant(double temperature){

   // convert temperature to index
   const unsigned int Ti = int(temperature);

   // check for value larger than Tmax
   if(Ti>=Tmax) return k_Tmax;

   // otherwise return interpolated value
   else return m[Ti]*temperature+c[Ti];

}

//-------------------------------------------------------
// Prints interpolated values of input function to file
//
void lattice_anis_t::output_interpolated_function(int i){

   const unsigned int ten_Tmax = 10*Tmax;

   // open output file
   std::ofstream ofile;
   std::stringstream fname_ss;
   fname_ss << "interpolated-lattice-anisotropy-" << i+1 << ".latt";
   ofile.open((std::string(fname_ss.str()).c_str()));

   // loop over temperature values and output to file
   for(unsigned int tempi=0; tempi<ten_Tmax;tempi++){

      double temperature=0.1*double(tempi);

      ofile << temperature << "\t" << get_lattice_anisotropy_constant(temperature)  << std::endl;

   }

   // output final value
   ofile << 10000.0 << "\t" << get_lattice_anisotropy_constant(10000.0) << std::endl;

   // close output file
   ofile.close();

   return;

}
