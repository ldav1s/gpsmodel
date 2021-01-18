# gpsmodel

The `gpsmodel` program is a program that sets the program model for u-blox 8 / u-blox M8 receivers.

This has been tried out on a Raspberry Pi 2 Model B using the
[Uputronics Raspberry Pi+ GPS Expansion Board](https://store.uputronics.com/index.php?route=product/product&path=60_64&product_id=81)
It claims on that page to be able to run on the original RPi 1 Model B+, but I wasn't able to get it working in that
configuration.

FWIW, the specific board I have says it's a "Raspberry Pi+ ublox GPS Expansion Board v4.1".  The chip on it is a
ublox MAX-M8Q-0-10.

Terminal settings and save from [this gist](https://gist.github.com/SlightlyLoony/d94cce218a9f650e6ad2de6a6ae7550e).
Defaults and descriptions from 33.10.17 UBX-CFG-NAV5 and C.10 Navigation Settings (UBX-CFG-NAV5) from the
[hardware sheet](https://www.u-blox.com/sites/default/files/products/documents/u-blox8-M8_ReceiverDescrProtSpec_(UBX-13003221)_Public.pdf)

Like others I was going through the [*5 minute guide to making a GPS Locked Stratum 1 NTP Server with a Raspberry Pi*](https://ava.upuaut.net/?p=951)
and was not excited to compile code just to set the stationary mode which can be accopmlished
using a script.  Also was not excited about the "magic bytes" aspect of the C code referenced there.
