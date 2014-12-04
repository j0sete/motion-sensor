all:
	echo "Update the sistem"
	sudo apt-get upgrade -y
	sudo apt-get update -y
	echo "Change seguridad.rpi to executable"
	chmod +x seguridad.rpi
	echo "Download all necessaries libreries"
	sudo apt-get -y install build-essential cmake cmake-curses-gui pkg-config libpng12-0 libpng12-dev libpng++-dev libpng3 libpnglite-dev zlib1g-dbg zlib1g zlib1g-dev pngtools libtiff4-dev libtiff4 libtiffxx0c2 libtiff-tools libeigen3-dev
	sudo apt-get -y install libjpeg8 libjpeg8-dev libjpeg8-dbg libjpeg-progs ffmpeg libavcodec-dev libavcodec53 libavformat53 libavformat-dev libgstreamer0.10-0-dbg libgstreamer0.10-0 libgstreamer0.10-dev libxine1-ffmpeg libxine-dev libxine1-bin libunicap2 libunicap2-dev swig libv4l-0 libv4l-dev python-numpy libpython2.6 python-dev python2.6-dev libgtk2.0-dev
	echo "Download the last update of OpenCV"
	git clone https://github.com/Itseez/opencv.git
	unzip opencv-2.4.8.zip
	cd opencv-2.4.8
	mkdir release
	ccmake ../
	make
	sudo make install
	
	
