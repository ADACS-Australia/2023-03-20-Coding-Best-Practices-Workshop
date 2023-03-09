#! /usr/bin/env bash
#
#SBATCH --job-name=helloMPI
#SBATCH --output=/fred/oz983/%u/MPI_Hello_%A_out.txt
#SBATCH --error=/fred/oz983/%u/MPI_Hello_%A_err.txt
#
#SBATCH --ntasks=8
#SBATCH --cpus-per-task=1
#SBATCH --time=00:01:00

# move to the directory where the script/data are
cd /fred/oz983/${USER}

srun /fred/oz983/KLuken_HPC_workshop/hello_mpi
