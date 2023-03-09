#! /bin/bash -l
#SBATCH --export=NONE
#SBATCH --time=10:00:00
#SBATCH --nodes=1

base=BASEDIR
image=IMAGE

# load singularity
module load apptainer/latest
# list my loaded modules (for debugging)
module list

# define my container setup
cont="singularity run -B $PWD:$PWD aegean_main.sif"
# define some macros that run aegean/BANE from within the container
aegean="${cont} aegean"
BANE="${cont} BANE"

# Print commands and their arguments as they are executed (for debugging)
set -x

# start a code block
{

# move into the working directory
cd ${base}

# look for the background/noise files
if [ ! -e "${image%.fits}_bkg.fits" ] # Use the bash string substitution syntax
then
    ${BANE} ${image}
fi

# process the image
${aegean} --autoload ${image} --table out.fits,out.csv

# for this code block:
#  redirect STDERR/STDOUT to a subprocess that will prepend all lines
#  with a date and time, and then redirect back to STDERR/STDOUT
} 2> >(awk '{print strftime("%F %T")";",$0; fflush()}' >&2) \
  1> >(awk '{print strftime("%F %T")";",$0; fflush()}')