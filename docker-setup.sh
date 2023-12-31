INSTALL_PATH=$(pwd)

docker
if [[ $? -ne 0 ]] ; then
clear
echo -e "Docker is not installed. Please install docker for linux"
exit
else
echo -e "Docker already installed."
fi
clear
echo "Docker installed"
echo "$(docker --version)"

# Set xhost for system
xhost +local:docker
if [[ $? -ne 0 ]] ; then
echo "xhost display connection failed. Please make sure xhost is installed."
exit
else
echo -e "xhost connection done."
fi

# build the image
echo -e "Running docker build"
sudo docker build -t power-pass $INSTALL_PATH

if [[ $? -ne 0 ]] ; then
echo -e "DOcker build failed!"
exit
fi

echo 'alias powerpass="sudo docker run -i -e DISPLAY=$DISPLAY -v /tmp/.X11-unix:/tmp/.X11-unix -t power-pass"' >> ~/.bashrc
echo -e "Docker setup complete. Reopen the terminal and type 'powerpass' to start the app."
