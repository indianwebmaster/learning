import os
import time
import winsound

class FTimer:
    def __init__(self, soundFile=None):
        self.__soundFile = soundFile

    def count_down(self, secs, message=None, soundFile=None):
        for i in range(int(secs), -1, -1):
            pstr = self.secs_to_printable(i)
            print("\r" + pstr + " ", end='', flush=True)
            time.sleep(1)

        if message is not None: print("\n" + message)
        if soundFile is None and self.__soundFile is not None: soundFile = self.__soundFile
        if soundFile is not None: winsound.PlaySound(soundFile, winsound.SND_FILENAME)

    def secs_to_printable(self, secs, pstr=None):
        if pstr is None: pstr = ""
        if secs < 60:
            if secs > 1:
                pstr += str(secs) + " secs "
            else:
                pstr += str(secs) + " sec "
        elif secs < (60 * 60):
            mins = secs // 60
            if mins > 1:
                pstr += str(mins) + " mins "
            else:
                pstr += str(mins) + " min "

            rem_secs = secs - (mins * 60)
            if rem_secs >= 0:
                pstr = self.secs_to_printable(rem_secs, pstr)
        else:
            hours = secs // 3600
            if hours > 1:
                pstr += str(hours) + " hours "
            else:
                pstr += str(hours) + " hour "

            rem_secs = secs - (hours * 3600)
            if rem_secs >= 0:
                pstr = self.secs_to_printable(rem_secs, pstr)
        return (pstr)

if __name__ == "__main__":
    timer = FTimer(soundFile=F"..{os.sep}resources{os.sep}boxing_bell.wav")
    timer.count_down(0,"test")