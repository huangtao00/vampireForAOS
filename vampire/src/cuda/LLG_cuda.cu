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
#ifdef CUDA
#include "atoms.hpp"
#include "material.hpp"
#include "errors.hpp"
#include "LLG.hpp"
#include "vcuda.hpp"

//int calculate_spin_fields(const int,const int);
//int calculate_external_fields(const int,const int);

namespace vcuda{
	  bool initf=false;
	  bool initLLGf=false;
	  // device arrays for atoms data


}


namespace vcuda{

int initLLG(){
    return EXIT_SUCCESS;

/*        LLG_arrays::x_spin_storage_array.resize(atoms::num_atoms,0.0);
        LLG_arrays::y_spin_storage_array.resize(atoms::num_atoms,0.0);
        LLG_arrays::z_spin_storage_array.resize(atoms::num_atoms,0.0);

        LLG_arrays::x_initial_spin_array.resize(atoms::num_atoms,0.0);
        LLG_arrays::y_initial_spin_array.resize(atoms::num_atoms,0.0);
        LLG_arrays::z_initial_spin_array.resize(atoms::num_atoms,0.0);

        LLG_arrays::x_euler_array.resize(atoms::num_atoms,0.0);
        LLG_arrays::y_euler_array.resize(atoms::num_atoms,0.0);
        LLG_arrays::z_euler_array.resize(atoms::num_atoms,0.0);

        LLG_arrays::x_heun_array.resize(atoms::num_atoms,0.0);
        LLG_arrays::y_heun_array.resize(atoms::num_atoms,0.0);
        LLG_arrays::z_heun_array.resize(atoms::num_atoms,0.0);

        LLG_arrays::LLG_set=true;*/

}

int LLG(const int num_steps){
    // Function to perform num_steps LLG integration steps on cuda enables device

    // check calling of routine if error checking is activated
    //if(err::check==true){std::cout << "vcuda::LLG has been called" << std::endl;}

    // check cuda atom arrays are initialised
    //if(vcuda::initf==false){
    //  std::cerr << "Warning - cuda device atom arrays are not initialised, initialising" << std::endl; 
    //}
    // check cuda LLG arrays are initialised
    //if(vcuda::initLLGf==false){
    //  std::cerr << "Warning - cuda device LLG arrays are not initialised, initialising" << std::endl;
    //}

    
			



	return EXIT_SUCCESS;
}

} // end of namespace vcuda
#endif

