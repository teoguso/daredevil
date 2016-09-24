sudo apt-get install gr-osmosdr gnuradio-dev cmake swig build-essential doxygen python-scipy
git clone https://github.com/ptrkrysik/multi-rtl.git
cd multi-rtl
mkdir build
cd build
cmake ..
sudo make install
sudo ldconfig
