#! /bin/bash
function usage()
{
echo "obs_sfind.sh [-g group] [-d dep] [-q queue] [-M cluster] [-t] image
  -g group   : group (account) to run as, default=oz983
  -d dep     : job number for dependency (afterok)
  -q queue   : job queue, default=<blank>
  -t         : test. Don't submit job, just make the batch file
               and then return the submission command
  image      : the image to process" 1>&2;
# ^ we send the help documentation to STDERR with 1>&2
exit 1;
# exit with status 1 (not ok)
}

#default values for my arguments
account="#SBATCH --account oz983"
depend=''
queue=''
tst=
extras=''


# Parse option arguments.
#    
# Getopts is used by shell procedures to parse positional parameters
# as options.
# 
# OPTSTRING contains the option letters to be recognised; if a letter
# is followed by a colon, the option is expected to have an argument,
# which should be separated from it by white space.
while getopts 'g:d:q:M:t' OPTION
do
    case "$OPTION" in
	g)
	    account="#SBATCH --account ${OPTARG}"
	    ;;
	d)
	    depend="#SBATCH --dependency=afterok:${OPTARG}"
	    ;;
	q)
	    queue="#SBATCH -p ${OPTARG}"
	    ;;
	t)
	    tst=1
	    ;;
	? | : | h)
	    usage
	    ;;
  esac
done
# set the obsid to be the last argument provided
# by renaming the positional parameters
shift  "$(($OPTIND -1))"
image=$1

# Treat unset variables as an error when substituting.
# Catches silly errors earlier on
set -u

# if obsid is empty then just print help
if [[ -z ${image} ]]
then
    usage
fi


# The working directory for our script
base='/fred/oz983/phancock/'
# The name of the script that we'll create and the location of the log files
script="${base}queue/sfind_${image%.fits}.sh"
output="${base}queue/logs/sfind_${image%.fits}.o%A"
error="${base}queue/logs/sfind_${image%.fits}.e%A"

# build the sbatch header directives
sbatch="#SBATCH --output=${output}\n#SBATCH --error=${error}\n${queue}\n${account}\n${depend}"

 # replace IMAGE and BASEDIR
cat sfind.sh | sed -e "s:IMAGE:${image}:g" \
                   -e "s:BASEDIR:${base}:g"  \
                   -e "0,/#! .*/a ${sbatch}" > ${script}
# ^appeend ${sbatch} after the first line matching the given pattern

# job invocation command, with a pause of 15s before the job starts
sub="sbatch --begin=now+15 ${script}"

# if tst is not zero then
# return the location of the script and the submission command
if [[ ! -z ${tst} ]]
then
    echo "script is ${script}"
    echo "submit via:"
    echo "${sub}"
    exit 0
fi

# submit job and capture the output as a list
jobid=($(${sub}))
# output looks like "Submitted batch job 0123456"
jobid=${jobid[3]}

# rename the err/output files as we now know the jobid
error=$( echo ${error} | sed "s/%A/${jobid}/" )
output=$( echo ${output} | sed "s/%A/${jobid}/" )

echo "Submitted ${script} as ${jobid}"
echo "STDOUT is looged to ${output}"
echo "STDERR is logged to ${error}"