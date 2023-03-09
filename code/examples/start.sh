#! /usr/bin/env bash
#
#SBATCH --job-name=start
#SBATCH --output=/fred/oz983/%u/start_%A_out.txt
#SBATCH --error=/fred/oz983/%u/start_%A_err.txt
#
#SBATCH --ntasks=1
#SBATCH --time=00:05
#SBATCH --mem-per-cpu=1G

# move to the directory where the script/data are
cd /fred/oz983/${USER}

#make a file
touch input_data.txt

echo "doing some pre-processing work"

# put some data in
for i in 3 4 5 6 7 8;
do
  echo ${i} >> input_data.txt
done

