cd /tmp
git clone https://github.com/micropython/micropython-lib
rm -rf ~/.micropython/lib
cd micropython-lib
make install

cd ~/.micropython/lib
DEST=/home/builder/micropython/ports/esp8266/modules

modules=($MICROPYTHON_LIB)

echo "Copy modules..."

for i in "${modules[@]}";
do
    cp -avr $i $DEST
    echo $i
done

cd /home/builder/micropython/ports/esp8266

make

cp /home/builder/micropython/ports/esp8266/build/firmware-combined.bin /home/builder/build