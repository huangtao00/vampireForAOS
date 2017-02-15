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
///
/// @file
/// @brief Contains the partial hysteresis program
///
/// @details Performs a partial field loop to calculate field dependent magnetisation
///
/// @section License
/// Use of this code, either in source or compiled form, is subject to license from the authors.
/// Copyright \htmlonly &copy \endhtmlonly Richard Evans, 2009-2010. All Rights Reserved.
///
/// @section info File Information
/// @author  Richard Evans, richard.evans@york.ac.uk
/// @version 1.0
/// @date    02/12/2013
/// @internal
///	Created:		02/12/2013
///	Revision:	02/12/2013
///=====================================================================================
///

// Standard Libraries
#include <cstdlib>

// Vampire Header files
#include "vmath.hpp"
#include "errors.hpp"
#include "sim.hpp"
#include "stats.hpp"
#include "vio.hpp"


namespace program{

/// @brief Function to calculate the partial hysteresis loop
///
/// @callgraph
/// @callergraph
///
/// @details sim:program=partial-hysteresis-loop simulates a partial hysteresis loop, starting at
///          sim:minimum-applied-field-strength to sim:maximum-applied-field-strength in steps of
///          sim:applied-field-strength-increment. Note that the sign of the increment is
///          significant, indicating the direction of the loop. Invalid combinations (which lead to
///          an infinite loop) are checked during the initialisation and will print out a warning.
///          As with the full hysteresis loop, the minimum resolution of the applied field 
///          increment is 1 uT. 
///
/// @section License
/// Use of this code, either in source or compiled form, is subject to license from the authors.
/// Copyright \htmlonly &copy \endhtmlonly Richard Evans, 2009-2010. All Rights Reserved.
///
/// @section Information
/// @author  Richard Evans, richard.evans@york.ac.uk
/// @version 1.0
/// @date    02/12/20103
///
/// @return EXIT_SUCCESS
/// 
/// @internal
///	Created:		02/12/2013
///	Revision:	  ---
///=====================================================================================
///
void partial_hysteresis_loop(){
   
   // check calling of routine if error checking is activated
   if(err::check==true){std::cout << "program::partial-hysteresis has been called" << std::endl;}
   
   // Equilibrate system in saturation field
   sim::H_applied=sim::Heq;
   sim::integrate(sim::equilibration_time);
      
   // Setup min and max fields and increment (uT)
   int iHmax=vmath::iround(double(sim::Hmax)*1.0E6);
   int iHmin=vmath::iround(double(sim::Hmin)*1.0E6);
   int iHinc=vmath::iround(double(sim::Hinc)*1.0E6);

   // Check for loop direction and adjust parameters
   // so that field loop works in positive sense
   double parity=1.0;
   if(iHinc < 0){
      iHmax=-iHmax;
      iHmin=-iHmin;
      iHinc=-iHinc;
      parity=-1.0;
   }

   // Perform Field Loop
   for(int H=iHmin;H<=iHmax;H+=iHinc){
      
      // Set applied field (Tesla)
      sim::H_applied=double(H)*parity*1.0e-6;
      
      // Reset start time
      int start_time=sim::time;
      
      // Reset mean magnetisation counters
      stats::mag_m_reset();

      // Integrate system
      while(sim::time<sim::loop_time+start_time){

         // Integrate system
         sim::integrate(sim::partial_time);
      
         // Calculate mag_m, mag
         stats::mag_m();

      }

      // Output to screen and file after each field
      vout::data();
      
   } // End of field loop

   return;
}

}//end of namespace program


