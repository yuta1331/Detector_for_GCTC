#build docker image
sudo docker build --no-cache=true -t watermark `pwd`

#run docker container
OUT_PORT=8888
CONF_DIR="../WestlabGCTCGUI/config_jsons" #relative path allowed. change here for config json files
CONF_DIR=$(cd $(dirname $0) && cd $CONF_DIR && pwd) #convert to absolute path
OUTP_DIR="output" #relative path allowed. change here for config json files
OUTP_DIR=$(cd $(dirname $0) && cd $OUTP_DIR && pwd) #convert to absolute path
sudo docker run -it -v $CONF_DIR:/program/config_jsons -v $OUTP_DIR:/program/output -p $OUT_PORT:80 --rm watermark python /program/main.py

