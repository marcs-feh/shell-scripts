#!/bin/sh

mpdIsRunning="$(pgrep mpd)"

if [ ! -z ${mpdIsRunning} ]
then
	st -e ncmpcpp	
else
	mpd
	st -e ncmpcpp
fi
