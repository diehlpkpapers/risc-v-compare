git clone https://github.com/lanl/UME
cd UME
mkdir build_mpi
cd build_mpi
cmake cmake -DCXX_FLAGS="-std=c++20" -DUSE_CATCH2=NO -DUSE_KOKKOS=NO -DUSE_MPI=YES -DUSE_OPENACC=NO -DCMAKE_BUILD_TYPE=Release ..
make

This will build UME with executable in the build_mpi/src directory. I uploaded few inputs for UME. These are for four ranks.
