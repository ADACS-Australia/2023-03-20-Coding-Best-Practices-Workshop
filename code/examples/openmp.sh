#! /usr/bin/env bash
#
#SBATCH --job-name=helloMP
#SBATCH --output=/fred/oz983/%u/OpenMP_Hello_%A_out.txt
#SBATCH --error=/fred/oz983/%u/OpenMP_Hello_%A_err.txt
#
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=8
#SBATCH --time=00:01:00

# move to the directory where the script/data are
cd /fred/oz983/${USER}

export OMP_NUM_THREADS=$SLURM_CPUS_PER_TASK
/fred/oz983/KLuken_HPC_workshop/hello
