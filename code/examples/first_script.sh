#! /usr/bin/env bash
#
#SBATCH --job-name=hello
#SBATCH --output=res.txt
#
#SBATCH --ntasks=1
#SBATCH --time=05:00
#SBATCH --mem-per-cpu=200

# load the python module
module load python/3.8.5

# move to the work directory
cd /fred/oz983/${USER}
# do the work
python3 ../KLuken_HPC_workshop/hello.py | tee hello.txt
sleep 120
