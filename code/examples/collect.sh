#! /usr/bin/env bash
#
#SBATCH --job-name=collect
#SBATCH --output=/fred/oz983/%u/collect_%A_out.txt
#SBATCH --error=/fred/oz983/%u/collect_%A_err.txt
#
#SBATCH --ntasks=1
#SBATCH --time=00:05
#SBATCH --mem-per-cpu=200


# move to the directory where the script/data are
cd /fred/oz983/${USER}

# list all the files that we will 'process'
files=$(ls *gon.txt)

# this is where the 'proccessed' data will end up
outfile=collected.txt

echo "collecting outputs from : ${files}"
echo "results will be in: ${outfile}"

# delete the outfile before we write to it
if [[ -e ${outfile} ]]; then rm ${outfile};fi

# do the 'processing' and write to the outfile
for f in ${files}; do
  cat ${f} >> ${outfile}
  # delete the intermediate files to save space
  rm ${f}
done


echo "Phew! Hard work complete..."
