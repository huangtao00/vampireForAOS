//-----------------------------------------------------------------------------
//
// This source file is part of the VAMPIRE open source package under the
// GNU GPL (version 2) licence (see licence file for details).
//
// (c) R F L Evans 2014. All rights reserved.
//
//-----------------------------------------------------------------------------

// System headers
#include <fstream>
#include <iostream>
#include <string>
#include <sstream>

// Program headers
#include "atoms.hpp"
#include "errors.hpp"
#include "random.hpp"
#include "sim.hpp"
#include "vio.hpp"

//-----------------------------------------------------------------------------
// Function to save checkpoint file
//-----------------------------------------------------------------------------
void save_checkpoint(){

   // convert number of atoms, rank and time to standard long int
   uint64_t natoms64 = uint64_t(atoms::num_atoms-vmpi::num_halo_atoms);
   int64_t time64 = int64_t(sim::time);
   int64_t eqtime64 = int64_t(sim::equilibration_time);

   // determine checkpoint file name
   std::stringstream chkfilenamess;
   chkfilenamess << "vampire" << vmpi::my_rank << ".chk";
   std::string chkfilename = chkfilenamess.str();

   // open checkpoint file
   std::ofstream chkfile;
   chkfile.open(chkfilename.c_str(),std::ios::binary);

   // check for open file
   if(!chkfile.is_open()){
      terminaltextcolor(RED);
      std::cerr << "Error: Unable to open checkpoint file " << chkfilename << " for writing. Exiting." << std::endl;
      terminaltextcolor(WHITE);
      zlog << zTs() << "Error: Unable to open checkpoint file " << chkfilename << " for writing. Exiting." << std::endl;
      err::vexit();
   }

   // get state of random number generator
   std::vector<uint32_t> mt_state(624); // 624 is hard coded in mt implementation. uint64 assumes same size as unsigned long
   int32_t mt_p=0; // position in rng state
   mt_p=mtrandom::grnd.get_state(mt_state);

   // write checkpoint variables to file
   chkfile.write(reinterpret_cast<const char*>(&natoms64),sizeof(uint64_t));
   chkfile.write(reinterpret_cast<const char*>(&time64),sizeof(int64_t));
   chkfile.write(reinterpret_cast<const char*>(&eqtime64),sizeof(int64_t));
   chkfile.write(reinterpret_cast<const char*>(&mt_p),sizeof(int32_t));
   chkfile.write(reinterpret_cast<const char*>(&mt_state[0]),sizeof(uint32_t)*mt_state.size());

   // write spin array to file
   chkfile.write(reinterpret_cast<const char*>(&atoms::x_spin_array[0]),sizeof(double)*natoms64);
   chkfile.write(reinterpret_cast<const char*>(&atoms::y_spin_array[0]),sizeof(double)*natoms64);
   chkfile.write(reinterpret_cast<const char*>(&atoms::z_spin_array[0]),sizeof(double)*natoms64);

   // close checkpoint file
   chkfile.close();

   // log writing checkpoint file 
   zlog << zTs() << "Checkpoint file written to disk." << std::endl;

   return;

}

//-----------------------------------------------------------------------------
// Function to save checkpoint file
//-----------------------------------------------------------------------------
void load_checkpoint(){

   // convert number of atoms, rank and time to standard long int
   uint64_t natoms64;
   int64_t time64;
   int64_t eqtime64;

   // variables for loading state of random number generator
   std::vector<uint32_t> mt_state(624); // 624 is hard coded in mt implementation. uint64 assumes same size as unsigned long
   int32_t mt_p=0; // position in rng state

   // determine checkpoint file name
   std::stringstream chkfilenamess;
   chkfilenamess << "vampire" << vmpi::my_rank << ".chk";
   std::string chkfilename = chkfilenamess.str();

   // open checkpoint file
   std::ifstream chkfile;
   chkfile.open(chkfilename.c_str(),std::ios::binary);
 
   // check for open file
   if(!chkfile.is_open()){
      terminaltextcolor(RED);
      std::cerr << "Error: Unable to open checkpoint file " << chkfilename << " for reading. Exiting." << std::endl;
      std::cerr << "Info: sim:continue may be specified in the input file which requires a valid checkpoint file." << std::endl;
      terminaltextcolor(WHITE);
      zlog << zTs() << "Error: Unable to open checkpoint file " << chkfilename << " for reading. Exiting." << std::endl;
      zlog << zTs() << "Info: sim:continue may be specified in the input file which requires a valid checkpoint file." << std::endl;
      err::vexit();
   }

   // read checkpoint variables from file
   chkfile.read((char*)&natoms64,sizeof(uint64_t));
   chkfile.read((char*)&time64,sizeof(int64_t));
   chkfile.read((char*)&eqtime64,sizeof(int64_t));
   chkfile.read((char*)&mt_p,sizeof(int32_t));
   chkfile.read((char*)&mt_state[0],sizeof(uint32_t)*mt_state.size());

   // if continuing set state of rng
   if(sim::load_checkpoint_continue_flag) mtrandom::grnd.set_state(mt_state, mt_p);

   // check for rational number of atoms
   if((atoms::num_atoms-vmpi::num_halo_atoms)!=natoms64){
      terminaltextcolor(RED);
      std::cerr << "Error: Mismatch between number of atoms in checkpoint file (" << natoms64 << ") and number of generated atoms (" << atoms::num_atoms-vmpi::num_halo_atoms << "). Exiting." << std::endl;
      terminaltextcolor(WHITE);
      zlog << zTs() << "Error: Mismatch between number of atoms in checkpoint file (" << natoms64 << ") and number of generated atoms (" << atoms::num_atoms-vmpi::num_halo_atoms << "). Exiting." << std::endl;
   }

   // Load saved time if simulation continuing
   if(sim::load_checkpoint_continue_flag){
      sim::time = time64;
      sim::equilibration_time = eqtime64;
   }

   // Load spin positions
   chkfile.read((char*)&atoms::x_spin_array[0],sizeof(double)*natoms64);
   chkfile.read((char*)&atoms::y_spin_array[0],sizeof(double)*natoms64);
   chkfile.read((char*)&atoms::z_spin_array[0],sizeof(double)*natoms64);

   // close checkpoint file
   chkfile.close();

   // log reading checkpoint file 
   zlog << zTs() << "Checkpoint file loaded at sim::time " << sim::time << "." << std::endl;

   return;

}

