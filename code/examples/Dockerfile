# use a pre-made container as base
FROM python:3.8.5

# download the file into /user/bin and change permissions
RUN cd /tmp &&\
    git clone https://github.com/PaulHancock/symmetrical-octo-parakeet.git &&\
    cd symmetrical-octo-parakeet && pip install .

# set the default work directory
WORKDIR /app
